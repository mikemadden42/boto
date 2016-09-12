#!/usr/bin/env python
"""List boto3 version."""

import boto3
import sys


def version():
    """List boto3 version."""
    print 'boto3 %s on %s.' % (boto3.__version__, sys.platform)


if __name__ == '__main__':
    version()
