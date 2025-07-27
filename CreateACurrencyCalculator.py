#can use this for any currency to see how much you have left in USD


p = int(input("What do you have left in pesos? "))    
s = int(input("What do you have left in soles? "))
r = int(input("What do you have left in reais? "))
peso = p * .054  #current exchange rate of peso to USD. $1 peso = .$054 USD
sole = s * .28   #current exchange rate of sole to USD
reais = r * .18  #current exchange rate of reais to USD
x = peso + sole + reais    #adding all of the final values together 
print(f"${x:.2f} in USD")   #.2f ensures 2 decimal points



#acurrency calculator from USD to Euros

i = int(input("Enter an amount in $USD: "))
euro = i * .85  #current exchange rate of USD to Euro
print(f"{euro: .2f}")
