#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto.ec2
import sys


def instances():
    print 'boto %s on %s.' % (boto.Version, sys.platform)

    conn = boto.ec2.connect_to_region("us-east-1")
    reservations = conn.get_all_reservations()

    for r in reservations:
        instances = r.instances
        for i in instances:
            # print dir(i)
            print i.id
            print i.instance_type
            print i.ip_address
            print i.key_name
            print i.launch_time
            print i.region.name
            print i.state


if __name__ == '__main__':
    instances()
