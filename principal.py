import math
def area_cuadrado(lado):
	area=lado**2
	print(f"El area es {area}")

def rhombusArea(d1,d2): 
    area = (d1*d2)/2
    return area

def circleArea(r):
    result = (math.pi)*(r*r)
    return result

# volumen de un paralelepipedo Jaime Díaz
def Volumen_del_paralelepipedo(n1,n2,n3):
    volum = (n1*n2*n3)
    return volum
	
area_cuadrado(6) 
rhombusArea(5,10):
	
 
n1 = float( input("Ingreasa medida del lado a: " ))
n2 = float( input("Ingreasa medida del lado b: " ))
n3 = float( input("Ingreasa medida del lado c: " ))

res = Volumen_del_paralelepipedo(n1,n2,n3)
print(f"El volumen es {res}")

def volcub(a):
    volC = a * a * a
    print(f"El volúmen del cubo es: {volC} cm")
volcub(5)
