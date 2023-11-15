"""Implementacion"""
class NodoTrie:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.hijos = {}  # a b c d ... z
        self.eow = False # fin de palabra(eow)

class Trie:
    def __init__(self) -> None:
        self.raiz = NodoTrie("ROOT")

    def insertar(self, palabra):  # interact
        actual = self.raiz
        for char in palabra:
            if char not in actual.hijos:
                actual.hijos[char] = NodoTrie(char)
            actual = actual.hijos[char]
        actual.eow = True

    def pre_order(self):
        self.pre_order_(self.raiz)

    def pre_order_(self, nodo):  # ROOT - CHILDREN
        print(nodo.valor)
        for char in nodo.hijos.values():
            self.pre_order_(char)

    def post_order(self):
        self.post_order_(self.raiz)

    def post_order_(self, node):  # CHILDREN - ROOT
        for char in node.hijos.values():
            self.post_order_(char)
        print(node.valor)

    def imprimir_trie(self):
        self.imprimir_trie_(self.raiz, "")

    def imprimir_trie_(self, nodo, prefijo):
        if nodo.eow:
            print(prefijo + '|--', nodo.valor, '(eow)')
        else:
            print(prefijo + '|--', nodo.valor)
        prefijo = prefijo + "|  "
        for char in nodo.hijos:
            self.imprimir_trie_(nodo.hijos[char], prefijo)

    def buscar(self, palabra):
        actual = self.raiz
        for char in palabra:
            if char not in actual.hijos:
                return False
            actual = actual.hijos[char]
        return actual.eow

    def eliminar(self, palabra):
        if palabra is None: return
        self.eliminar_(self.raiz, palabra, 0)

    def eliminar_(self, nodo, palabra, indice):
        if indice == len(palabra):
            nodo.eow = False
            return
        char = palabra[indice]
        hijo = nodo.hijos.get(char, None)
        self.eliminar_(hijo, palabra, indice + 1)
        if len(hijo.hijos) == 0 and not hijo.eow:
            nodo.hijos.pop(char)

    def contar_palabras(self):
        return self.contar_palabras_(self.raiz)

    # Time Complexity: O(n) n is the number of characters
    # Space Complexity: O(m*L)
    # --> m is the number of words, L length of each word
    def contar_palabras_(self, nodo):
        contador = 0
        if nodo.eow: contador += 1
        for item in nodo.hijos.values():  # times m
            contador += self.contar_palabras_(item)  # length of word/item
        return contador


trie = Trie()
trie.insertar("INTERACT")
trie.insertar("INTERNATIONAL")
trie.insertar("INTERNET")
print(trie.buscar("INTERACT"))
print(trie.buscar("INTERN"))
#trie.delete("INTERNATIONAL")
#trie.pre_order()
#trie.print()
trie.post_order()
print(trie.contar_palabras())


"""Ejercicio 01: Construir un trie(inicio)"""
"""Ejercicio 01: Construir un trie(fin)"""

"""Ejercicio 01: Construir un trie(inicio)"""
"""Ejercicio 01: Construir un trie(inicio)"""