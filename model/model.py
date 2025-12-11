import networkx as nx
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
        self.connessioni = DAO.read_connessioni(year)
        self.rifugi = DAO.read_rifugi(year)

        self.G.clear()
        self.G.add_nodes_from(self.rifugi)
        self.mappa_rifugi = {r.id: r for r in self.rifugi}

        for c in self.connessioni:
            weight = float(c.distanza) * float(c.difficolta)
            r1 = self.mappa_rifugi[c.id_rifugio1]
            r2 = self.mappa_rifugi[c.id_rifugio2]
            self.G.add_edge(r1, r2, weight=weight)


    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        # TODO
        return (min(d['weight'] for u, v, d in self.G.edges(data=True)),
                max(d['weight'] for u, v, d in self.G.edges(data=True)))

    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        # TODO
        minori = 0
        maggiori = 0
        for u, v, d in self.G.edges(data=True):
            peso = d['weight']
            if peso > soglia:
                maggiori += 1
            elif peso < soglia:
                minori += 1
        return minori, maggiori

    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
    def trova_cammino_minimo(self, soglia):
        """
        Trova il cammino più breve (somma dei pesi minima) con:
        - archi > soglia
        - almeno 2 archi (3 nodi)

        Restituisce il cammino minimo come lista di nodi oppure [] se non esiste.
        """

        edges_filtrati = [(u, v, d) for u, v, d in self.G.edges(data=True) if d['weight'] > soglia]
        G_filtrato = nx.Graph()
        G_filtrato.add_nodes_from(self.G.nodes())
        G_filtrato.add_edges_from(edges_filtrati)

        min_path = None
        min_distanza = 0
        nodes = list(G_filtrato.nodes())

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                u = nodes[i]
                v = nodes[j]
                try:
                    distanza = nx.shortest_path_length(G_filtrato, u, v, weight='weight')
                    path = nx.shortest_path(G_filtrato, u, v, weight='weight')

                    if len(path) >= 3 and (distanza < min_distanza or min_distanza==0):
                        min_path = path
                        min_distanza = distanza

                except nx.NetworkXNoPath:
                    continue

        return min_path if min_path is not None else []




