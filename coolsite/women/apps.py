from django.apps import AppConfig
#А оно для настройки текущего приложения

class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
