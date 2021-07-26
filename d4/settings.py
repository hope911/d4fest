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
# Homepage

DONATORS_GOAL = 950

HOMEPAGE_BACKGROUND = 'bg_pattern.png'
HOMEPAGE_ART_GRADIENT = True

HOMEPAGE_ARTS = [{
    'url': 'default_art.png',
}]

HOMEPAGE_ART_SIDE = 'left'
HOMEPAGE_ART_POSITION = {
    'position': 'center right',
    'size': '150%',
    'y': '30%',
    'x': '100%',
}

USERS_BIRTHDAYS_BANNER = 'happy_birthday.png'

GET_BACKGROUNDS = getBackgrounds
GET_HOMEPAGE_ARTS = getHomepageArts
RANDOM_ART_FOR_CHARACTER = randomArtForCharacter

HOME_ACTIVITY_TABS = DEFAULT_HOME_ACTIVITY_TABS.copy()
if 'staffpicks' in HOME_ACTIVITY_TABS:
    del(HOME_ACTIVITY_TABS['staffpicks'])
HOME_ACTIVITY_TABS['top_this_week'] = {
    'title': _('TOP'),
    'icon': 'trophy',
    'form_fields': {
        'ordering': '_cache_total_likes,id',
    },
}

############################################################
# First steps

FIRST_COLLECTION = 'collectiblecard'
GET_STARTED_VIDEO = 'TqL9nSNouhw'

############################################################
# Activities

ACTIVITY_TAGS = [
    # D4DJ!
    ('anime', lambda: u'{} / {} / {}'.format(
        _('Anime'),
        _('Manga'),
        _('Movie'),
    )),
    ('members', _('Characters')),
    # Groovy Mix
    ('cards', _('Cards')),
    ('scout', _('Scouting')),
    ('event', _('Events')),
    ('live', _('Songs')),
    # Generic
    ('birthday', _('Birthday')),

    # Restricted
    ('communityevent', {
        'translation': _('Community event'),
        'has_permission_to_add': lambda r: r.user.hasPermission('post_community_event_activities'),
    }),

] + DEFAULT_ACTIVITY_TAGS
###########################################################
# User preferences and profiles

CUSTOM_PREFERENCES_FORM = True

EXTRA_PREFERENCES = DEFAULT_EXTRA_PREFERENCES + [
    ('i_favorite_unit', lambda: _('Favorite {thing}').format(thing=_('Unit').lower())),
]

FAVORITE_CHARACTERS_MODEL = models.Member

USER_COLORS = [
    ('street', _('Street'), 'Street', '#FF2D54'),
    ('cool', _('Cool'), 'Cool', '#4057E3'),
    ('elegant', _('Elegant'), 'Elegant', '#44C527'),
    ('party', _('Party'), 'Party', '#FF8400'),
]

ACCOUNT_TAB_ORDERING = ['about', 'collectiblecard', 'eventparticipation', 'playedsong', 'item', 'clubitem']


############################################################
# Technacal settings

SITE_NAME = 'D4 Fest'
SITE_URL = 'http://sample.com/'
SITE_IMAGE = 'sample.png'
DISQUS_SHORTNAME = 'sample'
SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.sample.com/'

ACCOUNT_MODEL = models.Account

############################################################
# Customize pages

ENABLED_PAGES = DEFAULT_ENABLED_PAGES

ENABLED_PAGES['wiki'][0]['enabled'] = True
ENABLED_PAGES['wiki'][1]['enabled'] = True
ENABLED_PAGES['wiki'][0]['divider_before'] = True
ENABLED_PAGES['wiki'][0]['navbar_link_list'] = 'girlsbandparty'

ENABLED_PAGES['map']['share_image'] = 'screenshots/map.png'
ENABLED_PAGES['map']['navbar_link_list'] = 'community'

ENABLED_PAGES['settings']['custom'] = True

ENABLED_PAGES['teambuilder'] = {
    'title': _('Team builder'),
    'icon': 'settings',
    'navbar_link': False,
    'authentication_required': True,
    'as_sidebar': True,
    'show_title': True,
    #'navbar_link_list': 'groovymix',
}

ENABLED_PAGES['gallery'] = {
    'title': _('Gallery'),
    'icon': 'pictures',
    'navbar_link_list': 'girlsbandparty',
    'page_description': lambda: u'{} - {}'.format(_('Gallery of {license} images').format(
        license=unicode(GAME_NAME)), u', '.join(
            [unicode(_d['translation']) for _d in models.Asset.TYPES.values()])),
}

ENABLED_PAGES['officialart'] = {
    'title': lambda _c: _('{things} list').format(things=_('Official art')),
    'icon': 'pictures',
    'navbar_link_list': 'bangdream',
    'redirect': '/assets/officialart/',
    'divider_before': True,
}


############################################################
# Customize nav bar

ENABLED_NAVBAR_LISTS = DEFAULT_ENABLED_NAVBAR_LISTS
ENABLED_NAVBAR_LISTS['d4dj'] = {
    'title': _('D4DJ'),
    #'image': 'D4DJ',
    'order': ['member_list', 'song_list', 'officialart'],
}
ENABLED_NAVBAR_LISTS['Groovy Mix'] = {
    'title': _('Groovy Mix'),
    #'image': 'GroovyMix',
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

############################################################
# Groups

GROUPS = DEFAULT_GROUPS

_HDESIGN = dict(GROUPS)['design'].copy()
_HDESIGN.update({
    'translation': string_concat(_('Graphic designer'), ' - ', _('Manager')),
    'requires_staff': True,
    'permissions': [
        'access_site_before_launch',
        'beta_test_features',
        'upload_custom_2x',
        'upload_custom_thumbnails',
    ],
})
GROUPS.append(('hdesign', _HDESIGN))
© 2021 GitHub, Inc.
