#!/usr/bin/env python
"""List ec2 regions."""

import boto.ec2


def instances():
    """List ec2 regions."""
    regions = boto.ec2.regions()

    for region in regions:
        print region.name


if __name__ == '__main__':
    instances()
