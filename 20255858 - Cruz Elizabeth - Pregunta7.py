DUI = input()

exten = len(DUI)
condi1 = exten == 10

condi2 = DUI[8] == "-"

condi3 = DUI[-1] == int #aqui no se una condicion que me haga saber si es entero o no 

print(condi1 and condi2 and condi3)


