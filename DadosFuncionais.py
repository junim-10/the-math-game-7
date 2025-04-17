import random

class DadosFuncionais:
    @staticmethod
    def gerarNumeros():
        return random.randint(1, 10), random.randint(1, 10)

    @staticmethod
    def selecionarOperador():
        return random.choice(['+', '-', '*', '/'])

    @staticmethod
    def calcularResultado(num1, num2, operador):
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return "Erro: Divisão por zero"
            return num1 / num2
        return None

# Se você tiver outra classe de lógica (DadosOperacionais), coloque-a aqui também
# class DadosOperacionais:
#     pass