from typing import Any, Dict, List, Union
from pathlib import Path
import json

class TreeAnalyzer:
    def __init__(self, data: Union[Dict, List]):
        self.data = data
        self._node_paths = []
        
    def traverse(self, callback: callable):
        """Core traversal engine with path tracking"""
        self._traverse_node(self.data, [], callback)
    
    def _traverse_node(self, node, current_path: List[str], callback: callable):
        """Recursive node traversal"""
        callback(node, current_path)
        
        if isinstance(node, dict):
            for key, value in node.items():
                self._traverse_node(value, current_path + [f'["{key}"]'], callback)
        elif isinstance(node, (list, tuple)):
            for idx, item in enumerate(node):
                self._traverse_node(item, current_path + [f'[{idx}]'], callback)
    
    def find_nodes_by_key(self, search_key: str) -> List[Dict]:
        """Find all nodes containing specific key"""
        results = []
        
        def callback(node, path):
            if isinstance(node, dict) and search_key in node:
                results.append({
                    "path": ''.join(path),
                    "value": node[search_key]
                })
        
        self.traverse(callback)
        return results