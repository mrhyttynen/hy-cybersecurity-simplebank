# used chatgpt for this file
import logging
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from django.dispatch import receiver

logger = logging.getLogger("insecurebank")


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info(
        f"User logged in: {user.username}",
        extra={
            "username": user.username,
            "ip": request.META.get("REMOTE_ADDR"),
        },
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(
        f"User logged out: {user.username}",
        extra={
            "username": user.username,
            "ip": request.META.get("REMOTE_ADDR"),
        },
    )

# A09-1: not logging failed login attempts
# FIX A09-1: log them as below
# @receiver(user_login_failed)
# def log_user_login_failed(sender, credentials, request, **kwargs):
#     username = credentials.get("username")
#     logger.warning(
#         f"User login failed: {username}",
#         extra={
#             "username": username,
#             "ip": request.META.get("REMOTE_ADDR") if request else None,
#         },
#     )