import yaml

def create_config(bot_id: str, bot_token: str, *commands) -> str:
    config = {
        "bot_id": bot_id,
        "bot_token": bot_token,
        "commands": [
            {"description": description, "function": function}
            for description, function in commands
        ]
    }
    return yaml.dump(config, allow_unicode=True, default_flow_style=False)
bot_id = "457"
bot_token = "1249774028390"
commands = [
    ("Приветствие", "greet_user"),
    ("Получить прогноз погоды", "get_weather")
]
