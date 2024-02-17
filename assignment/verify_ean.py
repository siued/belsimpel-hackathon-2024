def ean_verified(ean: str, eans: list) -> bool:
    if ean in eans:
        return True
    return False
