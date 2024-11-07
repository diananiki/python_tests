from math import sin, cos
from typing import Callable


def newton(f: Callable[[float], float], f_prime: Callable[[float], float],
	x0: float, eps: float = 1e-3, kmax: int = 1e3) -> float:
    x, x_prev, i = x0, x0 + 2 * eps, 0
    step = 0
    while abs(x - x_prev) >= eps and i < kmax:
        x, x_prev, i = x - f(x) / f_prime(x), x, i + 1
        r = x_prev - x
        step += 1
        print("{} {:10.8f} {:10.8f}".format(step, x, r))
    return x


def f(x: float) -> float:
    return 3 * x - cos(x) - 1


def f_prime(x: float) -> float:
    return 3 + sin(x)


x0 = 0.6

if __name__ == '__main__':
    newton(f, f_prime, x0)