from dataclasses import dataclass, field
from math import atan2, cos, degrees, hypot, radians, sin
from operator import attrgetter
from typing import ClassVar, List, Optional


EPS = 1e-9


@dataclass(frozen=True)
class Ponto:
    _EPS: ClassVar[float] = EPS

    x: float = 0
    y: float = 0

    @staticmethod
    def ordena(pontos: List["Ponto"]) -> List["Ponto"]:
        """Ordena por x, depois y, em O(n log n), sem alterar a lista original."""
        return sorted(pontos, key=attrgetter("x", "y"))

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
    def colineares(a: "Ponto", b: "Ponto", c: "Ponto") -> bool:
        """Verifica colinearidade por direcionais iguais ou opostos, incluindo pontos repetidos."""
        ab, bc = Vetor(a, b), Vetor(b, c)
        if ab.eh_nulo or bc.eh_nulo:
            return True

        u, v = ab.vetor_direcional, bc.vetor_direcional
        return u.igual(v) or Vetor.sao_opostos(u, v)

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


@dataclass(frozen=True)
class Vetor:
    """Vetor bidimensional representado por suas componentes x e y."""

    _EPS: ClassVar[float] = EPS
    origem: ClassVar[Ponto] = Ponto(0, 0)

    x: float = 0
    y: float = 0
    _modulo: float = field(init=False, repr=False, compare=False)
    _angulo_radianos: Optional[float] = field(init=False, repr=False, compare=False)
    _angulo_graus: Optional[float] = field(init=False, repr=False, compare=False)
    _vetor_direcional: Optional["Vetor"] = field(init=False, repr=False, compare=False)

    def __init__(self, a: Ponto, b: Optional[Ponto] = None):
        """Cria o vetor da origem até a, ou de a até b quando b é informado."""
        if b is None:
            b = Vetor.origem
            a, b = b, a

        x, y = b.x - a.x, b.y - a.y

        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)

        modulo = hypot(x, y)
        rad = atan2(y, x) if modulo != 0 else None
        graus = degrees(rad) if rad is not None else None
        object.__setattr__(self, "_modulo", modulo)
        object.__setattr__(self, "_angulo_radianos", rad)
        object.__setattr__(self, "_angulo_graus", graus)

        unitario = None
        if modulo != 0:
            # Evita chamar __init__ recursivamente para criar o vetor unitário.
            unitario = object.__new__(Vetor)
            object.__setattr__(unitario, "x", x / modulo)
            object.__setattr__(unitario, "y", y / modulo)
            object.__setattr__(unitario, "_modulo", 1.0)
            object.__setattr__(unitario, "_angulo_radianos", rad)
            object.__setattr__(unitario, "_angulo_graus", graus)
            object.__setattr__(unitario, "_vetor_direcional", unitario)
        object.__setattr__(self, "_vetor_direcional", unitario)

    def igual(self, outro: "Vetor") -> bool:
        """Compara as duas componentes com tolerância _EPS."""
        return abs(self.x - outro.x) <= self._EPS and abs(self.y - outro.y) <= self._EPS

    @staticmethod
    def sao_opostos(u: "Vetor", v: "Vetor") -> bool:
        """Verifica se u e v têm componentes opostas, com tolerância _EPS."""
        return abs(u.x + v.x) <= Vetor._EPS and abs(u.y + v.y) <= Vetor._EPS

    def perpendicular(self, outro: "Vetor") -> bool:
        """Testa produto escalar próximo de zero; vetores nulos retornam False."""
        return Vetor.sao_perpendiculares(self, outro)

    def paralelo(self, outro: "Vetor") -> bool:
        """Testa produto vetorial próximo de zero; vetores nulos retornam False."""
        return Vetor.sao_paralelos(self, outro)

    @staticmethod
    def sao_perpendiculares(u: "Vetor", v: "Vetor") -> bool:
        """Compara o produto escalar com zero usando tolerância absoluta _EPS."""
        if u.modulo == 0 or v.modulo == 0:
            return False
        return abs(Vetor.produto_escalar(u, v)) <= Vetor._EPS

    @staticmethod
    def sao_paralelos(u: "Vetor", v: "Vetor") -> bool:
        """Compara o produto vetorial com zero; inclui sentidos opostos e rejeita nulos."""
        if u.modulo == 0 or v.modulo == 0:
            return False
        return abs(Vetor.produto_vetorial(u, v)) <= Vetor._EPS

    @property
    def eh_nulo(self) -> bool:
        """Verifica se ambas as componentes são exatamente zero."""
        return self.x == 0 and self.y == 0

    @property
    def eh_quase_nulo(self) -> bool:
        """Verifica se ambas as componentes são zero dentro da tolerância _EPS."""
        return abs(self.x) <= self._EPS and abs(self.y) <= self._EPS

    @property
    def modulo(self) -> float:
        """Retorna o comprimento do vetor."""
        return self._modulo

    @property
    def angulo_graus(self) -> float:
        """Retorna o ângulo em graus com o eixo x positivo, de -180 a 180."""
        if self._angulo_graus is None:
            raise ValueError("O vetor nulo não possui ângulo definido.")
        return self._angulo_graus

    @property
    def angulo_radianos(self) -> float:
        """Retorna o ângulo com o eixo x positivo, em radianos, de -pi a pi."""
        if self._angulo_radianos is None:
            raise ValueError("O vetor nulo não possui ângulo definido.")
        return self._angulo_radianos

    @property
    def vetor_direcional(self) -> "Vetor":
        """Retorna o vetor unitário no mesmo sentido; rejeita o vetor nulo."""
        if self._vetor_direcional is None:
            raise ValueError("O vetor nulo não possui direção definida.")
        return self._vetor_direcional

    @staticmethod
    def somar(u: "Vetor", v: "Vetor") -> "Vetor":
        """Retorna a soma componente a componente, preservando os vetores originais."""
        return Vetor(Ponto(0, 0), Ponto(u.x + v.x, u.y + v.y))

    @staticmethod
    def multiplicar_escalar(v: "Vetor", escalar: float) -> "Vetor":
        """Multiplica as componentes pelo escalar, retornando um novo vetor."""
        return Vetor(Ponto(0, 0), Ponto(v.x * escalar, v.y * escalar))

    @staticmethod
    def angulo_entre_radianos(u: "Vetor", v: "Vetor") -> float:
        """Retorna o menor ângulo entre vetores, de 0 a pi; rejeita nulos."""
        # Os unitários já estão calculados; evitam produtos com módulos grandes.
        a, b = u.vetor_direcional, v.vetor_direcional
        return atan2(abs(Vetor.produto_vetorial(a, b)), Vetor.produto_escalar(a, b))

    @staticmethod
    def angulo_entre_graus(u: "Vetor", v: "Vetor") -> float:
        """Retorna o menor ângulo entre vetores, de 0 a 180 graus; rejeita nulos."""
        return degrees(Vetor.angulo_entre_radianos(u, v))

    @staticmethod
    def produto_escalar(u: "Vetor", v: "Vetor") -> float:
        """Retorna u.x * v.x + u.y * v.y; preserva inteiros se as componentes forem inteiras."""
        return u.x * v.x + u.y * v.y

    @staticmethod
    def produto_vetorial(u: "Vetor", v: "Vetor") -> float:
        """Retorna a componente z do produto em 3D: u.x * v.y - u.y * v.x."""
        return u.x * v.y - u.y * v.x

    @staticmethod
    def direcional(v: "Vetor") -> "Vetor":
        """Retorna o vetor unitário no mesmo sentido; rejeita o vetor nulo."""
        return v.vetor_direcional
    
    @staticmethod
    def rotacionar(v: "Vetor", angulo: float) -> "Vetor":
        """Retorna um novo vetor rotacionado em graus; positivo é anti-horário."""
        rad = radians(angulo)
        c, s = cos(rad), sin(rad)
        x = v.x * c - v.y * s
        y = v.x * s + v.y * c
        return Vetor(Ponto(0, 0), Ponto(x, y))

    @staticmethod
    def girar_90_horario(v: "Vetor") -> "Vetor":
        """Retorna (y, -x), sem trigonometria e preservando componentes inteiras."""
        return Vetor(Ponto(0, 0), Ponto(v.y, -v.x))

    @staticmethod
    def girar_90_anti_horario(v: "Vetor") -> "Vetor":
        """Retorna (-y, x), sem trigonometria e preservando componentes inteiras."""
        return Vetor(Ponto(0, 0), Ponto(-v.y, v.x))

    @staticmethod
    def girar_180(v: "Vetor") -> "Vetor":
        """Retorna (-x, -y), sem trigonometria e preservando componentes inteiras."""
        return Vetor(Ponto(0, 0), Ponto(-v.x, -v.y))
