import time

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class listaSimples:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        else:
            self.primeiro = self.primeiro.proximo

    def alterar(self, valor1, valor2):
        no = self.localizar(valor1)
        if no == None:
            return None
        else:
            no.valor = valor2

    def listar(self):
        if self.primeiro == None:
            print('A lista está vazia')
        else:
            atual = self.primeiro
            while atual != None:
                print(atual.valor)
                atual = atual.proximo


    def localizar(self, valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        atual = self.primeiro
        while atual != None:
            if atual.valor == valor:
                print(atual)
                return None
            else:
                atual = atual.proximo
        print('Valor não existe')

    def bubble_sort(self):
        atual = self.primeiro
        foi = True
        while atual.proximo != None:
            if atual.valor > atual.proximo.valor:
                val1 = atual.valor
                val2 = atual.proximo.valor
                atual.valor = val2
                atual.proximo.valor = val1
                foi = False
            else:
                atual = atual.proximo
        if not foi:
            self.bubble_sort()
            
    def merge_sort(self, prim):
        if prim.proximo == None or prim == None:
            return prim
        rapido = prim
        devagar = prim
        meio = None
        while rapido.proximo != None and rapido.proximo.proximo != None:
            devagar = devagar.proximo
            rapido = rapido.proximo.proximo
        if devagar != None:
            meio = devagar
        meia = meio.proximo
        meio.proximo = None
        esq = self.merge_sort(prim)
        dir = self.merge_sort(meia)
        return self.merge(esq, dir)

    def merge(self, esq, dir):
        tras = None
        if dir == None:
            return esq
        if esq == None:
            return dir
        if esq.valor < dir.valor:
            tras = esq
            tras.proximo = self.merge(esq.proximo, dir)
        else:
            tras = dir
            tras.proximo = self.merge(esq, dir.proximo)
        return tras

    def tempo_bubble(self):
        tic = time.perf_counter()
        self.bubble_sort()
        toc = time.perf_counter()
        som = toc - tic
        return som

    def tempo_merge(self):
        tic = time.perf_counter()
        self.merge_sort(self.primeiro)
        toc = time.perf_counter()
        som = toc - tic
        return som

lista = listaSimples()
lista.inserir_inicio(6)
lista.inserir_inicio(7)
lista.inserir_inicio(3)
lista.inserir_inicio(8)
lista.inserir_inicio(42)
lista.inserir_inicio(84)
print(lista.tempo_merge())