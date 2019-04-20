from urllib.parse import urlparse

import lxml.html
import requests


def hostname(url: str) -> str:
    return urlparse(url).hostname


giga_viewer = "//span[@class='series-episode-list-date']"
xpath_dict = {
    "comic-meteor.jp": "//div[@class='latest_info_date']",
    "comic-boost.com": "//div[@class='product_item']/p[@class='date']",
    "web-ace.jp": "//span[@class='updated-date']",
    "pocket.shonenmagazine.com": giga_viewer,
    "kuragebunch.com": giga_viewer,
    "tonarinoyj.jp": giga_viewer,
}


def main(opt):
    url = "https://comic-boost.com/series/86"

    r = requests.get(url)
    html = lxml.html.fromstring(r.content)
    if hostname(url) in xpath_dict.keys():
        htmltag = html.xpath(xpath_dict[hostname(url)])
        if htmltag is not None:
            print(htmltag[0].text)


if __name__ == "__main__":
    main({})
