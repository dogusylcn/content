import demistomock as demisto
from CommonServerPython import *


def regex_create():
    domain = r'(?:[.-]?[a-zA-Z\d]+)+'
    general_local_part_allowed = r"\d\w!#$%&'*+\-/=?^_`{|}~"
    lacal_part = rf"(?:[{general_local_part_allowed}](?:[{general_local_part_allowed}]|\.(?!\.))*)"

    return rf'(?:^|(?<=[<\s])){lacal_part}@{domain}(?:(?=[>\s])|$)'


EMAIL_REGEX = re.compile(regex_create())


def main():
    try:
        list_results = []
        for val in argToList(demisto.args().get('value')):
            list_results.extend(list(re.findall(EMAIL_REGEX, val)))
        return_results(list_results)
    except Exception as error:
        return_error(str(error), error)


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
