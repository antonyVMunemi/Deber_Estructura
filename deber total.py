#Nombre: Robert Antony Vera Medina
#Asignatura: Estructura de datos 
#Carrera: Ingenieria en software A1
#nivel: tercer semestre

from datetime import date
class Operaciones:

     #Operaciones de suma,resta,multiplicacion , division, modulo

    def operaciones(self):
        numero1 = int(input("ingresar un numero:"))
        numero2= int(input("Ingresar el segundo numero:"))
        a =  numero1 + numero2 
        b =  numero1 - numero2
        c =  numero1 * numero2 
        d =  numero1 / numero2
        e =  numero1 % numero2

        print ("La suma es: {}".format(a))
        print ("La resta es: {}".format(b))
        print ("La multiplicacion es: {}" .format(c)) 
        print ("La division es: {}".format(d))
        print ("La modulo es: {}".format(e))

     #Resolver la hipotenusa
    def hipotenusa(self):
        numero1 = int(input("Ingresar un numero: "))
        numero2 = int(input("Ingresar el segundo numero: "))
        h= ((numero1)^2 + (numero2)^2)**0.5
        print("La hipotenusa es: {}".format(h))

     # Resolver la resolvente
    def resolvente(self):
        numero1=int(input("Ingresar el primer numero numero: "))
        numero2=int(input("Ingresar el segundo numero: "))
        num3=int(input("Ingresar el tercer numero: "))

        determinante = ((numero2)^2)- 4 * numero1 * num3

        if determinante > 0:
            x1 = (-numero2 + (determinante))**0.5/(2*numero1)
            x2 = (-numero2 - (determinante))**0.5/(2*numero1)
            print ("Tiene dos soluciones")
        elif determinante == 0:
            x = -numero2 / (2*numero1)
            print ("Tiene una sola solucion")
        else:
            print ("No tiene solucion")

     #Saber cuando un numero es par e impar
    def paridadEimparidad(self):
        numero1 = int(input("Ingresar un numero: "))
        if numero1 % 2 == 0:
            x4 = "0 par"
            return x4
        else:
            x5 = "1 impar" 
            return x5 
        
     #Dado un (1) n??mero binario de cuatro (4) d??gitos imprimir su bit da paridad El bit 
     #de paridad es 1 si el n??mero de bits 1 es impar y 0 en caso contrario
    def bitParidad(self):
        binario = int(input("Ingesar un numeor binario de 4 digitos: "))
        bit1 = int(binario[0])
        bit2 = int(binario[1])
        bit3 = int(binario[2])
        bit4 = int(binario[3])
        contador = bit1 + bit2 + bit3 + bit4
        if contador % 2 == 0:
            print ("El bit de paridad es 0")
        else:
            print ("El bit de paridad es 1")

     #Dado un (1) n??mero binario de cuatro (4) d??gitos imprimir su valor
    def imprimeValor(self):
        nbin = int(input("Ingresar un segundo numero binario de 4 digitos: "))
        m1 = int (nbin[0])
        m2 = int (nbin[1])
        m3 = int (nbin[2])
        m4 = int (nbin[3])
        bin_decimal = (m4*2**0) + (m3*2**1) + (m2 *2**2) + (m1 *2**3)
        print ("El valor del numero binario es: {}".format(bin_decimal))

     #Calcular un numero verificanco cual es la unidad de mil, centena, decena, unidad
    def cuatroDigitos(self):
        num6 = int(input("Ingresar un numero que tenga 5 digitos o mayor: "))
        while num6 > 1000 or num6 < 9999:
            unidadDemil = num6 // 1000 
            print ("la unidad de mil es:", unidadDemil)
            centena = (num6 - (unidadDemil * 1000))//100
            print ("la centena es:", centena)
            decena = (num6-(unidadDemil * 1000 + centena * 100))// 10
            print ("La decena es:", decena)
            unidad = (num6-(unidadDemil * 1000 + centena *100 + decena *10))//1
            print ("La unidad es:", unidad)
            break

        #Calcular cuando es un a??o bisiesto
    def bisiesto(self):
        ddmmaaaa = int(input("Ingresar un numero en el formato ddmmaaaa: "))
        a??o = ddmmaaaa % 10000
        dia = ddmmaaaa // 1000000
        mes = (ddmmaaaa // 10000) % 100
        if ((a??o % 4 == 0) and (a??o % 100 != 0) or (a??o % 400 == 0)):
            print ("Es Bisiesto")
            
        else:
            print ("No es bisiesto")

        #Ejercicio de un cuando un numero es capicua
    def capicua(self):
        num7= int(input("Ingresar un numero que tenga mas de 5 digitos: "))
        if num7 > 9999 and num7 < 99999:
            if str(num7) == str(num7)[::-1]:
                print("es capicua")
            else:
                print("no es capicua")
        else:
            print("La cantidad de digitos no es correcta")

        #Cree un algoritmo que tome por entrada las horas y minutos de un d??a y d?? como 
        #resultado su equivalente en segundos
    def entradaHoraMinuto (self):
        hora = int(input("Ingresar las hora: "))
        minutos = int(input("Ingresar los minutos: "))
        segund_1 = hora * 60 * 60
        print("La hora equivalente en segundo es: {}".format(segund_1))
        segund_2 = minutos * 60
        print ("Los minutos equivalente en segundo es: {}".format(segund_2))


         # Para un valor entero positivo que representa una cantidad en segundos, indicar 
         #su equivalente en minutos, horas y d??as
    def convertirSegundo(self):
        segundos_0 = int(input("Ingresar un numero en segundos: "))
        if segundos_0 > 0:
            minutos = segundos_0 / 60
            minutosround = round(minutos,2)
            print ("Son:", minutosround, "minutos")

            horas = segundos_0 / 3600
            horasround = round (horas, 2)
            print ("Son:", horasround, "Horas")

            dias = segundos_0 / 86400
            diasround = round(dias, 2)
            print ("Son:",diasround, "dias")
        else:
            print ("El valor es negativo, vuelva a ingresar un dato")

        #Dados tres n??meros enteros positivos A, B y C, determine ??cu??l de ellos es el 
        #mayor? y ??cu??l es el segundo mayor?
    def mayorSegundoMayor(self):
        A = int(input("Ingresar un numero: "))
        B = int(input("Ingresar el segundo numero: "))
        C = int(input("Ingresar el tercer numero: "))
        
        if A and B and C > 0:
            if C < B > A:
                print("El primer numero mayor es: {}".format(B))
                if A > C:
                    print("El segundo numero mayor es: {}".format(A))
                else:
                    print("El segundo numero mayor es: {}".format(C))
            elif B < C > A:
                print ("El primer numero mayor es: {}".format(C))
                if A > B:
                    print("El segundo mayor es: {}".format(A))
                else:
                    print("El segundo mayor es: {}".format(B))
            elif C < A > B:
                print("El primer mayor es: {}".format(A))
                if B > C:
                    print("El segundo mayor es: {}".format(B))
                else:
                    print("El segundo mayor es: {}".format(C))
            else:
                print("Todos los numeros son iguales")
        else:
            print("Digite un numero que sea mayor que 0")
         #El IMC resulta de la divisi??n de la masa del individuo (en kilogramos) entre el 
         #cuadrado de la estatura (en metros) El ??ndice de masa corporal es un indicador 
         #del peso de una persona en relaci??n con su altura
    def pesoCorporal(self):
        libra = float(input("ingrese el peso el libras: "))
        centime = int(input("ingrese la altura en centimetros: "))

        kgramo = libra * 0.453592
        metro = centime / 100 

        imc = kgramo / (metro ** 2)

        print ("Su peso es de: ",round(kgramo, 1),"kg")
        print ("Su IMC es de: ",round(imc, 1))

        if imc <= 15:
            print("Condicion: Criterio de ingreso")
        elif imc >= 16 and imc <= 16.9: 
            print("Condicion: Infra peso")
        elif imc >= 17 and imc <= 18.4:
            print("Condicion: Bajo peso")
        elif imc >= 18.5 and imc <= 24.9: 
            print("Condicion: Peso Normal")
        elif imc >= 25 and imc <= 29.9:
            print("Condicion: Sobrepeso")   
        elif imc >= 30 and imc <= 34.9: 
            print("Condicion: Obesidad pre-m??rbida")
        elif imc >= 40 and imc <= 45:
            print("Condicion: Obesidadad M??rbida")
        else:
            print("Condicion: Obesidad hiper-m??rbida")

     #Escriba un algoritmo que reciba una fecha (d??a y mes) correspondiente al a??o 
     #2014 e imprima por pantalla el n??mero de d??as que han pasado desde el 1 de 
     #Enero de 2014 hasta la fecha dada
    def recibaFecha(self):
        mesd = int(input("ingresar un mes: "))
        dias = int(input("Ingresar un dia: ")) 
        hoy = date(2014,mesd, dias)
        otra_fecha = date(2014,1,1)
        dias_pasan = hoy - otra_fecha
        print ("Han pasado", dias_pasan.days, "dias desde el 1 de enero del 2014")
    
        #Saber por medio del numero si son los meses del a??o
    def mesCorrespondiente (self):
        meses = int(input("Ingresar un numero del 1-12: "))
        if meses >= 1 and meses <= 12:
            if meses == 1:
                print("Enero")
            if meses == 2:
                print("febrero")
            if meses == 3:
                print("marzo")
            if meses == 4:
                print("abril")
            if meses == 5:
                print("mayo")
            if meses == 6:
                print("junio")
            if meses == 7:
                print("julio")
            if meses == 8:
                print("agosto")
            if meses == 9:
                print("septiembre")
            if meses == 10:
                print("octubre")
            if meses == 11:
                print("noviembre")
            if meses == 12:
                print("diciembre")
        else:
            print("dato mal dado")

      #En un almac??n se hace un 20% de descuento a los clientes cuya compra supere 
      #los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a 
      #pagar por el cliente y arroje como salida el monto aplicando el descuento de ser 
      #necesario
    def compra(self):
        precio = float(input("Ingresar un precio que sea mayor de 1000: "))
        if precio > 1000:
            descuento = precio * 0.20
            precio_final = precio - descuento
            print ("El precio a pagar del producto es:",precio_final)
        elif precio < 1000:
            precio_final = precio 
            print ("El precio del producto a pagar es de:", precio_final)
    
     #Dado un n??mero entero N, calcular e informar al usuario cu??ntos d??gitos tiene 
     #dicho n??mero
    def informeUsuario(self):
        entero = int(input("Ingresar un numero entero:"))
        while entero < 0 or entero >= 0 :
            digitos = len(str(entero))
            print ( "El numero tiene",digitos,"digitos")
            break
     #Dado un n??mero, determine si es capic??a
     #Nota: un n??mero capic??a es aquel que se lee igual hacia adelante que hacia atr??s
    def variaci??nCapic??a(self):
        num15 = int(input("Ingresar un numemero:"))
        if str(num15) == str(num15)[::-1]:
            print ("%i es capic??a" %num15)
        else:
            print ("%i no es capic??a" %num15)
    
     #Dado un n??mero N determinar si es un n??mero primo
     #Nota: Un n??mero primo es aquel que solo es divisible por 1(uno) y por el mismo
    def numeroPrimo(self):
        nprimo = int(input("Ingresar un numero para saber si es primo:"))
        for i in range(2, nprimo):
            if nprimo % i == 0:
                print ("El numero {}".format(nprimo),"no es primo")
            else:
                print("El numero {}".format(nprimo),"s?? es primo ")
                break
     #Construya un programa que dado un valor entero N, haga el c??lculo de la funci??n 
     #factorial utilizando estructuras iterativas
    def calculoFuncion(self):
        n = int(input("Ingresar un numero para calcular el factorial:"))
        if n > 0:
            z = 1
            for i in range(1, n+1):
                z = z * i
            print("El factorial de",n,"es", z)
        else:
             print("El numero no puede ser negativo!!!!!!!!!")

     #Dado un n??mero entero N que representa una contrase??a y asumiendo que una contrase??a debe tener al menos 10 d??gitos para ser segura, determine si la 
     #contrase??a ingresada por el usuario es correcta, de no serlo debe pedirla nuevamente hasta que tenga los 10 (diez) d??gitos solicitados y al ser correcta 
     #mostrar un mensaje de ??xito al usuario, por salida est??ndar
    def Inicio (self):
        contrase??a = int(input("Ingresar una contrase??a de 10 digitos:"))
        m = 0
        while contrase??a > 0:
            contrase??a //= 10
            m = m +  1
        if m == 10:
            print("la contrase??a es correcta")
        else:
            print("La contrase??a es incorrecta")

     #Dada una secuencia de n??meros terminada en cero (0), elaborar un algoritmo que 
     #informe al usuario qu?? valor tiene el n??mero mayor y qu?? valor tiene el n??mero 
     #menor, sin contar el cero (0)
    def pedir_numero(self):
        lista = []
        a = True
        while a:
            num = int(input("Ingresar un numero(ingrese el 0 si desea terminar)"))
            if num == 0:
                a = False
            else:
                lista.append(num)
        mayor,menor=Operaciones.mayor_menor(lista)
        if len(lista) > 0:
            print("El numero mayor es:",mayor)
            print("El numero menor es:",menor)
    def mayor_menor(lista):
        mayor = 0
        menor = 9999999999999999999999
        for num in lista:
            if num > mayor:
                mayor = num
            
            if num < menor:
                menor = num
        return mayor,menor

     #Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla 
     #del 1 hasta la del 10
    def tablaMultiplicar(self):
        mult = int(input("Ingresar un numero para saber la tabla de multiplicar:"))
        for i in range(0,11):
            resultado = i * mult
            print (mult,"x",i,"=",resultado)

     #Escribir un algoritmo que muestre todas las fichas de domin??, sin repetir
    def domino(self):
        for i in range(0,7):
            for j in range(0 , i + 1):
                print("|"+ str(i) + "|"+str(j) + "|")

     #Dados N n??mero positivos (N>1) calcular el promedio de esta serie Considere que 
     #la serie termina al leer un 0
    def promedio(self):
        num20 = int(input("Ingresar un numero:"))

        contador = 0
        suma = 0
        while num20 > 1:
            num20 = int(input("ingreser otro dato"))
            suma = suma + num20
            contador = contador + 1
        if contador == 0:
            print("No tiene ningun digito")
        else:
            promedio = suma / contador
            print("El promedio de los {}".format(contador), "numero es igual a {}".format(promedio))


        # Construya una funci??n que solicite edades al usuario y determine el promedio de 
        # las edades mayores a 18 a??os. El usuario indicar?? cuando desea dejar de 
        # suministrar datos de entrada. En la Acci??n Principal se informar?? el promedio 
        # calculado.
    def edades(self):
        lista = []
        t = True
        while t:
            edad = int(input("Ingresar una edad y si desea parar ingresar cero pero las edades deben ser mayor de 18:"))
            if edad > 18:
                lista.append(edad)
            else:
                t = False

        promedio = Operaciones.promedio_edad(lista)
        if len(lista) > 0:
            print("El promedio de todas las edades es:",promedio)
        else:
            print("No se puede calcular el promedio:")

    def promedio_edad(lista):
        for edad in lista:
            if edad > 18:
                promedio = sum(lista)/len(lista)
                return promedio

     #Construya una funci??n ???Eleva??? Que reciba como par??metros una base y un 
     #exponente y retorne al algoritmo principal el resultado de elevar un numero al otro
    def Eleva(self):
        base = int(input("Ingresar un numero: "))
        exponente = int(input("Ingreser un exponente: "))
        potencia = Operaciones.potencia(self,base,exponente)
        print("El numero {}".format(base),"elevado al exponente {}".format(exponente),"es {}".format(potencia))
    def potencia(self,base,exponente):
        potencia = base ** exponente
        return potencia

     #Escriba una funci??n que calcule el per??metro del pent??gono (siendo el per??metro la 
     #suma de los lados del pol??gono)
    def perimetropentagono(self):
        acum = 0
        for i in range(5):
            lado = int(input("Ingrese la medida de un lado: "))
            acum = Operaciones.perimetro(acum,lado)
        print ("El perimetro es: {}".format(acum))
        
    def perimetro(acum,lado):
        acum = acum +lado
        return acum


    #En una empresa pagan seg??n las horas trabajadas y una tarifa fija por hora. Si la cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se 
    #incrementa en un 35% para las horas extras. Escribe una acci??n principal que solicite la identificaci??n de 5 empleados, el monto cancelado por hora, y la cantidad de horas trabajadas por cada uno, llame a acciones/funciones que 
    #calculen el salario semanal por horas trabajadas (<=40) y los ingresos por concepto de horas extras, y finalmente informe los resultados en la acci??n 
    #principal.
    def nombreTrabajador(self):
        id = {}
        acp = Operaciones()

        while len(id) <= 4:
            a = input("Ingresar su identificacion(Nombre): ")
            id[a] = int(input("Ingresar horas trabajadas {}: ".format(a)))
        horas = int(input("Ingresar el monto por hora: "))

        ss = acp.calcularSalario(id,horas)
        for i in ss:
            print(i,"cobrara",ss[i][1])
    def calcularSalario(self,a , ht):
        Cacp = Operaciones()
        for i in a:
            if a[i] <= 40:
                a[i] = [a[i],(a[i]*ht)]
            
            else:
                a[i] = [a[i],(40*ht)]
                a[i][1] = Cacp.aumentoTarifa(a[i],ht)
        print("*"*20)
        return a
    def aumentoTarifa(self,k ,ht):
        extr = k[1] + ((k[0]-40)*(ht+(ht*0.35)))
        return extr

        # Escriba una acci??n (MillasAKilometros) que convierta una distancia en millas a kil??metros (1milla = 1.60935km). Esta acci??n recibir?? como par??metros: el nombre 
        # de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre ellas y debe retornar la distancia entre las ciudades en kil??metros.Desarrolle adem??s una acci??n principal en donde utilice a la acci??n 
        # MillasAKilometros para convertir e informar la distancia en kil??metros entre 4 pares de ciudades suministradas por el usuario.
    def nombreCiudad(self):
        for i in range (4):
            ciudad_1 = input("Ingrese la ciudad de origen: ")
            ciudad_2 = input("Ingresar la ciudad de destino: ")
            kilometros = Operaciones.MillasAkilometro(self)
            print("La distancia entre: {}".format(ciudad_1),"y {}".format(ciudad_2), "es de {}".format(kilometros),"Km")

    def MillasAkilometro(ciudad):
        numero_millas = float(input("Ingrese una distancia(en millas): "))
        kilometros = numero_millas * 1.60935
        return kilometros


var = Operaciones()
