import requests
import os.path
ROOT_PATH = os.getcwd()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    # Получить ссылку на аплоад файла
    def get_upload_link(self, file_path):
        self.upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        self.params = {
            'path': file_path,
            'overwrite': 'true'
        }
        return requests.get(url=self.upload_url, headers=self.headers, params=self.params).json()


    # Аплоад файла
    def upload(self, file_path: str):
        # full_path = os.path.join(ROOT_PATH, file_path)
        href = self.get_upload_link(file_path).get('href', '')
        response = requests.put(url=href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Успешно'
        else:
            return 'Ошибка'

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '123.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)