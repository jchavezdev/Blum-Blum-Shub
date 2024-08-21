#Exporta las librerias necesarias para la parte gráfica
from tkinter import *
#Exporto las librerias para operaciones aritméticas
from math import *

#p,q Dos numeros primos grandes
#p,q Deben ser congruentes a 3 mod 4
#x0  Es la semilla a usar (debe estar en binario)
#i   Es el numero de bits a incluir en la secuencia

def monobit(bin_data: str):

    count = 0
    # 
    for char in bin_data:
        if char == '0':
            count -= 1
        else:
            count += 1
    # Calcula según el método de monobit
    sobs = count / sqrt(len(bin_data))
    p_val = erfc(fabs(sobs) / sqrt(2))

    if p_val <= 0.5 and p_val > 0 : 
    	return True
    elif p_val >= -0.5 and p_val <0:
    	return True
    elif p_val==0:
    	return True
    else:
    	return False

def dec_to_bin(x):
    return int(bin(x)[2:])

def BlumBlumShub():

	try:
		num_dec = int(str(e3.get()),2)
		sec   = []
		for var in range(1,(int(e4.get())+1)):
			num_dec = num_dec*num_dec
			num_dec = num_dec % (int(e1.get())*int(e2.get()))
			bit   = str(dec_to_bin(num_dec))
			bit   = bit[-1:]
			sec.append(bit)
			print  (var,num_dec, str(dec_to_bin(num_dec)),bit)
		sec = ''.join(sec)
		e5.delete(0,len(e5.get()))
		#insert coloca la cadena 
		e5.insert(0,str(sec))
		#Verifica que la cadena sea buena

		result = monobit(sec)
		#print(result)
		if result==True:
			#Declaro un objeto de la clase Text
			texto2=Text(v)
			#Inserto el mensaje
			texto2.insert(INSERT,"La cadena es segura")
			#Posiciono el mensaje
			texto2.place(x=10,y=360)
		else:
			#Declaro un objeto de la clase Text
			texto2=Text(v)
			#Inserto el mensaje
			texto2.insert(INSERT,"La cadena no es segura")
			#Posiciono el mensaje
			texto2.place(x=10,y=360)

		return

	except ValueError:
		 #Declaro un objeto de la clase Text
		texto=Text(v)
		#Inserto el mensaje
		texto.insert(INSERT,"Debes introducir una cadena que sea un número")
		#Posiciono el mensaje
		texto.place(x=10,y=360)

	except Exception as e:
		print(type(e).__name__)

#def BlumBlumShub(p,q,x0,i):
   #num_dec = int(str(x0),2)
   #sec   = []
   
   #print "Semilla X0 = ", x0, " en decimal = ", num_dec
   #print "Numero primo p = ", p
   #print "Numero primo q = ", q
   #print "Numero de bits en la secuencia a generar = ", i
   
   #for var in range(1,i+1):
     #num_dec = num_dec*num_dec
     #num_dec = num_dec % (p*q)
     #bit   = str(dec_to_bin(num_dec))
     #bit   = bit[-1:]
     #sec.append(bit)
     #print  (var,num_dec, str(dec_to_bin(num_dec)),bit)
   #sec = ''.join(sec)
   #print (sec)
   #return


#Aqui declaramos nuestra ventana principal
v=Tk()

########################################################
######Declaramos las entradas de nuestro programa#######
########################################################

#Crea un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l1=Label(v,text="Inserta un número primo p")
#Posiciono mi objeto
l1.place(x=10,y=10)
#La funcion recibe la ventana donde estara y el texto a mostrar
l6=Label(v,text="p debe ser un número grande y congruente a 3 mod 4")
#Posiciono mi objeto
l6.place(x=10,y=40)
#Creo la entrada 
#La funcion recibe la ventana donde estara y su tamaño
e1=Entry(v,bd=5)
#Posiciono mi entrada
e1.place(x=200,y=10)

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l2=Label(v,text="Inserta un número primo q")
#Posiciono mi ventana
l2.place(x=10,y=90)
#La funcion recibe la ventana donde estara y el texto a mostrar
l7=Label(v,text="q debe ser un número grande y congruente a 3 mod 4")
#Posiciono mi ventana
l7.place(x=10,y=120)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e2=Entry(v,bd=5)
#Posiciono mi entrada
e2.place(x=200,y=90)

#Crea un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l3=Label(v,text="Inserta la semilla inicial en binario")
#Posiciono mi objeto
l3.place(x=10,y=170)
#La funcion recibe la ventana donde estara y el texto a mostrar
l8=Label(v,text="Es la semilla a usar")
#Posiciono mi objeto
l8.place(x=10,y=195)
#Creo la entrada 
#La funcion recibe la ventana donde estara y su tamaño
e3=Entry(v,bd=5)
#Posiciono mi entrada
e3.place(x=200,y=170)

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l4=Label(v,text="Indica el número de bits")
#Posiciono mi ventana
l4.place(x=10,y=235)
#La funcion recibe la ventana donde estara y el texto a mostrar
l9=Label(v,text="No debe ser mayor a 20")
#Posiciono mi ventana
l9.place(x=10,y=255)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e4=Entry(v,bd=5)
#Posiciono mi entrada
e4.place(x=200,y=235)

#########################################################
##########Declaro el boton accionador####################
#########################################################
#Creo el botón
b=Button(v,text="Calcular",command=BlumBlumShub)
#Posiciono el botón
b.place(x=230,y=280)

#########################################################
##############Declaramos las salidas#####################
#########################################################

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l5=Label(v,text="Cadena resultante")
#Posiciono mi ventana
l5.place(x=10,y=320)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e5=Entry(v,bd=5)
#Posiciono la entrada
e5.place(x=200,y=320)

#BlumBlumShub(11,19,11,5)

#Tamaño de la ventana
v.geometry("400x400+10+10")
#La ventana principal esta en un loop infinito porque no queremos que se cierre
v.mainloop()