for numero in range(1,101):
    primo = True
    for i in range(1,numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero)
   
