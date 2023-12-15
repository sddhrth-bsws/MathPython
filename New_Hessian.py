import sympy as sp
import numpy as np

# Define symbolic variables
OR, a, b, CP, CHO, CHR, CS, LAMDA, ALPHA, BETA, SR, p, ETA, IP, IC, L, Q, SIGMA, n, C1, C2, C3, D, TV, M, E1, E2, G, ZETA, X, T1, T2, T = sp.symbols('OR a b CP CHO CHR CS LAMDA ALPHA BETA SR p ETA IP IC L Q SIGMA n C1 C2 C3 D TV M E1 E2 G ZETA X T1 T2 T')

# Define a function

#f = x**2 + y**2 + z**2 + x*y + y*z
f = ((1 / T) * (OR + (CP*Q) - (((a-(b*p))/(LAMDA+BETA))*((1.5*LAMDA*((T1)**2))+(0.5*BETA*((T1)**2))+(2*T1)))*CHR
                       + CHO * SR * T1 * (1 - (ALPHA * T1 * 0.5))) + CHO * (ALPHA + LAMDA) * (T2 * (T2 - T1)
                        - 0.5 * (T2 - T1) ** 2 + (0.5 * (ALPHA + LAMDA) ** 2) * (T2 ** 2) * (T2 - T1) -
             ALPHA * T2 * 0.5 * (T2 - T1) ** 2 - ALPHA * 0.5 * (ALPHA + LAMDA) ** 2 * (T2 ** 2) * 0.5 * (T2 - T1) ** 2)
            + CS * ETA * (a - b * p) * (((1 / 6) * LAMDA * T ** 3) - ((1 / 6) * LAMDA * T2 ** 3) + 0.5 * T ** 2
            - T * (0.5 * LAMDA * T2 ** 2 + T2) -0.5 * T2 ** 2 + T2 * (0.5 * LAMDA * T2 ** 2 + T2)) +
            ((0.5) * (n + 1) * (1 / n) * IC * L * SIGMA * CP * Q)+ 8 * (C1 + (2 * D * TV * C2) + (D * TV * C3 * M * Q)
            + (2 * D * E1 + D * E2 * Q) * (1 - ZETA * (1 - sp.exp(-X * G)))) + G * T)

# Compute the Hessian matrix
hessian_matrix = sp.hessian(f, (T1, T2, T))


# Display the Hessian matrix
print("Hessian Matrix:")
print(hessian_matrix)

'''
# Evaluate the Hessian matrix
hessian_matrix_evaluated = hessian_matrix.doit()

# Display the Hessian matrix as a formatted matrix
print("Hessian Matrix:")
sp.pretty_print(sp.Matrix(hessian_matrix_evaluated))
'''