def euler(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t, y = t0, y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def runge_kutta(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t, y = t0, y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y

f = lambda t, y: t - y**2
t0, y0, t_end, n = 0, 1, 2, 10

euler_result = euler(f, t0, y0, t_end, n)
runge_kutta_result = runge_kutta(f, t0, y0, t_end, n)

print(f"{euler_result:.{np.finfo(float).precision}g}")
print(f"{runge_kutta_result:.{np.finfo(float).precision}g}")
 
