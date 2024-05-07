class TareasPendientes:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, posicion):
        if 0 <= posicion < len(self.tareas):
            self.tareas[posicion]["completada"] = True
        else:
            raise IndexError("La posición de la tarea no es válida")

    def mostrar_todas_las_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i + 1}. {tarea['descripcion']} - {estado}")

    def eliminar_tarea(self, posicion):
        if 0 <= posicion < len(self.tareas):
            del self.tareas[posicion]
        else:
            raise IndexError("La posición de la tarea no es válida")


def main():
    lista_tareas = TareasPendientes()

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
                print("Tarea agregada exitosamente")
            elif opcion == 2:
                posicion = int(input("Ingrese la posición de la tarea completada: ")) - 1
                lista_tareas.marcar_completada(posicion)
                print("Tarea marcada como completada")
            elif opcion == 3:
                lista_tareas.mostrar_todas_las_tareas()
            elif opcion == 4:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
                lista_tareas.eliminar_tarea(posicion)
                print("Tarea eliminada correctamente")
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 5")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        except IndexError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
