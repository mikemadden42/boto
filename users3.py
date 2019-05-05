#!/usr/bin/env python
"""List IAM users"""
import boto3


def users():
    """List IAM users"""

    # Create IAM client
    iam = boto3.client("iam")

    # List users with the pagination interface
    paginator = iam.get_paginator("list_users")
    for response in paginator.paginate():
        print(response)


if __name__ == "__main__":
    users()
