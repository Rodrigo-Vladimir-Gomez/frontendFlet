import flet as ft

def pantalla_dos():
    # Formulario de Administración de Usuarios
    form_content = ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Nombre:", color="black", size=14, weight="bold"),
                            ft.TextField(
                                hint_text="Ingrese el/los nombres",
                                width=240,
                                border_radius=10,
                            ),
                        ]
                    ),
                    ft.Column(
                        [
                            ft.Text("Apellidos:", color="black", size=14, weight="bold"),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="Ingrese los apellidos",
                                        width=200,
                                        border_radius=10,
                                    ),
                                    ft.ElevatedButton(
                                        text="Buscar",
                                        bgcolor="blue",
                                        color="white",
                                        on_click=lambda e: print("Buscando apellidos"),
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
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Contraseña:", color="black", size=14, weight="bold"),
                            ft.TextField(
                                hint_text="Ingrese la contraseña",
                                password=True,
                                width=240,
                                border_radius=10,
                            ),
                        ]
                    ),
                    ft.Column(
                        [
                            ft.Text("Rol:", color="black", size=14, weight="bold"),
                            ft.Dropdown(
                                width=240,
                                options=[
                                    ft.dropdown.Option("Motorista"),
                                    ft.dropdown.Option("Jefe"),
                                    ft.dropdown.Option("Administrador"),
                                ],
                                hint_text="Seleccione un rol",
                            ),
                        ]
                    ),
                ],
                spacing=10,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("Username:", color="black", size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese el nombre de usuario",
                width=500,
                border_radius=10,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("Estatus:", color="black", size=14, weight="bold"),
            ft.Dropdown(
                width=500,
                options=[
                    ft.dropdown.Option("Activo"),
                    ft.dropdown.Option("Desactivado"),
                ],
                hint_text="Seleccione el estatus",
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Guardar Usuario",
                        bgcolor="green",
                        color="white",
                        on_click=lambda e: print("Usuario guardado"),
                    ),
                    ft.ElevatedButton(
                        text="Actualizar Usuario",
                        bgcolor="orange",
                        color="white",
                        on_click=lambda e: print("Usuario actualizado"),
                    ),
                    ft.ElevatedButton(
                        text="Eliminar Usuario",
                        bgcolor="red",
                        color="white",
                        on_click=lambda e: print("Usuario eliminado"),
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    # Contenedor con scroll automático para el formulario
    scrollable_form = ft.Container(
        content=ft.Column([form_content], scroll=ft.ScrollMode.AUTO),  # Scroll automático
        padding=20,
        width=800,
        bgcolor="white",
        border_radius=10,
        border=ft.border.all(1, ft.colors.BLACK),
    )

    # Retornar la pantalla con el formulario
    return ft.Column(
        controls=[
            #ft.Text("Pantalla 2", size=30, weight=ft.FontWeight.BOLD),
            scrollable_form,
        ]
    )