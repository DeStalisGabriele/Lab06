# database/Vendita.py
class Vendita:
    def __init__(self, anno, product_name, retailer_name, ricavo):
        self.anno = anno
        self.product_name = product_name
        self.retailer_name = retailer_name
        self.ricavo = ricavo

    def __str__(self):
        return f"{self.anno} - {self.product_name} - {self.retailer_name}: €{self.ricavo:.2f}"