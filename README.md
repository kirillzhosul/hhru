# hhru

[HH.ru](https://hh.ru/) wrapper library for Python.

There is providers for API and Web (Currently, not implemented) \
For authentication, there is `Anonymous` mode, along with other authentications (currently, also not implemented)

### Features

- Anonymous vacancies searches via API

(There is currently boilerplates / not finished features for using authentication / web provider)

### How to install

```
pip install hhru
```

### Example usage

```python
import hhru

# Default client, with `Anonymous` auth and `API` provider
client = hhru.Client()
```

```python

# List first page of Python remote vacancies, sorted by new. 
# You can use strings as params or look into `consts` module
vacancies = client.search_vacancies_over_pages(
  text="Python",
  search_field="name",
  order_by="publication_time",
  schedule="remote",
)
```


### Using web provider or custom authentication

```python

# Client with web provider and given authentication data
# TODO: Currently, that will behave like API provider (no implementations for web)
client = hhru.Client(
  backend=hhru.BackendWebProvider(
    auth=DirectAuthProvider(
      login="login", 
      password="password"
    )
  )
)
```


### References

- API repo: https://github.com/hhru/api
- API docs: https://api.hh.ru/openapi/redoc
