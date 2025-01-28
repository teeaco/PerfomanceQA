import requests

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
