# Trabalhopratico1-SO
## Trabalho Prático 1: Algoritmo do Banqueiro
  Este projeto implementa o Algoritmo do Banqueiro, um mecanismo de gestão de recursos que garante a segurança do sistema e evita a ocorrência de deadlocks (bloqueios mútuos) em ambientes multithreaded.
### 1. Introdução
  O objetivo deste trabalho é simular um sistema operacional que gere a requisição e libertação de recursos por parte de diversos processos (clientes). O "Banqueiro" atua como um gestor central, permitindo uma alocação apenas se o estado resultante for seguro, ou seja, se existir uma sequência de execução que permita a todos os processos terminarem as suas tarefas.
### 2. Tecnologias Utilizadas
* Linguagem: Python 3.
* Concorrência: Utilização da biblioteca threading para simular múltiplos clientes em paralelo.
* Sincronização: Implementação de threading.Lock (Mutex) para garantir a exclusão mútua e evitar condições de corrida ao aceder às estruturas de dados partilhadas.

### 3. Estrutura do Projeto

O sistema controla os recursos através das seguintes estruturas:

* Available: Vetor com a quantidade disponível de cada tipo de recurso.
* Maximum: Matriz que define a demanda máxima de cada cliente por recurso.
* Allocation: Matriz que regista o montante de recursos atualmente alocados a cada cliente.
* Need: Matriz que calcula a necessidade restante de cada cliente (Máximo - Alocação).

### 4. Como Executar

1 - Pré-requisitos
  Ter o Python 3 instalado no sistema.
  
2 - Instruções de Execução
  Transfira o ficheiro trabalhopratico1.py para uma pasta local.
  
3 - Abra o terminal (ou PowerShell) nessa pasta.
  Execute o programa passando os valores iniciais para os 4 recursos configurados no código.
Exemplo de comando:

* python trabalhopratico1.py 10 5 7 8

### 5. Funcionamento

* Ciclo dos Clientes: Cada thread de cliente opera num loop contínuo: solicita uma quantidade aleatória de recursos, aguarda um tempo, e liberta os recursos posteriormente.
* Decisão do Banqueiro: Sempre que um recurso é pedido, o algoritmo verifica se há unidades suficientes e se a alocação não levará o sistema a um estado de bloqueio.
* Logs do Terminal: O programa exibe mensagens em tempo real:

  [ACEITO]: Quando o estado é seguro e os recursos são entregues.
  
  [NEGADO]: Quando o pedido é recusado para evitar instabilidade.
  
  [LIBERADO]: Quando um cliente devolve recursos ao banco.
