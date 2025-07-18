from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import webbrowser
from typing import Dict, List
import json

class HTMLExporter:
    def __init__(self, template_dir: str = "templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template("base.html")
    
    def export(self, data: Dict, output_path: str, dark_mode: bool = True):
        # Collect all paths for suggestions
        paths = self._collect_paths(data)
        
        rendered = self.template.render(
            tree_data=json.dumps(data),
            paths=paths,
            dark_mode=dark_mode
        )
        
        with open(output_path, 'w') as f:
            f.write(rendered)
        
        webbrowser.open(output_path)
    
    def _collect_paths(self, data: Dict) -> List[str]:
        """Collect all JSON paths for suggestions"""
        paths = []
        
        def callback(node, current_path):
            if isinstance(node, (dict, list, tuple)):
                paths.append(''.join(current_path))
        
        analyzer = TreeAnalyzer(data)
        analyzer.traverse(callback)
        return sorted(paths, key=len)