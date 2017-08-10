# encoding: utf-8
"""
Common ratelimit check code used by Foursquare and Twitter.
"""

from __future__ import division, print_function

import calendar
from datetime import datetime

import wriggler.const as const

SERVER_TIME_FMT = "%a, %d %b %Y %H:%M:%S %Z"

def get_remaining(headers):
    """
    Get the ratelimit header.
    """

    remain = headers.get("X-Rate-Limit-Remaining", None)
    if remain is None:
        remain = headers.get("X-RateLimit-Remaining", None)
    if remain is None:
        return 0

    try:
        remain = int(remain)
    except ValueError:
        return 0

    return remain

def get_reset_time(headers):
    """
    Get the reset header.
    """

    reset_time = headers.get("X-Rate-Limit-Reset", None)
    if reset_time is None:
        reset_time = headers.get("X-RateLimit-Reset", None)
    if reset_time is None:
        return None

    try:
        reset_time = int(reset_time)
    except ValueError:
        return None

    return reset_time

def get_server_time(headers):
    """
    Get the server time.
    """

    # Get the server time.
    try:
        server_time = headers["date"]
        server_time = datetime.strptime(server_time, SERVER_TIME_FMT)
        server_time = calendar.timegm(server_time.timetuple())
    except (KeyError, ValueError):
        return None

    return server_time

def check_rate_limit(headers):
    """
    Return the number of seconds to sleep off the rate limit.
    """

    # Check if we have hit the rate limit
    # In case the header was not found,
    # assume rate limit was hit
    remain = get_remaining(headers)

    # We still have more api calls left
    if remain > 0:
        return 0

    reset_time = get_reset_time(headers)
    server_time = get_server_time(headers)

    # If we dont have either of the headers return default
    if reset_time is None or server_time is None:
        return const.API_RETRY_AFTER

    # Return recommended seconds to sleep
    sleep_time = reset_time - server_time
    sleep_time = max(sleep_time, 0)
    return sleep_time + const.API_RESET_BUFFER
