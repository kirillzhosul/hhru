import hhru

# Show Python vacancies (one page).
api = hhru.Api()
for vacancy in api.method("vacancies", text="Python").items:
    print("\t", vacancy["name"])
