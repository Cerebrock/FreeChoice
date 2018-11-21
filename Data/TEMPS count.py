def contarV(respuestas):
    subs = ['D', 'C', 'H', 'I', 'A']
    intervalos = [(1, 21), (22, 42), (43, 63), (64, 84), (85, 110)]
    return {k:v for k, v in zip(subs, [respuestas[interv[0] - 1: interv[1]].count('1') for interv in intervalos])}