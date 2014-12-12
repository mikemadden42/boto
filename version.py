#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto
import sys


def version():
    print 'boto %s on %s.' % (boto.Version, sys.platform)


if __name__ == '__main__':
    version()
