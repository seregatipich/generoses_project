from asyncio import run
from logging import INFO, basicConfig
from sys import stdout

from bot import bot, dp
from handlers import categories, sub_categories, welcome


async def main() -> None:
    dp.include_routers(categories.rt, sub_categories.rt, welcome.rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    basicConfig(
        level=INFO,
        stream=stdout
    )
    run(main())
