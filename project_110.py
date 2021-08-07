import pandas as pd
import statistics
import random 
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")

reading_time = df["reading_time"].tolist()

population_mean = statistics.mean(reading_time)

def random_set_of_mean(counter):
    data_list = []
    random_index = random.randint(0, len(reading_time) - 1)
    value = reading_time[random_index]
    data_list.append(value)
    return statistics.mean(data_list)

def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Mean of random 30 samples"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(1000):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_figure(mean_list)
    return mean_list

sampling_mean = statistics.mean(setup())

print("Population Mean is {}".format(population_mean))
print("Sampling Mean is {}".format(sampling_mean))