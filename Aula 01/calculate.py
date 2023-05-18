import pandas as pd

def calculator():
    database = pd.read_csv(r"C:\Users\meyso\Downloads/Compras.csv", sep=";")

    # r = raw, para formatar o path e o python não se perder

    print(database)
   

    #Somar a coluna valor final
    total_gasto = database['ValorFinal'].sum()

    #Somar a coluna quantidade

    quantidade = database['Quantidade'].sum()

    #Total gasto / quantidade

    preco_medio = total_gasto / quantidade
    

    result = {
        "total_gasto": total_gasto,
        "quantidade": quantidade,
        "preco_medio": preco_medio
        }

    return result

result = calculator()
print(result)

