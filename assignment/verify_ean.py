def is_valid_ean(eans: list, item: str) -> bool:
    if item in eans:
        return True
    return False
