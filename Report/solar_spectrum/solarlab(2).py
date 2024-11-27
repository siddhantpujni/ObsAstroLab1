"""
Program to read in spectral data from .csv file for multiple elevations, fix y-axis point and plot

To use this program you must make sure to change the input parameters to suit your input file.
The plot is saved as a .png file under the same name as your .csv file.
"""
# importing the necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
import sys

# ****** File Inputs ********* # ***************************************************************** #
# Enter the filenames here for the elevation filter files					   #
filename_spec1 = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/Elevations/sky_45.csv"							     	   
filename_spec2 = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/Elevations/sky_90.csv"									   #
filename_spec3 = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/Elevations/sky_horizon.csv"									   #
figure_filename = "test.png"   # Output filename to save the plot to (or test.pdf) 		   #
delimiter = ';'              # Character separating your columns.                                  #
nheaderlines = 33              # Number of header lines in your csv file.                          #
nfooterlines = 1               # Number of footer lines in your csv file.                          #
# ****** Other Inputs ******** # ***************************************************************** #
wave = 720                     # Wavelengths to normalise spectra at                               #
minwav = 150                  # Minimum Wavelength. Change this to zoom in on particular regions. #
maxwav = 1050                  # Maximum Wavelength. Change this to zoom in on particular regions. #
# **************************** # ***************************************************************** #


# Read in data (Change the filename and delimiter to suit your data):
data_spec1 = np.genfromtxt(filename_spec1, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines) 
data_spec2 = np.genfromtxt(filename_spec2, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines) 
data_spec3 = np.genfromtxt(filename_spec3, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines) 

# Deal with first spectrum #
# Find the start and end of your wavelength range
start = np.argmin(np.abs(data_spec1[:, 0] - minwav))
stop = np.argmin(np.abs(data_spec1[:, 0] - maxwav))

# Now save it to x and y variables:
x_val_spec1 = data_spec1[start:stop, 0]
y_val_spec1 = data_spec1[start:stop, 1]

# Now deal with second spectrum #
# Find the start and end of your wavelength range
start = np.argmin(np.abs(data_spec2[:, 0] - minwav))
stop = np.argmin(np.abs(data_spec2[:, 0] - maxwav))

# Now save it to x and y variables:
x_val_spec2 = data_spec2[start:stop, 0]
y_val_spec2 = data_spec2[start:stop, 1]

# Now deal with third spectrum #
# Find the start and end of your wavelength range
start = np.argmin(np.abs(data_spec3[:, 0] - minwav))
stop = np.argmin(np.abs(data_spec3[:, 0] - maxwav))

# Now save it to x and y variables:
x_val_spec3 = data_spec3[start:stop, 0]
y_val_spec3 = data_spec3[start:stop, 1]

# Find the data point in your array when wavelength is = wave
arg_1 = np.argmin(np.abs(x_val_spec1 - wave))

# Plot this for two filters by normalising y-axis data at chosen wavelength point (wave)

fig = plt.figure()
plt.plot(x_val_spec1, y_val_spec1/y_val_spec1[arg_1], color="red", label='45')
plt.plot(x_val_spec2, y_val_spec2/y_val_spec2[arg_1], color="blue", label='90')
plt.plot(x_val_spec3, y_val_spec3/y_val_spec3[arg_1], color="green", label='Horizon')

plt.legend()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Intensity of Solar Spectrum at Varying Elevations')
# Save and plot
plt.savefig(figure_filename)
plt.show()