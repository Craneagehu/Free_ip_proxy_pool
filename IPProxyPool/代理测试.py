import requests

test_url = 'http://httpbin.org/get'
test_url = "http://httpbin.org/get?show_env=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
proxies = {
        "http":"http://114.239.145.167:9999",
        "https":"https://114.239.145.167:9999"
    }
response = requests.get(test_url,proxies=proxies,timeout = 10,headers=headers)
print(response.text)



