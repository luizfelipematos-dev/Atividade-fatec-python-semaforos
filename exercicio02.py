import multiprocessing
import time
import random

def pessoa(id, sem):
    distancia: float = 200.0
    velocidade: float = random.uniform(4.0, 6.0)
    tempo_percurso: float = distancia / velocidade
    print('Pessoa', id, 'caminhando pelo corredor')
    time.sleep(tempo_percurso / 40)
    with sem:
        print('Pessoa', id, 'abrindo e cruzando a porta')
        tempo_porta: float = random.uniform(1.0, 2.0)
        time.sleep(tempo_porta)
        print('Pessoa', id, 'terminou de cruzar a porta')

def main():
    num_pessoas: int = 4
    params = []
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        for i in range(num_pessoas):
            params.append((i + 1, sem))
        with multiprocessing.Pool(processes=num_pessoas) as pool:
            pool.starmap(pessoa, params)

if __name__ == '__main__':
    main()