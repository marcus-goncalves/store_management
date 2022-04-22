from fastapi import HTTPException, status

from models.provider import Provider, PaginatedProviders
import repositories.provider as repo

providers = []


def insert_provider(provider: Provider) -> None:
    try:
        repo.insert(provider.dict())

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"invalid data - {err}")


def get_all_providers(page_size: int = 10, page: int = 1) -> PaginatedProviders:
    start: int = (page - 1) * page_size
    end: int = start + page_size

    providers = repo.read_all()

    pages = round(len(providers) / page_size, 0)
    output = {
        "data": providers[start:end],
        "page_size": page_size,
        "page": page,
        "pages": pages
    }

    res = PaginatedProviders(**output)
    return res


def update_provider(id: str, new_provider: Provider) -> Provider:
    data = repo.update(id, new_provider.dict())
    res = Provider(**data)

    return res


def delete_provider(id: str) -> None:
    repo.delete(id)
