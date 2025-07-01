from django.apps import AppConfig
class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Distributor_app.dashboard'  # ✅ Fully qualified name


    def ready(self):
        import Distributor_app.dashboard.signals
  # Make sure signals are loaded

