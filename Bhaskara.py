a=float(input("Leia A: "))
b=float(input("Leia B: "))
c=float(input("Leia C: "))
delta=(b**2)-(4*a*c)
import math
if delta<0:
	print("Delta menor que zero. Não há raizes reais nesta equação.")
	
 else: 
	if delta==0:
		x= (-b+delta) / (2*a)
		print ("Único resultado: ", x)
		
if delta>0:
		x1= (-b + math.sqrt(delta)) / (2*a)	
		x2= (-b - math.sqrt(delta)) / (2*a)	
		print ("Raízes são: ", x1, " e ", x2)
	
	

	
---------------------------
a=float(input("Leia A: "))
b=float(input("Leia B: "))
c=float(input("Leia C: "))
delta=(b**2)-(4*a*c)
import math
if delta<0:
	print("Delta menor que zero. Não há raizes.")
else: 
	    if delta==0:
		    x= (-b+delta) / (2*a)
		    print ("Único resultado: ", x)
		    
if delta>0: 
		      x1= (-b + math.sqrt(delta)) / (2*a)	
		      x2= (-b - math.sqrt(delta)) / (2*a)	
		      print ("Raízes são: ", x1, " e ", x2)
	