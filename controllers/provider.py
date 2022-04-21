from fastapi import HTTPException, status


from models.provider import Provider, PaginatedProviders

providers = []


def insert_provider(provider: Provider) -> dict:
    try:
        provider.id = len(providers) + 1
        providers.append(provider)

        print(providers)
        return provider
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"invalid data - {err}")


def get_all_providers(page_size: int, page: int) -> PaginatedProviders:
    ...
