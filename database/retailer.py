# database/Retailer.py
class Retailer:
    def __init__(self, retailer_name):
        self.retailer_name = retailer_name

    def __str__(self):
        return self.retailer_name