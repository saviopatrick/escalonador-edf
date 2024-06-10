import time
import random
from queue import PriorityQueue
from colorama import Fore, Style

# Definição da classe Tarefa
class Tarefa:
    def __init__(self, nome, prazo, duracao):
        # Inicializa uma nova tarefa com nome, prazo e duração
        self.nome = nome
        self.prazo_original = prazo
        self.prazo = prazo
        self.duracao = duracao
        self.restante = duracao
    
    def __lt__(self, other):
        # Define a comparação entre tarefas com base no prazo
        return self.prazo < other.prazo

    def __repr__(self):
        # Representação textual da tarefa
        return f"Tarefa(nome={self.nome}, prazo={self.prazo}, duracao={self.duracao})"

def escalonador_edf():
    # Cria uma fila de prioridades
    fila = PriorityQueue()
    tempo_atual = 0
    
    # Define um número aleatório de tarefas entre 3 e 6
    num_tarefas = random.randint(3, 6)
    tarefas = []
    print("Lista de Tarefas:")
    
    # Gera tarefas aleatórias e as adiciona à fila
    for i in range(num_tarefas):
        nome = f"Tarefa {i+1}"
        prazo = random.randint(1, 10)
        duracao = random.randint(1, 5)
        tarefa = Tarefa(nome, prazo, duracao)
        tarefas.append(tarefa)
        print(f"Tarefa {i+1}: Nome={tarefa.nome}, Prazo={tarefa.prazo}, Duração={tarefa.duracao}")
        fila.put((prazo, tarefa))
    
    tarefa_atual = None
    
    # Loop principal do escalonador
    while not fila.empty() or tarefa_atual:
        if not tarefa_atual and not fila.empty():
            # Se nenhuma tarefa está em execução, pega a próxima tarefa da fila
            _, tarefa_atual = fila.get()
        
        if tarefa_atual:
            # Executa a tarefa atual
            print(f"Tempo atual: {tempo_atual}")
            print(f"{Fore.GREEN}Executando => {tarefa_atual.nome} (Prazo: {tarefa_atual.prazo}, Restante: {tarefa_atual.restante}){Style.RESET_ALL}")
            tarefa_atual.restante -= 1
            time.sleep(0.5)  # Simula a execução da tarefa por um tempo
            
            if tarefa_atual.restante == 0:
                # Se a tarefa atual está concluída, remove-a
                print(f"{Fore.RED}{tarefa_atual.nome} concluída{Style.RESET_ALL}")
                tarefa_atual = None

        # Incrementa o tempo atual
        tempo_atual += 1

# Executa o escalonador EDF
escalonador_edf()
