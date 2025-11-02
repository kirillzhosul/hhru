# HeadHunter Python Library

Python Library for interacting with [HeadHunter](https://hh.ru/) jobs searching website


## Features
- Fully typed and uses DTOs
- Search vacancies from HeadHunter

## Planned features
These features are only planned and will be implemented only if there is some Issues inside [GitHub repository](https://github.com/kirillzhosul/hhru)

- Async support
- Web Backend Provider
- Authentication
- Search parameters value / types
- More methods (requires authentication mostly)

## Example usage
```python
from hhru import Client
from hhru import VacancyDTO

# By default use API + Anonymous auth (backend parameter is skipped)
client = Client()

# To search vacancies you use `search_vacancies` or `search_vacancies_over_pages` 
# (helper generator for iterating over paginated response)
# (`search_vacancies` retrieves only single page of vacancies)
vacancies: list[VacancyDTO] = client.search_vacancies()
vacancies: list[VacancyDTO] = list(client.search_vacancies_over_pages()) # Slow, as obtains all vacancies from search query

# Inside `VacancyDTO` you may see all possible fields that any vacancy on HH has
salary_to = vacancies[0].salary.to
```

## Search query
Searching by any parameter is done by passing search query as `**kwargs` into search method like:
```
client.search_vacancies(text="...") # Search by text in vacancy

# Or for some cases, via filtering
# (filter / generator)
for vacancy in client.search_vacancies():
    if "..." not in vacancy.text:
        continue
    pass
```

You may find these parameters on [HH docs](https://api.hh.ru/openapi/redoc), currently it is not documented inside library


## Searching over pages

As said in example usage `search_vacancies` returns only single page (you must paginate via passing `page` parameter)
for searching *over* pages you may used `search_vacancies_over_pages`
```python
# Loads pages until generator is not closed (break)
for vacancy in client.search_vacancies_over_pages():
    if vacancy.text == "...":
        break
```


## Async support

Async support is available only for HTTP API provider, and not documented/tested as being in process of development, you may view example in `examples/async_mean_salary.py`

Async requires providing custom Async client:
```python
client = AsyncClient(
    backend=BackendAsyncApiProvider(
        auth_provider=AnonymousAuthProvider(),
        concurrent_max_requests=5,
    )
)
# concurrent_max_requests is an semaphore for not flooding API (also big number throws an unknown error)
```

```python
# For Async call use `search_vacancies_async_burst`
vacancies: list[VacancyDTO]: await search_vacancies_async_burst()
# Q: Why it is named burst?
# A: it performs all API calls in *burst*, by gathering futures and performing them at once, only capped by `concurrent_max_requests` semaphore inside
```

## Helping constants
You may import and use `hhru.consts` for useful constants like:
```
from hhru.consts import VACANCY_SEARCH_ORDER_DISTANCE
client.search_vacancies(order_by=VACANCY_SEARCH_ORDER_DISTANCE)
```

## Installation

You can install library from PyPi via running command below (You may use your preferred package manager)
```shell
pip install hhru
```
