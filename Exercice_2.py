# Exercice sur les conditions : 

print (" Entrer le premier nombre : ")
a = input() 

print (" Entrer le deuxieme nombre : ")
b = input() 

print (" Entrer l'operateur : ")
c = input()

if (c == "+") :
    S = int (a) + int (b)
    print("La somme des deux nombres ",a, "et" ,b, " est " ,S)
elif (c == "-") :
    Sou = int (a) - int (b)  
    print("La soustraction des deux nombres ",a, "et" ,b, " est " ,Sou)
elif (c == "/" and b!=0):
    Div = int (a) / int (b)
    print("la division des deux nombres ",a, "et" ,b, " est " ,Div)
else : 
    Mult = int (a)* int(b)
    print("La multiplication des deux nombres ",a, "et" ,b, " est " ,Mult)   






