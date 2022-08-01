

print("!!!Bievenido¡¡¡")
print("Vamos a averiguar cuanto dinero ha ganado en Cryptos")

#What Crypto

crypto = str(input("¿Como se llama la crypto que compraste? "))
print("Ummm,",crypto,"esta muy bien.")


#How many times did he\she bought

times = int(input("¿Cuantas veces compraste? "))

for ejecution in range(times) :

    #First buy

    how_many = float(input("¿Cuantas monedas compraste? "))
    price_before = float(input("¿A cuanto cotizaba en ese momento? "))
    price_now = float(input("¿A cuanto cotiza ahora? "))


    #Diference of one crypto
    
    diference = price_now - price_before
    earnings = diference * how_many
    if earnings >= 0 :
        print("Con esta compra has ganado", earnings,"$")

    else :
        print("Con esta compra has perdido", earnings,"$")
