
# Lyell Coding Challenge

## Table of Contents

  - [Github Actions Deployment](#github-actions-deployment)
  - [Local Development](#local-development)
    - [Requirements](#requirements)
    - [Python Setup and Testing](#python-setup-and-testing)
    - [Local Deployment](#local-deployment)
  - [Useful commands](#useful-commands)

## Github Actions Deployement

This repository is configured with a Github Actions workflow. To deploy with Github Actions, fork the repository and create 2 [encrypted repository secrets:](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository)

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

On the forked repository page go to  `Actions` and enable the workflow. You can now run the `s3Notifier` workflow by passing a `cdk` command to the `CDK Operation` field. Simply pass `deploy` to deploy the stack and `destroy` to delete the stack.

## Local Development

This project demonstrates a CDK app with an instance of a stack (`s3notifier_stack`)
which contains a SQS queue that is subscribed to a SNS topic, a S3 bucket with `Put` event notification going to the SNS topic, and a text file upload to the s3 bucket.

### Requirements

The following packages and their prerequisites are required to be installed and configured:

- [python3.6 or newer](https://www.python.org/downloads/)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
- [AWS CLI](https://aws.amazon.com/cli/)

If you're operating system supports [Homebrew](https://brew.sh/) the supplied Brewfile can be installed with `brew bundle`. The AWS CDK will still need to be configured.

### Python Setup and Testing

The `cdk.json` file tells the CDK Toolkit how to execute your app.

To manually create a virtualenv on MacOS and Linux:

```sh
python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```sh
source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```sh
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```sh
cdk synth
```

you can run the unit tests for the code.

```sh
pytest
```

### Local Deployment

CDK requires bootstrapping to deploy this stack. To bootstrap specific accounts or for advanced bootstrapping with multiple accounts see the [CDK docs](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html#bootstrapping-howto).

```sh
cdk bootstrap
```

After bootstrapping you can deploy the stack.

```sh
cdk deploy
```

You can also delete the deployed resource in the stack.

```sh
cdk destroy
```

To clean up the bootstrapping environment:

```sh
aws s3 rb --force s3://$(aws s3 ls | grep cdktoolkit | cut -d' ' -f3)
aws cloudformation delete-stack --stack-name CDKToolkit
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
