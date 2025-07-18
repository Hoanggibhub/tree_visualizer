from graphviz import Digraph
import tempfile
import os
from typing import Dict, Union, List, Optional, Literal

class GraphvizExporter:
    def __init__(self):
        self._highlight_path = None
        self._style_config = {
            'node_shape': 'box',
            'node_fillcolor': 'lightgrey',
            'highlight_color': 'yellow',
            'fontname': 'Arial',
            'rankdir': 'TB'  # TB (top-bottom) hoặc LR (left-right)
        }

    def set_style(self, **kwargs):
        """Customize graph appearance"""
        valid_rankdir = {'TB', 'LR', 'BT', 'RL'}
        if 'rankdir' in kwargs and kwargs['rankdir'] not in valid_rankdir:
            raise ValueError(f"rankdir must be one of {valid_rankdir}")
        self._style_config.update(kwargs)

    def build_graph(
        self,
        tree: Union[Dict, List],
        parent_id: str = 'root',
        graph: Optional[Digraph] = None,
        counter: List[int] = [0],
        current_path: str = ''
    ) -> Digraph:
        if graph is None:
            graph = Digraph()
            graph.attr('graph', rankdir=self._style_config['rankdir'])
            graph.attr('node', 
                      shape=self._style_config['node_shape'],
                      style='filled',
                      fillcolor=self._style_config['node_fillcolor'],
                      fontname=self._style_config['fontname'])
            graph.node('root', 'ROOT')

        for key, value in tree.items():
            node_id = f"node{counter[0]}"
            counter[0] += 1
            path = f"{current_path}/{key}" if current_path else key
            
            # Highlight logic
            is_highlighted = self._highlight_path and path in self._highlight_path
            node_attrs = {
                'label': str(key),
                'fillcolor': self._style_config['highlight_color'] if is_highlighted 
                           else self._style_config['node_fillcolor']
            }
            
            graph.node(node_id, **node_attrs)
            graph.edge(parent_id, node_id)

            if isinstance(value, dict):
                self.build_graph(value, node_id, graph, counter, path)
            elif isinstance(value, list):
                for idx, item in enumerate(value):
                    self.build_graph(
                        {f"[{idx}]": item}, 
                        node_id, 
                        graph, 
                        counter,
                        f"{path}[{idx}]"
                    )

        return graph

    def export(
        self,
        tree: Union[Dict, List],
        output_path: str,
        format: Literal['png', 'pdf', 'svg'] = 'png',  # Thêm PDF/SVG
        highlight_path: Optional[List[str]] = None
    ) -> str:
        """Export tree to image file with optional path highlighting"""
        if format not in ['png', 'pdf', 'svg']:
            raise ValueError("Format must be png, pdf or svg")
        
        with tempfile.TemporaryDirectory() as tmpdir:
            dot = self.build_graph(tree)
            temp_file = os.path.join(tmpdir, "tree")
            
            # Render with specified format
            dot.render(temp_file, format=format, cleanup=True)
            output_file = f"{output_path}.{format}"
            os.replace(f"{temp_file}.{format}", output_file)
            
        return output_file