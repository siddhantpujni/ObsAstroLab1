import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def read_and_process_data(file_path):
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()
    
    wavelength = data['Wavelength'] * 1e9  # Convert from meters to nanometers
    uncertainty_wavelength = data['Uncertainty_Wavelength'] * 1e9  # Convert from meters to nanometers
    sin_phi = data['sin(phi)']
    uncertainty_sin_phi = data['Uncertainty_sin(phi)']
    
    return wavelength, uncertainty_wavelength, sin_phi, uncertainty_sin_phi

def linear_func(x, m):
    return m * x

def plot_and_fit_data(wavelength, uncertainty_wavelength, sin_phi, uncertainty_sin_phi):

    params, covariance = curve_fit(linear_func, wavelength, sin_phi)
    best_fit_line = linear_func(wavelength, *params)

    m = params[0]
    m_uncertainty = np.sqrt(np.diag(covariance))[0]

    inverse_m = 1 / m
    inverse_m_uncertainty = m_uncertainty / (m ** 2)

    ss_tot = np.sum((sin_phi - np.mean(sin_phi)) ** 2)
    ss_res = np.sum((sin_phi - best_fit_line) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    print(f"d: {inverse_m} ± {inverse_m_uncertainty} nm")
    print(f"R^2: {r_squared}")

    plt.figure(figsize=(10, 6))
    plt.errorbar(wavelength, sin_phi, xerr=uncertainty_wavelength, yerr=uncertainty_sin_phi, fmt='o', ecolor='red', capsize=5, label='Data with uncertainties')
    plt.plot(wavelength, best_fit_line, color='blue', label=f'Best fit line: y = {m:.4e}x')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel(r'$\sin(\varphi)$')
    plt.title(r'Wavelength vs. $\sin(\varphi)$ - Grating 2')
    plt.legend()
    plt.show()

    return sin_phi - best_fit_line, uncertainty_sin_phi, m, m_uncertainty

def plot_residuals(wavelength, residuals, uncertainty_sin_phi):
    plt.figure(figsize=(10, 6))
    plt.errorbar(wavelength, residuals, yerr=uncertainty_sin_phi, fmt='o', ecolor='red', capsize=5)
    plt.axhline(0, color='blue', linestyle='--')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Residuals')
    plt.title(r'Residuals of $\sin(\varphi)$ vs. Wavelength - Grating 2')
    plt.show()    

def monte_carlo_uncertainty(wavelength, sin_phi, uncertainty_wavelength, uncertainty_sin_phi, num_samples=10000):
    m_samples = []

    for _ in range(num_samples):
        # Generate samples for the entire dataset
        wavelength_samples = np.random.normal(wavelength, uncertainty_wavelength)
        sin_phi_samples = np.random.normal(sin_phi, uncertainty_sin_phi)

        # Fit a line to the samples
        params, _ = curve_fit(linear_func, wavelength_samples, sin_phi_samples)
        m_samples.append(params[0])

    # Calculate mean and uncertainty in the gradient
    m_samples = np.array(m_samples)

    # Calculate inverse of the gradient and its uncertainty
    inverse_m_samples = 1 / m_samples
    inverse_m_mean = np.mean(inverse_m_samples)
    inverse_m_uncertainty = np.std(inverse_m_samples)

    print(f"d: {inverse_m_mean:.5} ± {inverse_m_uncertainty:.5} nm")
    
    # Plot histogram of d values
    plt.figure(figsize=(10, 6))
    plt.hist(inverse_m_samples, bins=30, edgecolor='black', alpha=0.7)
    plt.xlabel('Groove Spacing, d (nm)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Groove Spacing from Monte Carlo Simulation - Grating 2')
    plt.show()

# Example usage for two different CSV files
file_path1 = r'C:\Users\pujni\OneDrive\Desktop\University\Year 3\Observational Astronomy\Semester 1\Labs\Report\grating_exp\grating_1.csv'
file_path2 = r'C:\Users\pujni\OneDrive\Desktop\University\Year 3\Observational Astronomy\Semester 1\Labs\Report\grating_exp\grating_2.csv'

# Process and plot data for the first file
wavelength1, uncertainty_wavelength1, sin_phi1, uncertainty_sin_phi1 = read_and_process_data(file_path1)
residuals1, uncertainty_sin_phi1, m1, m_uncertainty1 = plot_and_fit_data(wavelength1, uncertainty_wavelength1, sin_phi1, uncertainty_sin_phi1)
plot_residuals(wavelength1, residuals1, uncertainty_sin_phi1)
monte_carlo_uncertainty(wavelength1, sin_phi1, uncertainty_wavelength1, uncertainty_sin_phi1)

# Process and plot data for the second file
wavelength2, uncertainty_wavelength2, sin_phi2, uncertainty_sin_phi2 = read_and_process_data(file_path2)
residuals2, uncertainty_sin_phi2, m2, m_uncertainty2 = plot_and_fit_data(wavelength2, uncertainty_wavelength2, sin_phi2, uncertainty_sin_phi2)
plot_residuals(wavelength2, residuals2, uncertainty_sin_phi2)
monte_carlo_uncertainty(wavelength2, sin_phi2, uncertainty_wavelength2, uncertainty_sin_phi2)