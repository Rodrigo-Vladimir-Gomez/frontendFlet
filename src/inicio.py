import flet as ft

def pantalla_inicio(page):
    def navegar_menu(e):
        # Cambiar el contenido a la vista del menú principal
        page.controls.clear()  # Limpia todos los controles actuales
        from main import cargar_menu_principal
        cargar_menu_principal(page)

    return ft.Container(
        content=ft.Column(
            [
                ft.ElevatedButton(
                    "Iniciar",
                    bgcolor=ft.Colors.BLACK,  # Botón negro
                    color=ft.Colors.WHITE,    # Texto blanco
                    on_click=navegar_menu,    # Navegar al menú
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar el botón verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar el botón horizontalmente
        ),
        expand=True,
        bgcolor=ft.Colors.WHITE,  # Fondo blanco para la pantalla
    )
