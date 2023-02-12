import re
def extract_days(str):
    pattern = "([0-9]+) - ([0-9]+)day"

    result = re.search(pattern, str)
    first_day = int(result.group(1))
    last_day = int(result.group(2))

    for i in range(first_day, last_day+1):
        print(i)