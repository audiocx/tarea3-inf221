# La v2 permite generar mayor solape entre horarios
import uuid
import random

print("Ingrese la cantidad de asignaturas ofrecidas en el semestre que desea")
l = int(input())

N = 1000  # Rango de horario sería hasta N
delta = 100  # Define la mínima diferencia entre s y f

namefile = r"C:\Users\claud\Desktop\2022-1\INF221 (algoco)\tarea3\Input.dat"

file = open(namefile, "w")
file.write(str(l)+"\n")

for i in range(l):
    s = random.randint(1, N-delta)
    f = random.randint(s+delta, N)
    file.write(str(s)+" " + str(f) + "\n")
file.close()
