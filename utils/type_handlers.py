def is_primitive(val):
    return isinstance(val, (str, int, float, bool, type(None)))

def to_display_string(val):
    if isinstance(val, str):
        return f'"{val}"'
    elif isinstance(val, (int, float, bool, type(None))):
        return str(val)
    elif isinstance(val, dict):
        return "{...}"
    elif isinstance(val, list):
        return "[...]"
    elif isinstance(val, tuple):
        return "(...)"
    elif isinstance(val, set):
        return "{...}"
    return str(val)

def get_type(val):
    return type(val).__name__
