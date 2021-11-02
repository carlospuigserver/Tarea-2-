# Juego Adivinar el número
for x in range(100):
    from random import randint
    cpu=randint(0,99)
numero=int(input("Dame un número (0-99)"))
intento=1

while numero!=cpu:
    while numero<0 or numero>100:
        print("No puedes jugar con este número")
        numero=int(input("Dame un número (0-99"))
        intento=intento+1
    if numero<cpu:
        print("El número que has elegido es demasiado pequeño")
        numero=int(input("Dame un número (0-99"))
        intento=intento+1
    else:
        print("El número que has elegido es demasiado grande")
        numero=int(input("Dame un número (0-99"))
        intento=intento+1
else:
    print("Felicidades, has conseguido finalizar el juego")
print("Has tenido que emplear",intento,"oportunidades para lograrlo" )    