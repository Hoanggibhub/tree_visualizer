from jinja2 import Template
from typing import Dict, List

class WebGraphvizExporter:
    WEB_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@hpcc-js/wasm@1.12.5/dist/graphviz.umd.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/d3-graphviz@3.1.0/build/d3-graphviz.min.js"></script>
    <style>
        #graph { width: 100%; height: 100vh; }
        .node.highlight-1 { stroke: #FF6B6B; stroke-width: 3px; }
        .node.highlight-2 { stroke: #4ECDC4; stroke-width: 3px; }
        .node.highlight-3 { stroke: #45B7D1; stroke-width: 3px; }
        #search-box {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 100;
        }
    </style>
</head>
<body>
    <div id="search-box">
        <input type="text" id="path-input" placeholder="Enter path (e.g. user/profile)">
        <button id="highlight-btn">Highlight Path</button>
        <select id="color-select">
            <option value="1">Red</option>
            <option value="2">Teal</option>
            <option value="3">Blue</option>
        </select>
    </div>
    <div id="graph"></div>
    <script>
        const colorClasses = {
            '1': 'highlight-1',
            '2': 'highlight-2',
            '3': 'highlight-3'
        };
        
        const graphviz = d3.select("#graph").graphviz()
            .fit(true)
            .zoomScaleExtent([0.1, 8]);
        
        // Load DOT graph
        const dot = `{{ dot_content }}`;
        graphviz.renderDot(dot);
        
        // Path highlighting
        document.getElementById('highlight-btn').addEventListener('click', () => {
            const path = document.getElementById('path-input').value;
            const color = document.getElementById('color-select').value;
            
            // Remove previous highlights
            d3.selectAll('.node').classed(colorClasses[color], false);
            
            // Find and highlight nodes
            const pathParts = path.split('/');
            let selector = '.node';
            pathParts.forEach(part => {
                selector += ` > title:contains('${part}')`;
            });
            
            d3.selectAll(selector).each(function() {
                d3.select(this.parentNode).classed(colorClasses[color], true);
            });
        });
        
        // Mini-map with pan/zoom
        // ... (giữ nguyên phần mini-map trước) ...
    </script>
</body>
</html>
    """

    def export_web(
        self,
        tree: Dict,
        output_path: str,
        highlight_paths: Dict[str, str] = None
    ):
        """Generate interactive web visualization with multi-color highlights"""
        dot_content = self._tree_to_dot(tree)
        template_vars = {
            'dot_content': dot_content,
            'highlight_paths': highlight_paths or {}
        }
        
        with open(output_path, 'w') as f:
            f.write(Template(self.WEB_TEMPLATE).render(**template_vars))