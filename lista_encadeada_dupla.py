import time

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class listaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        if self.primeiro == None and self.ultimo == None:
            self.primeiro = novo
            self.ultimo = novo
        else:
            novo.proximo = self.primeiro
            self.primeiro.anterior = novo
            self.primeiro = novo


    def inserir_fim(self, valor):
        novo = No(valor)
        if self.ultimo == None and self.primeiro == None:
            self.ultimo = novo
            self.primeiro = novo
        else:
            novo.anterior = self.ultimo
            self.ultimo.proximo = novo
            self.ultimo = novo


    def excluir_inicio(self):
        if self.primeiro == None and self.ultimo == None:
            print('A lista está vazia')
            return None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None

    def excluir_fim(self):
        if self.primeiro == None and self.ultimo == None:
            print('A lista está vazia')
            return None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None

    def alterar(self, valor1, valor2):
        no = self.localizar(valor1)
        if no == None:
            return None
        else:
            no.valor = valor2

    def listar_inicio(self):
        if self.primeiro == None and self.ultimo == None:
            print('A lista está vazia')
        else:
            atual = self.primeiro
            while atual != None:
                print(atual.valor)
                atual = atual.proximo

    def listar_fim(self):
        if self.primeiro == None and self.ultimo == None:
            print('A lista está vazia')
        else:
            atual = self.ultimo
            while atual != None:
                print(atual.valor)
                atual = atual.anterior


    def localizar(self, valor):
        if self.primeiro == None and self.ultimo == None:
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

    def bubble_sort_inicio(self):
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
            self.bubble_sort_inicio()

    def bubble_sort_fim(self):
        atual = self.ultimo
        foi = True
        while atual.anterior != None:
            if atual.valor > atual.anterior.valor:
                val1 = atual.valor
                val2 = atual.anterior.valor
                atual.valor = val2
                atual.anterior.valor = val1
                foi = False
            else:
                atual = atual.anterior
        if not foi:
            self.bubble_sort_fim()

    def merge_sort_inicio(self, prim):
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
        esq = self.merge_sort_inicio(prim)
        dir = self.merge_sort_inicio(meia)
        return self.merge_inicio(esq, dir)

    def merge_inicio(self, esq, dir):
        tras = None
        if dir == None:
            return esq
        if esq == None:
            return dir
        if esq.valor < dir.valor:
            tras = esq
            tras.proximo = self.merge_inicio(esq.proximo, dir)
        else:
            tras = dir
            tras.proximo = self.merge_inicio(esq, dir.proximo)
        return tras

    def merge_fim(self, esq, dir):
        frente = None
        if dir == None:
            return esq
        if esq == None:
            return dir
        if esq.valor > dir.valor:
            frente = esq
            frente.anterior = self.merge_fim(esq.anterior, dir)
        else:
            frente = dir
            frente.anterior = self.merge_fim(esq, dir.anterior)
        return frente

    def merge_sort_fim(self, ult):
        if ult.anterior == None or ult == None:
            return ult
        rapido = ult
        devagar = ult
        meio = None
        while rapido.anterior != None and rapido.anterior.anterior != None:
            devagar = devagar.anterior
            rapido = rapido.anterior.anterior
        if devagar != None:
            meio = devagar
        meia = meio.anterior
        meio.anterior = None
        esq = self.merge_sort_fim(ult)
        dir = self.merge_sort_fim(meia)
        return self.merge_fim(esq, dir)

    def tempo_bubble(self):
        tic = time.perf_counter()
        self.bubble_sort_inicio()
        toc = time.perf_counter()
        som = toc - tic
        return som

    def tempo_merge(self):
        tic = time.perf_counter()
        self.merge_sort_inicio(self.primeiro)
        toc = time.perf_counter()
        som = toc - tic
        return som