def paginate(page_size: int, data: list, res: dict) -> dict:
    start = 0
    pages = int(len(data) / page_size)
