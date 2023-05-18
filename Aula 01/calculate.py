import pandas as pd

def calculator():
    database = pd.read_csv(r"C:\Users\meyso\Downloads/Compras.csv", sep=";")

    # r = raw, para formatar o path e o python não se perder

    print(database)