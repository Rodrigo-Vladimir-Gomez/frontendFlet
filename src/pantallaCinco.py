import flet as ft

def pantalla_cinco():
    # Formulario de Administración de Roles de Trabajadores
    form_content = ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Rol del Trabajador:", color='black', size=14, weight="bold"),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="Ingrese el puesto del trabajador",
                                        width=400,
                                        border_radius=10,
                                    ),
                                    ft.ElevatedButton(
                                        text="Buscar",
                                        bgcolor="blue",
                                        color="white",
                                        on_click=lambda e: print("Buscando rol del trabajador"),
                                    ),
                                ],
                                spacing=10,
                            ),
                        ],
                    ),
                ],
                spacing=10,
            ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Guardar",
                        bgcolor="green",
                        color="white",
                        on_click=lambda e: print("Rol guardado"),
                    ),
                    ft.ElevatedButton(
                        text="Actualizar",
                        bgcolor="orange",
                        color="white",
                        on_click=lambda e: print("Rol actualizado"),
                    ),
                    ft.ElevatedButton(
                        text="Eliminar",
                        bgcolor="red",
                        color="white",
                        on_click=lambda e: print("Rol eliminado"),
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.START,
    )

    # Contenedor para el formulario
    form_container = ft.Container(
        content=form_content,
        padding=20,
        width=800,
        bgcolor="white",
        border_radius=10,
        border=ft.border.all(1, ft.colors.BLACK),
    )

    # Retornar la pantalla con el formulario
    return ft.Column(
        controls=[
            #ft.Text("Pantalla 5", size=30, weight=ft.FontWeight.BOLD),
            form_container,
        ]
    )