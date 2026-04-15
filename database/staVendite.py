class StatVendite:
    def __init__(self, giroAffari, numeroVendite, retCoinvolti, prodCoinvolti):
        self.giroAffari = giroAffari
        self.numeroVendite = numeroVendite
        self.retCoinvolti = retCoinvolti
        self.prodCoinvolti = prodCoinvolti

    def __str__(self):
        return (f"Statistiche vendite: \n "
                f"Giro affari :{self.giroAffari} \n "
                f"Numero vendite: {self.numeroVendite}\n"
                f"Numero retailers coinvolti: {self.retCoinvolti}\n"
                f"Numero prodotti coinvolti: {self.prodCoinvolti}")