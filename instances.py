#!/usr/bin/env python3
"""List ec2 instances."""

import boto.ec2


def list_instances():
    """List ec2 instances."""
    conn = boto.ec2.connect_to_region("us-east-1")
    reservations = conn.get_all_reservations()

    for reservation in reservations:
        instances = reservation.instances
        for i in instances:
            print(i.id)
            print(i.instance_type)
            print(i.ip_address)
            print(i.key_name)
            print(i.launch_time)
            print(i.region.name)
            print(i.state)


if __name__ == '__main__':
    list_instances()
