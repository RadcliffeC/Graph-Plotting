import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def makeplot(data, gtype):
    filepath = f'HotfireData/{data}'
    df = pd.read_csv(filepath)
    x = 'Time'
    y = 'Value'
    if data == 'combined_cf.csv' or data == 'fuel_coldflow.csv':
        y = 'Pressure'

    match gtype:
        case 'scatter':
            sns.scatterplot(x=x, y=y, data=df)
        case 'line':
            sns.lineplot(x=x, y=y, data=df)
        case 'bar':
            sns.barplot(x=x, y=y, data=df)
        case 'hist':
            sns.histplot(x=x, y=y, data=df)
        case _:
            print("Invalid gtype")

    plt.draw()
    plt.show()

if __name__ == '__main__':
    while True:
        csv = input("Enter csv file\n")

        if csv == 'quit':
            break

        gtype = input("Enter gtype, scatter, line, bar, hist\n")
        makeplot(csv, gtype)
