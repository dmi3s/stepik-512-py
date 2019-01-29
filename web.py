import re
import requests


def get_all_refs(url):
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException:
        return []
    if res.status_code != 200:
        return False

    refs = re.findall(r"<\s*a\s+href\s*=\s*\"([^\"]+)\"\s*>", res.text)
    return refs


def is_accessible(a_url, b_url):
    refs_from_a = get_all_refs(a_url)
    return b_url in refs_from_a


def is_accessible_by_c(a_url, b_url):
    refs_from_a = get_all_refs(a_url)
    for ref in refs_from_a:
        if is_accessible(ref, b_url):
            return True
    return False


def main():
    a_url = input().strip()
    b_url = input().strip()
    answer = "Yes" if is_accessible_by_c(a_url, b_url) else "No"
    print(answer)


main()


def test_get_all_refs():
    refs = get_all_refs("test")
    assert len(refs) == 0
    refs = get_all_refs("https://stepic.org/media/attachments/lesson/24472/sample0.html")
    assert refs is not None
    assert len(refs) > 0
    assert refs[0].start_with("http")


def test_accessible():
    accessible = is_accessible_by_c("https://stepic.org/media/attachments/lesson/24472/sample0.html",
                                    "https://stepic.org/media/attachments/lesson/24472/sample2.html")
    assert accessible is True

    accessible = is_accessible_by_c("https://stepic.org/media/attachments/lesson/24472/sample0.html",
                                    "https://stepic.org/media/attachments/lesson/24472/sample1.html")
    assert accessible is False
