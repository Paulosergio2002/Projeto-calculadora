from time import sleep
def soma(number_1, number_2):
    return number_1 + number_2
def subtracao(number_1, number_2):
    return number_1 - number_2
def multiplicacao(number_1, number_2):
    return number_1 * number_2
def divisao(number_1, number_2):
    return number_1 / number_2


number_1 = float(input('Digite o primeiro número: '))
number_2 = float(input('Digite o próximo número: '))
operador = input('Qual operador deseja utilizar? (+, -, * ou/)')
operaçoes = {'+': soma,
                     '-': subtracao,
                     '*': multiplicacao,
                     '/': divisao}

funcao = operaçoes.get(operador)
if funcao: 
    resultado = funcao(number_1, number_2)
    print(resultado)
else:
    print('Operação Inválida')
sleep(5)     


    

