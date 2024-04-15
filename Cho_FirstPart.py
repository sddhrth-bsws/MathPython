import sympy as sp
OR, a, b, CP, CHO, CHR, CS, LAMDA, ALPHA, BETA, SR, p, ETA, IP, IC, L, Q, SIGMA, n, C1, C2, C3, D, TV, M, E1, E2, G, ZETA, X, T1, T2, T = sp.symbols('OR a b CP CHO CHR CS LAMDA ALPHA BETA SR p ETA IP IC L Q SIGMA n C1 C2 C3 D TV M E1 E2 G ZETA X T1 T2 T')

f = (a-b*p)*(T2 - T1)*(1 +((0.5*(T2 + T1)*(ALPHA+LAMDA)**2)))*T1*(1-(ALPHA*T1*0.5))

df_dT1 = sp.diff(f, T1)

print("Partial Derivative with respect to T1:")
print(df_dT1)