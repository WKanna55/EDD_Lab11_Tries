"""Implementacion"""


class NodoTrie:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.hijos = {}  # a b c d ... z
        self.eow = False


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

    def search(self, palabra):
        current = self.raiz
        for char in palabra:
            if char not in current.hijos:
                return False
            current = current.hijos[char]
        return current.eow

    def delete(self, palabra):
        if palabra is None: return
        self.delete_(self.raiz, palabra, 0)

    def delete_(self, nodo, palabra, indice):
        if indice == len(palabra):
            nodo.eow = False
            return
        char = palabra[indice]
        child = nodo.hijos.get(char, None)
        self.delete_(child, palabra, indice + 1)
        if len(child.hijos) == 0 and not child.eow:
            nodo.hijos.pop(char)

    def remove(self, palabra):
        actual = self.raiz
        for char in palabra:
            if char not in actual.hijos:
                return False
            actual = actual.hijos[char]
        if actual.eow:
            actual.eow = False
            for child in actual.hijos.values():
                self.remove(child.valor)
            return True
        if actual.hijos:
            actual.hijos = {}
            return True
        actual.valor = None
        return True

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
print(trie.search("INTERACT"))
print(trie.search("INTERN"))
#trie.delete("INTERNATIONAL")
#trie.pre_order()
#trie.print()
trie.post_order()
print(trie.contar_palabras())
