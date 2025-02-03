# Сеть
# Здесь описано некоторое API, в котором есть доступ к базе пользователей, постов, комментариев и т.д. Методы, которые мы будем использовать, описаны в разделе Resources. Примеры использования API (правда, на JavaScript'е) описаны на том же сайте по ссылке Guide. Вам нужно для каждого пользователя посчитать количество оставленных постов и количество оставленных комментариев. Всю информацию для этого нужно стягивать GET-запросами по API. Результат нужно отправить в ваше пространство в https://webhook.site в виде POST-запроса, содержащего JSON следующего формата:
#   "statistics": [
#     {
#       "id": 1,
#       "username": "lolkek",
#       "email": "user1@mail.dot",
#       "posts": 125,
#       "comments": 1358
#     },
#     {
#       "id": 2,
#       "username": "cheburek",
#       "email": "user2@mail.dot",
#       "posts": 5,
#       "comments": 12
#     }
#   ]
# }
# Задача - реализовать функцию process_user_data(), которая собирает информацию о пользователях из публичного API и отправляет статистику о каждом пользователе на заданный вебхук. Функция должна возвращать response объект ответа запроса - 
# return requests.post(.....)
# Реализуйте функцию , которая возвращает результат в виде JSON следующего формата:

import requests #no solution

def process_user_data():
    base_url = "https://jsonplaceholder.typicode.com"
    webhook_url = "https://webhook.site/your-webhook-url" 

    try:
        users = requests.get(f"{base_url}/users").json()
        statistics = []

        for user in users:
            user_id = user["id"]
            username = user["username"]
            email = user["email"]
            posts = requests.get(f"{base_url}/posts", params={"userId": user_id}).json()
            post_count = len(posts)
            comments = requests.get(f"{base_url}/comments", params={"email": email}).json()
            comment_count = len(comments)

            statistics.append({
                "id": user_id,
                "username": username,
                "email": email,
                "posts": post_count,
                "comments": comment_count
            })

        data = {"statistics": statistics}

        response = requests.post(webhook_url, json=data)
        return response 

    except requests.RequestException as e:
        print(f"Произошла ошибка при запросе к API: {e}")
        return None
