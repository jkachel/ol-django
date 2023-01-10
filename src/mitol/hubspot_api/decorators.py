"""Decorators for hubspot_api"""
import functools
from typing import Callable

from hubspot.crm.objects import ApiException

from mitol.hubspot_api.exceptions import TooManyRequestsException


def raise_429(func) -> Callable:
    """
    Convert an ApiException to a TooManyRequestsException if status code is 429

     Returns:
         Callable: wrapped function (typically a celery task)
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as ae:
            if int(ae.status) == 429:
                raise TooManyRequestsException(ae)
            else:
                raise

    return wrapper
