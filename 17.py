import bz2
import http.cookiejar
import requests
import urllib
import xmlrpc.client

def extract_info_cookie(cookiejar):
    for cookie in cookiejar:
        if cookie.name == 'info':
            return cookie.value

def autobot(nothing, cookies):
    cookiejar = http.cookiejar.CookieJar()
    cookieproc = urllib.request.HTTPCookieProcessor(cookiejar)
    opener = urllib.request.build_opener(cookieproc)

    param = urllib.parse.urlencode({'busynothing' : nothing})
    response = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % param)

    words = response.read()
    cookie = extract_info_cookie(cookiejar)
    print(words.decode('utf-8'), cookie)
    cookies.append(cookie)

    if words != b"that's it.":
        return words.split()[-1]

def call_father():
    with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
        print(proxy.phone("Leopold"))

def inform_father():
    print(requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php',
        cookies={'info': 'the flowers are on their way'}).text)

if __name__ == "__main__":
    start = '12345'
    cookies = []
    while len(start) > 0:
        start = autobot(start, cookies)
        if start is None:
            break
    words = urllib.parse.unquote_to_bytes(''.join(cookies))
    print(bz2.decompress(words).decode('utf-8'))

    call_father()

    inform_father()
