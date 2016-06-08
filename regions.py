#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto.ec2


def instances():
    regions = boto.ec2.regions()

    for r in regions:
        print r.name


if __name__ == '__main__':
    instances()
