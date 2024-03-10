# for python in less than 3.10
# from typing import Optional
class Nodo(object): 
    def __init__(self, value):
        self.value = value
        # self.left: Optional[Nodo] = None
        # self.right: Optional[Nodo] = None
        self.left: Nodo | None = None
        self.right: Nodo | None = None
    def vacio(self) -> bool:
        return (self.value == None) 
    def __str__(self) -> str:
         return str(self.value) 


class Arbol(object): 
    def __init__(self, root):
        self.root = Nodo(root)

    def imprimirArbol(self):
        return self._preOrderPrint(self.root, "")
    
    def insertar(self, value):
        if self.root is None:
            self.root = value
        else:
            self._insertar_recursivo(value, self.root)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.value:
            if nodo_actual.left is None:
                nodo_actual.left = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.left)
        elif valor > nodo_actual.value:
            if nodo_actual.right is None:
                nodo_actual.right = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.right)

    def _preOrderPrint(self, start , text: str) -> str:
        # Root -> Left -> Right
        if (start):
            text += str(start.value) + "-"
            text = self._preOrderPrint(start.left, text) 
            text = self._preOrderPrint(start.right, text)
        return text

    def buscarNodo(self, valor):
        return self._buscar_recursivo(valor, self.root)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.value:
            return True
        elif valor < nodo_actual.value:
            return self._buscar_recursivo(valor, nodo_actual.left)
        else:
            return self._buscar_recursivo(valor, nodo_actual.right)

if __name__ == "__main__":
    arbol = Arbol(1)
    arbol.insertar(2)
    arbol.insertar(3)
    arbol.insertar(4)
    arbol.insertar(5)
    arbol.insertar(6)
    #test
    print(arbol.root.vacio())
    print(arbol.buscarNodo(3))
    print(arbol.imprimirArbol())
    # arbol.root.left = Nodo(2) 
    # arbol.root.right = Nodo(3) 
    # arbol.root.left.left = Nodo(4) 
    # arbol.root.left.right = Nodo(5) 
    # arbol.root.right.left = Nodo(6) 
    # arbol.root.right.right = Nodo(7) 
