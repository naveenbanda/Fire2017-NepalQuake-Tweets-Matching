"""
A simple and robust way for making http requests.

This library wraps python-requests. The errors handled by this module are
connection requests and server side errors. The error handling strategy
is quite simple. Wait for fixed number of seconds on error and then retry.
"""

import requests
from time import sleep

from wriggler import log, Error
import wriggler.const as const

class ConnectFailError(Error):
    """
    Raised on error cases.
    """

def robust_http(url, method, args, kwargs):
    """
    Repeat the HTTP GET/POST operatopn in case of failure.
    """

    assert method in ("get", "post")

    # Get the function to be called
    session = kwargs.pop("session", None)
    if session is None:
        to_call = getattr(requests, method)
    else:
        to_call = getattr(session, method)

    # Keep trying for downlod
    for tries in xrange(const.CONNECT_RETRY_MAX):
        try:
            return to_call(url, *args, **kwargs)
        except requests.RequestException:
            msg = u"Try L0: {} - {} Request Failed\n{}\n"
            log.info(msg, tries, method.upper(), url, exc_info=True)
            sleep(const.CONNECT_RETRY_AFTER)
        except Exception: # pylint: disable=broad-except
            msg = u"Try L0: {} - {} Request Failed\n{}\n"
            log.warn(msg, tries, method.upper(), url, exc_info=True)
            sleep(const.CONNECT_RETRY_AFTER)

    # Cant help any more; Quit program
    raise ConnectFailError(url, method)

def get(url, *args, **kwargs):
    """
    Perform a robust GET request.
    """

    return robust_http(url, "get", args, kwargs)

def post(url, *args, **kwargs):
    """
    Perform a robust POST request.
    """

    return robust_http(url, "post", args, kwargs)

