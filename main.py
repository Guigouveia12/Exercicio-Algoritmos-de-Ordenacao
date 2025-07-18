import time
import sys

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return list(map(int, f.read().split()))

def salvar_resultado(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        f.write(' '.join(map(str, dados)))

def main():
    if len(sys.argv) < 2:
        print("Uso: python ordenacao.py <arquivo_de_teste>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    dados_originais = carregar_arquivo(nome_arquivo)

    # Selection Sort
    dados_selection = dados_originais.copy()
    inicio_sel = time.time()
    selection_sort(dados_selection)
    fim_sel = time.time()
    tempo_sel = fim_sel - inicio_sel
    salvar_resultado("saida_selection.txt", dados_selection)

    # Insertion Sort
    dados_insertion = dados_originais.copy()
    inicio_ins = time.time()
    insertion_sort(dados_insertion)
    fim_ins = time.time()
    tempo_ins = fim_ins - inicio_ins
    salvar_resultado("saida_insertion.txt", dados_insertion)

    # Resultados
    print(f"Tempo de execução Selection Sort: {tempo_sel:.6f} segundos")
    print(f"Tempo de execução Insertion Sort: {tempo_ins:.6f} segundos")

    if tempo_sel < tempo_ins:
        print("Selection Sort foi mais rápido.")
    elif tempo_ins < tempo_sel:
        print("Insertion Sort foi mais rápido.")
    else:
        print("Os dois algoritmos tiveram o mesmo tempo de execução.")

if __name__ == "__main__":
    main()
