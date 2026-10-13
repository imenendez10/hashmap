class MyHashMap:
    """Taula hash amb encadenament separat i redimensionament."""

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def _bucket_put(self, j, key, value):
        if self._table[j] is None:
            self._table[j] = []

        for pareja in self._table[j]:
            if pareja[0] == key:
                pareja[1] = value
                return

        self._table[j].append([key,value])
        self._n +=1


    def _bucket_get(self, j, key):
        llista = self._table[j]
        if llista is not None:
            for pareja in llista:
                if pareja[0]==key:
                    return pareja[1]
        return -1

    def _bucket_remove(self, j, key):
        llista = self._table[j]
        if llista is None:
            return

        for i, pareja in enumerate(llista):
            if pareja[0] == key:
                llista.pop(i)
                self._n -=1

                if not llista:
                    self._table[j] = None
                return


    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        self._bucket_put(j,key,value)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)


    def get(self, key: int) -> int:
        j = self._hash_function(key)
        return self._bucket_get(j,key)
    

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        self._bucket_remove(j,key)

    def _resize(self,c):
        tabla_antigua = self._table
        self._table = [None] * c

        self._n = 0
        for lista in tabla_antigua:
            if lista is not None:
                for clave, valor in lista:
                    j = self._hash_function(clave)
                    self._bucket_put(j, clave, valor)


    def __len__(self):
        return self._n