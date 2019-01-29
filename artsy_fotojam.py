import string
import sys
from operator import itemgetter
from typing import List

import requests

# _token = {
#     "type": "xapp_token",
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU0OTQwMjg4MiwiaWF0IjoxNTQ4Nzk4MDgyLCJhdWQiOiI1YzUwYzg4MmJlMTlkMTA2YWEzNjRjZmMiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWM1MGM4ODJiZTE5ZDEwNmFhMzY0Y2ZkIn0.MAJHt0Pr58at4yi0lhq_XqYAkcEmmkRM5BLLL6gdXmg",
#     "expires_at": "2019-02-05T21:41:22+00:00",
#     "_links": {}
# }
#
# test_ = {
#     "id": "4d8b92b34eb68a1b2c0003f4",
#     "name": "Andy Warhol"
# }
#
# ######################################
#
# name_ = "fotojam"
# client_id_ = "2f3f261f7d60f4f40751"
# client_secret_ = "7109f1db488159b79d92c489be3dafdf"
#
#
#
# # создаем заголовок, содержащий наш токен
# headers_ = {"X-Xapp-Token": token}
#
# artist_id_ = "4d8b92b34eb68a1b2c0003f4"


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU0OTQwMjg4MiwiaWF0IjoxNTQ4Nzk4MDgyLCJhdWQiOiI1YzUwYzg4MmJlMTlkMTA2YWEzNjRjZmMiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWM1MGM4ODJiZTE5ZDEwNmFhMzY0Y2ZkIn0.MAJHt0Pr58at4yi0lhq_XqYAkcEmmkRM5BLLL6gdXmg"


def get_artist_info_by_id(artist_id: string) -> (int, string):
    headers = {"X-Xapp-Token": token}

    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{artist_id}", headers=headers)

    # разбираем ответ сервера
    j = r.json()  # json.loads(r.text)
    return int(j["birthday"]), j["sortable_name"]


def test_artist_info():
    print(get_artist_info_by_id("4d8b92b34eb68a1b2c0003f4"))


def process_ids(ids : []) -> [int, string]:
    infos = [i for i in map(get_artist_info_by_id, ids)]
    return infos


def test_process_ids():
    infos = process_ids(["4d8b92b34eb68a1b2c0003f4"])
    assert infos == 1928, "Warhol Andy"


def main():
    ids = list(map(lambda s: s.strip(), sys.stdin.readlines()))
    info_list = process_ids(ids)
    sorted_info_list = sorted(info_list, key=itemgetter(0, 1))
    for __, name in sorted_info_list:
        print(name)


main()
