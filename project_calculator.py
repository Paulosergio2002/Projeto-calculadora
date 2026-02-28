import time
def calculadora(number_1, number_2, operador):
    if operador == '+':
        return(number_1 + number_2)
    elif operador == '-':
        return(number_1 - number_2)
    elif operador == '*':
        return(number_1 * number_2)
    elif operador == '/':
        if number_2 != 0:
            return(number_1 / number_2)
        else:
            return 'Erro por divisão 0!'
    else:
        return('Operação Inválida')
number_1 = float(input('Digite o primeiro número: '))
number_2 = float(input('Digite o próximo número: '))
operador = str(input(f'Qual operador você deseja? '))
resultado = calculadora(number_1, number_2, operador)
print(resultado)
time.sleep(5)       


    

