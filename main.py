import functools
import hhru

api = hhru.Api()


MAX_PER_PAGE = 100


def get_vacancies(language: str, max_page: int = 21):
    print(f"Fetching jobs from hh.ru for `{language}` language...")
    page = 0
    total = 0
    while True:
        response = api.method(
            "vacancies",
            text=language.lower(),
            per_page=MAX_PER_PAGE,
            page=page,
            search_field="name",
            order_by="publication_time",
            schedule="remote",
        )
        if response.raw_response().status_code != 200:
            print(response.raw_json())
            raise Exception
        if page == 0:
            print(f"Server said that there is {response.found} vacancies. Fetching...")
        print(f"\tFetched page {response.page + 1}/{response.pages} [{max_page}]...")
        total += len(response.items)
        for item in response.items:
            yield item
        page += 1
        if page >= response.pages or page >= max_page:
            break
    print(f"Finished fetching jobs! Totally fetched {total} vacancies!")


def filter_vacancy(vacancy):
    return vacancy


def print_vacancy(vacancy):
    print(">>>", vacancy["name"])
    # has_test, response_letter_required'
    # print(vacancy)


vacancies = list(
    filter(
        functools.partial(filter_vacancy),
        get_vacancies(language="Python Django"),
    )
)

[print_vacancy(vac) for vac in vacancies[0:50]]
