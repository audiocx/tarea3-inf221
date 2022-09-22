import sys


def inscribir_greedy(h: list[tuple]):
    res = []

    # Ordenamos las tuplas de horario de menor a mayor segun fi - si
    h_ord = sorted(h, key=lambda x: x[1] - x[0])

    # Recorremos los horarios ordenados agregandolos al resultado si no solapan
    for hor in h_ord:
        solapa = False
        for r in res:
            if (hor[0] <= r[0] <= hor[1]) or (hor[0] <= r[1] <= hor[1]):
                solapa = True
        if not solapa:
            res.append(hor)

    # Ordenamos por horario de inicio
    res = sorted(res, key=lambda x: x[0])

    return res


def main():
    data = sys.stdin.readlines()
    N = int(data[0])

    horarios = []
    for i in range(1, N):
        h_in, h_fin = data[i].strip().split(" ")
        horarios.append((int(h_in), int(h_fin)))

    inscripciones = inscribir_greedy(horarios)

    print(len(inscripciones))
    for inicio, final in inscripciones:
        print(str(inicio) + " " + str(final))


if __name__ == "__main__":
    main()
