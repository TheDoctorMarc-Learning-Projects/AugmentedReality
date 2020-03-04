import numpy as np

def gaussianKernel(krad): 
    sigma = krad/3
    ksize = krad*2 + 1
    krn = np.zeros((ksize, ksize))
    for i in range(0, ksize): 
        for j in range(0,ksize): 
            d = np.sqrt((krad - i)**2 + (krad - j)**2)
            krn[i, j] = np.exp(-d**2 / (2*sigma))
    krn /= krn.sum()
    return krn 