from statistics import mean

from hhru import Client
from hhru.consts import CURRENCY_RUR

SELECTED_CURRENCY = CURRENCY_RUR
SELECTED_TEXT = "Уборщик"

vacancies = [
    v
    for v in Client().search_vacancies_over_pages(text=SELECTED_TEXT)
    if v.salary and v.salary.currency == SELECTED_CURRENCY
]

mean_from_salary = mean(
    [vac.salary.from_ for vac in vacancies if vac.salary and vac.salary.from_]
)

mean_to_salary = mean(
    [vac.salary.to for vac in vacancies if vac.salary and vac.salary.to]
)

print(
    f"Average (mean) salary for given request is from {mean_from_salary:.0f} to {mean_to_salary:.0f}{SELECTED_CURRENCY}"
)
