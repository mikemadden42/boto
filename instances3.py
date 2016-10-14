#!/usr/bin/env python
"""List ec2 instances."""

import boto3


def list_instances():
    """List ec2 instances."""
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }])
    for i in instances:
        print i.id
        print i.instance_type
        print i.ip_address
        print i.key_name
        print i.launch_time
        print i.region.name
        print i.state


if __name__ == '__main__':
    list_instances()
