#1- Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite o primeiro número \n"))
n2 = float(input("Digite o segundo número \n"))

if n1 > n2:
    print(f"O maior número é {n1}")
    print(f"O menor número é {n2}")
elif n1 < n2:
    print(f"O maior número é {n2}")
    print(f"O menor número é {n1}")
else:
    print("Os números são exatamente iguais !")

#2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input("Digite um número, vamos descobrir se ele é positivo ou negativo \n"))

if n1 > 0:
    print("O número é positivo !")
elif n1 < 0:
    print("O número é negativo !")
else:
    print("Você digitou o número 0")

#3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Olá ! Qual o seu sexo ? (F - Feminino ou M - Masculino): \n")

sexo = sexo.upper()

if sexo == "F":

    print("Você é do sexo Feminino !")

elif sexo == "M":

    print("Você é do sexo Masculino !")

else:

    print("Error: Digite um caractere válido")


#4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ['a', 'e', 'i', 'o', 'u']

l = input("Digite uma letra: \n")
l = l.lower()

if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
    print("Você digitou uma vogal !")
elif l.isalpha():
    print("Você digitou uma consoante !")
else:
    print("Error: Input Inválido")

#5 - Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada pelo aluno e apresentar:"
# A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
# A mensagem “Reprovado”, se a média for menor do que sete;
# A mensagem “Aprovado com Distinção”, se a média for igual a dez.”

n1 = float(input("Informe a primeira nota parcial \n"))
n2 = float(input("Informe a segunda nota parcial \n"))
media = (n1 + n2) / 2

if media >= 7.0:
    print(f"Aluno aprovado com média {media}!")
else:
    print(f"Aluno reprovado com média {media} !")

#6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro número: \n"))
n2 = float(input("Digite o segundo número: \n"))
n3 = float(input("Digite o terceiro número: \n"))

if n1 > n2 and n3 < n1:
    maior = n1
elif n2 > n1 and n3 < n2:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3
    print(f"{menor} é o menor número !")
    print(f"{maior} é o maior número !")

#7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_1 = float(input("Infome o preço do primeiro produto: \n"))
preco_2 = float(input("Infome o preço do segundo produto: \n"))
preco_3 = float(input("Infome o preço do terceiro produto: \n"))

menor = preco_1
if preco_2 < preco_3 and preco_2 < preco_1:
    menor = preco_2
elif preco_3 < preco_2 and preco_3 < preco_1:
    menor = preco_3
print("O produto de menor valor custa R$ {:.2f}".format(menor))
print("Portanto você deveria comprar o de menor valor")

#8 -  Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite o primeiro número: \n"))
n2 = float(input("Digite o segundo número:  \n"))
n3 = float(input("Digite o terceiro número: \n"))

maior = n1
if n2 > n1 and n2 > n3:
        maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3
    medio = n1
if n2 < maior and n2 > menor:
    medio = n2
elif n3 < maior and n3 > menor:
    medio = n3
print(f"Os números digitados em ordem decrescente são: {maior}, {medio}, {menor}")

#9 - Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso

turno = input("Qual o turno em que você estuda ? (M - Manhã, V - Vespertino, N - Noite)\n")
turno = turno.upper()
if turno == "M":
    print("Bom dia !")
elif turno == "V":
    print("Boa tarde !")
elif turno == "N":
    print("Boa noite !")
else:
    print("Error: valor inválido !")

#10 -  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa #que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float (input("Informe o salário atual: \n"))
if salario <= 280.00:
    salarioReajust = salario * 1.2
    percentual = 20
elif salario > 280.00 and salario <= 700.00:
    salarioReajust = salario * 1.15
    percentual = 15
elif salario > 700.00 and salario <= 1500.00:
    salarioReajust = salario * 1.10
    percentual = 10
elif salario > 1500.00:
    salarioReajust = salario * 1.05
    percentual = 5

reajuste = salarioReajust - salario

print(f"Você informou o salário de: R${salario:.2F}, portanto, o seu percentual de aumento será de {percentual}%, e o seu aumento em reais é de: R${reajuste:.2F}")
print(f"Resultando em um salário atualizado de R${salarioReajust:.2F}")

# 11 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações

horas = float(input("Quantas horas foram trabalhadas ?  \n"))
valorHora = float(input("Digite o valor/hora: \n"))
salarioBruto = horas * valorHora
fgts = salarioBruto * 0.11
descSind = salarioBruto * 0.03

if salarioBruto <= 900.00:
    salarioLiquido = salarioBruto - descSind
    percentIR = 0
    impostoRenda = 0.00
elif salarioBruto > 900.00 and salarioBruto <= 1500.00:
     impostoRenda = salarioBruto * 0.05
     salarioLiquido = salarioBruto - descSind - impostoRenda
     percentIR = 5
elif salarioBruto > 1500.00 and salarioBruto <= 2500.00:
    impostoRenda = salarioBruto * 0.10
    salarioLiquido = salarioBruto - descSind - impostoRenda
    percentIR = 10
elif salarioBruto > 2500.00:
    impostoRenda = salarioBruto * 0.20
    salarioLiquido = salarioBruto - descSind - impostoRenda
    percentIR = 20

print(f"O valor do seu salário bruto é R${salarioBruto:.2f}, e com os descontos correspontes ao valor do salário bruto: de FGTS no valor de R${fgts:.2F}, correspondente a 11%; desconto do sindicato, correspondente a 3% no valor de R${descSind:.2f}; e desconto do imposto de renda de ({percentIR}%) no valor de R${impostoRenda:.2f}.")
print(f"O seu salário líquido será, portanto, R${salarioLiquido:.2f}")

# 12 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor #deve aparecer valor inválido.

diaDaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

print("Qual o dia da semana ? Informe um número de 1 à 7 referente ao dia da semana \n")
dia = int(input("1 - Domingo | 2 - Segunda-feira | 3 - Terça-feira | 4 - Quarta-feira | 5 - Quinta-feira | 6 - Sexta-feira | 7 - Sábado \n"))

if dia == 1:
    print(f"Hoje é {diaDaSemana[0]}")
elif dia == 2:
    print(f"Hoje é {diaDaSemana[1]}")
elif dia == 3:
    print(f"Hoje é {diaDaSemana[2]}")
elif dia == 4:
    print(f"Hoje é {diaDaSemana[3]}")
elif dia == 5:
    print(f"Hoje é {diaDaSemana[4]}")
elif dia == 6:
    print(f"Hoje é {diaDaSemana[5]}")
elif dia == 7:
    print(f"Hoje é {diaDaSemana[6]}")
else:
    print("Dia da semana inválido!")

# 13 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.#5 C Entre 4.0 e 6.0 D Entre 4.0 e zero
# E O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou #“REPROVADO” se o conceito for D ou E.

conceito = ['A', 'B', 'C', 'D', 'E']

n1 = float(input("Informe a primeira nota parcial: \n"))
n2 = float(input("Informe a segunda nota parcial: \n"))

media = (n1 + n2) / 2

if media <= 10.0 and media >= 0:
    if media <= 10.0 and media > 9.0:
        conceito2 = conceito[0]
        situacao = 'Aprovado'
    elif media <= 9.0 and media > 7.5:
        conceito2 = conceito[1]
        situacao = 'Aprovado'
    elif media <= 7.5 and media > 6.0:
        conceito2 = conceito[2]
        situacao = 'Aprovado'
    elif media <= 6.0 and media > 4.0:
        conceito2 = conceito[3]
        situacao = 'Reprovado'
    elif media <= 4.0 and media > 0.0:
        conceito2 = conceito[4]
        situacao = 'Reprovado'

    print(f"A média do aluno: {media:.1f}")
    print(f"O conceito do aluno: {conceito2}")
    print(f"A situação do aluno: {situacao}")

else:
    print("Error")

# 14 - Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, #caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

l1 = int(input("Informe o primeiro lado \n"))
l2 = int(input("Informe o segundo lado \n"))
l3 = int(input("Informe o terceiro lado \n"))

if l1 == l2 == l3:
   print("Triângulo Equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
   print("Triângulo Isósceles")
elif l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
   print("Não pode ser um triangulo")
else:
   print("Triângulo Escaleno")

# 15 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c

print("Vamos calcular as raízes de equações de segundo grau")

a = float(input("Qual o valor de a: \n"))
b = float(input("Qual o valor de b: \n"))
c = float(input("Qual o valor de c: \n"))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Não possui raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f"x1: {x1}, x2: {x2}")

# 16 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print("Vamos descobrir se um ano é bissexto")

anoX = int(input("Informe um ano \n"))

if (anoX % 4 == 0 and anoX % 100 != 0) or (anoX % 400 == 0):
    print("O ano informado é bissexto")
else:
    print("O ano informado não é bissexto")

# 17 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("Informe uma data no formato xx/xx/xxxx, vamos verificar se ela é válida")

dia = int(input("Informe um dia: \n"))
mes = int(input("Informe um mês: \n"))
ano = int(input("Informe um ano: \n"))

if dia > 0 and mes > 0 and mes <= 12:
    if mes >= 1 and mes <= 12:
        mesValido = True
    else:
        mesValido = False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31 and dia >= 1:
            diaValido = True
        else:
            diaValido = False
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30 and dia >= 1:
            diaValido = True
        else:
            diaValido = False
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29 and dia >= 1:
                diaValido = True
        elif dia <= 28 and dia >= 1:
            diaValido = True
        else:
            diaValido = False
    if diaValido == True and mesValido == True:
        print(f"A data informada: {dia}/{mes}/{ano} é válida")
    else:
        print("Error: Data inválida")
else:
        print("Error: Data inválida")

# 18 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

n1 = int(input("Insira um número de 0 à 9999: \n"))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f"A unidade é {u}, a dezena é {d}, a centena é {c} e o milhar é {m}")
