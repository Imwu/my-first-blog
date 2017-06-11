if 3>2:
    print("Funguje to!")
if 3>2:
	print("5 je fakt vetsi nez 2")
else:
	print("5 neni vetsi nez 2")

name= "Ivana"
if name == "Ola":
	print("Ahoj Olo!")
elif name == "Ivana":
	print("Ahoj Ivano!")
else:
	print("Ahoj cizinko!")

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

#Change the volume if its too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That is better!")
