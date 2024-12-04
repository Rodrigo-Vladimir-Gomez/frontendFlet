import flet as ft

def pantalla_seis():
    # Crear una tabla de ejemplo
    table = ft.DataTable(
        width="100%",  # Asegura que la tabla ocupe todo el ancho disponible
        columns=[
            ft.DataColumn(ft.Text("ID", color="black")),
            ft.DataColumn(ft.Text("Nombre", color="black")),
            ft.DataColumn(ft.Text("Estado", color="black")),
        ],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text(" ")), ft.DataCell(ft.Text(" ")), ft.DataCell(ft.Text(" "))]),
            ft.DataRow(cells=[ft.DataCell(ft.Text(" ")), ft.DataCell(ft.Text(" ")), ft.DataCell(ft.Text(" "))]),
            ft.DataRow(cells=[ft.DataCell(ft.Text(" ")), ft.DataCell(ft.Text(" ")), ft.DataCell(ft.Text(" "))]),
        ],
    )

    # Botón para mostrar logs
    show_logs_button = ft.ElevatedButton(
        text="Mostrar Logs",
        bgcolor="blue",
        color="white",
        on_click=lambda e: print("Mostrando logs..."),
    )

    # Retornar la pantalla con la tabla y el botón
    return ft.Column(
        controls=[
            #ft.Text("Pantalla 6", size=30, weight=ft.FontWeight.BOLD),
            table,
            show_logs_button,
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )