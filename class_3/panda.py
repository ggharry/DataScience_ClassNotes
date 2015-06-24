import pandas as pd
import requests
from numpy import *
import matplotlib.pyplot as plt

def get_data():
    has_header = False

    with open('nyt.csv', 'wb') as csv:
        for n in range(1,31):
            url = 'http://stat.columbia.edu/~rachel/datasets/nyt'+str(n)+'.csv'

            r = requests.get(url, stream=True)

            assert r.ok

            firstline = True
            for block in r.iter_lines(512):
                if firstline and has_header:
                    firstline = False
                    continue

                has_header = True

                csv.write(block)
                csv.write("\n")


def analyze():
    df = pd.read_csv('nyt.csv')

    # Describe
    print df.describe()

    # Histogram Plot
    df.hist(figsize=(18,12))
    plt.show()

    # Distribution Plot
    # x = linspace(-15,15,100) # 100 linearly spaced numbers
    # y = sin(x)/x # computing the values of sin(x)/x

    # fig = plt.figure(figsize=(18, 8), dpi=300)
    # plt.plot(x,y) # sin(x)/x
    # plt.plot(x,y,'co') # same function with cyan dots
    # plt.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
    # plt.show() # show the plot

get_data()
analyze()