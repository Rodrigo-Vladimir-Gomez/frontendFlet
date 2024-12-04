import flet as ft

def pantalla_tres():
    # Formulario de Administración de Proyectos con scroll
    form_content = ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Nombre del Proyecto:", color="black", size=14, weight="bold"),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="Ingrese el nombre del proyecto",
                                        width=400,
                                        border_radius=10,
                                    ),
                                    ft.ElevatedButton(
                                        text="Buscar",
                                        bgcolor="blue",
                                        color="white",
                                        on_click=lambda e: print("Buscando proyecto"),
                                    ),
                                ],
                                spacing=10,
                            ),
                        ]
                    ),
                ],
                spacing=20,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("Dirección del Proyecto:", color="black", size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese la dirección del proyecto",
                multiline=True,
                min_lines=2,
                max_lines=5,
                width=500,
                height=70,
                border_radius=10,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("Estado del Proyecto:", color="black", size=14, weight="bold"),
            ft.Dropdown(
                width=500,
                options=[
                    ft.dropdown.Option("Activo"),
                    ft.dropdown.Option("Desactivado"),
                ],
                hint_text="Seleccione el estado del proyecto",
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Guardar Proyecto",
                        bgcolor="green",
                        color="white",
                        on_click=lambda e: print("Información del proyecto guardada"),
                    ),
                    ft.ElevatedButton(
                        text="Actualizar Proyecto",
                        bgcolor="orange",
                        color="white",
                        on_click=lambda e: print("Información del proyecto actualizada"),
                    ),
                    ft.ElevatedButton(
                        text="Eliminar Proyecto",
                        bgcolor="red",
                        color="white",
                        on_click=lambda e: print("Información del proyecto eliminada"),
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
    )

    # Contenedor con scroll automático para el formulario
    scrollable_form = ft.Container(
        content=ft.Column([form_content], scroll=ft.ScrollMode.AUTO),
        padding=20,
        width=800,
        bgcolor="white",
        border_radius=10,
        border=ft.border.all(1, ft.colors.BLACK),
    )

    # Retornar la pantalla con el formulario
    return ft.Column(
        controls=[
            #ft.Text("Pantalla 3", size=30, weight=ft.FontWeight.BOLD),
            scrollable_form,
        ]
    )