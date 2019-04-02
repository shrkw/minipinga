import requests
import lxml.html


def main():
    url = "https://comic-meteor.jp/idrunk/"
    r = requests.get(url)
    html = lxml.html.fromstring(r.content)
    htmltag = html.xpath("//div[@class='latest_info_date']")

    for tag in htmltag:
        print(tag.text)


if __name__ == "__main__":
    main()

