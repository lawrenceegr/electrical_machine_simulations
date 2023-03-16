# Python code to calculate the net magnetic field produced
# by a three-phase stator.
import numpy as np
import matplotlib.pyplot as plt

# Set up the basic conditions
bmax = 1  # Normalize bmax to 1
freq = 60  # 60 Hz
w = 2 * np.pi * freq  # angular velocity (rad/s)

# First, generate the three component magnetic fields
t = np.arange(0, 1 / 60, 1 / 6000)
Baa = np.sin(w * t) * (np.cos(0) + 1j * np.sin(0))
Bbb = np.sin(w * t - 2 * np.pi / 3) * (np.cos(2 * np.pi / 3) + 1j * np.sin(2 * np.pi / 3))
Bcc = np.sin(w * t + 2 * np.pi / 3) * (np.cos(-2 * np.pi / 3) + 1j * np.sin(-2 * np.pi / 3))

# Calculate Bnet
Bnet = Baa + Bbb + Bcc

# Calculate a circle representing the expected maximum value of Bnet
circle = 1.5 * (np.cos(w * t) + 1j * np.sin(w * t))

# Plot the magnitude and direction of the resulting magnetic fields.
# Note that Baa is black, Bbb is blue, Bcc is magenta, and Bnet is red.
for ii in range(len(t)):
    # Plot the reference circle
    plt.plot(circle, 'k')
    

    # Plot the four magnetic fields.
    plt.plot([0, np.real(Baa[ii])], [0, np.imag(Baa[ii])], 'k', linewidth=2)
    plt.plot([0, np.real(Bbb[ii])], [0, np.imag(Bbb[ii])], 'b', linewidth=2)
    plt.plot([0, np.real(Bcc[ii])], [0, np.imag(Bcc[ii])], 'm', linewidth=2)
    plt.plot([0, np.real(Bnet[ii])], [0, np.imag(Bnet[ii])], 'r', linewidth=3)

    plt.axis('square')
    plt.axis([-2, 2, -2, 2])
    plt.draw()
    plt.pause(0.001)
    plt.clf()
    
