import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler
from ..data import data
from .. import main


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )
    
async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# async def chuck()

if __name__ == '__main__':
    application = ApplicationBuilder().token(data.TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    # chuck_handler = CommandHandler('chuck', chuck)
    # application.add_handler(chuck_handler)
    
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)

    application.run_polling()

