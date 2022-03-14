import math
def area_cuadrado(lado):
	area=lado**2
	print(f"El area es {area}")

def rhombusArea(d1,d2): 
    area = (d1*d2)/2
    return area
	
area_cuadrado(6) 
	
# coding: utf-8
# volumen de un paralelepipedo Jaime Díaz
def Volumen_del_paralelepipedo(n1,n2,n3):
    volum = (n1*n2*n3)
    return volum
    
n1 = float( input("Ingreasa medida del lado a: " ))
n2 = float( input("Ingreasa medida del lado b: " ))
n3 = float( input("Ingreasa medida del lado c: " ))

res = Volumen_del_paralelepipedo(n1,n2,n3)
print(f"El volumen es {res}")
