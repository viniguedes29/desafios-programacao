from dataclasses import dataclass
from math import hypot
from typing import ClassVar


EPS = 1e-9


@dataclass(frozen=True)
class Ponto:
    _EPS: ClassVar[float] = EPS

    x: float = 0
    y: float = 0

    def igual(self, outro: "Ponto") -> bool:
        """Verifica se outro é igual a este ponto, com tolerância _EPS."""
        return Ponto.sao_iguais(self, outro)

    def outro_esta_acima(self, outro: "Ponto") -> bool:
        """Verifica se outro está acima deste ponto, com tolerância _EPS."""
        return outro.y - self.y > self._EPS

    def outro_esta_a_esquerda(self, outro: "Ponto") -> bool:
        """Verifica se outro está à esquerda deste ponto, com tolerância _EPS."""
        return self.x - outro.x > self._EPS

    @staticmethod
    def sao_iguais(p: "Ponto", q: "Ponto") -> bool:
        """Compara as duas coordenadas com tolerância _EPS."""
        return abs(p.x - q.x) <= Ponto._EPS and abs(p.y - q.y) <= Ponto._EPS
    
    @staticmethod
    def distancia(p: "Ponto", q: "Ponto") -> float:
        """Retorna a distância euclidiana entre dois pontos."""
        return hypot(p.x - q.x, p.y - q.y)

    @staticmethod
    def distancia_quadrada(p: "Ponto", q: "Ponto") -> float:
        """Retorna o quadrado da distância, preservando inteiros se as coordenadas forem inteiras."""
        dx = p.x - q.x
        dy = p.y - q.y
        return dx * dx + dy * dy

    @staticmethod
    def ponto_medio(p: "Ponto", q: "Ponto") -> "Ponto":
        """Retorna o ponto médio entre p e q."""
        return Ponto((p.x + q.x) / 2, (p.y + q.y) / 2)

    @staticmethod
    def transladar(p: "Ponto", dx: float, dy: float) -> "Ponto":
        """Retorna um novo ponto deslocado por (dx, dy)."""
        return Ponto(p.x + dx, p.y + dy)
