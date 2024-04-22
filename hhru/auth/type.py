from enum import Enum, auto


class AuthAccessType(Enum):
    """
    Abstract meaning of the access that is allowed for authentication

    Mostly, only some of them are used right now (TODO)

    """

    # NOTICE: Will reject all requests, only for internals
    abstract = auto()

    # No auth at all, will allow only basic stuff like searching
    anonymous = auto()

    # TODO: not used, actually OAuth client scope
    application = auto()

    # Most relevant one, default auth type for employee
    applicant = auto()

    # Employer states
    # TODO: Paid status is not used
    employer = auto()
    employer_paid = auto()
