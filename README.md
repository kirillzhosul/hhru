# hh.ru
HH.ru API library for Python.


### Example usage.

```python
import hhru
# List first page of Python remote vacancies, sorted by new. (See API docs)
vacancies = hhru.Client().api.method(
  "vacancies",
  text="Python",
  search_field="name",
  order_by="publication_time", 
  schedule="remote",
)

```

### API documentation.
- https://github.com/hhru/api
- https://api.hh.ru/openapi/redoc
