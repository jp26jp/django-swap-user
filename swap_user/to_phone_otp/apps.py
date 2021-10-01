from django.apps import AppConfig


class PhoneOTPUserConfig(AppConfig):
    # `name` for INSTALLED_APPS
    name = "swap_user.to_phone_otp"
    # `label` used for relations reference in format `app_label.Model`
    # also it used for `AUTH_USER_MODEL` settings and fixtures definition
    label = "to_phone_otp"
    # `verbose name` for Admin panel display
    verbose_name = "Django Swap User"
