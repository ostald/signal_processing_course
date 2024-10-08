import matplotlib.pyplot as plt
import numpy as np
# Commonly used window functions are found in
# the scipy.signal.windows module.
from scipy.signal.windows import hann


# Calculate the DTFT of signal x using zero-padded FFT
# at N evenly spaced points between -\pi and \pi.
def dft_dtft(x, N, sample_rate=1e3):
    # fftshift shifts the frequencies so that we obtain
    # normalized angular frequency between -\pi to \pi,
    # instead of 0 to 2\pi.
    X = np.fft.fftshift(np.fft.fft(x, N))

    # Normalized angular frequencies.
    freqs = np.fft.fftshift(np.fft.fftfreq(N, d=1.0/sample_rate))

    return X, freqs


# Signal (FIR filter coefficients).
sample_rate = 10e3
t = np.arange(-20, 20)/sample_rate
# Make a filter that selects 1 kHz signals.
f0 = 1e3

# Rectangular windowed frequency selective filter.
h_R = np.cos(2.0*np.pi*f0*t)

# Hann windowed frequency selective filter.
h_H = hann(40)*np.cos(2.0*np.pi*f0*t)

# Frequency response of both filters.
H_R, freqs = dft_dtft(h_R, 1000, sample_rate)
H_H, freqs = dft_dtft(h_H, 1000, sample_rate)
plt.figure(figsize=(8, 5))
plt.subplot(211)
plt.plot(t, h_R, label="Rectangular windowed")
plt.plot(t, h_H, label="Hann windowed")
plt.ylim([-1.5, 1.5])
plt.xlabel("Time (s)")
plt.ylabel("Impulse response $h[n]$")
plt.legend()
plt.subplot(212)
plt.plot(freqs/1e3, 10.0*np.log10(np.abs(H_R)**2.0), label="Rectangular windowed")
plt.plot(freqs/1e3, 10.0*np.log10(np.abs(H_H)**2.0), label="Hann windowed")
plt.xlabel("Frequency (kHz)")
plt.ylabel("Power response (dB)")
plt.legend()
plt.ylim([-100, 50])
plt.tight_layout()
plt.savefig("freq_filter.png")
plt.show()
