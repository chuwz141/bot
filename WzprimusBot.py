import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# Hàm xử lý tin nhắn
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    if "https://drive.google.com/file/d/" in user_message:
        try:
            file_id = user_message.split('/d/')[1].split('/view')[0]
            api_link = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key=AIzaSyDBCQLrdiYRF4JDhwEV78rHUsbORSUSeks"
            await update.message.reply_text(api_link)
        except Exception as e:
            await update.message.reply_text("Đã xảy ra lỗi khi xử lý link Google Drive.")
    else:
        await update.message.reply_text("Vui lòng gửi một link Google Drive hợp lệ.")

# Hàm khởi tạo bot
async def main():
    TOKEN = "7518073972:AAGc6z6CguEixJDLOgE5jqUKvPAzClBJVos"
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await application.run_polling()

if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
