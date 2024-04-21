import functools
from typing import Any

import hhru

client = hhru.Client()


def filter_vacancy(vacancy: Any) -> Any:
    return vacancy


def print_vacancy(vacancy: Any) -> None:
    print(">>>", vacancy["name"])


def main():
    text = "Python Django"

    # Get all vacancies with generator and filter by filter vacancies function.
    vacancies = list(
        filter(
            functools.partial(filter_vacancy),
            client.search_vacancies_over_pages(
                text=text.lower(),
                search_field=hhru.consts.VACANCY_SEARCH_FIELD_NAME,
                order_by=hhru.consts.VACANCY_SEARCH_ORDER_PUBLICATION_TIME,
                schedule=hhru.consts.SCHEDULE_REMOTE,
            ),
        )
    )

    # Print 50 first vacancies.
    [print_vacancy(vac) for vac in vacancies[0:50]]


if __name__ == "__main__":
    main()
