#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto


def buckets():
    conn = boto.connect_s3()
    rs = conn.get_all_buckets()

    for b in rs:
        print b.name


if __name__ == '__main__':
    buckets()
