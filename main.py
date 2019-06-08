import dataclasses
import datetime
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

import lxml.html
import requests


def hostname(url: str) -> str:
    return urlparse(url).hostname


@dataclasses.dataclass
class MangaSite:
    url: str
    indication_text_xpath: str
    has_feed: bool


manga_sites: Dict[str, MangaSite] = {
    "comic-meteor.jp": MangaSite(
        "comic-meteor.jp", "//div[@class='latest_info_date']", False
    ),
    "comic-boost.com": MangaSite(
        "comic-boost.com", "//div[@class='product_item']/p[@class='date']", False
    ),
    "web-ace.jp": MangaSite("web-ace.jp", "//span[@class='updated-date']", False),
    "pocket.shonenmagazine.com": MangaSite("pocket.shonenmagazine.com", "", True),
    "kuragebunch.com": MangaSite("kuragebunch.com", "", True),
    "tonarinoyj.jp": MangaSite("tonarinoyj.jp", "", True),
}


@dataclasses.dataclass
class Subscription:
    url: str
    title: str
    last_checked_date: datetime.datetime
    indication_text_value: str


subscriptions: List[Subscription] = [
    Subscription(
        "https://comic-boost.com/series/86", "ken", datetime.datetime.today(), "a"
    ),
    Subscription(
        "https://comic-meteor.jp/idrunk/", "idrunk", datetime.datetime.today(), "a"
    ),
    Subscription(
        "https://web-ace.jp/youngaceup/contents/1000118/",
        "FGO seraph",
        datetime.datetime.today(),
        "a",
    ),
]


def save(url: str, text: str):
    pass


def notify(text: str):
    print(text)


def check_update(sub: Subscription) -> Tuple[bool, Optional[str]]:
    r = requests.get(sub.url)
    html = lxml.html.fromstring(r.content)
    host = hostname(sub.url)
    if host in manga_sites.keys():
        element = html.xpath(manga_sites[host].indication_text_xpath)
        if len(element) == 0:
            raise AssertionError("elements for updated_date are not found", sub)
        text = element[0].text
        if text != sub.indication_text_value:
            return (True, text)
        return (False, None)
    else:
        raise AssertionError("unknown host!", sub)


def main(opt):
    for sub in subscriptions:
        updated, indication_text_value = check_update(sub)
        if updated:
            notify(f"{sub.title} が {indication_text_value} に更新されている可能性があります {sub.url}")


if __name__ == "__main__":
    main({})
