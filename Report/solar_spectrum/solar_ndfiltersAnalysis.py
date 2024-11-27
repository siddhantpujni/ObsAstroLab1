"""
Program to read in spectral data from .csv file for a single ND filter and plot
** NOTE ** You'll have to edit the code so that it can read and plot the ND filter spectrum

To use this program you must make sure to change the input parameters to suit your input file.
The plot is saved as a .png file under the same name as your .csv file.
"""
# importing the necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

# ****** File Inputs ********* # ***************************************************************** #
# Enter the filename here for the elevation filter file
filename_spec = r"C:/Users/pujni/OneDrive/Desktop/University/Year 3/Observational Astronomy/Semester 1/Labs/Solar Lab/ND_filters/ND1-backup.csv"
figure_filename = "test2.png"   # Output filename to save the plot to (or test.pdf)
delimiter = ';'              # Character separating your columns.
nheaderlines = 33              # Number of header lines in your csv file.
nfooterlines = 1               # Number of footer lines in your csv file.
# ****** Other Inputs ******** # ***************************************************************** #
minwav = 150                   # Minimum Wavelength. Change this to zoom in on particular regions.
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

# Fraunhofer lines
fraunhofer_lines = {
    'Ca K': 393.366,
    'Ca H': 396.847,
    'H-alpha': 656.281,
    'H-beta': 486.134,
    'H-gamma': 434.047,
    'H-delta': 410.175
}

# Telluric lines
telluric_lines = {
    'O2 A': 759.370,
    'O2 B': 686.719,
    'Mg b4': 516.733,
}

# Sodium doublet lines
sodium_doublet = {
    'Na D1': 589.592,
    'Na D2': 588.995
}

# Plot the spectrum
fig = plt.figure()
plt.plot(x_val_spec, y_val_spec, color="red", label='ND1-Spectrum')

# Mark Fraunhofer lines with a tolerance of 0.3 nm
tolerance = 0.3
for line, wavelength in fraunhofer_lines.items():
    color = 'blue' if 'Ca' in line else 'purple'
    plt.axvline(x=wavelength, color=color, linestyle='--', label=f'{line} ({wavelength} nm)')
    plt.fill_betweenx([0, max(y_val_spec)], wavelength - tolerance, wavelength + tolerance, color=color, alpha=0.1)

# Mark Telluric lines with a tolerance of 0.3 nm
for line, wavelength in telluric_lines.items():
    plt.axvline(x=wavelength, color='green', linestyle='--', label=f'{line} ({wavelength} nm)')
    plt.fill_betweenx([0, max(y_val_spec)], wavelength - tolerance, wavelength + tolerance, color='green', alpha=0.1)

# Mark Sodium doublet lines with a tolerance of 0.3 nm
for line, wavelength in sodium_doublet.items():
    plt.axvline(x=wavelength, color='orange', linestyle='--', label=f'{line} ({wavelength} nm)')
    plt.fill_betweenx([0, max(y_val_spec)], wavelength - tolerance, wavelength + tolerance, color='orange', alpha=0.1)

plt.legend()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Spectrum with Fraunhofer and Telluric Lines')
plt.savefig(figure_filename)
plt.show()

# Zoom in on Ca H&K lines
minwav_zoom = 390
maxwav_zoom = 400

# Find the start and end of your wavelength range for zoomed in plot
start_zoom = np.argmin(np.abs(data_spec[:, 0] - minwav_zoom))
stop_zoom = np.argmin(np.abs(data_spec[:, 0] - maxwav_zoom))

# Now save it to x and y variables for zoomed in plot
x_val_spec_zoom = data_spec[start_zoom:stop_zoom, 0]
y_val_spec_zoom = data_spec[start_zoom:stop_zoom, 1]

# Plot the zoomed in spectrum
fig_zoom = plt.figure()
plt.plot(x_val_spec_zoom, y_val_spec_zoom, color="red", label='ND1-Spectrum (Zoomed)')

# Mark Ca H&K lines with a tolerance of 0.3 nm
for line, wavelength in {'Ca K': 393.366, 'Ca H': 396.847}.items():
    plt.axvline(x=wavelength, color='blue', linestyle='--', label=f'{line} ({wavelength} nm)')
    plt.fill_betweenx([0, max(y_val_spec_zoom)], wavelength - tolerance, wavelength + tolerance, color='blue', alpha=0.1)

plt.legend()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Zoomed Spectrum with Ca H&K Lines')
plt.savefig("zoomed_" + figure_filename)
plt.show()

# Measure the wavelength at the center of each Ca H&K line
ca_k_center = x_val_spec_zoom[np.argmin(np.abs(x_val_spec_zoom - 393.366))]
ca_h_center = x_val_spec_zoom[np.argmin(np.abs(x_val_spec_zoom - 396.847))]

print(f"Ca K line center wavelength: {ca_k_center} nm")
print(f"Ca H line center wavelength: {ca_h_center} nm")