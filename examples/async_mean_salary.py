import asyncio
from statistics import mean

from hhru.auth.providers.anonymous import AnonymousAuthProvider
from hhru.backend.api.provider import BackendAsyncApiProvider
from hhru.client import AsyncClient
from hhru.consts import CURRENCY_RUR

SELECTED_CURRENCY = CURRENCY_RUR
SELECTED_TEXT = "Уборщик"

client = AsyncClient(
    backend=BackendAsyncApiProvider(
        auth_provider=AnonymousAuthProvider(),
        concurrent_max_requests=5,
    )
)


async def main():
    vacancies = [
        v
        for v in await client.search_vacancies_async_burst(text=SELECTED_TEXT)
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


asyncio.run(main())
