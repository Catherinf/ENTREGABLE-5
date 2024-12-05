estudiantes = ["Juan", "Ana", "Luis"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

contactos = {
    "Juan": "juan@example.com",
    "Ana": "ana@example.com"
}
for clave, valor in contactos.items():
    print(f"Nombre: {clave}, Correo: {valor}")

nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print("Lista actualizada de estudiantes:", estudiantes)

nuevo_contacto = input("Introduce un nombre para actualizar/agregar: ")
nuevo_correo = input("Introduce el correo de este contacto: ")
contactos[nuevo_contacto] = nuevo_correo
print("Contactos actualizados:", contactos)