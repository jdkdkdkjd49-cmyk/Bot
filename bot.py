import logging
import os
import random
from typing import Dict, List

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

GACHI_EMOTIONS: Dict[str, List[str]] = {
    "hype": [
        "♂️ LET'S GOOOO, BROTHER! ♂️",
        "🔥 WOO! DUNGEON MASTER MODE ACTIVATED!",
        "💪 FULL POWER GACHI ENERGY!",
    ],
    "sad": [
        "😔 Today is not gym day, brother...",
        "💔 No reps, no glory... but tomorrow we rise.",
        "🥀 Even legends miss a set sometimes.",
    ],
    "rage": [
        "😡 WHO TOOK MY PROTEIN?!",
        "⚡ TOO MUCH MADNESS, NEED MORE BENCH PRESS!",
        "🔥 RAGE MODE: TURN THE MUSIC LOUDER!",
    ],
    "chill": [
        "😌 Easy day, smooth reps, calm mind.",
        "🌙 Brotherhood and peace. Keep it steady.",
        "🧘 Deep breath, bro. Form over ego.",
    ],
}

KEYWORDS = {
    "радость": "hype",
    "грусть": "sad",
    "злость": "rage",
    "спокойствие": "chill",
    "hype": "hype",
    "sad": "sad",
    "rage": "rage",
    "chill": "chill",
}


def random_emotion(category: str | None = None) -> str:
    if category and category in GACHI_EMOTIONS:
        return random.choice(GACHI_EMOTIONS[category])

    all_phrases = [phrase for values in GACHI_EMOTIONS.values() for phrase in values]
    return random.choice(all_phrases)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "Привет, брат. Я бот для гачи эмоций 💪\n\n"
        "Команды:\n"
        "/emotion — случайная гачи эмоция\n"
        "/emotion <hype|sad|rage|chill> — эмоция по категории\n"
        "/help — помощь"
    )
    await update.message.reply_text(message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Напиши /emotion или укажи категорию: hype, sad, rage, chill.\n"
        "Также можно отправить слова: радость, грусть, злость, спокойствие."
    )


async def emotion(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    category = context.args[0].lower() if context.args else None
    await update.message.reply_text(random_emotion(category))


async def text_router(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower().strip()
    category = KEYWORDS.get(text)

    if category:
        await update.message.reply_text(random_emotion(category))
        return

    await update.message.reply_text(
        "Я пока понимаю только эмоции. Попробуй /emotion или /help."
    )


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Set BOT_TOKEN environment variable before running the bot")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("emotion", emotion))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_router))

    logger.info("Gachi emotions bot is running")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
