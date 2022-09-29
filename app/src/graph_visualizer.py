from pyvis.network import Network

from app.classes.graph_node import GraphNode

class GraphVisualizer:
    def __init__(self):
        self.__nickname_dict = {
            'PAtom': 'Ptm',
            'PredicateFunction': 'PrF',
            'SymEvent': 'Sev',
            'PointExpression': 'Px'
        }

        self.__color_dict = {
            'prop': 'red',
            'subclass': 'blue',
            'ROOT': 'black'
        }


    def _get_nickname(self, name: str) -> str:
        if name in self.__nickname_dict:
            nickname = self.__nickname_dict[name]
        else:
            nickname = ''.join([s for s in name if s.isupper()])
        
        return nickname


    def _get_color(self, x: GraphNode) -> str:
        if len(x.subclasses) == 0 and len(x.props) == 0:
            color = 'green'
        else:
            if x.node_type in self.__color_dict:
                color = self.__color_dict[x.node_type]
            else:
                color = 'grey'
        
        return color

    # Run g.show('nx.html') to create the file afterwards. It can be viewed in a browser
    def create_viz(self, node_list: list[GraphNode]) -> Network:
        G = Network(directed=True)

        # Build the nodes
        for x in node_list:
            nickname = self._get_nickname(x.name)
            color = self._get_color(x)

            G.add_node(nickname, color=color)
            

        # Add the edges
        for x in node_list:
            nickname = self._get_nickname(x.name)
            
            for y in x.subclasses:
                yn = self._get_nickname(y)
                G.add_edge(nickname, yn)
            
            for y in x.props:
                yn = self._get_nickname(y)
                G.add_edge(nickname, yn)
        
        return G