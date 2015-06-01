__author__ = 'dexofan'
import vk
import time

album_id = ['wall', 'profile', 'saved']
photos_ids = []
targer_id = Ид цели
i = 0
vkapi = vk.API('Ид приложения', 'Логин', 'Пароль')

for album in album_id:
    photos_list = vkapi('photos.get', owner_id=targer_id, album_id=album, count=1000)
    for photos in photos_list['items']:
        photos_ids.append(photos['id'])

total = len(photos_ids)
print('Count: '+str(total))
print('start')
for each_id in photos_ids:
    try:
        i+=1
        vkapi('likes.add', type='photo', owner_id=targer_id, item_id=each_id)
    except vk.VkAPIMethodError:
        pass
    finally:
        print(str(i)+'/'+str(total))
        time.sleep(1)
print('finish')
