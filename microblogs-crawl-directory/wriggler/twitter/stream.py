"""
Robust Twitter streaming API interface.
"""

import ssl
import httplib
from time import sleep

from requests_oauthlib import OAuth1

from wriggler import log
from wriggler.twitter import list_to_csv
import wriggler.const as const
import wriggler.req as req

def stream_call(endpoint, auth, params, method):
    """
    Do the streaming api.
    """

    auth = OAuth1(signature_type="auth_header", **auth.token)

    # Enter the infinite loop
    while True:
        if method == "get":
            r = req.get(endpoint, params=params, auth=auth,
                        timeout=60.0, stream=True)
        elif method == "post":
            r = req.post(endpoint, data=params, auth=auth,
                         timeout=60.0, stream=True)
        else:
            raise ValueError("Invalid value for parameter 'method'")

        if r.status_code == 200:
            # Loop over the lines
            try:
                for line in r.iter_lines():
                    if line:
                        yield line
            except ssl.SSLError as e:
                log.info(u"ssl.SSLError - {}", e)
            except httplib.IncompleteRead as e:
                log.info(u"httplib.IncompleteRead - {}", e)
            except Exception: # pylint: disable=broad-except
                log.warn(u"Unexepectd exception", exc_info=True)

        else: # Dont expect anything else
            msg = u"Unexepectd response - {0}".format(r.status_code)
            log.warn(msg)
            try:
                for line in r.iter_lines():
                    log.info(line.strip())
            except Exception: # pylint: disable=broad-except
                msg = (u"Unexepectd exception "
                       u"while processing unexpected response.")
                log.warn(msg, exc_info=True)

            # Try to sleep over the problem
            sleep(const.API_RETRY_AFTER)

def statuses_filter(auth, **params):
    """
    Collect tweets from the twitter statuses_filter api.
    """

    endpoint = "https://stream.twitter.com/1.1/statuses/filter.json"

    if "follow" in params and isinstance(params["follow"], (list, tuple)):
        params["follow"] = list_to_csv(params["follow"])
    if "track" in params and isinstance(params["track"], (list, tuple)):
        params["track"] = list_to_csv(params["track"])

    params.setdefault("delimited", 0)
    params.setdefault("stall_warnings", 1)

    return stream_call(endpoint, auth, params, "post")

def statuses_sample(auth):
    """
    Collect the twitter public stream.
    """

    endpoint = "https://stream.twitter.com/1.1/statuses/sample.json"
    params = {"delimited": 0, "stall_warnings": 1}

    return stream_call(endpoint, auth, params, "get")

