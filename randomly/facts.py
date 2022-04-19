from typing import Dict, Union

import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format: str, language: str) -> Union[str, Dict]:
    """Fetch a random fact from the Useless Facts API

    Parameters
    ----------
    output_format : {"html", "json", "txt", "md"}
        Desired format for the returned fact.
    language : {"en", "de"}
        Desired language for the fact. English and German supported.

    Returns
    -------
    fact : Union[str, Dict]
        The result of the query. If ``output_format=="json"``, it returns a dictionary.
        Otherwise, a string is returned.

    Raises
    ------
    ValueError
        When ``language`` is not one of ``{"en", "de"}``.
    ValueError
        When ``output_format`` not one of ``{"html", "json", "txt", "md"}``.
    RequestException
        When the request response is anything other than a 200 (success).
    """

    # Validate that inputs match supported values
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    # Query random fact API
    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    if response.status_code == 200:
        # Get the proper format for the output
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
