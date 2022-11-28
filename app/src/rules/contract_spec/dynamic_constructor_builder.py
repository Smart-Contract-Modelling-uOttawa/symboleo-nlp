from app.classes.spec.symboleo_spec import PAtom
from app.src.graph.graph_builder import GraphBuilder
from app.src.dynamic_constructor import DynamicObjectConstructor

# May want to store this for easy access...
class DynamicConstructorBuilder:
    @staticmethod
    def build():
        graph_builder = GraphBuilder()
        #graph_visualizer = GraphVisualizer()

        digraph = graph_builder.build(PAtom)

        #gv = graph_visualizer.create_viz(digraph.nodes)
        #gv.show('nx.html')

        dynamic_constructor = DynamicObjectConstructor(digraph)
        return dynamic_constructor