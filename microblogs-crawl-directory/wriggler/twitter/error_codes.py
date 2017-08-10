"""
Description of Error codes.

https://dev.twitter.com/docs/error-codes-responses
"""

HTTP_STATUS_CODES = {
    200: ("OK", "Success!"),
    304: ("Not Modified", "There was no new data to return."),
    400: ("Bad Request", "The request was invalid or cannot be otherwise served. An accompanying error message will explain further. In API v1.1, requests without authentication are considered invalid and will yield this response."),
    401: ("Unauthorized", "Authentication credentials were missing or incorrect."),
    403: ("Forbidden", "The request is understood, but it has been refused or access is not allowed. An accompanying error message will explain why. This code is used when requests are being denied due to update limits."),
    404: ("Not Found", "The URI requested is invalid or the resource requested, such as a user, does not exists. Also returned when the requested format is not supported by the requested method."),
    406: ("Not Acceptable", "Returned by the Search API when an invalid format is specified in the request."),
    410: ("Gone", "This resource is gone. Used to indicate that an API endpoint has been turned off. For example: \"The Twitter REST API v1 will soon stop functioning. Please migrate to API v1.1.\""),
    420: ("Enhance Your Calm", "Returned by the version 1 Search and Trends APIs when you are being rate limited."),
    422: ("Unprocessable Entity", "Returned when an image uploaded to POST account/update_profile_banner is unable to be processed."),
    429: ("Too Many Requests", "Returned in API v1.1 when a request cannot be served due to the application's rate limit having been exhausted for the resource. See Rate Limiting in API v1.1."),
    500: ("Internal Server Error", "Something is broken. Please post to the group so the Twitter team can investigate."),
    502: ("Bad Gateway", "Twitter is down or being upgraded."),
    503: ("Service Unavailable", "The Twitter servers are up, but overloaded with requests. Try again later."),
    504: ("Gateway timeout", "The Twitter servers are up, but the request couldn't be serviced due to some failure within our stack. Try again later.")
}

ERROR_CODES = {
    32: ("Could not authenticate you", "Your call could not be completed as dialed."),
    34: ("Sorry, that page does not exist", "Corresponds with an HTTP 404 - the specified resource was not found."),
    64: ("Your account is suspended and is not permitted to access this feature", "Corresponds with an HTTP 403 - the access token being used belongs to a suspended user and they can't complete the action you're trying to take"),
    68: ("The Twitter REST API v1 is no longer active. Please migrate to API v1.1. https://dev.twitter.com/docs/api/1.1/overview", "Corresponds to a HTTP request to a retired v1-era URL."),
    88: ("Rate limit exceeded", "The request limit for this resource has been reached for the current rate limit window."),
    89: ("Invalid or expired token", "The access token used in the request is incorrect or has expired. Used in API v1.1"),
    130: ("Over capacity", "Corresponds with an HTTP 503 - Twitter is temporarily over capacity."),
    131: ("Internal error", "Corresponds with an HTTP 500 - An unknown internal error occurred."),
    135: ("Could not authenticate you", "Corresponds with a HTTP 401 - it means that your oauth_timestamp is either ahead or behind our acceptable range"),
    161: ("You are unable to follow more people at this time", "Corresponds with HTTP 403 - thrown when a user cannot follow another user due to some kind of limit"),
    179: ("Sorry, you are not authorized to see this status", "Corresponds with HTTP 403 - thrown when a Tweet cannot be viewed by the authenticating user, usually due to the tweet's author having protected their tweets."),
    185: ("User is over daily status update limit", "Corresponds with HTTP 403 - thrown when a tweet cannot be posted due to the user having no allowance remaining to post. Despite the text in the error message indicating that this error is only thrown when a daily limit is reached, this error will be thrown whenever a posting limitation has been reached. Posting allowances have roaming windows of time of unspecified duration."),
    187: ("Status is a duplicate", "The status text has been Tweeted already by the authenticated account."),
    215: ("Bad authentication data", "Typically sent with 1.1 responses with HTTP code 400. The method requires authentication but it was not presented or was wholly invalid."),
    231: ("User must verify login", "Returned as a challenge in xAuth when the user has login verification enabled on their account and needs to be directed to twitter.com to generate a temporary password."),
    251: ("This endpoint has been retired.", "Corresponds to a HTTP request to a retired URL.")
}
