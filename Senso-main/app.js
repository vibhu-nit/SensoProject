const express = require('express');
const bodyParser = require('body-parser');
const { static, request } = require('express');
const https = require('https');
//Import PythonShell module.
const { PythonShell } = require('python-shell');
const upload = require('express-fileupload');

const app = express();
app.use(express.static('public'));
app.use(upload());
app.use(bodyParser.urlencoded({extended:true}));
app.set('view engine','ejs');

app.get('/', function (req, res) {
  // res.send('sai h');
  res.render('index.ejs');
  // res.sendFile(__dirname+"/index.html");
});

app.post('/', function (req, res) {
  console.log(req.body);
  ans(req.body.song,res);

  // res.send(result.toString())
  // res.send("received");

  
});

app.post('/upload', function (req, res) {
console.log('In post');
if(req.files){
   console.log(req.files);
   var file = req.files.file;
   var filename = file.name;
   console.log(filename);
   file.mv('./public/userFile.wav', function (err){
     if(err){
       res.send(err);
     }
     else{
       ans('userFile.wav', res);
     }
   });
}

});

function ans(audioFile, res) {
  var selected_File = audioFile;

  let options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
    // scriptPath: 'path/to/my/scripts', //If you are having python_test.py script in same folder, then it's optional.
    args: [selected_File], //An argument which can be accessed in the script using sys.argv[1]
  };

  PythonShell.run('python_test.py', options, function (err, result) {
    if (err) throw err;
    // result is an array consisting of messages collected
    //during execution of script.
    console.log('result: ', result.toString());
    // res.send(result.toString());
    var Image = "graph/"+selected_File+".png";



    res.render('graph.ejs',{userName:selected_File , corrValue:result.toString() , userNameImage:Image});
  });
}

app.listen(8080, function () {
  console.log('listening on port 8080!');
});
