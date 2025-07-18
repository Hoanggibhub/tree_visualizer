# File __init__.py
from .core import TreeAnalyzer
from .exporters.html import HTMLExporter
from .exporters.graphviz import GraphvizExporter
from .exporters.xml import XMLHandler

class TreeVisualizer(TreeAnalyzer):
    def __init__(self, data):
        super().__init__(data)
        self.html_exporter = HTMLExporter()
        self.graphviz_exporter = GraphvizExporter()
    
    def to_html(self, output_file, **kwargs):
        """Export to interactive HTML"""
        self.html_exporter.export(self.data, output_file, **kwargs)
    
    def to_graphviz(self, output_file, **kwargs):
        """Export to graphviz image"""
        return self.graphviz_exporter.export(self.data, output_file, **kwargs)
    
    @classmethod
    def from_xml(cls, xml_string):
        """Create from XML data"""
        xml_data = XMLHandler.parse(xml_string)
        return cls(xml_data)