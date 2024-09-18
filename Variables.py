#Este archivo contara con las diferentes varibles
#que cuenta python
x=5         #x es una variable de tipo entero de tipo entero
y="John"    #y es una variable de tipo str (String) o cadena de texto
print(x)
print(y)

"""
Las variables tienen ciertas restricciones para ser nombradas como 
las que inician por numero, las que en su nombre 
llevan un - o un " " espacio

Para definir de manera estricta un tipo en una variable se crea de
la siguiente manera
"""
print("TIPOS DE VARIABLES")
x=str(3)    #Var del tipo str e imprime '3' de manera de texto
y=int(3)    #Var del tipo int e imprime 3
z=float(3)  #Var del tipo float e imprime 3.0
print(x)
print(y)
print(z)

"""
Se pueden crear multivariables, ¿a que refiere esto?, pues a que puedo
crear varias variables en una misma linea de la siguiente manera, sin
importar el tipo que sean
"""
print("MULTIVARIABLES")
x,y,z="Orange","Banana",9
print(x)
print(y)
print(z)
"""
Con este tipo de multivariables, se pueden almacenar los datos de una
lista en variables individuales
"""
print("DESARMAR LISTAS")
numbers = [7, 3.5, 6]
x, y, z = numbers
print(x)
print(y)
print(z)
"""
Existe una manera de ahorrarse prints, la cual es uniendo los datos
que quieras, con una comma o un +, eso si, si las variables son de diferentes
tipos, el + no servira para concatenar esos datos, exclusivamente en esos
casos se utilizara la comma
"""
print("CONCATENAR VARIABLES")
x, y= 5, 10
print(x+y)
str1,str2= "Hola", "Mundo"
print(str1+str2)
"""
Las variables globales se pueden crear de 2 maneras creandola afuera de
la funcion o con la keyword "global" dentro de la funcion
"""
print("VARIABLES GLOBALES")
x=154
def myFunction():
    print("the number is:", x)
myFunction()
    
def fuction():
    global y
    y="Pop"
    print("The bomb", y)
fuction()
