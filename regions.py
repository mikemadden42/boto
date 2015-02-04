#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto.ec2
import sys


def instances():
    print 'boto %s on %s.' % (boto.Version, sys.platform)

    regions = boto.ec2.regions()

    for r in regions:
        print r.name


if __name__ == '__main__':
    instances()
