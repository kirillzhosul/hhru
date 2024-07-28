import hhru

for vac in hhru.Client().search_vacancies():
    print(">>>", vac.name, vac.salary)


# Will iterate pages (generator inside) and yield batch within page limit ~ 100
# Notice that there is a over-pages limit in 2000 vacancies (means there 21 page max)
for vac in hhru.Client().search_vacancies_over_pages():
    print(">>>", vac.name, vac.salary)


# Example of kwargs:
"""
client.search_vacancies_over_pages(
    text=text.lower(),
    search_field=hhru.consts.VACANCY_SEARCH_FIELD_NAME,
    order_by=hhru.consts.VACANCY_SEARCH_ORDER_PUBLICATION_TIME,
    schedule=hhru.consts.SCHEDULE_REMOTE,
),
"""
