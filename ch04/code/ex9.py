import numpy as n
import scipy.io.wavfile as sio
import matplotlib.pyplot as plt

# amplifier gain
alpha = 2.0

# cut off
beta = 0.08

# a function to compress a signal x
def distortion(x,alpha,beta):
    y = n.zeros(x.size)

    for i in range(0,x.size):
        if alpha*x[i] < -beta:
            y[i] = -beta
        elif n.abs(alpha*x[i]) <= beta:
            y[i] = alpha*x[i]
        else:
            y[i] = beta

    return y

# read wav file (read only one stereo channel)
wav = sio.read("guitar_clean.wav")
sample_rate = wav[0]
# read only one stereo channel
x = wav[1][:,0]

# scale to near unity, as the maximum allowed amplitude is +/- 1 for an audio waveform
x = 0.9*x / n.max(n.abs(x))

# create time vector (independent variable)
time_vec = n.arange(len(x))/float(sample_rate)

# apply distortion to the signal
out = distortion(x,alpha,beta)

# plot original and amplified
plt.plot(time_vec,out,label="Distorted")
plt.plot(time_vec,x,label="Original")
plt.legend()
plt.xlabel("Time $t$")
plt.ylabel("Relative air pressure $y(t)$")
plt.show()

# scale maximum absolute amplitude to 0.9, because 1.0 is the 
# maximum allowed by the file format
out = 0.9*out/n.max(n.abs(out))
# write compressed output to wav file
sio.write("guitar_dist.wav",sample_rate,n.array(out,dtype=n.float32))