#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto
import sys


def buckets():
    print 'boto %s on %s.' % (boto.Version, sys.platform)

    conn = boto.connect_s3()
    rs = conn.get_all_buckets()

    for b in rs:
        print b.name


if __name__ == '__main__':
    buckets()
