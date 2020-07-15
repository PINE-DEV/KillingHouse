DEFAULT_LANG = 'en'

TEXTS = {
    'start.explanation':{
        'en': "Welcome to the KillerHouse Bot. This bot was created to aid when playing \"Killer House\"",
        'es': "Bienvenido al Bot KillerHouse. Este bot ha sido creado como ayuda para jugar a \"Killer House\"",
        'gl': "__Welcome to the KillerHouse Bot. This bot was created to aid when playing \"Killer House\""
    },
    'target.info': {
        'en': "Target: *{}*\n Weapon: *{}* \n Location: *{}*",
        'es': "Objetivo: *{}*\n Arma: *{}* \n Lugar: *{}*",
        'gl': "__Target: *{}*\n __Weapon: *{}* \n __Location: *{}*"
    },
    'dead.who_was_it': {
        'en': "Who was your killer/snitch?",
        'es': "Quién fue tu asesino/soplón?",
        'gl': "__Who was your killer/snitch?"
    }
}

def get_text(string_id, lang):
    """I don't know how I will end up implementing i18n yet, so I created this function to serve as a wrapper.
    For now, it reads from a dictionary"""
    try:
        i18ntext = TEXTS[string_id][lang]
    except IndexError:
        try:
            i18ntext = TEXTS[string_id][DEFAULT_LANG]
        except IndexError:
            # Maybe return en as default, and only if it does not exist, return this fallback
            return '__{0}.{1}'.format(string_id, lang)

    return i18ntext
