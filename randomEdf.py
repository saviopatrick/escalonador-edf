import time
from queue import PriorityQueue
import random

class Tarefa:
    def __init__(self, nome, prazo, duracao):
        self.nome = nome
        self.prazo_original = prazo
        self.prazo = prazo
        self.duracao = duracao
        self.restante = duracao
    
    def __lt__(self, other):
        return self.prazo < other.prazo

    def __repr__(self):
        return f"Tarefa(nome={self.nome}, prazo={self.prazo}, duracao={self.duracao})"

def escalonador_edf():
    fila = PriorityQueue()
    tempo_atual = 0
    
    num_tarefas = random.randint(3, 6)
    tarefas = []
    print("Lista de Tarefas:")
    for i in range(num_tarefas):
        nome = f"Tarefa {i+1}"
        prazo = random.randint(1, 10)
        duracao = random.randint(1, 5)
        tarefa = Tarefa(nome, prazo, duracao)
        tarefas.append(tarefa)
        print(f"Tarefa {i+1}: Nome={tarefa.nome}, Prazo={tarefa.prazo}, Duração={tarefa.duracao}")
        fila.put((prazo, tarefa))
    
    tarefa_atual = None
    
    while not fila.empty() or tarefa_atual:
        if not tarefa_atual and not fila.empty():
            _, tarefa_atual = fila.get()
        
        if tarefa_atual:
            print(f"Tempo atual: {tempo_atual}")
            print(f"Executando Tarefa: {tarefa_atual.nome} (Prazo: {tarefa_atual.prazo}, Restante: {tarefa_atual.restante})")
            tarefa_atual.restante -= 1
            time.sleep(0.5)
            
            if tarefa_atual.restante == 0:
                print(f"{tarefa_atual.nome} concluída")
                tarefa_atual = None

        tempo_atual += 1

escalonador_edf()
