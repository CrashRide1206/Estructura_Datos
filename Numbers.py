"""
Como lo mencionamos en nuestro archivo DataTypes.py, existen diferentes
tipos numericos para crear variables, como el int, el float o el complex

"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
"""
Empecemos por explicar el tipo int o integer, que abarca positivos y
negativos de longitud ilimitada
"""
x = 6
y = 45522153862
z = -885512563

print(type(x))
print(type(y))
print(type(z))
"""
Los Floats es el tipo de dato que contempla los numeros decimales
"""
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
"""
Los datos complejos son aquellos que abarca la parte imaginaria de los numeros
"""
x = 7+1j
y = 4j
z = -14j

print(type(x))
print(type(y))
print(type(z))

"""
Los datos se pueden convertir a otros como lo observaremos a continuacion
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)

b = int(y)

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
