import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(self.token)
    }

    def upload(self, file_path: str, file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        disk_file_path = file_name # Для того что бы файл падал в основную директорию
        headers = self.get_headers()
        params = {"path": 'test', "overwrite": "true"}
        response_lnk = requests.get(upload_url, headers=headers, params=params)
        upload_link = response_lnk.json()
        href = upload_link.get('href',"")
        print(href)
        response = requests.put(href, data = open(((file_path)+('\\')+(file_name)), 'rb'))
        if response.status_code == 201:
            pprint('Succses!')
        """Метод загружает файлы по списку file_list на яндекс диск"""


if __name__ == '__main__':
    path_to_file = 'C:\\Users\\Mytth\Desktop\\Netology\\Yandex'
    token = 'TOKEN'
    f_name = 'test.txt'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, f_name)