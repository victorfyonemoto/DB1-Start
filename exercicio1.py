#1: Faça um Programa que mostre a mensagem "Alo mundo" na tela.


print("Hello World !")
print("Alo Mundo")


#2: Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número].""

n1 = int(input("Digite um número inteiro: \n"))

print(f"O número que você digitou foi: {n1} !")


#3: Faça um Programa que peça dois números e imprima a soma.


print("Vamos somar dois números")

n1 = float(input("Digite o primeiro número: \n"))

n2 = float(input("Digite o segundo número: \n"))

soma = n1 + n2

print(f"O resultado da soma é {soma}")


#4: Faça um Programa que peça as 4 notas bimestrais e mostre a média.


primeiraNota = float(input("Digite a nota do primeiro bimestre: \n"))

segundaNota = float(input("Digite a nota do segundo bimestre: \n"))

terceiraNota = float(input("Digite a nota do terceiro bimestre: \n"))

quartaNota = float(input("Digite a nota do quarto bimestre: \n"))

media = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

print(f"Sua média é {media:.1f}.")


#5: Faça um Programa que converta metros para centímetros.


medidaMetros = float(input("Digite uma medida em metros: \n"))

medidaCent = medidaMetros * 100

print(f"{medidaMetros} metro(s) é equivalente a {medidaCent} centímetro(s)")


#6: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


import math

raioCirculo = float(input("Digite o raio do círculo na medida que desejar: \n"))

areaCirculo = math.pi * (raioCirculo ** 2)

print(f"A área do círculo é de {areaCirculo:.1f} da medida ao quadrado")


#7: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.


dimensaoQuadrado = float(input("Digite a dimensão do quadrado: \n"))

areaQuadrado = dimensaoQuadrado * dimensaoQuadrado

dobro = areaQuadrado * 2

print (f"O dobro da área desse quadrado é de {dobro:.1f}")