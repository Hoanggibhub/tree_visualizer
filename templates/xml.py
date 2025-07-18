import xmltodict
from typing import Union

class XMLHandler:
    @staticmethod
    def parse(xml_string: str) -> dict:
        """Convert XML to dictionary"""
        return xmltodict.parse(xml_string)
    
    @staticmethod
    def to_xml(data: dict) -> str:
        """Convert dictionary to XML"""
        return xmltodict.unparse(data, pretty=True)