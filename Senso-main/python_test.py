# Senso

# import these libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.fftpack
from scipy.fftpack import fft
from scipy.io.wavfile import read
import struct
import wave
import sys

sound = sys.argv[1]
# sound = 'Rooster.wav'

Fs1,S1 = read('public/Chainsaw2.wav','r')
Fs2,S2 = read('public/'+sound,'r')
Fs3,S3 = read('public/Rainbow.wav','r')
Fs4,S4 = read('public/bark.wav','r')

if len(S2.shape)==2:
    S2=S2[:,0]
    # print(S2.shape)

if len(S2)>len(S1):
    S1=np.zeros(S2.shape)
    S1[:len(S1)]=S1

if len(S1)<len(S3):
    s1 = np.zeros(S3.shape)
    s1[:len(S1)]= S1
    # print(s1.shape)
if len(S3)<len(S1):
    s3 = np.zeros(S1.shape)
    s3[:len(S3)]=S3
    # print(s3.shape)

if len(S4)<len(S1):
    s4 = np.zeros(S1.shape)
    s4[:len(S4)] = S4
    # print(s4.shape)

if len(S2)<len(S1):
    s2 = np.zeros(S1.shape)
    s2[:len(S2)] = S2
    # print(s2.shape)
else:
    s2=S2
    
s1 = s3+s4+S1  
# print(s2.shape)
# print(s1.shape)

T = 1/Fs1
L = len(s1)
t = np.arange(L)
# print(Fs1)
t= t*T
# print(t)
plt.plot(1000*t[:500],s1[:500])
plt.xlabel('t (in milliseconds)')
plt.ylabel("s1(t)")
plt.savefig('public/fig1.png')
plt.figure()
# plt.show()


y = fft(s1)
P1 = abs(y/L)
f1 = (Fs1*np.arange(L))/L
plt.plot(f1,P1)
plt.xlabel('frequency')
plt.ylabel('Amp')
plt.savefig('public/fig2.png')
plt.figure()
# plt.show()



plt.plot(1000*t[:500],s2[:500])
plt.xlabel("Time in milliseconds")
plt.ylabel("S2(time)")
plt.savefig('public/fig3.png')
plt.figure()
# plt.show()



L=len(s2)
Y_Orig=fft(s2)
P1_Orig=abs(Y_Orig/L)
f2=(Fs2*np.arange(L))/L
plt.plot(f2,P1_Orig)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.savefig('public/fig4.png')
plt.figure()
# plt.show()


plt.xcorr(P1_Orig,P1)
plt.xlabel('frq')
plt.ylabel('peak')
plt.savefig('public/fig5.png')
plt.figure()
# # plt.show()

# a = P1**2
# b = P1_Orig**2
# q = np.correlate(P1_Orig,P1,mode ='same')
# q = q/((np.sum(a)*np.sum(b))**(1/2))
# plt.plot(P1,q)
# plt.savefig('public/fig6.png')
# plt.figure()

q=np.corrcoef(P1,P1_Orig)
xaxis = [0,0]
yaxis = [0,q[0,1]]
plt.plot(xaxis,yaxis)
plt.savefig('public/fig6.png')
plt.figure()
# plt.show()
print(q[0,1])

