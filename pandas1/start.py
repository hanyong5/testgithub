
import warnings
warnings.filterwarnings(action='ignore') 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import scipy as sp
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from dateutil.relativedelta import relativedelta
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import datetime 


plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False  # '- 표시
