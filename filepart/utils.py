
class exceptions:
    class FilePartBaseException(Exception):
        pass

    class UnitError(FilePartBaseException):
        pass

    class ValueError(FilePartBaseException):
        pass

    class SizeError(FilePartBaseException):
        pass

    class InvalidValue(FilePartBaseException):
        pass

def test(unit, units, s = True):
    for un in units:
        if s:
            if unit.endswith(un) or unit.endswith(un + "s") or unit.startswith(un) or unit.startswith(un + "s"):
                return True
        else:
            if unit.endswith(un) or unit.startswith(un):
                return True

    return False

def format_size(unit, valueb, value):
    if value % 1 == 0:
        value = int(value)

    if unit != "byte" and unit != "part":
        if value > 1:
            r =  unit + "s (" + str(valueb) + " " + "bytes)"
        else:
            r =  unit + " (" + str(valueb) + " " + "bytes)"
    else:
        if value > 1:
            r =  unit + "s"
        else:
            r =  unit

    return str(value) + " " + r

def parse_size(size):
    size = str(size).lower().strip()
    size = size.replace(" ", "")
    allowed_chars = "0123456789prgiameklobytes.-"
    parsed_size = ""

    for char in size:
        if char in allowed_chars:
            parsed_size += char

    size_int = "".join([s for s in parsed_size if s.isdigit() or test(s, [".", "-"], False)])
    if size_int == "":
        raise exceptions.ValueError("Please give a value.")
        
    size_int = float(size_int)
    size_unit = "".join([s for s in parsed_size if not s.isdigit()])

    if size_int < 1:
        raise exceptions.SizeError("Please give a bigger value.")

    if test(size_unit, ["part", "pt"]) or size_unit == "":
        size_in_bytes = 0
        size_unit = "part"
    elif test(size_unit, ["kilobyte", "kb"]):
        size_in_bytes = int(size_int * 1024**1)
        size_unit = "kilobyte"
    elif test(size_unit, ['megabyte', 'meg', 'mb']):
        size_in_bytes = int(size_int * 1024**2)
        size_unit = "megabyte"
    elif test(size_unit, ['gigabyte', 'gig', 'gb']):
        size_in_bytes = int(size_int * 1024**3)
        size_unit = "gigabyte"
    elif test(size_unit, ["byte", "b"]):
        size_in_bytes = int(size_int * 1024**0)
        size_unit = "byte"
    else:
        raise exceptions.UnitError("Please give a valid unit.")

    if size_unit == "part" and not size_int % 1 == 0:
        raise exceptions.InvalidValue("Invalid value " + str(size_int))

    formatted = format_size(size_unit, size_in_bytes, size_int)

    return {"size_in_bytes": int(size_in_bytes), "size": float(size_int), "formatted": str(formatted), "unit": str(size_unit)}
