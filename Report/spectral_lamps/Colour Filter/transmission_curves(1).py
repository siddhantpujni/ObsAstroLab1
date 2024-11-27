"""
Program to read in spectral data from .csv file for two filters and compute the transmission curves

To use this program you must make sure to change the input parameters to suit your input file.
The plot is saved as a .png file under the same name as your .csv file.
"""
# importing the necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
import os

# ****** File Inputs ********* # ************************************************************************** #
# Enter the filenames for you files here for the elevation filter files					    #
filename_spec1 = r"C:\Users\pujni\OneDrive\Desktop\University\Year 3\Observational Astronomy\Semester 1\Labs\Report\spectral_lamps\Colour Filter\white_light_trace.csv"								    #
filename_spec2 = r"C:\Users\pujni\OneDrive\Desktop\University\Year 3\Observational Astronomy\Semester 1\Labs\Report\spectral_lamps\Colour Filter\filter_A4_B2.csv"									    	    #
figure_filename = "transmission_A4_B2.png"   	  # Output filename to save the plot to (or test.pdf) 	    	    #
# tcurve_filename = "transmission_A1"       # Output filename to save the transmission curve  		      #
delimiter = ';'                		  # Character separating your columns.                              #
nheaderlines = 48              		  # Number of header lines in your csv file.                        #
nfooterlines = 1               		  # Number of footer lines in your csv file.                        #
# **************************** # ************************************************************************** #

# Read in data (Change the filename and delimiter to suit your data):
data_spec1 = np.genfromtxt(filename_spec1, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines) 
data_spec2 = np.genfromtxt(filename_spec2, delimiter=delimiter, skip_header=nheaderlines, skip_footer=nfooterlines) 

# Now save the first spectrum to x and y variables:
x_val_spec1 = data_spec1[:, 0]
y_val_spec1 = data_spec1[:, 1]

# Now deal with second spectrum #
x_val_spec2 = data_spec2[:, 0]
y_val_spec2 = data_spec2[:, 1]

# Plot the two spectra and then also the transmission curve
fig = plt.figure()
plt.plot(x_val_spec1, y_val_spec1, color="black", linewidth=0.3, label='spectrum 1')
plt.plot(x_val_spec2, y_val_spec2, color="blue", linewidth=0.3, label='spectrum 2')

transmission_yval = y_val_spec2/y_val_spec1 ###had to swap these two around to get the correct transmission curve

# This plots the transmission curve, which is the ratio of the two spectra.
# But, which spectra is the numerator and the denominator here?
plt.plot(x_val_spec1, transmission_yval, color="green", linewidth=0.4, label='spectrum 3')

# Limit the y-axis range to be between 0 and 1 - DO NOT CHANGE!
plt.ylim([0, 1])

# Plot the figure legend
plt.legend()

# Label the x and y axis of the plot before saving! Write code to label them here...
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")

# Save the plot in the same directory as filename_spec1
output_dir = os.path.dirname(filename_spec1)
output_path = os.path.join(output_dir, figure_filename)
plt.savefig(output_path)

"""
# Save the transmission curve to a .csv file
  - You can then load this .csv file for multiple filters and overplot multiple transmission curves using the above code
  - This has 2 columns, wavelength (x-axis) and transmission (y-axis)
  - * Note * - When loading in *ONLY* the transmission curve, modify this python script but with the following changes to input parameters:
    - nheaderlines = 0
    - nfooterlines = 0
"""
#################################################################################
"""
####### DO NOT EDIT CODE BELOW THIS LINE #######
"""
# Save the transmission curve to .csv file.
#with open(tcurve_filename, "w") as fout:
    #for i in range(len(transmission_yval)):
        #fout.write(str(x_val_spec1[i]) + ";" + str(transmission_yval[i]) + "\n")

# Show the plot
plt.show()