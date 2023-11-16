"""Ejercicio 01: Construir un trie(inicio)"""
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
    """Ejercicio 01: Construir un trie(fin)"""

    """Ejercicio 02: Busqueda un trie(inicio)"""
    def buscar(self, palabra):
        actual = self.raiz
        for char in palabra:
            if char not in actual.hijos:
                return False
            actual = actual.hijos[char]
        return actual.eow
    """Ejercicio 02: Busqueda un trie(fin)"""

    """Ejercicio 03: Contar palabras con cierto prefijo(inicio)"""
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
    def contar_palabra_prefijo(self, prefijo):
        actual = self.raiz
        for char in prefijo:
            if char not in actual.hijos:
                return False
            actual = actual.hijos[char]
        return self.contar_palabras_(actual)
    """Ejercicio 03: Contar palabras con cierto prefijo(fin)"""

    """Ejercicio 04: Eliminacion de palabras del trie(inicio)"""
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
    """Ejercicio 04: Eliminacion de palabras del trie(fin)"""

    """Ejercicio 05: Autocompletado(inicio)"""
    def completar(self, nodo, prefijo, resultado_array):
        if nodo.eow: resultado_array.append(prefijo)
        for char, hijo in nodo.hijos.items():
            self.completar(hijo, prefijo + char, resultado_array)
    def autocompletar(self, cadena):
        actual = self.raiz
        resultado = []
        for char in cadena:
            if char not in actual.hijos:
                return False
            actual = actual.hijos[char]
        self.completar(actual, cadena, resultado)
        return resultado
    """Ejercicio 05: Autocompletado(fin)"""

    """Ejercicio 06: Palabras unicas en un texto(inicio)"""
    def palabras_unicas(self, texto_largo):
        translator = str.maketrans('0123456789,.', ' ' * len('0123456789,.'))
        cadena_con_espacios = texto_largo.translate(translator)
        palabras = cadena_con_espacios.split()

        for palabra in palabras:
            self.insertar(palabra)

        return self.contar_palabras()
    """Ejercicio 06: Palabras unicas en un texto(fin)"""

    """Ejercicio 07: Longitud de la palabra más larga(inicio)"""
    def palabra_larga(self, nodo):
        if not nodo.hijos:
            return 0

        longitud = [self.palabra_larga(hijo) for hijo in nodo.hijos.values()]
        return 1 + max(longitud, default=0)

    """Ejercicio 07: Longitud de la palabra más larga(fin)"""



trie = Trie()
trie.insertar("INTERACT")
trie.insertar("INTERNATIONAL")
trie.insertar("INTERNET")
trie.insertar("AND")
trie.insertar("ANT")
trie.insertar("ANTHEM")
#print(trie.buscar("INTERACT"))
#print(trie.buscar("INTERN"))
#trie.delete("INTERNATIONAL")
#trie.pre_order()
#trie.imprimir_trie()
#trie.post_order()
#print(trie.contar_palabras())
#print(trie.contar_palabra_prefijo("ANT"))
cadena_input = "INTERN"
#print(trie.autocompletar(cadena_input))

#texto con 159 palabras
texto = """En un pequeño pueblo llamado Aldeavieja, vivía un anciano llamado Juan. Juan tenía una granja con muchos animales. Por las mañanas, Juan solía dar de comer a sus gallinas y ovejas. Las gallinas cacareaban y las ovejas balaban, creando un ambiente animado.
Un día, Juan decidió plantar un jardín. Plantó flores de colores brillantes, como rosas y lirios. También sembró vegetales como tomates, zanahorias y lechugas. El jardín de Juan se convirtió en un lugar hermoso y lleno de vida.
Los vecinos de Aldeavieja a menudo visitaban a Juan para disfrutar de su jardín y charlar con él. Compartían historias y risas, creando una comunidad unida. A veces, organizaban pequeñas fiestas en la granja de Juan, donde todos compartían comida y alegría.
A medida que pasaba el tiempo, las estaciones cambiaban, pero la amistad en Aldeavieja permanecía fuerte. Juan continuaba cuidando de sus animales y su jardín, y la gente seguía visitándolo para compartir momentos felices. La vida en Aldeavieja era simple pero llena de significado y conexión."""

trie2 = Trie()
#print(trie2.palabras_unicas(texto))

#print(trie.palabra_larga(trie.raiz))
