import numpy as np

#class Solution:
#    def __init__(self, x, y,)

def RungeKutta4(f, y_0, start=0, stop=1, N=1024, include_end=True):
    """
    f: f(x, y), y must be a numpy array and the return type must of the same order
    y_0: Initial consitions of the system
    """
    xs = np.linspace(start, stop, N, endpoint=include_end)
    dx = xs[1] - xs[0]
    ys = []
    yi = y_0
    ys.append(np.copy(yi))

    for x in xs[1:]:
        k1 = f(x, yi)
        k2 = f(x + 0.5*dx, yi + 0.5*dx*k1)
        k3 = f(x + 0.5*dx, yi + 0.5*dx*k2)
        k4 = f(x + dx, yi + dx*k3)
        yi += (k1 + 2.0*k2 + 2.0*k3 + k4) * dx/6.0

        ys.append(np.copy(yi))

    solution = np.array(ys)
    return solution, xs

   
   
if __name__ == "__main__":
   
    from matplotlib.pyplot import plot, show

    def SHM(t, y):
        x = y[0]
        v = y[1]
        dv = -x
        dx = v

        return np.array([dx, dv])

    y_0 = np.array([1.0,0])
    ys, ts = RungeKutta4(SHM, y_0, stop=20)
    xs = [ys[i][0] for i in range(len(ys))]
    vs = [ys[i][1] for i in range(len(ys))]
    plot(ts, xs)
    plot(ts, vs)

    show()
