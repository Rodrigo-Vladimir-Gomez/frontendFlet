import flet as ft
from pantallaUno import pantalla_uno
from pantallaDos import pantalla_dos
from pantallaTres import pantalla_tres
from pantallaCuatro import pantalla_cuatro
from pantallaCinco import pantalla_cinco
from pantallaSeis import pantalla_seis
from pantallaSiete import pantalla_siete

def main(page: ft.Page):
    page.title = "Administración"
    page.bgcolor = "white"  # Fondo blanco para la página

    # Barra superior nueva (AppBar)
    app_bar = ft.AppBar(
        title=ft.Text("Fundamentos de Base de Datos FBD135", color="white", weight="bold", size=20),
        bgcolor="blue",
    )

    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    # Contenido principal (donde se mostrarán las pantallas)
    contenido = ft.Container(
        expand=True,
        bgcolor=ft.colors.WHITE,  # Fondo blanco para el contenido
        padding=20,
        height=page.height,  # Mantener el tamaño de la pantalla
    )

    # Función para cambiar el contenido de la pantalla
    def cambiar_pantalla(e):
        ruta = e.control.data
        if ruta == "pantalla_1":
            contenido.content = pantalla_uno()
        elif ruta == "pantalla_2":
            contenido.content = pantalla_dos()
        elif ruta == "pantalla_3":
            contenido.content = pantalla_tres()
        elif ruta == "pantalla_4":
            contenido.content = pantalla_cuatro()
        elif ruta == "pantalla_5":
            contenido.content = pantalla_cinco()
        elif ruta == "pantalla_6":
            contenido.content = pantalla_seis()
        elif ruta == "pantalla_7":
            contenido.content = pantalla_siete()
            #Agregar las pantallas
        page.update()  # Actualiza la página para reflejar los cambios

    # Menú lateral con botones en lugar de ListTile
    menu_lateral = ft.Container(
        bgcolor=ft.colors.WHITE,  # Fondo blanco para el menú lateral
        content=ft.Column(
            controls=[
                ft.Row(
                    [
                        ft.Icon(ft.icons.PERSON, color="blue"),
                        ft.Text("Usuario", color="black", size=16, weight="bold"),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.ElevatedButton(
                    text="Gasolineras",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_1",  # Asignar el identificador de la pantalla
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto negro
                        bgcolor=ft.colors.BLUE_400,  # Fondo transparente
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 15, 10, 15),  # Ajuste de tamaño con padding
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Usuarios",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_2",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto negro
                        bgcolor=ft.colors.BLUE_400,  # Fondo transparente
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 15, 10, 15),  # Ajuste de tamaño con padding
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Proyectos",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_3",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto blanco
                        bgcolor=ft.colors.BLUE_400,  # Fondo azul
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 5, 10, 5),
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Vehiculos",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_4",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto blanco
                        bgcolor=ft.colors.BLUE_400,  # Fondo azul
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 5, 10, 5),
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Roles",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_5",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto blanco
                        bgcolor=ft.colors.BLUE_400,  # Fondo azul
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 5, 10, 5),
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Logs",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_6",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto blanco
                        bgcolor=ft.colors.BLUE_400,  # Fondo azul
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 5, 10, 5),
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Bitacora",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_7",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto blanco
                        bgcolor=ft.colors.BLUE_400,  # Fondo azul
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 5, 10, 5),
                    ),
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Salir",
                    on_click=lambda e: cambiar_pantalla(e),
                    data="pantalla_inicio",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,  # Texto blanco
                        bgcolor=ft.colors.RED,  # Fondo azul
                        elevation=3,  # Sombras del botón
                        padding=ft.Padding(10, 5, 10, 5),
                    ),
                    width=200,
                    height=50,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        ),
        expand=False,
        width=200,  # Ancho fijo del menú lateral
        height=page.height,  # Altura fija para el menú lateral
        padding=ft.Padding(10, 0, 10, 0),
    )

    # Layout principal
    page.add(app_bar)  # Agregar la barra superior directamente al page

    page.add(
        ft.Row(
            controls=[
                menu_lateral,  # Menú lateral
                contenido,  # Contenido principal
            ],
            expand=True,
        )
    )

    # Iniciar en la pantalla 1
    contenido.content = pantalla_uno()
    page.update()

ft.app(target=main)