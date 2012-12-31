import os
import logging
import djcelery

import l10n.locales
import datetime
djcelery.setup_loader()

# Make filepaths relative to settings.                                                                                                                                                          
ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

# Useful settings for running a local instance of batucada.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Include at least one admin who will receive the reports of abuse.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS
ADMIN_PROJECT_CREATE_EMAIL = tuple()


DATABASES = {

    # Uncomment the following lines to run on SQLite for development.
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lernanta.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',  # An empty string means localhost.
        'PORT': ''  # An empty string means the default port.
    },

    # Uncomment the following lines to run with MySQL.
    # Remember to also comment the previous section which enables SQLite.
#    'default': {
#        'NAME': 'lernanta',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'lernanta',
#        'PASSWORD': '',
#        'HOST': '',  # An empty string means localhost.
#        'PORT': '',  # An empty string means the default port.
#        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
#    },

    # Uncomment the following lines to enable integration
    # with the old drupal site.
#    'drupal_db': {
#        'NAME': 'drupal_db',
#        'TEST_NAME': 'drupal_db',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'drupal_db_user',
#        'PASSWORD': '',
#        'HOST': '',  # An empty string means localhost.
#        'PORT': '',  # An empty string means the default port.
#        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
#    },

    # Uncomment the following lines to enable integration
    # with the badges pilot.
#    'badges_db': {
#        'NAME': 'badges_db',
#        'TEST_NAME': 'badges_db',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'badges_db_user',
#        'PASSWORD': '',
#        'HOST': '',  # An empty string means localhost.
#        'PORT': '',  # An empty string means the default port.
#        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
#    },

}

TIME_ZONE = 'America/Toronto'

# Set to True to use https
SESSION_COOKIE_SECURE = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'std3j$ropgs216z1aa#8+p3a2w2q06mns_%2vfx_#$$i!+6o+x'

# Make sure this is unique and random
INTERNAL_API_KEY = 'dmWfPniIMhkPRmiLosOEGmVVppfoyEFhpoIgElfyUpgxtJNCsDcdnFZIeYIUuiom'

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a                                                                                                                  
# trailing slash.                                                                                                                                                                               
# Examples: "http://foo.com/media/", "/media/".                                                                                                                                                 
#ADMIN_MEDIA_PREFIX = '/admin-media/'                                                                                                                                                           

# Absolute path to the directory that holds static files.                                                                                                                                       
# Example: "/home/media/media.lawrence.com/static/"                                                                                                                                             
STATIC_ROOT = path('static_serv')

# URL that handles the static files served from STATIC_ROOT.                                                                                                                                    
# Example: "http://media.lawrence.com/static/"                                                                                                                                                  
STATIC_URL = '/static/'

# Directories containing static files                                                                                                                                                           
STATICFILES_DIRS = (
    path('static'),
)



# List of callables that know how to import templates from various sources.                                                                                                                     
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'lernanta.urls'

TEMPLATE_DIRS = (
    path('templates'),
)


SUPPORTED_LANGUAGES = tuple([(i.lower(), l10n.locales.LOCALES[i].native)
    for i in l10n.locales.LOCALES])

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not                                                                                                                       
# to load the internationalization machinery.                                                                                                                                                   
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and                                                                                                                           
# calendars according to the current locale                                                                                                                                                     
USE_L10N = True

SUPPORTED_NONLOCALES = ('media', 'static', '.well-known', 'pubsub', 'broadcasts',
'ajax', 'api',)


INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    #'south',                                                                                                                                                                                  
    'robots',
    'wellknown',
    'lernanta.apps.pagination',
    'lernanta.apps.users',
    'lernanta.apps.search',
    'lernanta.apps.chat',
    'lernanta.apps.l10n',
    'lernanta.apps.dashboard',
    'lernanta.apps.relationships',
    'lernanta.apps.activity',
    'lernanta.apps.statuses',
    'messages',
    'taggit',
    'lernanta.apps.preferences',
    'lernanta.apps.drumbeatmail',
    'lernanta.apps.links',
    'django_push.subscriber',
    'djcelery',
    'django_openid_auth',
    'ckeditor',
    'lernanta.apps.richtext',
    'lernanta.apps.replies',
    'lernanta.apps.signups',
    'lernanta.apps.content',
    'lernanta.apps.schools',
    'voting',
    'lernanta.apps.news',
    'lernanta.apps.pages',
    'lernanta.apps.projects',
    'lernanta.apps.learn',
    'lernanta.apps.courses',
    'lernanta.apps.content2',
    'lernanta.apps.badges',
    'lernanta.apps.drumbeat',
    'django_obi',
    'lernanta.apps.tags',
    'lernanta.apps.tracker',
    'lernanta.apps.reviews',
    'lernanta.apps.notifications',
    'lernanta.apps.api',
    'tastypie',
    'lernanta.apps.media',
    'social_auth',
    'debug_toolbar',
    'django_nose',
    'django.contrib.admindocs',
)

MIDDLEWARE_CLASSES = (
     'drumbeat.middleware.NotFoundMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    #'api.middleware.APISubdomainMiddleware',                                                                                                                                                   
    'l10n.middleware.LocaleURLRewriter',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    'commonware.middleware.ScrubRequestOnException',
    'commonware.middleware.FrameOptionsHeader',
    'django.middleware.locale.LocaleMiddleware',
    'users.middleware.ProfileExistMiddleware',
    'tracker.middleware.PageViewTrackerMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'drumbeat.context_processors.django_conf',
    'messages.context_processors.inbox',
    'users.context_processors.messages',
    'users.context_processors.redirect_urls',
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)


INTERNAL_IPS = ('127.0.0.1',)

# Sign up for an API key at https://www.google.com/recaptcha/admin/create
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_USE_SSL = True
RECAPTCHA_URL = ('https://api-secure.recaptcha.net/challenge?k=%s' %
                 RECAPTCHA_PUBLIC_KEY)

# Embed.ly
EMBEDLY_KEY = ''
EMBEDLY_CACHE_EXPIRES = datetime.timedelta(weeks=4)

P2PU_EMBEDS= (
    'http://pad.p2pu.org/',
    'http://etherpad.p2pu.org/'
)

# Site shortname to use for disqus
DISQUS_SHORTNAME = ''

# Use dummy caching for development.
CACHE_BACKEND = 'dummy://'
CACHE_PREFIX = 'lernanta'
CACHE_COUNT_TIMEOUT = 60

# RabbitMQ Config
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = ""
BROKER_PASSWORD = ""
BROKER_VHOST = ""

# Execute celery tasks locally, so you don't have to be running an MQ
CELERY_ALWAYS_EAGER = True

# Path to ffmpeg. This will have to be installed to create video thumbnails
FFMPEG_PATH = '/usr/bin/ffmpeg'

# Set to True at production before upgrading lernanta.
# Remember to login as admin before activating maintenance mode.
MAINTENANCE_MODE = False

# Prefixes ignored by the ProfileExistMiddleware.
NO_PROFILE_URLS = ('/media/', '/admin-media/',)

# Drupal urls
DRUPAL_URL = 'http://archive.p2pu.org/'
DRUPAL_FILES_URL = DRUPAL_URL + 'sites/archive.p2pu.org/files/'
FILE_PATH_PREFIX = 'sites/archive.p2pu.org/files/'

# Badges pilot url
BADGE_URL = 'http://badges.p2pu.org/badges/%(badge_id)s/%(badge_tag)s'
BADGE_EVIDENCE_URL = BADGE_URL + '?user_filter=%(username)s#badge_data'
BADGE_IMAGES_DIR = path('media/images/pilotbadges/')
BADGE_IMAGES_URL = 'images/pilotbadges/'

INVALID_USERNAMES = ('webcraft', 'about', 'user', 'sosi', 'get-involved',
    'math-future', 'license', 'contact-us', 'values', 'privacy',
    'terms-of-use', 'news', 'create-draft-course', 'create-draft-course-panel',
    'supporters', 'about-p2pu', 'tag', 'tags','school-of-ed',)

# Pagination
PAGINATION_DEFAULT_ITEMS_PER_PAGE = 20

# Used for open badges integration.
MOZBADGES = {
    # location of badge hub. Currently this is the only public one
    'hub': 'https://beta.openbadges.org',

    # method for getting badges for a user. Called with user object.
    'badge_getter': 'badges.models.get_awarded_badges',
}

# Metrics
STATISTICS_CSV_DOWNLOADERS = ('kfasimpaur',)

# Single Sign On (with multipass tender tokens)
SSO_REDIRECT_FIELD_NAMES = ['to']
SSO_EXTERNAL_REDIRECTS = {
    'http://help.p2pu.org/': {
        'site_key': 'p2pu',
        'api_key': ''
    },
}

# Statsd
STATSD_HOST = 'stats.p2pu.org'
STATSD_PORT = 8125

# Where the default image for sending to Gravatar
DEFAULT_PROFILE_IMAGE = '/static/images/member-missing.png'

# When set to True, if the request URL does not match any
# of the patterns in the URLconf and it doesn't end in a slash,
# an HTTP redirect is issued to the same URL with a slash appended.
APPEND_SLASH = True


# SuperFeedr settings                                                                                                                                                                           
SUPERFEEDR_URL = 'http://superfeedr.com/hubbub'
SUPERFEEDR_USERNAME = ''
SUPERFEEDR_PASSWORD = ''

# django-push settings                                                                                                                                                                          
PUSH_CREDENTIALS = 'links.utils.hub_credentials'
PUSH_HUB = 'http://pubsubhubbub.appspot.com/'
SOUTH_TESTS_MIGRATE = False

FEED_URLS = {
    'splash': 'http://info.p2pu.org/feed/',
}



AUTHENTICATION_BACKENDS = (
    'users.backends.DrupalUserBackend',
    'users.backends.DrupalOpenIDBackend',
    'users.backends.CustomUserBackend',
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
     'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'users.UserProfile'

MAX_IMAGE_SIZE = 1024 * 700
MAX_UPLOAD_SIZE = 1024 * 1024 * 50
MAX_PROJECT_FILES = 6

CACHE_BACKEND = 'caching.backends.memcached://localhost:11211'
CACHE_PREFIX = 'lernanta'
CACHE_COUNT_TIMEOUT = 60

# Ckeditor                                                                                                                                                                                      
CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/"
CKEDITOR_UPLOAD_PATH = path("media/uploads/images")
CKEDITOR_FILE_UPLOAD_PATH = path("media/uploads/files")
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_UPLOAD_EXTENSIONS = [
    '.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'
]
CKEDITOR_FILE_UPLOAD_EXTENSIONS = CKEDITOR_IMAGE_UPLOAD_EXTENSIONS + ['.pdf',
    '.doc', '.rtf', '.txt', '.xls', '.csv', '.mov', '.wmv', '.mpeg', '.mpg',
    '.avi', '.rm', '.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']

BOT_NAMES =['Googlebot', 'Slurp', 'Twiceler', 'msnbot',
    'KaloogaBot', 'YodaoBot', 'Baiduspider', 'googlebot',
    'Speedy Spider', 'DotBot', 'Sogou']

TRACKING_PREFIXES = [
    r'^/\w{2}/groups/[\w-]+/content/[\w-]+/$',
    r'^/\w{2}/groups/[\w-]+/$',
    r'^/\w{2}/schools/[\w-]+/sets/[\w-]+/$',
    r'^/\w{2}/schools/[\w-]+/$',
]


# social-auth-keys
# please generate key and add 
TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''


#social-auth-links
LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'
