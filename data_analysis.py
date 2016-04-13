#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def wavepacket(x, k, sigma):
    """This function creates a wavepacket on the interval defined by x with
    wavevector k and standard deviation sigma."""
    return np.sin(k*x) *  np.exp(-(x**2)/(2*sigma**2))


def main():
    """This function sould call noisy_packet() to get a Gaussian wave
    packet, call clean_data() to apply a low pass filter to the data and
    finally plot the result."""
    #TODO add your code here
    #x_values = np.arange()
    #noisy_y=noisy_packet(x_values, 5, 1, 0.2)
    


def noisy_packet(x_values, k, sigma, noise_amplitude):
    """This function returns a noisy Gaussian wavepacket with wave
    vector k, standard deviation sigma and Gaussian noise of standard
    deviation noise_amplitude."""
    clean_y = wavepacket(x_values,k,sigma)
    noisy_y = clean_y + noise_amplitude*np.random.randn(len(x_values))
    return noisy_y

def clean_data(x_values,y_values):
    """This function should take a set of y_values, perform the Fourier
    transform on it, filter out the high frequency noise, transform the
    signal back into real space, and return it."""

    pass #TODO add your code here
    #return y_clean

main()  # calls your main function
