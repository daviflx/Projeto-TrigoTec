import math

class TrigoTec:
    def __init__(self):
        self.angulo = 0

    def set_angulo(self, angulo):
        self.angulo = angulo

    def seno(self):
        # Converte o ângulo de graus para radianos
        radianos = math.radians(self.angulo)
        return math.sin(radianos)

    def cosseno(self):
        # Converte o ângulo de graus para radianos
        radianos = math.radians(self.angulo)
        return math.cos(radianos)

    def tangente(self):
        # Converte o ângulo de graus para radianos
        radianos = math.radians(self.angulo)
        return math.tan(radianos)

    def mostrar_resultados(self):
        print(f"Ângulo: {self.angulo}°")
        print(f"Seno: {self.seno():.4f}")
        print(f"Cosseno: {self.cosseno():.4f}")
        print(f"Tangente: {self.tangente():.4f}")

# Uso da calculadora TrigoTec
if __name__ == "__main__":
    calculadora = TrigoTec()
    
    # Defina o ângulo que deseja calcular
    angulo = float(input("Digite o ângulo em graus: "))
    calculadora.set_angulo(angulo)
    
    # Exibe os resultados
    calculadora.mostrar_resultados()
