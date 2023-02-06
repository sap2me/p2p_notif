import asyncio

import click

from accounts import accounts
from buff import Buff
from csgofloat import CSGOFloat
from settings import settings
from telegram import Telegram

cli = click.Group()


@cli.command()
def serve():
    asyncio.run(_serve())


async def _serve():
    telegram = Telegram(
        token=settings.TELEGRAM_BOT_TOKEN,
        chat_id=settings.TELEGRAM_CHAT_ID,
    )

    users = {}
    tasks = []
    for username, account in accounts.items():
        acc_float = account["csgofloat"]
        csgofloat = CSGOFloat(acc_float)
        users[username] = csgofloat

        buff = Buff(username, account["buff"], telegram)
        tasks.append(asyncio.create_task(buff.start_waiting()))

    while True:
        # print("csgofloat loop...")
        try:
            await wait_market(users, telegram)

        except Exception as error:
            print(repr(error))

        await asyncio.sleep(settings.CSGO_FLOAT_CHECK_INTERVAL)


async def wait_market(users, telegram):
    for username, csgofloat in users.items():
        data = await csgofloat.fetch_me()
        trades = data["trades_to_send"]
        if not trades:
            continue

        for trade in trades:
            await check_trade(telegram, username, csgofloat, trade)


async def check_trade(telegram, username, csgofloat, trade):
    id = trade["id"]

    if id in csgofloat._trade_ids:
        return False

    csgofloat._trade_ids.add(id)

    contract = trade["contract"]
    price_usd = round(contract["price"] / 100, 2)
    item = contract["item"]
    asset_id = item["asset_id"]
    float_value = str(item["float_value"])[:8]
    market_hash_name = item["market_hash_name"]
    stickers = [stick["name"] for stick in item["stickers"]]
    has_screenshot = item["has_screenshot"]
    if has_screenshot:
        screenshot_url = f"https://s.csgofloat.com/{asset_id}-front.png"

    msg = (
        f"<b>CSGOFLOAT</b> [{username}] - Listing has been purchased for <b>{price_usd}</b> $\n"
        f"- hash_name:\n"
        f"      <code>{market_hash_name}</code>\n"
        f"- float:\n"
        f"      <code>{float_value}</code>\n"
    )
    if stickers:
        msg += f"- stickers:\n"
        for sticker in stickers:
            msg += f"      <code>{sticker}</code>\n"

    if has_screenshot:
        await telegram.send_photo(screenshot_url, msg)  # type: ignore
    else:
        await telegram.send_message(msg)


if __name__ == "__main__":
    cli()
