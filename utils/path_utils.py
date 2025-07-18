def json_path_to_xpath(json_path: str) -> str:
    """Convert JSON path format to XPath"""
    import re
    # Example: ["user"]["name"] -> /user/name
    return re.sub(r'\["([^"]+)"\]', r'/\1', json_path)

def extract_keys_from_path(path: str) -> list:
    """Extract keys from path string"""
    import re
    return re.findall(r'\["([^"]+)"\]|\[(\d+)\]', path)