#definir funcion, respetar sangria

def menu():
    print("1. sumar\n")
    print("2. restar\n")
    print("3. multiplicar\n")
    print("4. division entera\n")
    print("5. division\n")
    print("6. modulo\n")
    print("7. potencia\n")
    print ("8. terminar programa\n")

def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a -b

def multiplicar(a, b):
    return a*b

#division
def div_entera(a, b):
    if b == 0:
        print("Error, division entre 0")
        return
    return a//b

def div(a, b):
    if b == 0:
        print("Error, division entre 0")
        return
    return a/b

def modulo(a, b):
    if b == 0:
        print("Error, division entre 0")
        return
    return a% b

def  potencia(a, b):
    return a**b

def main():
    menu()
    print("Ingrese una opcion")
    op = int(input()) 
    while op !=8:

        if op == 1:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())        
            print(sumar(x, y))
            menu()
            break

        elif op == 2:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())
            print(restar(x, y))
            menu()
            break

        elif op ==3:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())
            print(multiplicar(x, y))
            menu()
            break

        elif op == 4:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())
            print(div_entera(x, y))
            menu()
            break

        elif op == 5:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())
            print(div(x, y))
            menu()
            break

        elif op == 6:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())
            print(modulo(x, y))
            menu()
            break

        elif op == 7:
            print ("Ingrese dos valores")
            x = int(input())
            y = int(input())
            print(potencia(x, y))
            menu()
            break
        
        else:
            print("Opcion no valida")
            menu()
            break
    
    main()

  

   
        

if __name__ == "__main__": #solo se ejecuta si se escribe el nombre de codigo
    main()
    
        



