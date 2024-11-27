""" Example of a chi squared fit using python. This should be treated as an
example of an easy way to fit a best fit model to data in python.
We recommend playing about with it and trying to fit your data from the lab.
AUTHORS: Adam Carnall and Daniel Eastwood
email: adamc@roe.ac.uk; deastw@roe.ac.uk
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import optimize
from matplotlib import gridspec

def yfunc(param, x):
    """ Model to be fitted to the data. Model functional
    form can be changed for different circumstances
    """
    return param[0] * x**2 + param[1] * x + param[2]

def chisqd(param, x, y, yerr):
    """ function which, given an array of parameter values, and arrays of x, y
    and y error values, calculates model values using yfunc and returns the
    value of chi squared. 
    """
    model = yfunc(param, x) # calculate array of model y values
    chisq = np.sum(((model - y)/yerr)**2) # calculate chi squared value
    return chisq

def returnmodel(param, x):
    """ function which returns the model y values for a given set of parameters
    and x values (used for plotting only)
    """
    model = param[0] * x**2 + param[1] * x + param[2]
    return model

# ************************************************************
# ***   Here we create our fake data for this example.     ***
# ************************************************************
data = np.zeros(60) # build initial array to contain x, y, yerr values
data.shape = (20, 3) # make array 20 rows by 3 columns

# generate three random parameter values between zero and one.
# these will be recovered by the chi squared analysis
a = 1 + random.random()
b = 1 + random.random()
c = 100 + random.random()

print "input parameters " + str(a), str(b), str(c) # print input parameters

data[:, 0] = np.arange(1, 61, 3) # insert x values into the array
data[:, 1] = a*data[:, 0]**2 + b * data[:, 0] + c # create y data using input model parameters

for i in range(len(data[:, 0])): # add Gaussian noise to the y data
    data[i, 1] = data[i, 1] + random.gauss(0., data[i, 1] * 0.1)

data[:, 2] = data[:, 1] * 0.1 # create y error values to be 10% the y values they correspond to
# ************************************************************


# ************************************************************
# *** Find the chi squared minimum and the best fit model  ***
# ************************************************************
""" minimised the chi squared function by repeatedly calling
the chisqd function, the arguments are firstly the function to
be minimised, then the initial parameter values to start
searching from and then the arguments the chisqd function
requires after the list of parameter values, namely the arrays
of x, y and yerr values.
"""
# initial guess values for the parameters
initial_param = [1.5, 1.5, 100]
# minimise the chisquared function for our data
optresult = optimize.minimize(chisqd,
                              initial_param,
                              args=(data[:, 0], data[:, 1], data[:, 2]))

 # print parameters recovered by the chi squared analysis
print "output parameters " + str(optresult["x"][0]), str(optresult["x"][1]), str(optresult["x"][2])

# generate model values from the parameters obtained in the chi squared analysis.
model = returnmodel(optresult["x"], np.arange(1, 60, 0.1)) 
# ************************************************************

# ************************************************************
# ***   The rest of the code is just used to do the plot   ***
# ************************************************************
fig = plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1], hspace=0)

# Plot the errorbars and the fit to the data
ax1 = plt.subplot(gs[0])
ax1.plot(np.arange(1, 60, 0.1), model, ls='--')
ax1.set_ylabel("Flux")
ax1.errorbar(data[:, 0], data[:, 1], data[:, 2],
             color="black", linestyle=" ", lw=2,
             capsize=3, capthick=2)

# Plot residuals
ax2 = plt.subplot(gs[1], sharex = ax1)
plt.setp(ax1.get_xticklabels(), visible=False)
ax2.axhline(y=0.0, linewidth=1, color = 'r', ls='--')
ax2.errorbar(data[:, 0], data[:,1] - returnmodel(optresult["x"], np.arange(1, 61, 3)),
             data[:, 2], color="black", linestyle=" ", lw=2, capsize=3, capthick=2)
# Here we use spectral units as an example
ax2.set_xlabel("$\mathrm{Wavelength}\ \ \mathrm{\AA}$")
ax2.set_ylabel("Residuals")

# remove last tick label for the second subplot
yticks = ax1.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)

# Save and show plot
plt.savefig('examplefit.png') 
plt.show()
# ************************************************************
