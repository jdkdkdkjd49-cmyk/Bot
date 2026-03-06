# Telegram bot для гачи эмоций

Простой Telegram-бот, который отправляет случайные гачи-эмоции по команде или ключевому слову.

## Возможности
- `/start` — приветствие и краткая инструкция.
- `/emotion` — случайная гачи-эмоция.
- `/emotion <hype|sad|rage|chill>` — эмоция из выбранной категории.
- Текстовые триггеры: `радость`, `грусть`, `злость`, `спокойствие`.

## Запуск
1. Создайте бота через `@BotFather` и получите токен.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите бота:
   ```bash
   BOT_TOKEN=<your_token> python bot.py
   ```

## Пример
- `/emotion hype` → `♂️ LET'S GOOOO, BROTHER! ♂️`
- `грусть` → `😔 Today is not gym day, brother...`
