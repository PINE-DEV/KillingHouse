from telegram.ext import Updater, CommandHandler
import i18n

def start(update, context):
    from_user = update.message.from_user
    lang = from_user.language_code
    reply_text = i18n.get_text('start.explanation', lang)
    update.message.reply_text(reply_text, parse_mode='MarkdownV2')

def target(update, context):
    from_user = update.message.from_user
    lang = from_user.language_code
    target_name = 'Mister Jägger'
    weapon_name = 'Batuta'
    place_name = 'Hoguera'
    reply_text = i18n.get_text('target.info', lang).format(target_name, weapon_name, place_name)

    update.message.reply_text(reply_text, parse_mode='MarkdownV2')

def dead(update, context):
    from_user = update.message.from_user
    lang = from_user.language_code
    reply_text = i18n.get_text('dead.who_was_it', lang)
    update.message.reply_text(reply_text, parse_mode='MarkdownV2')

token = '675642506:AAHl_C8dtRpkFOxZuFsiKauvVwii_rsiSBU'
updater = Updater(token, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('target', target))
updater.dispatcher.add_handler(CommandHandler('dead', dead))
updater.start_polling()
updater.idle()
