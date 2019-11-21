from my_fake_useragent import UserAgent


def get_request_headers():
    ua = UserAgent()

    return {"User-Agent":ua.random()}

if __name__ == '__main__':
    UA = get_request_headers()
