# encoding=utf-8

settings = {
    "debug": True,
    'template_path': 'templates',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
    'cookie_secret': 'suoning',      # cookie自定义字符串加盐
    # 'xsrf_cookies': True,          # 防止跨站伪造
    # 'ui_methods': mt,              # 自定义UIMethod函数
    # 'ui_modules': md,
}

config = {}

weather_api = "http://www.sojson.com/open/api/weather/json.shtml"
qqmusic_api = "http://www.sojson.com/api/qqmusic/"
