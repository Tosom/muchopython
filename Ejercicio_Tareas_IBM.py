"""LISTA DE TAREAS
1_Función para agragar nueva tarea a lista de tareas pendientes
2_Marcar como completada una tarea según su posición
3_Mostrar en pantalla todas las tareas numeradas y estado (completada o pendiente)
4_Eliminar tarea según su posición
5_Manejo de excepciones en caso de opción no válida o posición inexistente
6_Código comentado"""

# Creamos la clase, el constructor y una lista
class TareasPendientes:
    def __init__(self):
        self.tareas = []

    # Método para añadir tareas y usamos un diccionario indicando que está pendiente por defecto
    def agregar_tarea(self, tarea):
        if tarea not in [t["descripcion"] for t in self.tareas]:
            self.tareas.append({"descripcion": tarea, "completada": False})
            print(f"Tarea '{tarea}' agregada correctamente")
        else:
            print("La tarea ya existe en la lista")

    # Método para marcar una tarea como completada, si ya está completada, da la opción de cambiar su estado
    def marcar_completada(self, posicion):
        if 0 <= posicion < len(self.tareas):
            tarea = self.tareas[posicion]
            if tarea["completada"]:  #Si quiere cambiar una tarea ya completada da la opción de volverla a pendiente
                opcion = input("La tarea ya está marcada como completada. ¿Desea cambiar su estado? (s/n): ")
                if opcion.lower() == "s":
                    tarea["completada"] = False
                    print(f"Estado de la tarea '{tarea['descripcion']}' cambiado a 'pendiente'")
                else:
                    print("No se ha realizado ningún cambio")
            else:
                tarea["completada"] = True
                print(f"Tarea '{tarea['descripcion']}' marcada como completada")
        else:
            raise IndexError("La posición no es válida")

    # Comprobamos si hay tareas pendientes y las numeramos
    def mostrar_todas_las_tareas(self):
        if not self.tareas:
            print("No tienes tareas pendientes")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "completada" if tarea["completada"] else "pendiente"
                print(f"{i + 1}. {tarea['descripcion']} - {estado}")

    # Eliminamos una tarea según su posición, si el valor no es válido saltamos a la excepción "IndexError"
    def eliminar_tarea(self, posicion):
        if 0 <= posicion < len(self.tareas):
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada correctamente")
        else:
            raise IndexError("La posición seleccionada no es válida")

# Creamos una instancia de TareasPendientes y la llamamos lista_tareas
def main():
    lista_tareas = TareasPendientes()

    # Creamos un bucle para imprimir en pantalla las opciones
    while True:
        print("\n1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                tarea = input("Ingrese la nueva tarea: ")
                lista_tareas.agregar_tarea(tarea)
            elif opcion == 2:
                # Mostrar todas las tareas antes de seleccionar cuál marcar como completada
                lista_tareas.mostrar_todas_las_tareas()
                posicion = int(input("Ingrese la posición de la tarea que quiere completar: ")) - 1 #ponemos -1 para ajustarlo a los valores que empiezan siempre en 0
                lista_tareas.marcar_completada(posicion)
            elif opcion == 3:
                lista_tareas.mostrar_todas_las_tareas()
            elif opcion == 4:
                # Mostrar todas las tareas antes de seleccionar cuál eliminar
                lista_tareas.mostrar_todas_las_tareas()
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1 #ponemos -1 para ajustarlo a los valores que empiezan siempre en 0
                lista_tareas.eliminar_tarea(posicion)
            elif opcion == 5:
                print("Hasta la vista...Baby")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número.")
        

if __name__ == "__main__":
    main()
    