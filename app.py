import requests

API_link = 'https://api.telegram.org/bot5543911980:AAFEjgdoFmUCOINyfKs2Q9MjDUk15QnMfvk'


chat_id_Rahul = '394761402'
chat_id_Sonya = '547112359'
text = 'Что%20сегодня%20смотрим?'
updates= requests.get('https://api.telegram.org/bot5543911980:AAFEjgdoFmUCOINyfKs2Q9MjDUk15QnMfvk/getUpdates').json()
print(updates)

for i in range(3):
    message = updates['result'][i]["message"]
    chat_id = message['from']['id']
    text = message['text']
    print(chat_id)
    print(text)

    text_hi = requests.get(API_link + '/sendMessage?chat_id=' + chat_id_Rahul + '&text=' + text)
sent_message = 1

