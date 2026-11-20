from urllib.parse import quote_plus


def job_search_links(role, location):
    q = quote_plus(f"{role} {location}")
    return [
        ("LinkedIn Jobs", f"https://www.linkedin.com/jobs/search/?keywords={q}"),
        ("Indeed", f"https://in.indeed.com/jobs?q={q}"),
        ("Naukri", f"https://www.naukri.com/{quote_plus(role).replace('+','-')}-jobs-in-{quote_plus(location).replace('+','-')}"),
        ("Google Jobs search", f"https://www.google.com/search?q={q}+jobs"),
    ]
