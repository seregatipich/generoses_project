from asyncio import run
from logging import INFO, basicConfig
from sys import stdout

from handlers import categories, sub_categories, welcome
from utils.bot import bot, dp


async def main() -> None:
    """
    The main coroutine for the Telegram bot.

    This coroutine is responsible for including routers for different categories of the bot and 
    starting the bot's polling process. It includes routers for categories, sub-categories, and a 
    welcome message, then starts polling for updates from Telegram.

    The function relies on globally defined 'dp' (Dispatcher) and 'bot' instances, as well as routers 
    defined in 'categories', 'sub_categories', and 'welcome' modules.

    Note:
        - This coroutine should be the entry point for running the bot.
        - Ensure that 'dp' and 'bot' are properly initialized before calling this function.
        - Routers for categories, sub-categories, and welcome messages must be defined in their 
          respective modules.
    """
    dp.include_routers(categories.rt, sub_categories.rt, welcome.rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    basicConfig(
        level=INFO,
        stream=stdout
    )
    run(main())
