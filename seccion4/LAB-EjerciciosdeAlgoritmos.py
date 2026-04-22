# 1. Puntaje total
print("\n=== 1. Puntaje total ===")
nivel1 = int(input("Puntos nivel 1: "))
nivel2 = int(input("Puntos nivel 2: "))
nivel3 = int(input("Puntos nivel 3: "))
print("Total:", nivel1 + nivel2 + nivel3)

# 2. Tiempo total en segundos
print("\n=== 2. Tiempo total en segundos ===")
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
print("Total segundos:", h*3600 + m*60 + s)

# 3. Daño total
print("\n=== 3. Daño total ===")
d1 = int(input("Daño 1: "))
d2 = int(input("Daño 2: "))
d3 = int(input("Daño 3: "))
print("Daño total:", d1 + d2 + d3)

# 4. Experiencia total
print("\n=== 4. Experiencia total ===")
e1 = int(input("XP 1: "))
e2 = int(input("XP 2: "))
e3 = int(input("XP 3: "))
print("XP total:", e1 + e2 + e3)

# 5. Porcentaje de vida
print("\n=== 5. Vida restante ===")
max_vida = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))
print("Vida %:", (vida_actual / max_vida) * 100)

# 6. Oro total
print("\n=== 6. Oro total ===")
o1 = int(input("Oro 1: "))
o2 = int(input("Oro 2: "))
o3 = int(input("Oro 3: "))
print("Oro total:", o1 + o2 + o3)

# 7. Velocidad promedio
print("\n=== 7. Velocidad promedio ===")
dist = float(input("Distancia: "))
time = float(input("Tiempo: "))
print("Velocidad:", dist / time)

# 8. Costo mejoras
print("\n=== 8. Costo mejoras ===")
c1 = float(input("Costo 1: "))
c2 = float(input("Costo 2: "))
c3 = float(input("Costo 3: "))
print("Total:", c1 + c2 + c3)

# 9. Tiempo restante
print("\n=== 9. Tiempo restante ===")
total = float(input("Tiempo total: "))
trans = float(input("Transcurrido: "))
print("Restante:", total - trans)

# 10. Nivel promedio
print("\n=== 10. Nivel promedio ===")
n1 = int(input("Nivel 1: "))
n2 = int(input("Nivel 2: "))
n3 = int(input("Nivel 3: "))
print("Promedio:", (n1 + n2 + n3) / 3)

# 11. Daño crítico
print("\n=== 11. Daño crítico ===")
base = float(input("Base: "))
multi = float(input("Multiplicador: "))
print("Crítico:", base * multi)

# 12. Minutos a horas
print("\n=== 12. Tiempo en horas y minutos ===")
minutos = int(input("Minutos: "))
print("Resultado:", minutos // 60, "horas y", minutos % 60, "minutos")

# 13. % misiones
print("\n=== 13. Misiones completadas ===")
total = int(input("Total: "))
comp = int(input("Completadas: "))
print("Porcentaje:", (comp / total) * 100)

# 14. Costo tienda
print("\n=== 14. Compra total ===")
o1 = float(input("Objeto 1: "))
o2 = float(input("Objeto 2: "))
o3 = float(input("Objeto 3: "))
print("Total:", o1 + o2 + o3)

# 15. Tiempo promedio partidas
print("\n=== 15. Promedio partidas ===")
t1 = float(input("Partida 1: "))
t2 = float(input("Partida 2: "))
t3 = float(input("Partida 3: "))
print("Promedio:", (t1 + t2 + t3) / 3)

# 16. % enemigos derrotados
print("\n=== 16. Enemigos derrotados ===")
total = int(input("Total enemigos: "))
der = int(input("Derrotados: "))
print("Porcentaje:", (der / total) * 100)
