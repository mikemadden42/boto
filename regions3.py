#!/usr/bin/env python
"""List ec2 regions."""

# http://stackoverflow.com/questions/38451032/how-to-list-available-regions-with-boto3-python

from boto3.session import Session


def instances():
    """List ec2 regions."""
    sess = Session()

    for region in sess.get_available_regions('s3'):
        print region


if __name__ == '__main__':
    instances()
