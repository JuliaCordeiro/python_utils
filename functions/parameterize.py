import re
from unidecode import unidecode

def parameterize(string, separator='-', preserve_case=False):
    parameterized_string = unidecode(string)
    parameterized_string = re.sub("[^a-z0-9\-_]+", separator, parameterized_string, 0, re.IGNORECASE)

    if separator == "-":
        re_duplicate_separator = "-{2,}"
        re_leading_trailing_separator = "^-|-$"
    else:
        re_sep = re.escape(separator)
        re_duplicate_separator = f"{re_sep}{2,}"
        re_leading_trailing_separator = f"^{re_sep}|{re_sep}$"

    if parameterized_string[-1] == "-":
        parameterized_string = parameterized_string[:-1]

    parameterized_string = re.sub(re_duplicate_separator, separator, parameterized_string, 0, re.IGNORECASE)
    parameterized_string = re.sub(re_leading_trailing_separator, "", parameterized_string, 0, re.IGNORECASE)

    if not preserve_case:
        parameterized_string = parameterized_string.lower()

    return parameterized_string
