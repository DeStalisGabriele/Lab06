from database.DB_connect import DBConnect
from database.anno import Anno
from database.brand import Brand
from database.retailer import Retailer
from database.topVendite import Vendita
from database.staVendite import StatVendite

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnno():
        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute(
            "SELECT DISTINCT YEAR(Date) as anno FROM go_daily_sales order by anno")  # scrivo l'azione (provare prima a faro direttamente su dbeaver)

        anni = []
        for row in cursor:
            anni.append(Anno(row["anno"]))  # non serve creare una classe Anno

        cursor.close()
        cnx.close()
        return anni

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute(
            "SELECT DISTINCT Product_brand as brand FROM go_products order by brand")  # scrivo l'azione (provare prima a faro direttamente su dbeaver)

        brands = []
        for row in cursor:
            brands.append(Brand(row["brand"]))  # non serve creare una classe Anno

        cursor.close()
        cnx.close()
        return brands

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute(
            "SELECT DISTINCT Retailer_name as RetName FROM go_retailers order by RetName")  # scrivo l'azione (provare prima a faro direttamente su dbeaver)

        retailers = []
        for row in cursor:
            retailers.append(Retailer(row["RetName"])) # non serve creare una classe Anno

        cursor.close()
        cnx.close()
        return retailers

    @staticmethod
    def getTopVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""
                       SELECT 
                            YEAR(s.Date) as anno, 
                            p.Product_brand, 
                            r.Retailer_name, 
                            (s.Unit_sale_price * s.Quantity) as ricavo
                        FROM go_daily_sales s
                        JOIN go_products p ON s.Product_number = p.Product_number
                        JOIN go_retailers r ON s.Retailer_code = r.Retailer_code
                        WHERE YEAR(s.Date) = %s 
                          AND p.Product_brand = %s 
                          AND r.Retailer_name = %s
                        ORDER BY ricavo DESC
                       """, (anno, brand, retailer))

        risultati = []
        for row in cursor:
            v = Vendita(row["anno"], row["Product_brand"], row["Retailer_name"], row["ricavo"])
            risultati.append(v)

        cursor.close()
        cnx.close()
        return risultati

    @staticmethod
    def getAnalizzaVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""
                   SELECT SUM(s.Unit_sale_price * s.Quantity) as GiroAffari,
                          SUM(s.Quantity)                     as NumVendite,
                          COUNT(DISTINCT s.Retailer_code)     as RetCoinvolti,
                          COUNT(DISTINCT s.Product_number)    as ProdCoinvolti
                   FROM go_daily_sales s
                            JOIN go_products p ON s.Product_number = p.Product_number
                            JOIN go_retailers r ON s.Retailer_code = r.Retailer_code
                   WHERE YEAR (s.Date) = %s
                     AND p.Product_brand = %s
                     AND r.Retailer_name = %s
                   """, (anno, brand, retailer))


        risultati = []
        for row in cursor:
            v = StatVendite(row["GiroAffari"], row["NumVendite"], row["RetCoinvolti"], row["ProdCoinvolti"])
            risultati.append(v)

        cursor.close()
        cnx.close()
        return risultati

    @staticmethod
    def getAnalizzaVenditeGlobali():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("""
                       SELECT SUM(s.Unit_sale_price * s.Quantity) as GiroAffari,
                              SUM(s.Quantity)                     as NumVendite,
                              COUNT(DISTINCT s.Retailer_code)     as RetCoinvolti,
                              COUNT(DISTINCT s.Product_number)    as ProdCoinvolti
                       FROM go_daily_sales s
                       """)  # Query pulita senza JOIN inutili e senza parametri

        row = cursor.fetchone()
        risultati = []
        if row and row["GiroAffari"] is not None:
            v = StatVendite(row["GiroAffari"], row["NumVendite"], row["RetCoinvolti"], row["ProdCoinvolti"])
            risultati.append(v)

        cursor.close()
        cnx.close()
        return risultati