from hhru import Client

SELECTED_TEXT = "C++"

vacancies = [v for v in Client().search_vacancies_over_pages(text=SELECTED_TEXT)]

p = len([v for v in vacancies if v.employer.accredited_it_employer])


print(
    f"Процент (%) акредитированных IT компаний среди {len(vacancies)} вакансий по запросу `{SELECTED_TEXT}`: {p / len(vacancies) * 100}%"
)
