def conversor_a_dolar(tipo_de_moneda, valor_dolar):
    pesos = float(input("\nCuantos pesos " + tipo_de_moneda + " quiere convertir? "))
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    print("\nEquivalen a:", dolar, "dolares\n")

def conversor_a_pesos(valor_dolar):
    dolar = float(input("\nCuantos dolares quiere convertir? "))
    pesos = dolar * valor_dolar
    pesos = round(pesos, 2)
    print("\nEquivalen a:", pesos, "pesos\n")

opc = input("Elija una opcion: \n   [1] De pesos argentinos a dolares \n   [2] De pesos colombianos a dolares \n   [3] De pesos mexicanos a dolares \n   [4] De dolares a pesos argentinos \n   [5] De dolares a pesos colombianos \n   [6] De dolares a pesos mexicanos \n\n   ")

if opc == "1":
        conversor_a_dolar("argentinos", 290)

elif opc == "2":
        conversor_a_dolar("colombianos", 3875)

elif opc == "3":
        conversor_a_dolar("mexicanos", 24)

elif opc == "4":
        conversor_a_pesos(290)

elif opc == "5":
        conversor_a_pesos(3875)

elif opc == "6":
        conversor_a_pesos(24)

else:
        print("********ERROR********")