import numpy as np
import matplotlib.pyplot as plt
import time

def func_py(x: list[float]) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [ np.sin(np.pi * xi / 23) for xi in x ]

def tabulate_py(a: float, b: float, n: int) -> dict[float]:
    x = [ a + x*(b - a)/n for x in range(n) ]
    y = func_py(x)
    return x, y

def tabulate_np(a: float, b: float, n: int) -> np.ndarray:
    x = np.linspace(a, b, n)
    y = np.sin(np.pi * x / 23)
    return x, y

def test_tabulation(f, a, b, n, axis):
    start_time = time.time()
    res = f(a, b, n)
    end_time = time.time()
    print(f"Час табулювання за допомогою {f.__name__}: {end_time - start_time} секунд")

    axis.plot(res[0], res[1])
    axis.grid()

def main():
    a, b, n = 0, 1, 1000

    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, a, b, n, ax1)
    test_tabulation(tabulate_np, a, b, n, ax2)
    plt.show()

if __name__ == '__main__':
    main()
