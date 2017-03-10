#!/usr/bin/env python
"""List boto version."""

import sys
import boto


def version():
    """List boto version."""
    print 'boto %s on %s.' % (boto.Version, sys.platform)


if __name__ == '__main__':
    version()
