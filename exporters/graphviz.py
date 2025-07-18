from graphviz import Digraph
import tempfile
import os

def build_graphviz(tree, parent_id='root', graph=None, counter=[0]):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='record')

    for key, value in tree.items():
        node_id = f"node{counter[0]}"
        counter[0] += 1
        label = f"{key}" if not isinstance(value, (dict, list)) else f"{key} : {type(value).__name__}"
        graph.node(node_id, label)

        graph.edge(parent_id, node_id)

        if isinstance(value, dict):
            build_graphviz(value, parent_id=node_id, graph=graph, counter=counter)
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                build_graphviz({f"[{idx}]": item}, parent_id=node_id, graph=graph, counter=counter)

    return graph

def export_graph(tree, output_path, format='png'):
    dot = build_graphviz(tree)
    with tempfile.TemporaryDirectory() as tmpdirname:
        filepath = os.path.join(tmpdirname, "graph")
        dot.render(filepath, format=format, cleanup=True)
        final_path = f"{filepath}.{format}"
        os.replace(final_path, output_path)
