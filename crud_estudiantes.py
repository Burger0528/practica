import json
ARCHIVO ="estudiantes.json"

def inicializar ():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def guardar(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

def crear(codigo, nombre, edad):
    data = inicializar()
    data[codigo] = {"nombre": nombre, "edad": edad}
    guardar(data)
    print("Estudiante creado.")

def leer():
    data = inicializar()
    for cod, info in data.items():
        print(cod, info)

def actualizar(codigo, nombre=None, edad=None):
    data = inicializar()
    if codigo in data:
        if nombre:
            data[codigo]["nombre"] = nombre
        if edad is not None:
            data[codigo]["edad"] = edad
        guardar(data)
        print("Estudiante actualizado.")
    else:
        print("Estudiante no encontrado.")

def eliminar(codigo):
    data = inicializar()
    if codigo in data:
        del data[codigo]
        guardar(data)
        print("Estudiante eliminado.")
    else:
        print("Estudiante no encontrado.")
        
if __name__ == "__main__":
    crear("A001", "Ana", 21)
    crear("A002", "Luis", 20)
    leer()
    actualizar("A001", edad=22)
    eliminar("A002")
    leer()