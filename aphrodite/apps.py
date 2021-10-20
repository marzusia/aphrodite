from django.apps import AppConfig


class AphroditeConfig(AppConfig):
    name = 'aphrodite'
    verbose_name = 'Aphrodite University'

    def ready(self):
        from . import signals
