from sqlalchemy.orm import Session
from telegram.ext import CallbackContext, Dispatcher
from core.models import User


class CoreContext(CallbackContext):
    def __init__(self, dispatcher: Dispatcher, session: Session, user: User):
        super(CoreContext, self).__init__(dispatcher)
        self._session = session
        self._user = user

    @property
    def session(self) -> Session:
        return self._session

    @property
    def user(self) -> User:
        return self._user
