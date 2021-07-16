from django.conf import settings as django_settings
from magi.default_settings import DEFAULT_ENABLED_COLLECTIONS, DEFAULT_ENABLED_PAGES
from sample import models, forms

from magi.default_settings import (
    DEFAULT_ACTIVITY_TAGS,
    DEFAULT_ENABLED_NAVBAR_LISTS,
    DEFAULT_ENABLED_PAGES,
    DEFAULT_NAVBAR_ORDERING,
    DEFAULT_JAVASCRIPT_TRANSLATED_TERMS,
    DEFAULT_GLOBAL_OUTSIDE_PERMISSIONS,
    DEFAULT_LANGUAGES_CANT_SPEAK_ENGLISH,
    DEFAULT_EXTRA_PREFERENCES,
    DEFAULT_HOME_ACTIVITY_TABS,
    DEFAULT_SEASONS,
    DEFAULT_GROUPS,
)

from magi.utils import tourldash
from bang.utils import (
    bangGlobalContext,
    randomArtForCharacter,
    getBackgrounds,
    getHomepageArts,
)

############################################################
# License, game and site settings

GAME_NAME = string_concat(_('D4DJ'), ' ', _('Groovy Mix'))
GAME_URL = 'https://d4dj.bushimo.jp/'

COLOR = '#1a1543'
SECONDARY COLOR = '#bf3055'

############################################################
# Images

SITE_NAV_LOGO = 'disk.png'

############################################################
# Technacal settings

SITE_NAME = 'D4 Fest'
SITE_URL = 'http://sample.com/'
SITE_IMAGE = 'sample.png'
DISQUS_SHORTNAME = 'sample'
SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.sample.com/'

ACCOUNT_MODEL = models.Account

############################################################
# Customize nav bar

ENABLED_NAVBAR_LISTS = DEFAULT_ENABLED_NAVBAR_LISTS
ENABLED_NAVBAR_LISTS['d4dj'] = {
    'title': _('D4DJ'),
    #'image': 'BanGDream',
    'order': ['member_list', 'song_list', 'officialart', 'comics'],
}
ENABLED_NAVBAR_LISTS['Groovy Mix'] = {
    'title': _('Groovy Mix'),
    #'image': 'GirlsBandParty',
    'order': [
        'card_list', 'cards_quickadd', 'costume_list',
        'event_list', 'gacha_list',
        'item_list', 'area_list',
        'wiki', 'gallery', 'teambuilder',
    ],
}
ENABLED_NAVBAR_LISTS['community'] = {
    'title': _('Community'),
    'icon': 'users',
    'order': ['activity_list', 'account_list', 'map', 'donate_list', 'discord', 'twitter', 'instagram'],
}
ENABLED_NAVBAR_LISTS['more']['order'] = ENABLED_NAVBAR_LISTS['more']['order'] + ['donate']

NAVBAR_ORDERING = ['card_list', 'member_list', 'song_list', 'events', 'community'] + DEFAULT_NAVBAR_ORDERING

