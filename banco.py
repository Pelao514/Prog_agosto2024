saldo= float (input("ingrese su saldo    "    ))
codigo= int( input ("ingrese codigo: 1 = extraccion - 2= prestamo - 3= pago servicio "))
if codigo==1:
    monto = float(input (" ingrese monto a extraer:   "))
    if monto<=saldo:
        saldo=saldo-monto
        print ("saldo actual es : ", saldo)
    else: 
        print (" no tiene saldo suficiente : ")
elif codigo==2:
    saldo=saldo+50000
    print ("saldo actual es :    ", saldo)
elif codigo==3:
    servicio=float (input (" ingrese el monto servicio a pagar :" )  )
    if servicio<=saldo:
        saldo=saldo-servicio
        print (" saldo actual es :    ", saldo)   
    else:
        print (" fondo insuficiente:   ", saldo )    
        
else: 
    print (" opcion no valida: ")            