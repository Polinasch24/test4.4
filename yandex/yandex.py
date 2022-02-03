import requests
TOKEN=''

def add_folder(TOKEN,folder_name):

    url='https://cloud-api.yandex.net/v1/disk/resources'

    params = {
        'path': {folder_name},
        'fields': 'json'
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {TOKEN} '
    }
    resp = requests.put(url, headers=headers, params=params)

    return resp.status_code

print(add_folder(TOKEN, '1'))

def delete_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    create_dir = requests.delete(url, headers=headers, params=params)
    return create_dir.status_code
print(delete_folder('1'))
