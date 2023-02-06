import aiohttp


class Telegram:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self._session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=15),
        )

    async def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML",
        }
        async with self._session.post(url, params=params) as response:
            data = await response.json()
            ok = data.get("ok")
            if not ok:
                raise ValueError(data)

    async def send_photo(self, photo_url, caption=None):
        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"
        params = {
            "chat_id": self.chat_id,
            "photo": photo_url,
            "parse_mode": "HTML",
        }
        if caption:
            params["caption"] = caption
        async with self._session.post(url, params=params) as response:
            data = await response.json()
            ok = data.get("ok")
            if not ok:
                raise ValueError(data)

    def __del__(self):
        if self._session:
            self._session._connector.close()  # type: ignore
