#!/usr/bin/env python3
"""List s3 buckets."""

import boto


def buckets():
    """List s3 buckets."""
    conn = boto.connect_s3()

    for bucket in conn.get_all_buckets():
        print(bucket.name)


if __name__ == '__main__':
    buckets()
