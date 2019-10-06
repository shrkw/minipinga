import dataclasses
import datetime
from typing import Dict, List, Optional, Any
from urllib.parse import urlparse

import lxml.html
import requests
from google.cloud import firestore

import notifier

db = firestore.Client()


def hostname(url: str) -> str:
    return urlparse(url).hostname


def save(id: str, indication_text_value: str) -> None:
    doc_ref = db.collection("subscriptions").document(id)
    doc_ref.update(
        {
            "indication_text_value": indication_text_value,
            "last_checked_date": datetime.datetime.now(),
        }
    )


def get_indicator(manga_site, content):
    html = lxml.html.fromstring(content)
    element = html.xpath(manga_site["indication_text_xpath"])
    if len(element) == 0:
        raise AssertionError("elements for updated_date are not found")
    text = element[0].text
    return text


def check_update(sub: Dict) -> Optional[str]:
    url = sub["url"]
    r = requests.get(url)
    host = hostname(url)

    doc_ref = db.collection("manga_sites").document(host)
    doc = doc_ref.get()
    manga_site = doc.to_dict()
    if manga_site is None:
        raise AssertionError("unknown host!", sub)

    value = get_indicator(manga_site, r.content)
    if value != sub["indication_text_value"]:
        return value
    return None


def minipinga(data: Dict, context: Any) -> None:
    subs_ref = db.collection("subscriptions")
    for sub in subs_ref.stream():
        sub_dict = sub.to_dict()
        indication_text_value = check_update(sub_dict)
        if indication_text_value:
            print(f"{sub_dict['title']} may be updated at {indication_text_value}")
            notifier.notify(
                f"{sub_dict['title']} が {indication_text_value} に更新されている可能性があります {sub_dict['url']}"
            )
            save(sub.id, indication_text_value)


if __name__ == "__main__":
    minipinga(dict(), None)
