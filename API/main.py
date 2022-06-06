import requests
from requests.exceptions import HTTPError


class Api:
    def __init__(self, id):
        self.id = id
        self.method = "https://api.vk.com/method/"
        self.user = "users.get?user_ids="
        self.fhotos = "photos.getAlbums?owner_id="
        self.albums = "&album_ids=title"
        self.friends = "friends.get?user_id="
        self.fields = "&fields=nickname"
        self.token = "&v=5.107&access_token=c5955299c5955299c595529924c5e72fd8cc595c59552999b481ea4a5e5e0d9b055d64f"
        self.request()

    def request(self):
        try:
            user = requests.get(f'{self.method}{self.user}{self.id}{self.token}')
            inf = user.json()['response'][0]
            self.id = inf['id']
            print("User:")
            print(inf["first_name"], inf['last_name'], '\n')
        except HTTPError as error:
            print(error)
        try:
            friends = requests.get(f'{self.method}{self.friends}{self.id}{self.fields}{self.token}')
            print("Friends:")
            inf = friends.json()["response"]["items"]
            for x in inf:
                print(x["first_name"], x['last_name'])
            print('\n')
        except HTTPError as error:
            print(error)
        try:
            photos = requests.get(f'{self.method}{self.fhotos}{self.id}{self.albums}{self.token}')
            print("Albums:")
            inf = photos.json()["response"]["items"]
            for x in inf:
                print(x['title'])
        except HTTPError as error:
            print(error)


if __name__ == '__main__':
    print("Введите id пользователя")
    request = input()
    ex = Api(request)
