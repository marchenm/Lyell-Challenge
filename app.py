#!/usr/bin/env python3

from aws_cdk import core

from s3notifier.s3notifier import s3notifier


app = core.App()
s3notifier(app, "s3notifier", env={"region": "us-west-2"})

app.synth()
