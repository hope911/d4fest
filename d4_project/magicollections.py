
# -*- coding: utf-8 -*-
import math, simplejson, random
from itertools import chain
from collections import OrderedDict
from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _, string_concat, get_language
from django.utils.formats import date_format
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Prefetch, Q
from django.db.models.fields import BLANK_CHOICE_DASH
from magi.magicollections import (
    MainItemCollection,
    AccountCollection as _AccountCollection,
    ActivityCollection as _ActivityCollection,
    BadgeCollection as _BadgeCollection,
    DonateCollection as _DonateCollection,
    UserCollection as _UserCollection,
    StaffConfigurationCollection as _StaffConfigurationCollection,
    PrizeCollection as _PrizeCollection,
)
from magi.utils import (
    setSubField,
    CuteFormType,
    CuteFormTransform,
    torfc2822,
    custom_item_template,
    staticImageURL,
    justReturn,
    toCountDown,
    translationURL,
    AttrDict,
    mergedFieldCuteForm,
    tourldash,
    getCharacterImageFromPk,
)
from magi.default_settings import RAW_CONTEXT
from magi.item_model import i_choices
from magi.models import Activity, Notification
from magi.forms import get_account_simple_form
from d4.constants import LIVE2D_JS_FILES
from magi import settings
from d4.utils import (
    rarity_to_stars_images,
    generateDifficulty,
    add_rerun_buttons,
    add_rerun_fields,
    subtitledImageLink,
    djGroupField,
)
from d4 import models, forms
