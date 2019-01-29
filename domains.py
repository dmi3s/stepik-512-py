import re
import requests


def get_all_refs(url):
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException:
        return []
    if res.status_code != 200:
        return []

    refs = re.findall(r"<\s*a\s+[^>]*href=[\"']([^\"']+)[\"'][^>]*>", res.text)
    return refs


def extract_site(url):
    result = re.sub(r"^(?:\w+://)?(?:([\w\-.]+)(?::[0-9]+)?)/?.*$", r"\1", url)
    if result.startswith(".") or result.startswith("/"):
        result = None
    return result


def extract_sites_from_urls(urls):
    result = set()
    for site in map(extract_site, urls):
        if site is not None:
            result.add(site)
    return list(result)


def main():
    url = input().strip()
    refs = get_all_refs(url)
    sites = extract_sites_from_urls(refs)
    sites.sort()
    for s in sites:
        print(s)


main()


def test_extract_sites_from_urls():
    urls = [
        "http://stepic.org/courses",
        "https://stepic.org",
        "http://neerc.ifmo.ru:1345",
        "ftp://mail.ru/distib",
        "ya.ru",
        "www.ya.ru",
        "../skip_relative_links"
    ]
    result = extract_sites_from_urls(urls)
    result.sort()
    print(result)



def test_extract_site():
    assert extract_site("http://stepic.org/courses") == "stepic.org"
    assert extract_site("https://stepic.org") == "stepic.org"
    assert extract_site("http://neerc.ifmo.ru:1345") == "neerc.ifmo.ru"
    assert extract_site("ftp://mail.ru/distib") == "mail.ru"
    assert extract_site("ya.ru") == "ya.ru"
    assert extract_site("www.ya.ru") == "ya.ru"
    assert extract_site("../skip_relative_links") is None

def test_get_all_refs():
    refs = get_all_refs("https://stepic.org/media/attachments/lesson/24472/sample0.html")
    assert refs is not None
    assert len(refs) > 0
    assert refs[0].start_with("http")
