# condicional - if
# operadores de comparacion
# > mayor
# < menor
# >= mayor igual
# <= menor igual

# ejemplo N°1 

precio= int ( input ("ingrese el precio"))
if precio > 500:
       print ("tiene descuento")
else:
       print ( " no tiene descuento ")
       
# igual ==

if precio== 500:
   print ("tiene descuento")
else :
    print ("no tiene descuento")   
          
 
# if caracteres o texto 

lenguaje=str (input (" ¿cual lenguaje de programcion esta estudiando?"))

#lenguaje= lenguaje.capitalize()

if lenguaje == "Python":
    print ("Excelente")
else:
    print ("mala eleccion")            
    
# upper () devuelve una cadena en mayuscula
# lover () devuelve una cadena en minuscula
# capitalize devuelve en la primera letra en mayucula

#Evaluar un Boolean

usuario=True
if usuario:
    print ("verdadero") 
else:
    print ("falso")    

#if anidados 

num3= int(input("ingrese un numero."))  
if num3% 2 == 0: # comprueba si el numero es par
    if num3 > 10:
        print (" el numero es mayor de 10 y es par " , num3)   
    else:
        print ("el numero no es mayor que 10, pero es par ", num3)   
else:
    print (" el numero no es par ", num3) 
               