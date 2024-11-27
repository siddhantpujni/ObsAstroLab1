"""
Program to read in spectral data from .csv file for different ND filters and plot
** NOTE ** You'll have to edit the code so that it can read and plot 3 ND filter spectra simultaneously

To use this program you must make sure to change the input parameters to suit your input file.
The plot is saved as a .png file under the same name as your .csv file.
"""
# importing the necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

# ****** File Inputs ********* # ***************************************************************** #
# Enter the filenames here for the elevation filter files					   #
filename_spec1 = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/ND_filters/ND1-backup.csv"								     	   #
filename_spec2 = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/ND_filters/ND2-backup.csv"									   #
filename_spec3 = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/ND_filters/ND3-backup.csv"									   #
figure_filename = "test2.png"   # Output filename to save the plot to (or test.pdf) 		   #
delimiter = ';'              # Character separating your columns.                                  #
nheaderlines = 33              # Number of header lines in your csv file.                          #
nfooterlines = 1               # Number of footer lines in your csv file.                          #
# ****** Other Inputs ******** # ***************************************************************** #
minwav = 150                   # Minimum Wavelength. Change this to zoom in on particular regions. #
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

# Now deal with third spectrum 
# Find the start and end of your wavelength range
start = np.argmin(np.abs(data_spec3[:, 0] - minwav))
stop = np.argmin(np.abs(data_spec3[:, 0] - maxwav))

# Now save it to x and y variables:
x_val_spec3 = data_spec3[start:stop, 0]
y_val_spec3 = data_spec3[start:stop, 1]

# Plot this for ND filters
"""
# Edit the code to be able to plot all 3 ND filters
"""

fig = plt.figure()
plt.plot(x_val_spec1, y_val_spec1, color="red", label='spectrum 1')
plt.plot(x_val_spec2, y_val_spec2, color="blue", label='spectrum 2')
plt.plot(x_val_spec3, y_val_spec3, color="green", label='spectrum 3')

plt.legend()
# Save and plot
plt.savefig(figure_filename)
plt.show()

"""fig, axs = plt.subplots(3, 1, figsize=(8, 12))

axs[0].plot(x_val_spec1, y_val_spec1, color="red", label='spectrum 1')
axs[0].legend()

axs[1].plot(x_val_spec2, y_val_spec2, color="blue", label='spectrum 2')
axs[1].legend()

axs[2].plot(x_val_spec3, y_val_spec3, color="green", label='spectrum 3')
axs[2].legend()

# Save and plot
plt.tight_layout()
plt.savefig(figure_filename)
plt.show()"""
