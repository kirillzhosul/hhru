import hhru
from hhru.dto.vacancy import VacancyDTO

client = hhru.Client()


def filter_vacancy(vacancy: VacancyDTO) -> bool:
    return True


def print_vacancy(vacancy: VacancyDTO) -> None:
    print(">>>", vacancy.name, vacancy.relations)


def main():
    text = "Python Django"

    vacancies_all = list(
        client.search_vacancies_over_pages(
            text=text.lower(),
            search_field=hhru.consts.VACANCY_SEARCH_FIELD_NAME,
            order_by=hhru.consts.VACANCY_SEARCH_ORDER_PUBLICATION_TIME,
            schedule=hhru.consts.SCHEDULE_REMOTE,
        ),
    )
    # Get all vacancies with generator and filter by filter vacancies function.
    vacancies = list(filter(filter_vacancy, vacancies_all))

    print(len(vacancies))
    # Print 50 first vacancies.
    [print_vacancy(vac) for vac in vacancies[0:50]]


if __name__ == "__main__":
    main()
