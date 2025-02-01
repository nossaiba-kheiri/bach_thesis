from scipy.stats import beta
import warnings

warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from matplotlib.widgets import Slider, Button
import random
random.seed(1)
paths_no=1000   #number of paths (states of the world)
path_list=[]
iterations= 1000
n = 2
t1=1 #red 
t2=2 #black
alpha=4
beta=3
t1_0=3
t2_0=2


def create_urn_list(n,t1_0,t2_0,t1,t2):
    "takes types of elements as keys and initial states and outputs a list representing the urn"
    
    return t1_0*[t1]+t2_0*[t2] 


def x_n(a,b):
    return a/(a+b)
                     
def polyar(iterations,alpha,beta,t1_0,t2_0,t1=1,t2=2):
    "Runs one polya urn simulation for a fixed number of iterations"
    
    urn = create_urn_list(n,t1_0,t2_0,t1,t2)
    count_object = {t1:t1_0,t2:t2_0}
    itere=[x_n(t1_0,t2_0)]
    
    for i in range(iterations):
        rand=random.choices([t1,t2],weights=[itere[i],1-itere[i]])[0]
        
        for element in count_object:
            if element==rand:
                count_object[element] += alpha
            else:
                count_object[element] += beta
        itere.append(x_n(count_object[1],count_object[2]))
    
    
    return count_object , count_object[1]/(count_object[1]+count_object[2]),itere

def multi_pathr(paths_no,iterations,alpha,beta,t1_0,t2_0):
    "runs simulation across multiple random paths"
    for _ in range(paths_no+1):  #multiple paths
        path_list.append(polyar(iterations,alpha,beta,t1_0,t2_0,t1=1,t2=2)[1])
    return path_list


# Create some sample data
np.random.seed(0)
init_a = 4 
init_b = 3



# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
sns.distplot(multi_pathr(paths_no,iterations,1,0,init_a,init_b),hist=True, kde=True,
              color = 'red', hist_kws={'edgecolor':'red'},label=f'distribution from simulation with a={init_a},b={init_b}')
data = beta.rvs(init_a,init_b, size=1000)
sns.distplot(data,bins=15,kde=True,
                  color='skyblue',
                  hist_kws={'edgecolor':'skyblue'},label="theoretical distribution")

#ax.set_xlabel('')




# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)



# Make a vertically oriented slider to control the amplitude
axa = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
a_slider = Slider(
    ax=axa,
    label="a",
    valmin=0,
    valmax=30,
    valinit=init_a,
    orientation="vertical"
)

# Make a horizontal slider to control the frequency.
axb = fig.add_axes([0.25, 0.1, 0.65, 0.03])
b_slider = Slider(
    ax=axb,
    label='b',
    valmin=0,
    valmax=10,
    valinit=init_b,
)
def update(val):
    # Update the distribution with the slider value
    sns.distplot(multi_pathr(paths_no,iterations,1,0,a_slider.val,b_slider.val),hist=True, kde=True,
              color = 'red', hist_kws={'edgecolor':'red'},label=f'distribution from simulation with a={t1_0},b={t2_0}')
    from scipy.stats import beta
    data = beta.rvs(t,t2_0, size=1000)
    sns.distplot(data,bins=15,kde=True,
                  color='skyblue',
                  hist_kws={'edgecolor':'skyblue'},label="theoretical distribution")
    fig.canvas.draw_idle()



# register the update function with each slider
a_slider.on_changed(update)
b_slider.on_changed(update)


plt.show()