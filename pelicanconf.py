AUTHOR = 'Jerry Chi'
SITENAME = "Jerry Chi's website"
SITESUBTITLE = "Jerry Chi<BR>Data Scientist in Tokyo<BR>(site is under construction)"
SITEURL = "http://127.0.0.1:8000"
SITELOGO = SITEURL + "/images/profilepic.jpg"


PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

# Blogroll
#LINKS = (('Site created by Pelican', 'https://getpelican.com/'),
#        )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/peacej'),
          ('medium', 'https://peacej2.medium.com/'),
          ('linkedin','https://www.linkedin.com/in/jerrychi/'),
          ('github', 'https://github.com/peacej'),
          ('envelope', 'mailto:jerrychi123@gmail.com'),
          ('rss', '//jerrychi.com/feeds/all.atom.xml')
          )

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = False

THEME="/Users/jchi/pelican-themes/Flex"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = False

USE_LESS = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True