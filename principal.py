import math
def area_cuadrado(lado):
	area=lado**2
	print(f"El area es {area}")

def rhombusArea(d1,d2): 
    area = (d1*d2)/2
    return area
	
area_cuadrado(6) 
	

def teoremaHeron(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s(s-a)(s-b)(s-c))
    return area
  
teoremadeHeron = teoremaHeron(5,6,3)
print(f"el area es: {teoremadeHeron}")
