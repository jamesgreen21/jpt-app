from django.apps import AppConfig


class HealthBlogConfig(AppConfig):
    name = 'health_blog'

    def ready(self):
        import health_blog.signals
