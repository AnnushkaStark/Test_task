import asyncio
import json

import httpx


URL = "https://jsonplaceholder.typicode.com/posts"
FILE_PATH = "result.json"


async def get_response_json(url: str) -> dict | None:
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(url=url)
        response_data = response.json()
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(response_data, file, ensure_ascii=False, indent=4)
            return "Данные успешно сохранены"


print(asyncio.run(get_response_json(url=URL)))
