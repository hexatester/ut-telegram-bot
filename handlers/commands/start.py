from sqlalchemy.orm import Session
from telegram import Update
from telegram.ext import CallbackContext
from core.session import message_wrapper
from core.models import User


@message_wrapper
def start(update: Update,
          context: CallbackContext,
          session: Session,
          user: User = None):
    if user and not user.started:
        user.started = True
        session.commit()
    update.effective_message.reply_text(
        f'Selamat datang {user.full_name}\n\n'
        'Daftar Perintah\n'
        '/start - Memulai bot\n'
        '/baca - Baca buku\n'
        '/buku - Cari buku\n'
        '/tiket - Mengecek tiket <a href="http://hallo-ut.ut.ac.id/">hallo-ut</a>\n'  # NOQA
        '/shortlink - Memendekan url dengan <a href="https://sl.ut.ac.id/">sl-ut</a>\n'  # NOQA
        '/link - Daftar link UT\n'
        '/formulir - Daftar Formulir\n'
        '/about - Tentang bot ini\n')
