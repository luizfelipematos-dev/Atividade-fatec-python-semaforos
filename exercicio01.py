import multiprocessing
import time

def carro(id, sentido, sem):
    with sem:
        sentido.value = id
        if sentido.value == 1:
            print('Carro', id, 'passando de cima para baixo')
        elif sentido.value == 2:
            print('Carro', id, 'passando da esquerda para a direita')
        elif sentido.value == 3:
            print('Carro', id, 'passando da direita para a esquerda')
        else:
            print('Carro', id, 'passando de baixo para cima')
        time.sleep(0.5)

def main():
    num_carros: int = 4
    params = []
    with multiprocessing.Manager() as manager:
        sentido = manager.Value('i', 0)
        sem = manager.Semaphore(1)
        for i in range(num_carros):
            params.append((i + 1, sentido, sem))
        with multiprocessing.Pool(processes=num_carros) as pool:
            pool.starmap(carro, params)

if __name__ == '__main__':
    main()