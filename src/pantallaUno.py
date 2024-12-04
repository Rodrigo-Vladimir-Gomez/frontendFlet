import flet as ft

def pantalla_uno():
    # Formulario de gasolinera
    form_content = ft.Column(
        controls=[
            # Título de la Gasolinera
            ft.Text("Nombre de la Gasolinería:", color='black', size=14, weight="bold"),
            ft.Row(
                controls=[
                    ft.TextField(
                        hint_text="Ingrese el nombre de la gasolinera",
                        width=400,
                        border_radius=10,
                    ),
                    ft.ElevatedButton(
                        text="Buscar",
                        bgcolor="blue",
                        color="white",
                        on_click=lambda e: print("Buscando información de gasolinera"),
                    ),
                ],
                spacing=10,
            ),
            ft.Divider(height=20, color="transparent"),  # Espacio entre secciones
            ft.Text("Dirección de la Gasolinería:", color='black', size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese la dirección de la gasolinera",
                multiline=True,
                min_lines=2,
                max_lines=5,
                width=500,
                height=100,
                border_radius=10,
            ),
            ft.Divider(height=20, color="transparent"),
            # Botones de acción
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="Guardar Información",
                        bgcolor="green",
                        color="white",
                        on_click=lambda e: print("Información de gasolinera guardada"),
                    ),
                    ft.ElevatedButton(
                        text="Actualizar Información",
                        bgcolor="orange",
                        color="white",
                        on_click=lambda e: print("Información de gasolinera actualizada"),
                    ),
                    ft.ElevatedButton(
                        text="Eliminar Información",
                        bgcolor="red",
                        color="white",
                        on_click=lambda e: print("Información de gasolinera eliminada"),
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,  # Alineación vertical al inicio (arriba)
    )

    # Contenedor para el formulario
    form_container = ft.Container(
        content=form_content,
        padding=20,
        width=800,  # Ancho ajustado para el formulario
        bgcolor="white",
        border_radius=10,
        border=ft.border.all(1, ft.colors.BLACK),
    )

    # Retornar el contenedor con el formulario dentro
    return ft.Column(
        controls=[
            #ft.Text("Pantalla 1", size=30, weight=ft.FontWeight.BOLD),
            form_container  # Formulario contenido dentro del contenedor
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,  # Alineación vertical al inicio (arriba)
    )