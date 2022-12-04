import matplotlib.pyplot as plt
import numpy as np
import csv
import math
import random
import pandas as pd

from BSE import market_session

# ---------------------------------------------------------------------------------------------------------
plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (15,8)
plt.rcParams.update({'font.size': 22})

def plot_ppc_individual(b_moving_avg,s_moving_avg,t_moving_avg, value, title):
    time_period = list(range(0,len(t_moving_avg.index)))
    plt.plot(time_period, t_moving_avg, label='Total profit(B+S)', linestyle='-') 
    plt.plot(time_period, b_moving_avg, label='Buyer (B) profit',linestyle='-') 
    plt.plot(time_period, s_moving_avg, label='Seller (S) profit', linestyle='-')

    plt.ylabel("Total (B+S) Profit Per Second aggregate)")
    plt.xlabel("Hours")
    plt.title(title+str(value))
    plt.legend(loc='best')

#calculating the moving average of pps for one trail - function
def calculate_ppc(file_name, value, title, plot):
    b_new_df = pd.DataFrame()
    s_new_df = pd.DataFrame()
    
    df = pd.read_csv(file_name+'_strats.csv',header=None)
    
    for row in range(0,len(df.index)):
        b_sum = 0
        s_sum = 0
        for col in range (8, 219 ,7):
            b_sum +=df.loc[row][col]
        b_new_df.loc[len(b_new_df.index), 0] = b_sum

        for col in range (225, 428,7):
            s_sum +=df.loc[row][col]
        s_new_df.loc[len(s_new_df.index), 0] = s_sum
    
#     s_new_df.replace(np.nan, 0)
#     b_new_df.replace(np.nan, 0)
    
    b_moving_avg = b_new_df.loc[:,0].rolling(5).mean()
    s_moving_avg = s_new_df.loc[:,0].rolling(5).mean() 
    np.nan_to_num(b_moving_avg)
    np.nan_to_num(s_moving_avg)
    t_moving_avg = np.add(b_moving_avg,s_moving_avg)
    

    if (plot == True):
        plot_ppc_individual(b_moving_avg,s_moving_avg,t_moving_avg, value, title)
    
    return t_moving_avg, len(df.index)

# ---------------------------------------------------------------------------------------------------------
from matplotlib import style
from matplotlib.pyplot import cm
import matplotlib.collections as mcoll

plt.style.use('ggplot')
plt.figure(figsize=(15,12))

def process_multiple_ppc(name,start_num, num_trails, step, save_location, title):
    all_trail_t_mov_avg = []
    
    for trial in list(np.arange(start_num,num_trails,step)):
        trail_t_mov_avg, hours = calculate_ppc(name%trial, trial,title, False)
        all_trail_t_mov_avg.append(trail_t_mov_avg)   
        
        time_period = list(np.arange(0,hours))
        plt.rcParams.update({'font.size': 13})
        plt.plot(time_period, trail_t_mov_avg,label=f'k = {trial:.1f}',linestyle='-')
        plt.title(f'{title}({start_num},{num_trails:.1f})')
        plt.ylabel("Total (B+S) Profit Per Second aggregate)")
        plt.xlabel("Hours")
        plt.legend(loc='best')
#     plt.savefig(save_location, dpi=400, facecolor="white")
        
    return(all_trail_t_mov_avg)

def make_array(list1):
    array1 = []
    for i, b in enumerate(list1):
        n = np.nan_to_num(list1[i])
        array1.append(n)
        array1[i] = (n)
    return(array1)

import seaborn as sns
from scipy.stats import kurtosis, skew
from scipy import stats
import statistics

def normal_distribution_tests(results_array, plot_median):
    for i in range(0, len(results_array)):
        sns.distplot(results_array[i], hist=True, kde=False, bins=int(180/5), hist_kws={'edgecolor':'black'})
        if (plot_median==True):
            plt.axvline(x=statistics.median(results_array[i]), color='blue' )
            plt.axvline(x=statistics.mean(results_array[i]), color='red')
        
#         print( 'excess kurtosis of normal distribution (should be 0): {}'.format( kurtosis(results_array[i]) ))
        print( 'skewness of normal distribution (should be 0): {}'.format( skew(results_array[i]) ))
        _, p = stats.shapiro(results_array[i])
        print('shapiro of normal distribution (p should be > 0.5):' + format(p,'.30f'))
#         print(f'median of data: %f' % statistics.median(results_array[i]))
        print()
        

def find_best_mean(all_trail_t_mov_avg, offset):
    all_means = []
    for i in range(len(all_trail_t_mov_avg)):
        mean_i = np.mean(all_trail_t_mov_avg[i])
        all_means.append(mean_i)

    print(all_means)
    print(np.argmax(all_means)+offset, max(all_means))

def find_best_median(all_trail_t_mov_avg, offset):
    all_median = []
    for i, x in enumerate(all_trail_t_mov_avg):
        median_i = statistics.median(all_trail_t_mov_avg[i])
        all_median.append(median_i)
        plt.bar(i+offset, median_i)

    print(np.argmax(all_median)+offset, max(all_median))
    return all_median

def top_n_medians(medians, n):
    top_n = []
    array_sort =np.argsort(medians)[-n:][::-1]
    for x, value in enumerate(array_sort):
        for i, median in enumerate(medians):
            if (value == i):
                print(i, median)
                top_n.append([i, median])
    return(top_n)