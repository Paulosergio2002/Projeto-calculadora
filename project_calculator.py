import time
number_1 = float(input('Digite o primeiro número: '))
number_2 = float(input('Digite o próximo número: '))
operador = str(input(f'Qual operador você deseja? '))
if operador == '+':
    print(number_1 + number_2)
elif operador == '-':
    print(number_1 - number_2)
elif operador == '*':
    print(number_1 * number_2)
elif operador == '/':
    print(number_1 / number_2)
else:
    print('Operação Inválida')
time.sleep(15)       


    

