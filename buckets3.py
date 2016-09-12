#!/usr/bin/env python
"""List s3 buckets."""

import boto3


def buckets():
    """List s3 buckets."""
    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        print bucket.name


if __name__ == '__main__':
    buckets()
