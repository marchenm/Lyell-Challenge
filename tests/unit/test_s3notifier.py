import json
import pytest

from aws_cdk import core
from s3notifier.s3notifier import s3notifier


def get_template():
    app = core.App()
    s3notifier(app, "test")
    return json.dumps(app.synth().get_stack("test").template)


def test_sqs_queue_created():
    assert "AWS::SQS::Queue" in get_template()


def test_sns_topic_created():
    assert "AWS::SNS::Topic" in get_template()


def test_s3_bucket_created():
    assert "AWS::S3::Bucket" in get_template()


def test_sns_subscription_created():
    assert "AWS::SNS::Subscription" in get_template()


def test_s3_bucket_notification_created():
    assert "Custom::S3BucketNotifications" in get_template()


def test_s3_bucket_deployment_created():
    assert "Custom::CDKBucketDeployment" in get_template()
