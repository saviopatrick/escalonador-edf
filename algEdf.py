import time
from queue import PriorityQueue
from colorama import init, Fore, Style

init()

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

def mostrar_estado(tempo_atual, fila, tarefa_atual):
    print("===========================================================")
    print(f"{Fore.CYAN}Tempo atual: {tempo_atual}{Style.RESET_ALL}")
    print("Tarefas na fila:")
    if fila.empty():
        print("    Nenhuma tarefa na fila")
    else:
        for i, (_, tarefa) in enumerate(fila.queue, start=1):
            print(f"    {i}. {tarefa.nome} (Prazo: {tarefa.prazo}, Duração: {tarefa.duracao})")
    if tarefa_atual:
        print(f"Tarefa em execução: {tarefa_atual.nome} (Prazo: {tarefa_atual.prazo}, Restante: {tarefa_atual.restante})")
    else:
        print("Nenhuma tarefa em execução")
    print("===========================================================")

def escalonador_edf():
    fila = PriorityQueue()
    tempo_atual = 0

    print("===========================================================")
    num_tarefas = int(input(f"{Fore.YELLOW}Digite o número de tarefas: {Style.RESET_ALL}"))
    print("===========================================================")
    for i in range(num_tarefas):
        print("===========================================================")
        nome = input(f"{Fore.YELLOW}Digite o nome da Tarefa {i+1}: {Style.RESET_ALL}")
        prazo = int(input(f"{Fore.YELLOW}Digite o prazo da Tarefa {i+1}: {Style.RESET_ALL}"))
        duracao = int(input(f"{Fore.YELLOW}Digite a duração da Tarefa {i+1}: {Style.RESET_ALL}"))
        print("===========================================================")
        tarefa = Tarefa(nome, prazo, duracao)
        fila.put((prazo, tarefa))
    
    tarefa_atual = None

    while not fila.empty() or tarefa_atual:
        if not tarefa_atual and not fila.empty():
            _, tarefa_atual = fila.get()
        
        if tarefa_atual:
            print(f"{Fore.GREEN}Tempo atual: {tempo_atual}")
            print(f"Executando => {tarefa_atual.nome} (Prazo: {tarefa_atual.prazo}, Restante: {tarefa_atual.restante}){Style.RESET_ALL}")
            tarefa_atual.restante -= 1
            time.sleep(0.5)
            
            if tarefa_atual.restante == 0:
                print(f"{Fore.RED}Tarefa {tarefa_atual.nome} concluída{Style.RESET_ALL}")
                tarefa_atual = None

        mostrar_estado(tempo_atual, fila, tarefa_atual)
        tempo_atual += 1

escalonador_edf()
