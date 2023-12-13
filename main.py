import cv2
import numpy as np
import pyautogui
import time
import networkx as nx
import threading



aux = 0
aux2 = 1
aux3 = 1
############
def print_graph_details(graph):
    print("Nós e seus atributos:")
    for node in graph.nodes(data=True):
        print(node)

    print("\nArestas e seus atributos:")
    for edge in graph.edges(data=True):
        print(edge)
############


# Criar um grafo direcionado
G = nx.DiGraph()

# Definir as ações possíveis
class Comando():

    @staticmethod
    def nothing():
        print('Passou no nada')
        return "nothing_state"

    @staticmethod
    def jump():
        print('Passou no pulo')
        pyautogui.keyDown('k')
        time.sleep(0.2)
        pyautogui.keyUp('k')
        return "jump_state"

    @staticmethod
    def stop():
        print('Passou no stop')
        pyautogui.keyUp('d')
        time.sleep(0.2)
        pyautogui.keyDown('d')
        return "stop_state"

    @staticmethod
    def back():
        print('Passou no voltar')
        pyautogui.keyUp('d')
        time.sleep(0.2)
        pyautogui.keyDown('a')
        time.sleep(0.2)
        pyautogui.keyUp('A')
        pyautogui.keyDown('d')
        return "back_state"

    comandos = [nothing, jump, stop, back]


    def execute_command(index):
        if 0 <= index < len(Comando.comandos):
            return Comando.comandos[index]()
        else:
            print("Índice de comando inválido")
            return None

def execute_command(command_method):
    new_state = command_method()
    G.add_node(new_state, command=command_method)
    return new_state


def gameStart():
    global aux3
    global aux2
    global aux
    template = cv2.imread('DEAD.png', 0)
    template2 = cv2.imread('TIME.jpg', 0)
    w, h = template.shape[::-1]

    print("Imagem2 encontrada na tela!")
    pyautogui.keyDown('shift')
    pyautogui.keyDown('f1')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('f1')
    time.sleep(0.5)
    aux3 = 1
    aux=1
    time.sleep(5)
    pyautogui.keyDown('k')
    pyautogui.keyUp('k')
    pyautogui.keyDown('d')
    

    while(True):
        

        screenshot = pyautogui.screenshot()
        gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        res2 = cv2.matchTemplate(gray, template2, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        loc2 = np.where(res2 >= threshold)

            

        if len(loc[0]) > 0:
            aux3 = 0
            time.sleep(5)
            
            aux3 = 1
            time.sleep(5)
            aux2 = 1
            time.sleep(5)
        pass

game_thread = threading.Thread(target=gameStart)
game_thread.start()

comandos = Comando()



current_state = "initial_state"
G.add_node(current_state)

current_state = "initial_state"
G.add_node(current_state)
node_count = 0
print(aux)
time.sleep(5)



while aux == 0:
    time.sleep(0.5)
pyautogui.keyDown('i')
pyautogui.keyUp('i')
while(aux == 1):
    if aux3 == 0:
        pyautogui.keyDown('f1')
        pyautogui.keyUp('f1')
        time.sleep(5)

    while aux2 == 0:
        time.sleep(0.00000001)
    
    time.sleep(3)
    pyautogui.keyDown('k')
    pyautogui.keyUp('k')
    
    while (aux3 == 1):
        command_index = 1  # Exemplo: índice 1 para o comando 'jump'
        new_state = Comando.execute_command(command_index)
        node_count += 1
        print(node_count)
        next_node = f"{new_state}_{node_count}"
        G.add_node(next_node)
        G.add_edge(current_state, next_node, action=Comando.comandos[command_index].__name__)
        current_state = next_node

    pass


