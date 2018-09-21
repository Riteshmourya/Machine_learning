# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 23:41:58 2018

@author: Ritesh Mourya
"""


from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
# Prog 1
def line_plot():
    file1='E:\Technology\Data Analytics\Python\Advance\Movie-Ratings.csv'
    data1 = read_csv(file1, delimiter=',')
    file2='E:\Technology\Data Analytics\Python\Advance\Movie-Data.csv'
    data2 = read_csv(file2, delimiter=',')
    ## Data from fiile 1
    df1=data1.filter(['Film','Year of release'], axis=1)
    # Data from file 2
    df2=data2.filter(['Movie Title', 'Release Date'], axis=1)
    df2.columns=['Film','Release Date']
    df2['Year of release'] = pd.DatetimeIndex(df2['Release Date']).year
    df2=df2.drop('Release Date', axis=1)
    # Concat both data frames
    df_new = [df2, df1]
    result=pd.concat(df_new)
    # Remove duplicate 
    y=result.drop_duplicates()
    mpl.rcParams.update(mpl.rcParamsDefault)
    a=y.groupby(['Year of release']).count()
    plt.plot(a)
    plt.title("Total number of movies per year")
    plt.xlabel("Years")
    plt.ylabel("Number of movies");
    plt.show()

# prog 2
def bar_chart():
    file1='E:\Technology\Data Analytics\Python\Advance\Movie-Data.csv'
    data = read_csv(file1, delimiter=',')
    
    df=data.filter(['Gross % US','US ($mill)','Overseas ($mill)','Release Date'], axis=1)
    
    df.columns=['Gross_US','US_mill','Overseas_mill','Release Date']
    # Extract year from date
    df['year'] = pd.DatetimeIndex(df['Release Date']).year
    # Getting total Revenue
    df['find_total']= df.US_mill * 100/ df.Gross_US
    df.loc[df['US_mill']==0, 'find_total'] = 245.1
       
    #print(df.describe())
    # Getting Overseas revenue
    df['Over_seas_gross']=df.find_total - df.US_mill
    df=df.drop('Release Date', axis=1)
    # Sum of Us revenue, year wise
    x=df.groupby('year')['US_mill'].sum()
    
    # Sum of Overseas revenue, year wise
    b=df.groupby('year')['Over_seas_gross'].sum()
    N = 45
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    # Set figure width to 12 and height to 9
    plt.rcParams["figure.figsize"] = [10,7]
    fig, ax = plt.subplots()
    
    rects1 = ax.bar(ind, x, width, color='r')
    rects2 = ax.bar(ind+width, b, width, color='g')
    ### add some text for labels, title and axes ticks
    ax.set_ylabel('Million $')
    ax.set_title('US Revenue and Overseas Revenue per year side –by side')
    ax.set_xticks(ind + width / 2)
    ax.legend((rects1[0], rects2[0]), ('Total US Revenue', 'Overseas Revenue'))
    xticklabels=df.year.unique()
    y=sorted(xticklabels, reverse=False)
    ax.set_xticklabels(y, rotation = 90)
    plt.show()
    
#Prog 3
def scatter_plot():
    file1='E:\Technology\Data Analytics\Python\Advance\Movie-Data.csv'
    data = read_csv(file1, delimiter=',')
    
    df=data.filter(['Gross % US','US ($mill)','IMDb Rating','Release Date'], axis=1)
    # Exract year from date
    df['year'] = pd.DatetimeIndex(df['Release Date']).year
    df.columns=['Gross_US','US_mill','IMDb Rating','Release Date','year']
    # Finding gross revenue
    df['find_total']= df.US_mill * 100/ df.Gross_US
    df.loc[df['US_mill']==0, 'find_total'] = 245.1
    # Average gross revenue, yearly
    a=df.groupby('year')['find_total'].mean()
    # Average IMDB rating of movies released on that year
    b=df.groupby('year')['IMDb Rating'].mean()
    print('Scatter Plots – Size by gross revenue and rating')
    # Correlation between the rating and total revenue
    m=df['IMDb Rating'].corr(df['find_total'])
    print('Actual correlation value', m)
    # Correlation value when we took average of both revenue and ratings
    k=a.corr(b)
    print('Correlation of Avg values', k)
    mpl.rcParams.update(mpl.rcParamsDefault)
    N=45
    x = b
    y = a
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()


Line_plot = line_plot()
Bar_chart = bar_chart()
Scatter_plot = scatter_plot()    