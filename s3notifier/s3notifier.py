from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_s3_deployment as s3deploy,
    core,
)


class s3notifier(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "sqsqueue", visibility_timeout=core.Duration.seconds(300)
        )

        topic = sns.Topic(self, "snstopic")

        topic.add_subscription(subs.SqsSubscription(queue))

        bucket = s3.Bucket(
            self,
            "s3Bucket",
            encryption=s3.BucketEncryption.KMS_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED_PUT, s3n.SnsDestination(topic)
        )

        s3deploy.BucketDeployment(
            self,
            "DeployFile",
            sources=[s3deploy.Source.asset("./assets")],
            destination_bucket=bucket,
            retain_on_delete=False,
        )
