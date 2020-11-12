from django.apps import AppConfig


class EmailUserConfig(AppConfig):
    # `name` for INSTALLED_APPS
    name = "swap_user.email"
    # `label` is like an alias for application,
    # used in model relations for example
    label = "swap_user_email"
    # `verbose name` for Admin panel display
    verbose_name = "Swap User"
