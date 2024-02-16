import requests


# page = requests.get("http://google.com",params={
#     "q": "cats"
# })
page = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = page.json()


if page.status_code == 200:
    # print("OK")
    # print(page.text)
    # print(page.url)
    # print(page.headers)
    print(data['userId'])
    print(page.headers['Content-Type'])

else:
    print("Eroor", page.status_code)