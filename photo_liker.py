import vk_requests
import oauth
import time

# Авторизация
login = 'login'
pwd = 'password'
app_id = 123456 # ID приложения VK
scopes = 2097151

# Настройки
album_id = ['wall', 'profile', 'saved']
targer_id = 123456 # ID цели

# Переменные
photos_ids = []
i = 0

# Начало скрипта
vkapi = vk_requests.create_api(app_id, login, pwd, api_version='5.44', timeout=10)

for album in album_id:
    photos_list = vkapi.photos.get(owner_id=targer_id, album_id=album, extended=0, count=1000)
    print(photos_list)
    for photos in photos_list['items']:
        photos_ids.append(photos['id'])

total = len(photos_ids)
print('Count: '+str(total))
print('start')
for each_id in photos_ids:
    try:
        i+=1
        vkapi.likes.add(type='photo', owner_id=targer_id, item_id=each_id)
    finally:
        print(str(i)+'/'+str(total))
        time.sleep(1)
print('finish')