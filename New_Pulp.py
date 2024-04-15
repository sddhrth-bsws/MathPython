import pulp

X = (1/T)*[Ordering Cost + Purchasing Cost + Holding Cost +
       Shortage Cost + Capital Cost + Reduced Transportation
       Cost + Green Tech]


prob = pulp.LpProblem("Product_Mix", pulp.LpMaximize)

Ordering Cost = OR
Purchasing Cost = Cp * [(a-bp)(t2 – t1)[1 + {(α + λ)2(t2 + t1)}/2] + (a-bp)t1[1 + {(λ+β1)t1}/2] – [η(a-bp)(t2 –T)[1+{
                  (t2+T)λ}/2]]]

CP * (a - (b*p))*(t2 - t1)*(1 + 0.5*((ALPHA + Lambda)**2)) + (a-(b*p)) * t1 * (1 + (0.5 * (LAMBDA + BETA) * t1)) - (
    ETA * (a - b *p))