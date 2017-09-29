#!/usr/bin/env python2
# encoding: utf-8
"""
Crawl a list of tweets using statuses/lookup.
"""

from __future__ import division, print_function


import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import json

import wriggler
from wriggler.twitter.auth import MultiAuth
from wriggler.twitter.rest import statuses_lookup

log = wriggler.Logger()

def do_crawl(key, ifname, ofname):
    """
    Do the crawl.
    """

    log.info("Reading tweet ids from {} ...", ifname)
    with open(ifname, "r") as fobj:
        all_tids = fobj.read().split()
    all_tids = map(int, all_tids)

    # Create the auth object
    auth = MultiAuth([key])

    log.info("Writing tweets to {} ...", ofname)
    with open(ofname, "w") as fobj:
        # Select 100 tweet ids at a time
        for i in xrange(0, len(all_tids), 100):
            tids = all_tids[i: i+100]

            try:
                data, meta = statuses_lookup(auth, id=tids)
                if meta["code"] == 200:
                    for tweet in data:
                        fobj.write(json.dumps(tweet) + "\n")
                else:
                    log.warn("Failed to get tweets {} to {} ...", i, i + 100)
                    log.warn("http_status_code={} : {} ", meta["code"], data)
            except wriggler.Error as e:
                log.warn("Failed to get tweets {} to {} ...", i, i + 100)
                log.warn(str(e))

            if i % 1000 == 0:	log.info("Crawled {} tweets ...", i)

def main():
    ifname = "NepalQuake-code-mixed-training-tweetids.txt"
    ofname = "NepalQuake-code-mixed-training-tweets.jsonl"

    key = {
        "client_key": "tgDwhsUArYx3xjS27jHnehjtL",
        "client_secret": "dQbCzhL7JNPLRLGckUomrPOZhdZ8CIbFu2yN7GLBvElT0AxOqE",
        "resource_owner_key": "700641895098109952-HX1iddf8ogk6x001JrAAYJXHOY1gGfY",
        "resource_owner_secret": "L6v5GPs2dHPiLtiaRXwtWl6OnZfmuPlVWz1zR9epwhLqk"
    }

    do_crawl(key, ifname, ofname)

if __name__ == '__main__':
    main()
