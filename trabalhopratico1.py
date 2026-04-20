import threading
import random
import sys
import time

NUMBER_OF_CUSTOMERS = 7
NUMBER_OF_RESOURCES = 4

available = []
maximum = []
allocation = [[0] * NUMBER_OF_RESOURCES for _ in range(NUMBER_OF_CUSTOMERS)]
need = []

mutex = threading.Lock()

def is_safe_state():
    """Ele verifica se o estado é seguro aqui"""
    work = list(available)
    finish = [False] * NUMBER_OF_CUSTOMERS
    
    while True:
        found = False
        for i in range(NUMBER_OF_CUSTOMERS):
            if not finish[i]:
                # Verifica se Need <= Work [cite: 129]
                if all(need[i][j] <= work[j] for j in range(NUMBER_OF_RESOURCES)):
                    for j in range(NUMBER_OF_RESOURCES):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    found = True
        if not found:
            break
            
    return all(finish)

def request_resources(customer_num, request):
    """ Quando é feita a solicitação"""
    with mutex:
        # Verifica se solicitaçao é menor q a necessidade
        if any(request[j] > need[customer_num][j] for j in range(NUMBER_OF_RESOURCES)):
            return -1
        
        # Verifica se solicitaçao <= disponível
        if any(request[j] > available[j] for j in range(NUMBER_OF_RESOURCES)):
            return -1
        
        # Alocacao temporaria
        for j in range(NUMBER_OF_RESOURCES):
            available[j] -= request[j]
            allocation[customer_num][j] += request[j]
            need[customer_num][j] -= request[j]
            
        if is_safe_state():
            print(f"[ACEITO] Cliente {customer_num} recebeu {request}. Disponível: {available}")
            return 0
        else:
            # Reverte se o estado é inseguro
            for j in range(NUMBER_OF_RESOURCES):
                available[j] += request[j]
                allocation[customer_num][j] -= request[j]
                need[customer_num][j] += request[j]
            print(f"[NEGADO] Cliente {customer_num} pediu {request} - Estado Inseguro.")
            return -1

def release_resources(customer_num, release):
    """A função de liberação"""
    with mutex:
        for j in range(NUMBER_OF_RESOURCES):
            available[j] += release[j]
            allocation[customer_num][j] -= release[j]
            need[customer_num][j] += release[j]
        print(f"[LIBERADO] Cliente {customer_num} devolveu {release}. Disponível: {available}")
        return 0

def customer(customer_id):
    """Loop contínuo para o cliente"""
    while True:
        # Gera pedido aleatório limitado
        request = [random.randint(0, need[customer_id][j]) for j in range(NUMBER_OF_RESOURCES)]
        if any(request):
            request_resources(customer_id, request)
        
        time.sleep(random.randint(1, 3))
        
        # Libera parte do que tem
        release = [random.randint(0, allocation[customer_id][j]) for j in range(NUMBER_OF_RESOURCES)]
        if any(release):
            release_resources(customer_id, release)
            
        time.sleep(random.randint(1, 3))

if __name__ == "__main__":
    if len(sys.argv) != NUMBER_OF_RESOURCES + 1:
        print(f"Uso: python {sys.argv[0]} <res1> <res2> <res3>") 
        sys.exit(1)

    # Inicializa recursos disponíveis via linha de comando 
    available = [int(x) for x in sys.argv[1:]]
    
    # Inicializa matrizes de necessidade 
    for i in range(NUMBER_OF_CUSTOMERS):
        max_val = [random.randint(0, available[j]) for j in range(NUMBER_OF_RESOURCES)]
        maximum.append(max_val)
        need.append(list(max_val))

    print(f"Sistema iniciado com recursos: {available}")

    # Cria as threads dos clientes 
    threads = []
    for i in range(NUMBER_OF_CUSTOMERS):
        t = threading.Thread(target=customer, args=(i,))
        threads.append(t)
        t.start()