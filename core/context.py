from sqlalchemy.orm import Session
from telegram import Update
from telegram.ext import CallbackContext, Dispatcher
from core.models import User


class CoreContext(CallbackContext):
    def __init__(self, dispatcher: Dispatcher):
        super(CoreContext, self).__init__(dispatcher)
        self._session = None
        self._user = None

    @property
    def session(self) -> Session:
        return self._session

    @session.setter
    def session(self, sesion) -> None:
        assert isinstance(sesion, Session)
        self._session = sesion

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, user) -> None:
        assert isinstance(user, User)
        self._user = user

    @classmethod
    def from_data(cls, update: Update, context: CallbackContext,
                  session: Session, user: User):
        self = cls(context.dispatcher)
        self._session = session
        self._user = user

        if update is not None and isinstance(update, Update):
            chat = update.effective_chat
            user = update.effective_user

            if chat:
                self._chat_data = context.dispatcher.chat_data[chat.id]
            if user:
                self._user_data = context.dispatcher.user_data[user.id]
        return self
