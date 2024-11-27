import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: Read the data from the CSV file
def read_prism_data(file_path):
    data = pd.read_csv(file_path)
    wavelengths = data['wavelength'].values
    uncertainty_wavelength = data['uncertainty_wavelength'].values
    d_min = data['Dmin'].values
    uncertainty_d_min = data['uncertainty_Dmin'].values
    return wavelengths, uncertainty_wavelength, d_min, uncertainty_d_min

# Step 2: Calculate the refractive index using the given equation
def calculate_refractive_index(d_min, A):
    return np.sin((d_min + A) / 2) / np.sin(A / 2)

# Step 3: Calculate the uncertainty in the refractive index
def calculate_uncertainty_n(d_min, uncertainty_d_min, A):
    return np.abs((0.5 * uncertainty_d_min * np.cos((d_min + A) / 2)) / np.sin(A / 2))

# Step 4: Define the Cauchy relation for fitting
def cauchy_relation(lambda_, A, B):
    return A + B / lambda_**2

# Step 5: Define a linear model for fitting
def linear_model(x, m, c):
    return m * x + c

# Step 7: Plot the refractive index as a function of wavelength and perform error analysis
def plot_refractive_index(wavelengths, uncertainty_wavelength, n, uncertainty_n):
    # Convert wavelengths from meters to nanometers
    wavelengths_nm = wavelengths * 1e9
    uncertainty_wavelength_nm = uncertainty_wavelength * 1e9

    plt.figure(figsize=(10, 6))
    plt.errorbar(wavelengths_nm, n, xerr=uncertainty_wavelength_nm, yerr=uncertainty_n, fmt='o', label='Refractive Index', capsize=5)
    
    # Fit the Cauchy relation to the data
    popt_cauchy, pcov_cauchy = curve_fit(cauchy_relation, wavelengths, n)
    A_cauchy, B_cauchy = popt_cauchy
    cauchy_fit = cauchy_relation(wavelengths, A_cauchy, B_cauchy)
    plt.plot(wavelengths_nm, cauchy_fit, '-', color = 'orange', label=f'Cauchy Fit: n(λ) = {A_cauchy:.4f} + {B_cauchy:.4e}/λ²')

    # Fit the linear model to the data
    popt_linear, pcov_linear = curve_fit(linear_model, wavelengths, n)
    m_linear, c_linear = popt_linear
    linear_fit = linear_model(wavelengths, m_linear, c_linear)
    plt.plot(wavelengths_nm, linear_fit, '--', color = 'green', label=f'Linear Fit: y = {m_linear:.4e}x + {c_linear:.4f}')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Refractive Index, n')
    plt.title('Refractive Index vs. Wavelength')
    plt.legend()
    plt.show()

    # Calculate residuals and R^2 for Cauchy fit
    residuals_cauchy = n - cauchy_fit
    ss_res_cauchy = np.sum(residuals_cauchy**2)
    ss_tot = np.sum((n - np.mean(n))**2)
    r_squared_cauchy = 1 - (ss_res_cauchy / ss_tot)

    # Calculate residuals and R^2 for Linear fit
    residuals_linear = n - linear_fit
    ss_res_linear = np.sum(residuals_linear**2)
    r_squared_linear = 1 - (ss_res_linear / ss_tot)

    # Print the refractive index values, R^2
    print("Refractive Index values and uncertainties:")
    for wl, ni, ui in zip(wavelengths_nm, n, uncertainty_n):
        print(f"Wavelength: {wl:.4e} nm, Refractive Index: {ni:.4f}, Uncertainty: {ui:.4f}")
    print(f"r^2 for Cauchy Fit: {r_squared_cauchy:.4f}")
    print(f"r^2 for Linear Fit: {r_squared_linear:.4f}")

    # Plot the residuals for both fits
    plt.figure(figsize=(10, 6))
    plt.errorbar(wavelengths_nm, residuals_cauchy, yerr=uncertainty_n, fmt='o', color = 'orange', label='Cauchy Residuals', capsize=5)
    plt.errorbar(wavelengths_nm, residuals_linear, yerr=uncertainty_n, fmt='x', color = 'green', label='Linear Residuals', capsize=5)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Residuals')
    plt.title('Residuals of Refractive Index Fits')
    plt.legend()
    plt.show()

def monte_carlo_simulation(wavelengths, d_min, uncertainty_d_min, A, num_samples=10000):
    n_samples_list = []

    for _ in range(num_samples):
        # Generate samples for the entire dataset
        d_min_samples = np.random.normal(d_min, uncertainty_d_min)
        
        # Calculate the refractive index for each sample
        n_samples = calculate_refractive_index(d_min_samples, A)
        n_samples_list.append(n_samples)

    # Convert list of arrays to a 2D numpy array
    n_samples_array = np.array(n_samples_list)

    # Calculate mean and standard deviation across the samples
    n_mean = np.mean(n_samples_array, axis=0)
    n_std = np.std(n_samples_array, axis=0)

    # Print the results
    for wl, n_m, n_s in zip(wavelengths, n_mean, n_std):
        print(f"Wavelength: {wl:.4e} m, Mean Refractive Index: {n_m:.4f}, Uncertainty: {n_s:.4f}")

# Example usage
file_path = r'C:\Users\pujni\OneDrive\Desktop\University\Year 3\Observational Astronomy\Semester 1\Labs\Report\prism_exp\prism_data.csv'
wavelengths, uncertainty_wavelength, d_min, uncertainty_d_min = read_prism_data(file_path)

# Set the prism angle A (in radians)
A = np.radians(60)  # Example: 60 degrees converted to radians

# Calculate the refractive index
n = calculate_refractive_index(d_min, A)

# Calculate the uncertainty in the refractive index
uncertainty_n = calculate_uncertainty_n(d_min, uncertainty_d_min, A)

# Plot the refractive index as a function of wavelength and perform error analysis
plot_refractive_index(wavelengths, uncertainty_wavelength, n, uncertainty_n)

# Call the function to perform Monte Carlo simulation, print, and plot results
monte_carlo_simulation(wavelengths, d_min, uncertainty_d_min, A, num_samples=10000)
