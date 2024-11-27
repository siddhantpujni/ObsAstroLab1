"""
Program to read in spectral data from .csv file, find the peaks, and plot.
AUTHOR: Daniel Eastwood, email: deastw@roe.ac.uk

To use this program you must make sure to change the input parameters to suit your input file.
The plot is saved as a .png file under the same name as your .csv file.
"""
import numpy as np # importing the necessary libraries.
import matplotlib.pyplot as plt
import sys
import os

# ****** File Inputs ********* # ***************************************************************** #
filename = r"C:\Users\pujni\OneDrive\Desktop\University\Year 3\Observational Astronomy\Semester 1\Labs\Report\spectral_lamps\lamp_4.csv"         # Name of your input file. Read in as an argument (Include '.csv'). #
delimiter = ';'              # Character separating your columns.                                #
nheaderlines = 49              # Number of header lines in your csv file.                          #
nfooterlines = 1               # Number of footer lines in your csv file.                          #
# ****** Other Inputs ******** # ***************************************************************** #
nmax = 5                     # Number of peaks you want to identify.                             #
minwav = 150                   # Minimum Wavelength. Change this to zoom in on particular regions. #
maxwav = 1050                  # Maximum Wavelength. Change this to zoom in on particular regions. #
peakwidth = 50                 # Increased pixel width of each peak.                               #
labelcolor = 'yellow'          # Background colour of your peak labels.                            #
labelpos = (-10, -5)      
altlabelpos = (-10, -20) # Adjusted relative position of the peak labels.                    #
# **************************** # ***************************************************************** #

# **** The following should not need changing ****

# Read in data (Change the filename and delimiter to suit your data):
my_data = np.genfromtxt(filename, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines) 

# Find the start and end of your wavelength range
start = np.argmin(np.abs(my_data[:, 0] - minwav))
stop = np.argmin(np.abs(my_data[:, 0] - maxwav))

# Now save it to x and y variables:
x_val = my_data[start:stop, 0]
y_val = my_data[start:stop, 1]

# Find first nmax peaks:

x_ymax = [] # initialising arrays
y_ymax = []
y_copy = y_val
for i in range(1, nmax+1):
    y_max = np.amax(y_copy)
    arg_yc = np.argmax(y_copy)
    arg = np.where(y_val == y_max)[0]
    x_ymax = np.append(x_ymax, x_val[arg])
    y_ymax = np.append(y_ymax, y_max)
    dellist = range(arg_yc-peakwidth, arg_yc+peakwidth+1)
    y_copy = np.delete(y_copy, dellist)

# Extract the base filename without extension for the title
base_filename = os.path.basename(filename)
title = os.path.splitext(base_filename)[0]

# Now plot it:
fig = plt.figure()
ax = fig.add_subplot(111)
# Change the labels to suit
ax.set_xlabel('$ Wavelength \, (nm)$')
ax.set_ylabel('$ Intensity \, (arbitrary \, units) $')
ax.set_xlim(minwav, maxwav)
ax.plot(x_val, y_val, linewidth=2) # Plot the input spectrum
ax.plot(x_ymax, y_ymax, lw=0, marker='o', color='r', markersize=10) # Plot peak points

# Annotate your plot with the peak wavelengths (in nm):
for i, (x, y) in enumerate(zip(x_ymax, y_ymax)):
    # Alternate label positions to avoid overlap
    offset = labelpos if i % 2 == 0 else altlabelpos
    plt.annotate(
        f'{x}',  # Format the label to 2 decimal places
        xy=(x, y), xytext=offset,
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round, pad=0.5', fc=labelcolor, alpha=0.5),
        arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=0'))

# Set the title of the plot
ax.set_title(title)

# Save and plot
plt.savefig(filename[:-4]+'.png')
plt.show()