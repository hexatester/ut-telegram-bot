from typing import List
from logging import Logger
from telegram.ext import Dispatcher, CommandHandler, Filters

# Commands
from .admin import admin
from .registrasi import registrasi
from .link import link
from .formulir import formulir
from .donasi import donasi
from .elearning import elearning
from .courses import courses
from .eula import eula
from .about import about
from .cancel import cancel
from .inline_help import inline_help
from .reset import reset
from .reset_token import reset_token
from .start_elearning import start_elearning
from .start import start

private_filter = Filters.private


class CommandMixin(object):
    logger: Logger = None
    COMMANDS_GROUP: int = 0
    COMMANDS: List[CommandHandler] = [
        CommandHandler("admin", admin, private_filter),
        CommandHandler("link", link, private_filter),
        CommandHandler("formulir", formulir, private_filter),
        CommandHandler("registrasi", registrasi, private_filter),
        CommandHandler("about", about, private_filter),
        CommandHandler("elearning", elearning, private_filter),
        CommandHandler("kursus", courses, private_filter),
        CommandHandler("eula", eula, private_filter),
        CommandHandler("reset", reset, private_filter),
        CommandHandler("reset_token", reset_token, private_filter),
        CommandHandler("donasi", donasi, private_filter),
        CommandHandler("cancel", cancel, private_filter),
        CommandHandler(
            "start",
            start_elearning,
            filters=Filters.private & Filters.regex(r"^\/start TOKEN-[a-z0-9]{32}$"),
        ),
        CommandHandler("start", inline_help, Filters.regex(r"^/start inline-help$")),
        CommandHandler("start", start, private_filter),
    ]

    def register_commands(self, dispatcher: Dispatcher):
        try:
            if self.COMMANDS:
                for conversation in self.COMMANDS:
                    dispatcher.add_handler(conversation, group=self.COMMANDS_GROUP)
                self.logger.info("Commands added!")
            return True
        except Exception as e:
            self.logger.exception(e)
            return False
