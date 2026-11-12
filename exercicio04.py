import multiprocessing
import time
import random

def piloto(id_equipe, id_carro, sem_pista, sem_equipe):
    nome: str = 'Equipe ' + str(id_equipe) + ' - Carro ' + str(id_carro)
    for volta in range(1, 4):
        time.sleep(random.uniform(0.1, 0.2))
        with sem_equipe:
            with sem_pista:
                print(nome, 'entrou na pista para a volta', volta)
                tempo: float = random.uniform(30.0, 45.0)
                time.sleep(0.3)
                print(nome, 'terminou a volta', volta, 'em', round(tempo, 2), 'segundos')

def main():
    num_equipes: int = 7
    carros_por_equipe: int = 2
    params = []
    with multiprocessing.Manager() as manager:
        sem_pista = manager.Semaphore(5)
        sem_equipes = [manager.Semaphore(1) for _ in range(num_equipes)]
        for eq in range(num_equipes):
            for car in range(carros_por_equipe):
                params.append((eq + 1, car + 1, sem_pista, sem_equipes[eq]))
        with multiprocessing.Pool(processes=14) as pool:
            pool.starmap(piloto, params)

if __name__ == '__main__':
    main()