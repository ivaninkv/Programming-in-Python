import requests
import operator
from datetime import datetime
from contracts import contract


ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'


@contract
def get_user_id(uid: str) -> int:
    '''
    Функция возвращает id пользователя по username или user_id.
    '''

    user_url = f'https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}'
    req = requests.get(user_url)
    res = req.json()    
    try:
        return res['response'][0]['id']
    except:
        return 0
    

@contract
def dict_to_sorted_list(dictionary: dict) -> list:
    '''
    Функция преобразовывает словарь в отсортированный список.
    '''
        
    sorted_items = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
    return list(sorted_items)


@contract
def calc_age(uid: str) -> list:
    '''
    Функция возвращает распределение друзей по возрасту.    
    '''    
    
    friends_url = f'https://api.vk.com/method/friends.get?v=5.71&access_token={ACCESS_TOKEN}&user_id={get_user_id(uid)}&fields=bdate'
    req = requests.get(friends_url)
    res = req.json()    
    ages = dict()
    try:        
        friends = res['response']['items']
        for friend in friends:
            if 'bdate' in friend:                
                bdate = friend['bdate']
                if bdate.count('.') == 2:
                    year = int(datetime.now().year) - int(bdate[-4:])
                    if year in ages:
                        ages[year] += 1
                    else:
                        ages[year] = 1                
    except:
        pass    

    return dict_to_sorted_list(ages)


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
    # print('='*50)
    # print(calc_age('id10'))
