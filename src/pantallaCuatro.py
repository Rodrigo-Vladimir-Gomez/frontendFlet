import flet as ft

def pantalla_cuatro():
    # Formulario de Administración de Vehículos
    form_content = ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Modelo del Vehículo:", color='black', size=14, weight="bold"),
                            ft.Row(
                                [
                                    ft.TextField(
                                        hint_text="Ingrese el modelo del vehículo",
                                        width=400,
                                        border_radius=10,
                                    ),
                                    ft.ElevatedButton(
                                        text="Buscar",
                                        bgcolor="blue",
                                        color="white",
                                        on_click=lambda e: print("Buscando modelo del vehículo"),
                                    ),
                                ],
                                spacing=10,
                            ),
                        ],
                    ),
                ],
                spacing=10,
            ),
            ft.Text("Marca del Vehículo:", color='black', size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese la marca del vehículo",
                width=500,
                border_radius=10,
            ),
            ft.Text("Placa del Vehículo:", color='black', size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese el número de la placa",
                width=500,
                border_radius=10,
            ),
            ft.Text("Rendimiento del Vehículo (km/gal):", color='black', size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese el rendimiento estimado (km/gal)",
                width=500,
                border_radius=10,
            ),
            ft.Text("Galonaje del Vehículo:", color='black', size=14, weight="bold"),
            ft.TextField(
                hint_text="Ingrese la capacidad total de galones",
                width=500,
                border_radius=10,
            ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Guardar Vehículo",
                        bgcolor="green",
                        color="white",
                        on_click=lambda e: print("Información del vehículo guardada"),
                    ),
                    ft.ElevatedButton(
                        text="Actualizar Información",
                        bgcolor="orange",
                        color="white",
                        on_click=lambda e: print("Información del vehículo actualizada"),
                    ),
                    ft.ElevatedButton(
                        text="Eliminar Información",
                        bgcolor="red",
                        color="white",
                        on_click=lambda e: print("Información del vehículo eliminada"),
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.START,
    )

    # Contenedor con ListView para scroll automático
    form_container = ft.Container(
        content=ft.ListView(  # Uso de ListView para scroll
            controls=form_content.controls,
            spacing=10,
        ),
        padding=20,
        width=800,
        height=600,  # Altura fija para el área desplazable
        bgcolor="white",
        border_radius=10,
        border=ft.border.all(1, ft.colors.BLACK),
    )

    # Retornar la pantalla con el formulario
    return ft.Column(
        controls=[
            #ft.Text("Pantalla 4", size=30, weight=ft.FontWeight.BOLD),
            form_container,
        ]
    )