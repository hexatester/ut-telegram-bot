from logging import getLogger
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from moodle.mod.forum import BaseForum

from core import CoreContext
from core.decorator import assert_token
from core.session import message_wrapper
from config import CALLBACK_SEPARATOR
from libs.elearning.forum import forum_text
from libs.utils.helpers import build_menu, make_data

logger = getLogger(__name__)


@message_wrapper
@assert_token
def forum(update: Update, context: CoreContext):
    datas = context.query.data.split(CALLBACK_SEPARATOR)
    # FORUM|course_id|forum_id
    course_id = int(datas[1])
    base_forum = BaseForum(context.moodle)
    forums = base_forum.get_forums_by_courses([course_id])
    context.query.answer()
    if not forums:
        context.query.edit_message_text("Forum tidak ditemukan.")
        return -1
    forum_id = int(datas[2])
    for fo in forums:
        if fo.id == forum_id:
            base_forum.view_forum(fo.id)
            break
    buttons = list()
    if fo.numdiscussions and fo.numdiscussions > 0:
        data = make_data("DISCUSSIONS", course_id, forum_id, 1)
        button = InlineKeyboardButton("Diskusi", callback_data=data)
        buttons.append(button)
    text = forum_text(fo)
    header = InlineKeyboardButton(
        fo.name, url=f"https://elearning.ut.ac.id/mod/forum/view.php?id={fo.cmid}"
    )
    back_data = make_data("COURSE", course_id)
    footer = [
        InlineKeyboardButton("< Kembali", callback_data=back_data),
        InlineKeyboardButton("Tutup ❌", callback_data="CLOSE"),
    ]
    keyboard = build_menu(
        buttons,
        header_buttons=header,
        footer_buttons=footer,
    )

    context.query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    return -1


forum_pattern = r"^FORUM\|\d+\|\d+$"
