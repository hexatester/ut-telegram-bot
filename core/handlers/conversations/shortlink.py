from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler, Filters, CommandHandler, MessageHandler
from libs import shorten_link

COMMAND = 'shortlink'

CREATE = range(1)


def valid_link(link: str = ''):
    return link and (link.startswith('https://') or link.startswith('http://')) and ' ' not in link


def short(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        '''
        Kirimkan link yang akan dipendekkan...
        Disertai dengan https://... atau http://
        /cancel untuk membatalkan perintah
        '''
    )
    return CREATE


def create(update: Update, context: CallbackContext):
    link: str = update.effective_message.text
    if link and not valid_link(link):
        update.effective_message.reply_text('Link tidak valid. :<')
    else:
        new_link = shorten_link(link)
        if new_link:
            update.effective_message.reply_text(
                f'''Sukses memendekan link <code>{link}</code> ,
                menjadi {new_link}'''
            )
        else:
            update.effective_message.reply_text('Gagal memendekkan link')
    return -1


def cancel(update: Update, context: CallbackContext):
    update.effective_message.reply_text(f'/{COMMAND} telah dibatalkan')


SHORTLINK = {
    'entry_points': [CommandHandler(COMMAND, short)],
    'states': {
        CREATE: [MessageHandler]
    },
    'fallbacks': [CommandHandler('cancel', cancel)]
}