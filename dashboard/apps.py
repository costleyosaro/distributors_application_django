from django.apps import AppConfig
class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'  # ✅ Fully qualified name


    def ready(self):
        import dashboard.signals
  # Make sure signals are loaded

