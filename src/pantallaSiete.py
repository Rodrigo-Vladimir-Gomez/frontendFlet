import flet as ft

def pantalla_siete():
    # Formulario de Bitácora
    form_content = ft.Column(
        [
            ft.Text("Comentario:", color='black', size=14, weight="bold"),
            ft.TextField(
                multiline=True,
                min_lines=5,
                max_lines=10,
                width=500,
                height=150,
                border_radius=10,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Kilómetros Iniciales:", color='black', size=14, weight="bold"),
                            ft.TextField(
                                keyboard_type=ft.KeyboardType.NUMBER,
                                width=200,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Text("Kilómetros Finales:", color='black', size=14, weight="bold"),
                            ft.TextField(
                                keyboard_type=ft.KeyboardType.NUMBER,
                                width=200,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Galones de Gasolina:", color='black', size=14, weight="bold"),
                            ft.TextField(
                                keyboard_type=ft.KeyboardType.NUMBER,
                                width=200,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Text("Tipo de Gasolina:", color='black', size=14, weight="bold"),
                            ft.TextField(
                                width=200,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Text("Precio:", color='black', size=14, weight="bold"),
                            ft.TextField(
                                keyboard_type=ft.KeyboardType.NUMBER,
                                width=200,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Guardar Bitácora",
                        bgcolor="green",
                        color="white",
                        on_click=lambda e: print("Bitácora guardada"),
                    ),
                    ft.ElevatedButton(
                        text="Modificar Bitácora",
                        bgcolor="blue",
                        color="white",
                        on_click=lambda e: print("Bitácora modificada"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=20,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    # Contenedor con el formulario dentro de una ListView
    form_container = ft.Container(
        content=ft.ListView(
            controls=form_content.controls,
            spacing=10,
        ),
        padding=20,
        width=800,
        height=600,
        bgcolor="white",
        border_radius=10,
        border=ft.border.all(1, ft.colors.BLACK),
    )

    # Retornar la pantalla con el formulario de bitácora
    return ft.Column(
        controls=[form_container],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )
