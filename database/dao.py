from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.rifugio import Rifugio

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    pass

    @staticmethod
    def read_rifugi(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """ SELECT r.*
                    FROM rifugio r,connessione c
                    WHERE (c.id_rifugio1 = r.id OR c.id_rifugio2 = r.id) AND c.anno <= %s"""

        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query, (anno,))
            for row in cursor:
                rifugio = Rifugio(row["id"],
                                  row["nome"],
                                  row["localita"], )
                result.append(rifugio)
        except Exception as e:
            print(f"Errore durante la query read_rifugi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def read_connessioni(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """ SELECT *
                    FROM connessione
                    WHERE anno <= %s"""
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query, (anno,))
            for row in cursor:
                if row["difficolta"] == 'facile':
                    row["difficolta"] = 1
                elif row["difficolta"] == 'media':
                    row["difficolta"] = 1.5
                elif row["difficolta"] == 'difficile':
                    row["difficolta"] = 2

                connessione = Connessione(row["id_rifugio1"],
                                          row["id_rifugio2"],
                                          row["difficolta"],
                                          row["distanza"],
                                          row["anno"],)
                result.append(connessione)
        except Exception as e:
            print(f"Errore durante la query read_connessioni: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result
