from telegram import Update, Message
from config import TOKEN, SQLALCHEMY_DATABASE_URI
from core.context import CoreContext
from core.session import message_wrapper

MESSAGE = """Selamat datang admin!
/admin ban userid untuk banned user
/admin status untuk menampilkan status
"""


@message_wrapper
def admin(update: Update, context: CoreContext):
    user = context.user
    args = context.args
    message: Message = update.message
    if not user.admin:
        if args and args[0] == TOKEN:
            user.admin = True
            context.session.commit()
            message.reply_text('Selamat datang admin!')
        return
    if 'status' in args:
        message.reply_text(f'DB {SQLALCHEMY_DATABASE_URI} ONLINE')
