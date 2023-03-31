import requests
import json


# Указываем константы скрипта
METHOD = 'listGoods'
LOGIN = '493358_stroyzar'
PASSWORD = 'sAVDkrEbqd'
# ART = 'OC47'
ART = input("Укажите артикул для поиска: ")


# Выполнение запроса к серверу API Форум-Авто
def get_answ_frm_api(METHOD, LOGIN, PASSWORD, ART):
    url = f"https://api.forum-auto.ru/v2/{METHOD}?login={LOGIN}&pass={PASSWORD}&art={ART}"
    # Обрабатываем возмужную ошибку
    try:
        src = requests.get(url=url)
    except:
        raise ConnectionError("Не удалось выполнить соединение с сервером.")  
    else:
        return src.text
    finally:
        print(src.text)


# Сохраняем ответ в JSON файл
def save_answ_to_json(src):
    with open('answer.json', 'w', encoding='UTF-8') as fp:
        json.dump(src, fp, indent=4, ensure_ascii=False)


# Включаем функции в скрипте
if __name__ == '__main__':
    src = get_answ_frm_api(METHOD, LOGIN, PASSWORD, ART)
    save_answ_to_json(src)
