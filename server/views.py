from aiohttp import web
import json
from hashlib import sha256


async def index(request):
    return web.Response(text="Hello Aiohttp!")


async def handle_healthcheck(request):
    return web.json_response(json.dumps({}), status=200)


# Метод: POST, Путь: /hash,
# Тело запроса: JSON объект с обязательным полем 'string'.
# Ответ: Если поле отсутствует - статус 400 и JSON
# с полем 'validation_errors'.
# В противном случае возвращается JSON с полем 'hash_string',
# содержащим хэш строки, вычисленный по алгоритму SHA256.


async def handle_posthash(request):
    request_data = await request.json()
    try:
        string = request_data["string"]
        send_data = json.dumps(
            {"hash_string": sha256(string.encode("utf-8")).hexdigest()}
        )
        return web.json_response(send_data)
    except KeyError as e:
        send_data = json.dumps({"validation_errors": e.__repr__()})
        return web.json_response(send_data, status=400)
