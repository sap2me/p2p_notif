import asyncio
import time

import aiohttp

from settings import settings
from utils import cny_to_usd

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Referer": "https://buff.163.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


class Buff:
    def __init__(self, username, account_data, telegram):
        self.telegram = telegram
        self._username = username
        self._account_data = account_data
        self._session = aiohttp.ClientSession(
            headers=headers,
            cookies=self._account_data["cookies"],
            timeout=aiohttp.ClientTimeout(total=15),
        )

    async def fetch_notifications(self):
        url = f"https://buff.163.com/api/message/notification"
        timestamp = int(time.time())
        params = {
            "_": timestamp,
        }
        async with self._session.get(url, params=params) as response:
            raw_data = await response.json()
            code = raw_data.get("code")
            if code != "OK":
                raise ValueError(f"Code is: {code}")
            data = raw_data["data"]
            to_deliver_order = data["to_deliver_order"].get("csgo", 0)
            to_handle_bargain = data["to_handle_bargain"].get("csgo", 0)
            to_send_offer_order = data["to_send_offer_order"].get("csgo", 0)

            return {
                "deliver_order": to_deliver_order,
                "handle_bargain": to_handle_bargain,
                "send_order": to_send_offer_order,
            }

    async def fetch_items_to_deliver(self):
        url = f"https://buff.163.com/api/market/sell_order/to_deliver"
        params = {
            "game": "csgo",
        }
        async with self._session.get(url, params=params) as response:
            raw_data = await response.json()
            code = raw_data.get("code")
            if code != "OK":
                raise ValueError(f"Code is: {code}")
            data = raw_data["data"]
            items = data["items"]
            for item in items:
                try:
                    await self.send_item(data, item, "sell")

                except Exception as error:
                    print(repr(error))

    async def fetch_items_bargain(self):
        url = f"https://buff.163.com/api/market/sell_order/received_bargain"
        params = {
            "game": "csgo",
        }
        async with self._session.get(url, params=params) as response:
            raw_data = await response.json()
            code = raw_data.get("code")
            if code != "OK":
                raise ValueError(f"Code is: {code}")
            data = raw_data["data"]
            items = data["items"]
            for item in items:
                try:
                    await self.send_item(data, item, "bargain")

                except Exception as error:
                    print(repr(error))

    async def send_item(self, data, item, mode):
        goods_id = item["goods_id"]
        good = data["goods_infos"][str(goods_id)]
        hash_name = good["market_hash_name"]
        price_cny = float(item["price"])
        price_usd = cny_to_usd(price_cny)

        asset_info = item["asset_info"]
        asset_id = asset_info["assetid"]
        float_value = str(asset_info["paintwear"])[:8]
        _stickers = asset_info["info"]["stickers"]
        stickers = [stick["name"] for stick in _stickers]

        bargains = item.get("bargains", [])
        screenshot_url = f"https://s.csgofloat.com/{asset_id}-front.png"
        async with self._session.get(screenshot_url) as response:
            if response.status != 200:
                has_screenshot = False
            else:
                has_screenshot = True

        if mode == "bargain":
            top_str = "New bargain for item listed for"
        else:
            top_str = "Listing has been purchased for"

        msg = (
            f"<b>BUFF163</b> {mode.upper()} [{self._username}] - {top_str} <b>{price_usd}</b> $ ({price_cny} CNY)\n"
            f"- hash_name:\n"
            f"      <code>{hash_name}</code>\n"
            f"- float:\n"
            f"      <code>{float_value}</code>\n"
        )
        if stickers:
            msg += f"- stickers:\n"
            for sticker in stickers:
                msg += f"      <code>{sticker}</code>\n"

        if bargains:
            msg += f"\nBARGAINS:\n"
        for ind, bargain in enumerate(bargains):
            bargain_price_cny = float(bargain["price"])
            bargain_price_usd = cny_to_usd(bargain_price_cny)
            bargain_msg = bargain.get("buyer_message", "")
            msg += f"      {ind + 1})<b>{price_usd}</b> $ ({price_cny} CNY) message: {bargain_msg}"

        if has_screenshot:
            await self.telegram.send_photo(screenshot_url, msg)  # type: ignore
        else:
            await self.telegram.send_message(msg)

    async def start_waiting(self):
        deliver_order = 0
        handle_bargain = 0
        send_order = 0

        while True:
            # print("buff loop...")
            try:
                data = await self.fetch_notifications()
                if data["deliver_order"] > deliver_order:
                    msg = f"<b>BUFF163</b> [{self._username}] - New delivery order/s"
                    await self.telegram.send_message(msg)
                    await self.fetch_items_to_deliver()

                if data["handle_bargain"] > handle_bargain:
                    msg = f"<b>BUFF163</b> [{self._username}] - New bargain/s"
                    await self.telegram.send_message(msg)

                if data["send_order"] > send_order:
                    msg = f"<b>BUFF163</b> [{self._username}] - New send order/s"
                    await self.telegram.send_message(msg)

                deliver_order = data["deliver_order"]
                handle_bargain = data["handle_bargain"]
                send_order = data["send_order"]

            except Exception as error:
                print(repr(error))

            await asyncio.sleep(settings.BUFF_CHECK_INTERVAL)

    def get_msg_template(self):
        msg = f"<b>BUFF163</b> [{self._username}] - New delivery order/s"

    def __del__(self):
        if self._session:
            self._session._connector.close()  # type: ignore
