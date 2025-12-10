import networkx as nx
from scipy.cluster.hierarchy import weighted
from scipy.sparse.csgraph import shortest_path

from database.dao import DAO

class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        # TODO
        self.G = nx.Graph()

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        # TODO
        self._edges = DAO.read_connessioni(year)
        self._nodes = DAO.read_rifugi(year)

        self.G.clear()
        self._mappa_rifugi = {rifugio.id: rifugio for rifugio in self._nodes}

        for connessione in self._edges:
            r1 = connessione.id_rifugio1
            r2 = connessione.id_rifugio2
            weight = connessione.difficolta * connessione.distanza
            print(r1, r2, weight)
            if r1 in self._mappa_rifugi and r2 in self._mappa_rifugi :
                self.G.add_node(r1, obj=self._mappa_rifugi[r1])
                self.G.add_node(r2, obj=self._mappa_rifugi[r2])
                self.G.add_weighted_edges_from(r1, r2,wheight=weight)
        print(self.G)

    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        # TODO
        weigth_min=0
        weight_max=0
        for node in self.G.nodes():

            for neighbor in self.G.neighbors(node):
                weighted_path = nx.shortest_path(self.G, source=node, target=neighbor, weight='weight')

    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        # TODO

    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
