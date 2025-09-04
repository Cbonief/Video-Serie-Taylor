import math

def raiz_derivada(k, x):
    """
    Calcula a k-ésima derivada de sqrt(x) de forma geral.
    """
    if k == 0:
        return math.sqrt(x)
    
    numerador = 1
    for i in range(1, k):
        numerador *= (2*i - 1)
    
    return ((-1)**(k-1)) * numerador / (2**k * x**(k - 0.5))


def raiz_taylor(x, a, n):
    """
    Aproxima sqrt(x) usando a série de Taylor em torno de 'a' com n termos.
    """
    resultado = 0
    for k in range(n):
        derivada = raiz_derivada(k, a)
        termo = derivada * (x - a)**k / math.factorial(k)
        resultado += termo
    return resultado


def gn_taylor(x0, delta_x, n):
    """
    Aproxima f(x0 + delta_x) usando a fórmula gn:
    gn(x0 + delta_x) = sum_{k=0}^{n} [n!/(k!(n-k)!)] * (delta_x/n)^k * f^(k)(x0)
    """
    resultado = 0
    for k in range(n + 1):
        coef_binomial = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        derivada = raiz_derivada(k, x0)
        termo = coef_binomial * (delta_x / n)**k * derivada
        resultado += termo
    return resultado


# Parâmetros
x0 = 4
delta_x = 1
n_termos = 6
x = x0 + delta_x

# Aproximação usando gn
aprox_gn = gn_taylor(x0, delta_x, n_termos)

# Aproximação usando série de Taylor tradicional
aprox_taylor = raiz_taylor(x, x0, n_termos)

# Valor real
valor_real = math.sqrt(x)

# Comparação final
print(f"Aproximação gn de sqrt({x}): {aprox_gn}")
print(f"Aproximação série de Taylor de sqrt({x}): {aprox_taylor}")
print(f"Valor real de sqrt({x}): {valor_real}")
