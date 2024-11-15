import sys
import random
import os
import time

def arquivo_vazio(arquivo_input): #Verifica se o Arquivo está vazio
    with open(arquivo_input, 'r') as file:
        return os.stat(arquivo_input).st_size == 1

def switch(numero, letra, arquivo_input):
    if arquivo_vazio(arquivo_input): #Para a execução se o arquivo for vazio
        print(f'O arquivo {arquivo_input} está vazio.')
        sys.exit()
        
    try:
        #Abre o arquivo e salva em letra e numero
        with open(arquivo_input, 'r') as file:
            numero = file.readline()
            letra = file.readline()
    except FileNotFoundError: #Verifica se o arquivo existe
        print("Error: O arquivo não foi encontrado")
        sys.exit()
    except IOError: #Verifica se foi aberto com sucesso
        print("Error: Erro ao abrir o arquivo")
        sys.exit()
    
    try: #Verifica se a letra é uma letra
        letra = int(letra)
        print(f"Error: Arquivo com a formatação invalida!")
        sys.exit()
    except ValueError:
        pass

    #Transforma numero em int, e retira o \n da variavel letra
    numero = int(numero)
    letra = letra.rstrip('\n')
    
    return numero, letra

def ordem_crescente(qnt): #Função que gera uma quantidade qnt de valores em ordem crescente
    return list(range(1, qnt + 1))

def ordem_decrescente(qnt): #Função que gera uma quantidade qnt de valores em ordem decrescente
    return list(range(qnt, 0, -1))

def ordem_aleatoria(qnt): #Função que gera uma quantidade qnt de valores em ordem aleatoria entre 0 e 32000
    numeros = list(range(1, qnt + 1))
    random.shuffle(numeros)
    return [random.randint(0, 32000) for _ in range(qnt)]

def insertionSort(lista_num):
    start_time = time.perf_counter()
    vetor = lista_num.copy()
    n = len(vetor)
    comp = 0
    
    #indica qual elemento que vai ser ordenado
    for I in range (1, n):
        auxiliar = vetor[I]
        comp = comp + 1
        J = I - 1
        
        while J >= 0 and auxiliar < vetor[J]:
            vetor[J + 1] = vetor[J]
            J = J - 1
        vetor[J + 1] = auxiliar
    
    end_time = time.perf_counter()
    tempo_execucao = (end_time - start_time) * 1000
    return f"{vetor}, {comp} comp, {tempo_execucao: .4}ms"

def selectionSort(lista_num):
    start_time = time.time()
    vetor = lista_num.copy()
    n = len(lista_num)
    comp = 0
    
    
    for N in range(n):
        menor = vetor[N]
        indice = N
        
        
        for i in range(N, n):
            if vetor[i] < menor:
                comp = comp + 1
                menor = vetor[i]
                indice = i
        if menor != vetor[N]:
            aux = vetor[N]
            vetor[N] = vetor[indice]
            vetor[indice] = aux
    end_time = time.perf_counter()
    tempo_execucao = (end_time - start_time) * 1000
    return f"{vetor}, {comp} comp, {tempo_execucao: .4}ms"
    
    
    

def bubbleSort(lista_num):
    vetor = lista_num.copy()
    comp = 0
    n = len(vetor)
    
    start_time = time.perf_counter()  # Marca o início do tempo de execução

    # Percorre toda a lista_num
    for i in range(n):
        trocou = False  # Flag para verificar se houve troca

        # Últimos elementos já estão na posição correta após cada iteração
        for j in range(0, n - i - 1):
            comp += 1  # Incrementa o contador de comparações
            
            # Compara os elementos adjacentes
            if vetor[j] > vetor[j + 1]:
                # Troca os elementos se estiverem na ordem errada
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocou = True

        # Se não houve troca, a lista_num já está ordenada
        if not trocou:
            break
    
    end_time = time.perf_counter()  # Marca o final do tempo de execução
    tempo_execucao = (end_time - start_time) * 1000 # Calcula o tempo de execução
    return f"{vetor}, {comp} comp, {tempo_execucao: .4}ms"
 
def mergeSort(vetor):
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    comp = [0]  # Contador de comparações, usando lista para ser mutável
    
    def mergesortRecursivo(vetor):
        if len(vetor) <= 1:
            return vetor
        meio = len(vetor) // 2
        esquerda = mergesortRecursivo(vetor[:meio])
        direita = mergesortRecursivo(vetor[meio:])
        return merge(esquerda, direita)

    def merge(esquerda, direita):
        resultado = []
        while esquerda and direita:
            comp[0] += 1  # Contabiliza a comparação
            if esquerda[0] < direita[0]:
                resultado.append(esquerda.pop(0))
            else:
                resultado.append(direita.pop(0))
        resultado.extend(esquerda)
        resultado.extend(direita)
        return resultado
    
    sorted_vetor = mergesortRecursivo(vetor)
    end_time = time.perf_counter()  # Finaliza a contagem do tempo
    tempo_execucao = (end_time - start_time) * 1000  # Tempo em milissegundos
    return f"{sorted_vetor}, {comp[0]} comparações, {tempo_execucao:.4f}ms"
            

def quicksort(lista_num):
    # Cria uma cópia do vetor para não modificar o original
    vetor = lista_num.copy()
    comp = [0] 
    # Chama a função recursiva para ordenar o vetor
    quicksortRecursivo(vetor, 0, len(vetor) - 1, comp)
    
    tempo_execucao = 0  # Placeholder para o tempo de execução
    return f"{vetor}, {comp[0]} comp, {tempo_execucao}ms"


def quicksortRecursivo(vetor, ini, fim, comp):
    if ini < fim:
        pivo = particiona(vetor, ini, fim, comp)
        quicksortRecursivo(vetor, ini, pivo - 1, comp)
        quicksortRecursivo(vetor, pivo + 1, fim, comp)


def particiona(vetor, ini, fim, comp):
    esq = ini + 1
    dir = fim
    pivo = vetor[ini]

    while esq <= dir:
        while esq <= fim and vetor[esq] <= pivo:
            esq += 1
            comp[0] += 1  # Incrementa o contador de comparações
        while dir > ini and vetor[dir] > pivo:
            dir -= 1
            comp[0] += 1  # Incrementa o contador de comparações
        if esq < dir:
            vetor[esq], vetor[dir] = vetor[dir], vetor[esq]

    # Coloca o pivô na posição correta
    vetor[ini], vetor[dir] = vetor[dir], vetor[ini]
    return dir


def heapify(vetor, n, i, comp):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Verifica o filho esquerdo
    if esquerda < n and vetor[esquerda] > vetor[maior]:
        maior = esquerda
        comp[0] += 1  # Incrementa o contador de comparações

    # Verifica o filho direito
    if direita < n and vetor[direita] > vetor[maior]:
        maior = direita
        comp[0] += 1  # Incrementa o contador de comparações

    # Se o maior não é o nó atual
    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]  # Faz a troca
        # Recursivamente aplica o heapify no subárvore afetada
        heapify(vetor, n, maior, comp)


def heapSortRecursivo(vetor):
    comp = [0]  # Contador de comparações
    
    n = len(vetor)

    # Constrói o heap (reorganiza o vetor)
    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i, comp)

    # Extrai elementos um a um da heap
    for i in range(n - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]  # Move o maior elemento para o fim do vetor
        heapify(vetor, i, 0, comp)  # Chama heapify no heap reduzido
    
    tempo_execucao = 0  # Placeholder para o tempo de execução
    return f"{vetor}, {comp[0]} comp, {tempo_execucao}ms"


def heapSort(lista_num):
    vetor = lista_num.copy()
    resultado = heapSortRecursivo(vetor)  # Chama a função recursiva e recebe o resultado
    return resultado  # Retorna o resultado para quem chamou a função
    
    

def chama_algoritimos(lista_num):
    
    
    #insertionSort, selectionSort, bubbleSort, mergeSort, quickSort, e heapSort;
    print(f"InsertionSort {insertionSort(lista_num)}")
    print(f"SelectionSort {selectionSort(lista_num)}")
    print(f"BubbleSort {bubbleSort(lista_num)}")
    print(f"MergeSort {mergeSort(lista_num)}")
    print(f"QuickSort {quicksort(lista_num)}")
    print(f"HeapSort {heapSort(lista_num)}")
    
def main():
    arquivo_python = os.path.basename(__file__)
    if len(sys.argv) != 3: #Verifica se foram passados a quantidade de argumentos certos no terminal
        print(f"Error, use: python {arquivo_python} <arquivo_input> <arquivo_output>")
        sys.exit()
        
    arquivo_input = sys.argv[1] #Arquivo de entrada/Leitura
    arquivo_output = sys.argv[2] #Arquivo de saida/Escrita
        
    letra = ''
    qnt = ''
    qnt, letra = switch(qnt, letra, arquivo_input) #Chama a funão que abre e verifica o arquivo, e retorna o que foi lido em 2 variaveis
    if qnt <= 0: #Verifica se o arquivo não contem um numero invalido de tamanho do vetor/lista_num
        print("Error: O arquivo contem um numero invalido para a execução do programa")
        sys.exit()

    if letra == 'c': #Verifica se o arquivo tem o caracter que corresponde a alguma função do programa
        lista_num = ordem_crescente(qnt)
    elif letra == 'd':
        lista_num = ordem_decrescente(qnt)
    elif letra == 'r':
        lista_num = ordem_aleatoria(qnt)
    else: #Sai do programa se o caracter nao for c, d ou r
        print("Error: O arquivo contem uma letra invalida para a execução do programa")
        sys.exit()
    
    chama_algoritimos(lista_num)
    

if __name__ == "__main__":
    main()
