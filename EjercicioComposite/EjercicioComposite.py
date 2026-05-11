from abc import ABC, abstractmethod

# 1. Base (Componente): Define la interfaz común para objetos simples y complejos
class Carga(ABC):
    @abstractmethod
    def obtener_peso(self) -> float:
        pass

# 2. Hoja (Leaf): El objeto final (un paquete individual o sobre)
class PaqueteIndividual(Carga):
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def obtener_peso(self) -> float:
        print(f"  Analizando paquete '{self.nombre}': {self.peso}kg")
        return self.peso

# 3. Compuesto (Composite): Puede contener hojas u otros compuestos (una caja o contenedor)
class ContenedorCarga(Carga):
    def __init__(self, nombre):
        self.nombre = nombre
        self._elementos = []

    def agregar(self, elemento: Carga):
        self._elementos.append(elemento)

    def obtener_peso(self) -> float:
        peso_total = 0
        print(f"Abriendo caja: {self.nombre}...")
        for elemento in self._elementos:
            peso_total += elemento.obtener_peso()
        print(f"Subtotal de '{self.nombre}': {peso_total}kg")
        return peso_total


if __name__ == "__main__":
    
    laptop = PaqueteIndividual("Laptop", 2.5)
    audifonos = PaqueteIndividual("Airpods", 1.0)
    balon = PaqueteIndividual("Balon Basketball", 1.0)

    caja_accesorios = ContenedorCarga("Caja de Accesorios")
    caja_accesorios.agregar(audifonos)
    caja_accesorios.agregar(balon)

    pallet_tecnologia = ContenedorCarga("Carga de Objetos Varios")
    pallet_tecnologia.agregar(laptop)        
    pallet_tecnologia.agregar(caja_accesorios) 

    print("--- INICIANDO PESO DE EMBARQUE ---")
    resultado_final = pallet_tecnologia.obtener_peso()
    
    print("-" * 35)
    print(f"PESO TOTAL: {resultado_final} kg")