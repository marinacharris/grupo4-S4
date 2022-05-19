#operaciones de los conjuntos
# operadores    métodos                 descripción
# | (alt +124)  union                   Unión
# &             intersecction           Intersección
# -             difference              Diferencia
# ^ alt+094     symmetric_difference    Diferencia simétrica

A = {'papa','maíz', 'trigo'}
B = {'plátano', 'maíz', 'caña'}
print(A|B)
print(A.union(B)) #línea 9 y 10 son equivalentes
print(A&B)
print(A-B)
print(A^B)