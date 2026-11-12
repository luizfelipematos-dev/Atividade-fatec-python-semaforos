import multiprocessing
import time
import random

pulo_max: int = 5
distancia_max: int = 100

def sapo(num, sem, colocacao):
    percorrido: int = 0
    salto: int = 0
    while percorrido < distancia_max:
        salto = random.randint(1, pulo_max)
        percorrido = percorrido + salto
        if percorrido > distancia_max:
            percorrido = distancia_max
        with sem:
            print('Sapo', num, 'pulou', salto, 'cm e ja percorreu', percorrido, 'cm')
        time.sleep(0.3)
    with sem:
        colocacao.value = colocacao.value + 1
        print('Sapo', num, 'CHEGOU em', colocacao.value, 'lugar!')

def main():
    num_sapos: int = 5
    params = []
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        colocacao = manager.Value('i', 0)
        for i in range(num_sapos):
            params.append((i + 1, sem, colocacao))
        with multiprocessing.Pool(processes=num_sapos) as pool:
            pool.starmap(sapo, params)

if __name__ == '__main__':
    main()