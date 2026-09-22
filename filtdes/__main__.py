import matplotlib.pyplot as plt
import numpy as np

SAMPLERATE = 16_000
BAND_LOW = 80
BAND_HIGH = 4000
NUM_CHANNELS = 8


base = (BAND_HIGH / BAND_LOW) ** ( 1 / (NUM_CHANNELS-1) )

centers = np.array(list(range(NUM_CHANNELS)))
centers = np.power(base, centers) * BAND_LOW


for center in centers:
    w0 = center * 2 * 3.14159265 / SAMPLERATE
    w1 = (center / base) * 2 * 3.14159265 / SAMPLERATE
    bw = (w0 - w1)
    q = w0 / bw
    alpha = np.sin(w0) / (2 * q)
    a0 = 1 + alpha
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha
    b0 = alpha
    b1 = 0
    b2 = -alpha
    a1 /= a0
    a2 /= a0
    b0 /= a0
    b1 /= a0
    b2 /= a0
    print(f"{{ {a0}, {a1}, {a2}, {b1}, {b2} }},")

