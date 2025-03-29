def main():
    # Crear un diccionario llamado informacion_personal
    informacion_personal = {
        "nombre": "KAREN",
        "apellido": "INFANTE",
        "edad": 20,
        "ciudad": "QUITO",
        "profesion": "Ingeniero"
    }

    # Mostrar la información original
    print("Información original:")
    print(f"Nombre: {informacion_personal['nombre']}")
    print(f"Apellido: {informacion_personal['apellido']}")
    print(f"Profesión: {informacion_personal['profesion']}")
    print(f"Ciudad: {informacion_personal['ciudad']}")

    # Solicitar al usuario que ingrese una nueva ciudad
    nueva_ciudad = input("Ingrese la nueva ciudad: ")
    # Modificar el valor de "ciudad"
    informacion_personal["ciudad"] = nueva_ciudad
    print("Ciudad modificada:", informacion_personal["ciudad"])

    # Agregar una nueva clave-valor para "telefono"
    if "telefono" not in informacion_personal:
        nuevo_telefono = input("Ingrese el número de teléfono: ")  # Solicitar número de teléfono
        informacion_personal["telefono"] = nuevo_telefono  # Agregar el número de teléfono
        print("Teléfono agregado:", informacion_personal["telefono"])

    # Eliminar la clave "edad"
    if "edad" in informacion_personal:
        del informacion_personal["edad"]
        print("Clave 'edad' eliminada.")

    # Imprimir el diccionario final
    print("Diccionario final:")
    for clave, valor in informacion_personal.items():
        print(f"{clave.capitalize()}: {valor}")

# Ejecutar la función main
if __name__ == "__main__":
    main()