import imageio
from PIL import Image
import glob
from typing import Dict, List, Union, Literal

class AnimatedGraphvizExporter(GraphvizExporter):
    def __init__(self):
        super().__init__()
        self._animation_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFBE0B']
        self._group_by: Literal['depth', 'path'] = 'depth'

    def set_animation_style(self, colors: List[str], group_by: Literal['depth', 'path'] = 'depth'):
        self._animation_colors = colors
        self._group_by = group_by

    def export_animation(
        self,
        tree: Union[Dict, List],
        output_path: str,
        duration: float = 0.5,
        build_order: List[str] = None
    ) -> str:
        """Create animated GIF showing tree construction"""
        temp_dir = tempfile.mkdtemp()
        frames = []
        
        if not build_order:
            build_order = self._get_default_build_order(tree)
        
        # Color mapping logic
        color_map = {}
        if self._group_by == 'depth':
            for path in build_order:
                depth = len(path.split('/')) - 1
                color_map[path] = self._animation_colors[depth % len(self._animation_colors)]
        else:  # group_by path
            from hashlib import md5
            for path in build_order:
                hash_int = int(md5(path.encode()).hexdigest(), 16)
                color_map[path] = self._animation_colors[hash_int % len(self._animation_colors)]
        
        # Generate frames
        for i, path in enumerate(build_order):
            self._highlight_path = build_order[:i+1]
            self.set_style(highlight_color=color_map[path])
            dot = self.build_graph(tree)
            dot.render(os.path.join(temp_dir, f"frame_{i}"), format='png', cleanup=True)
            
            img = Image.open(f"{temp_dir}/frame_{i}.png")
            frames.append(img)
        
        # Save animation
        output_file = f"{output_path}.gif"
        frames[0].save(
            output_file,
            save_all=True,
            append_images=frames[1:],
            duration=int(duration*1000),
            loop=0
        )
        
        return output_file

    def _get_default_build_order(self, tree: Union[Dict, List]) -> List[str]:
        """Generate depth-first build order"""
        order = []
        
        def traverse(node, path):
            order.append(path)
            if isinstance(node, dict):
                for k, v in node.items():
                    traverse(v, f"{path}/{k}" if path else k)
            elif isinstance(node, list):
                for i, item in enumerate(node):
                    traverse(item, f"{path}[{i}]")
        
        traverse(tree, "")
        return order