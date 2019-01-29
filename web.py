import re
import requests
from html.parser import HTMLParser
from urllib.parse import urlparse


def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item):
            return item
    return None


class HRefParser(HTMLParser):
    def __init__(self, refs):
        HTMLParser.__init__(self)
        self.refs = refs

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            href = find(lambda p: p is not None and p[0].lower() == "href", attrs)
            if href is not None:
                __, address = href
                self.refs.add(address)


def collect_refs_at(url, refs):
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException:
        return
    if res.status_code != 200:
        return

    parser = HRefParser(refs)
    parser.feed(res.text)


def get_unique_sites(url):
    refs = set()
    collect_refs_at(url, refs)
    locations = set()
    for href in refs:
        loc = urlparse(href).hostname
        if loc is not None and len(loc)>0:
            locations.add(loc)
    return locations


def main():
    url = input()
    sites = list(get_unique_sites(url))
    sites.sort()
    for s in sites:
        print(s)


main()


def test_href_parser():
    refs = set()
    parser = HRefParser(refs)
    parser.feed(
        ''' <a href="http://stepic.org/courses">;
            <a class = "hello" href= "http://ftepic.org/courses"; id="dfdf">
            <p class = "hello" href= "http://dtepic.org/courses">;
            <a class = "hello" href = "http://a.b.vc.ttepic.org/courses">;
            <a href='https://stepic.org'>;
            <a href='http://neerc.ifmo.ru:1345'>;
            <a href = "ftp://mail.ru/distib" >
            <a href= "ya.ru">
            <a href ="www.ya.ru">;
            <a href="../skip_relative_links">
            <link rel="image_src" href="https://examaple.org/files/6a2/72d/e09/6a272de0944f447fb5972c44cc02f795.png"; />
        ''')
    print(refs)


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


# main()


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
