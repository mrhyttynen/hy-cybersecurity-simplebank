from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'insecurebank.pages'
    def ready(self):
        import insecurebank.pages.signals
