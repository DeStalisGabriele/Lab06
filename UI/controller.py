import flet as ft
from  database.DAO import  *

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def getAnno(self):
        return DAO.getAnno()

    def getBrand(self):
        return DAO.getBrand()

    def getRetailer(self):
        return DAO.getRetailer()

    def getTopVendite(self, e):
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._view._ddRetailer.value
        topVendite = DAO.getTopVendite(anno, brand, retailer)
        topVendite = topVendite[:5]
        self._view.display_results(topVendite)
        self._view.update_page()

    def getAnalizzaVendite(self, e):
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._view._ddRetailer.value
        if anno =="Nessun filtro" and brand =="Nessun filtro" and retailer =="Nessun filtro":  statVendite = DAO.getAnalizzaVenditeGlobali ()
        else: statVendite = DAO.getAnalizzaVendite (anno, brand, retailer)
        self._view.display_results(statVendite)
        self._view.update_page()

