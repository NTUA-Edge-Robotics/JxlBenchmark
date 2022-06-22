def extract_convert_quality(method:str) -> int:
    """Extracts the distance from the method field and convert it to a quality factor

    Supports the following quality factors : 100, 90, 80, 70, 60, 50, 40

    Args:
        method (str): The method following that template : codec:effort:distance (e.g. jxl:falcon:d1)

    Returns:
        int: The quality factor
    """
    mapping = {"0": 100, "1":90, "1.9":80, "2.8":70, "3.7": 60, "4.6":50, "5.5":40}

    distance = method.split(":")[2][1:]

    return mapping[distance]