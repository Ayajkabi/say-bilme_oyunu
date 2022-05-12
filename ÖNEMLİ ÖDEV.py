import random as r
d=input("zor için z kolay icin k ara kolaylık icin o ")
if d=="z":
	c=2
elif d=="o":
	c=5
else:
	c=10
pc=int(r.random()*100)
for i in range(c):
	a=int(input("sec"))
	if a==pc:
		print("helal")
		break
	elif a>pc:
		print("daha kucuk")
	elif a<pc:
		print("daha buyuk")
	else:
		print("yanlış")
print("asıl sayı=",pc)