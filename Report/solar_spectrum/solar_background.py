"""
Program to read in spectral data from .csv file for the solar background and plot

To use this program you must make sure to change the input parameters to suit your input file.
The plot is saved as a .png file under the same name as your .csv file.
"""
# importing the necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

# ****** File Inputs ********* # ***************************************************************** #
# Enter the filename here for the solar background file
filename_spec = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Report/solar_spectrum/solar_background.csv"
figure_filename = "solar_background.png"   # Output filename to save the plot to (or test.pdf)
delimiter = ';'              # Character separating your columns.
nheaderlines = 33              # Number of header lines in your csv file.
nfooterlines = 1               # Number of footer lines in your csv file.
# ****** Other Inputs ******** # ***************************************************************** #
minwav = 150                  # Minimum Wavelength. Change this to zoom in on particular regions.
maxwav = 1050                  # Maximum Wavelength. Change this to zoom in on particular regions.
# **************************** # ***************************************************************** #

# Read in data (Change the filename and delimiter to suit your data):
data_spec = np.genfromtxt(filename_spec, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines)

# Deal with the spectrum #
# Find the start and end of your wavelength range
start = np.argmin(np.abs(data_spec[:, 0] - minwav))
stop = np.argmin(np.abs(data_spec[:, 0] - maxwav))

# Now save it to x and y variables:
x_val_spec = data_spec[start:stop, 0]
y_val_spec = data_spec[start:stop, 1]

# Plot the spectrum
fig = plt.figure()
plt.plot(x_val_spec, y_val_spec, color="red", label='Solar Background')

plt.legend()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Intensity of Solar Background Spectrum')
# Save and plot
plt.savefig(figure_filename)
plt.show()