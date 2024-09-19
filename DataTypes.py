"""
En Python existen diferentes tipos de datos para crear variables. A continuació
enumeraremos los tipos de datos:
Tipo texto: str
Tipo numerico: int, float, complex
Tipo Secuencial: list, tuple, range
Tipo Mapping: dict
Tipo Set: set, frozenset
Tipo Booleano: bool
Tipo Binario: bytes, bytearray, memoryview
Tipo None: NoneType
"""
print("TIPO DE DATOS")
a=str("Hola")
b=int(20)
c=float(23.4)
d=complex(1j)
e=["Arroz","Azucar"]
f=("Manzana","Pera")
g=range(6)
h={"Nombre":"Harol", "Edad": 18}
i={"fruta","vegetales"}
j=frozenset({"fruta","vegetales"})
k=bool(True)
l=b"Hola"
m=bytearray(5)
n=memoryview(bytes(5))
o= None