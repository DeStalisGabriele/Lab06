# database/Brand.py
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

    def __str__(self):
        return self.brand_name