from typing import Any, Optional

from pydantic import BaseModel, Field


class _EnumeratedFieldDTO(BaseModel):
    id: str
    name: str


class VacancyDTO(BaseModel):
    class _SalaryDTO(BaseModel):
        from_: float | None = Field(alias="from", default=None)
        to: float
        currency: str
        gross: bool

    class _AreaDTO(_EnumeratedFieldDTO):
        url: str

    class _MetroDTO(BaseModel):
        lat: float
        lng: float
        station_name: str
        line_name: str
        station_id: str
        line_id: str

    class _AddressDTO(BaseModel):
        city: str
        street: str
        building: str
        lat: float
        lng: float
        description: None
        raw: str
        id: int
        metro: Optional["VacancyDTO._MetroDTO"]
        metro_stations: list["VacancyDTO._MetroDTO"]

    class _EmployerDTO(_EnumeratedFieldDTO):
        url: str
        alternate_url: str
        logo_urls: dict[str, str]

        vacancies_url: str
        accredited_it_employer: bool
        trusted: bool

    class _SnippetDTO(BaseModel):
        requirement: str
        responsibility: str | None

    id: int
    premium: bool
    name: str
    department: None
    has_test: bool
    response_letter_required: bool

    response_url: str | None
    sort_point_distance: None  # TODO: type
    published_at: str  # TODO: parse date
    created_at: str  # TODO: parse date
    archived: bool
    apply_alternate_url: str
    show_logo_in_search: bool | None
    insider_interview: None
    url: str
    alternate_url: str
    is_adv_vacancy: bool
    accept_temporary: bool
    accept_incomplete_resumes: bool
    relations: list[Any]  # TODO: research
    contacts: None  # TODO: research
    working_days: list[Any]
    working_time_intervals: list[Any]
    working_time_modes: list[Any]
    adv_response_url: None
    adv_context: None

    snippet: _SnippetDTO
    employer: _EmployerDTO
    address: _AddressDTO | None
    area: _AreaDTO
    schedule: _EnumeratedFieldDTO
    professional_roles: list[_EnumeratedFieldDTO]
    experience: _EnumeratedFieldDTO
    employment: _EnumeratedFieldDTO
    salary: _SalaryDTO | None
    type_: _EnumeratedFieldDTO = Field(alias="type")
