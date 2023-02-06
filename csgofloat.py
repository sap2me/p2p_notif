import aiohttp

headers = {
    "authority": "csgofloat.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "origin": "https://csgofloat.com",
    "referer": "https://csgofloat.com",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


class CSGOFloat:
    def __init__(self, account_data):
        self._account_data = account_data
        headers["Authorization"] = account_data["api_key"]
        self._session = aiohttp.ClientSession(
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=15),
        )
        self._trade_ids = set()

    async def fetch_me(self):
        url = "https://csgofloat.com/api/v1/me"
        async with self._session.get(
            url=url,
        ) as response:
            data = await response.json()

            return data

    def __del__(self):
        if self._session:
            self._session._connector.close()  # type: ignore
