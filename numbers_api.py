import sys

import requests

api_url = "http://numbersapi.com/"
number_type = "math"

params = {
    "json": "true"
}


def get_number_info(num):
    api_num_url = "/".join([api_url, str(num), number_type])
    res = requests.get(api_num_url, params=params)
    if res.status_code != 200:
        return None
    return res.json()


def is_number_interesting(num):
    data = get_number_info(num)
    return data["found"]


def format_anser(is_interesting):
    return "Interesting" if is_interesting else "Boring"


def test_numbers():
    print(format_anser(is_number_interesting(31)))


def main():
    nums = map(int, sys.stdin.readlines())
    for n in nums:
        print(format_anser(is_number_interesting(n)))


main()
