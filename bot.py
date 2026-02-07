from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

scores = {}

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg:
        return

    # +1 по реплаю
    if msg.text == "+1" and msg.reply_to_message:
        user = msg.reply_to_message.from_user.id
        scores[user] = scores.get(user, 0) + 1
        await msg.reply_text("✅ +1")

    # показать счёт
    if msg.text == "/score":
        if not scores:
            await msg.reply_text("Пока пусто")
            return
        text = "\n".join([f"{uid}: {v}" for uid, v in scores.items()])
        await msg.reply_text(text)

app = ApplicationBuilder().token("8454992550:AAFjjSrIKp9k6f3iQOfDPS2IAxrp7HtfPZo").build()
app.add_handler(MessageHandler(filters.TEXT, handler))
app.run_polling()
