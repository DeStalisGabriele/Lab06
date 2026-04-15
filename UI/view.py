import flet as ft
from flet_core.colors import BROWN_200


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._txtTitle = None #title
        self._ddAnno = None #1
        self._ddBrand = None #1
        self._ddRetailer = None #1
        self._btnTopVendite = None #2
        self._btnAnalizzaVendite = None #2

    def load_interface(self):
        # title
        self._txtTitle = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._txtTitle)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)


        #row1
        self._ddAnno = ft.Dropdown(
            label="anno",
            value="Nessun filtro",
            options=[ft.dropdown.Option(str(anno)) for anno in self._controller.getAnno()]
        )

        self._ddBrand = ft.Dropdown(
            label="brand",
            value="Nessun filtro",
            options=[ft.dropdown.Option(str(brand)) for brand in self._controller.getBrand()]
        )

        self._ddRetailer = ft.Dropdown(
            label="retailer",
            value="Nessun filtro",
            options= [ft.dropdown.Option(str(retailer)) for retailer in self._controller.getRetailer()],
            expand=True
        )

        #row2
        self._btnTopVendite=ft.ElevatedButton(text="Top Vendite",
                                              on_click=self._controller.getTopVendite)

        self._btnAnalizzaVendite=ft.ElevatedButton(text="Analizza Vendite",
                                                   on_click=self._controller.getAnalizzaVendite)


        #creo le righe e la aggiungo alla pagina
        row1 = ft.Row([self._ddAnno, self._ddBrand, self._ddRetailer])
        row2 = ft.Row([self._btnTopVendite, self._btnAnalizzaVendite])
        self._page.controls.extend([row1, row2])



        # List View where the reply is printed
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def display_results(self, risultati):
        self.txt_result.controls.clear()

        if not risultati:
            self.txt_result.controls.append(ft.Text("Nessun risultato trovato.", color="red"))
        else:
            for vendita in risultati:
                self.txt_result.controls.append(
                    ft.Text(str(vendita), size=14)
                )

        self._page.update()