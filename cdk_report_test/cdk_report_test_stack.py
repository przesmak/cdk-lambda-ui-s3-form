from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3, 
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_s3_deployment as s3Deployment, 
)
from constructs import Construct

class CdkReportTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ui_bucket = s3.Bucket(
            self, 'uiBucketFront', 
            public_read_access= True,
            website_index_document='index.html'
        )

        bucketDeployment = s3Deployment.BucketDeployment(
            self, 'uiFrontDeployment',
            sources=[s3Deployment.Source.asset('ui/build')],
            destination_bucket= ui_bucket
        )        

        bucket = s3.Bucket(
            self, "cdk-report-templates",
            cors= [
                s3.CorsRule(
                    allowed_methods=[
                        s3.HttpMethods.GET,
                        s3.HttpMethods.POST,
                    ],
                    allowed_origins=['http://localhost:3000', '*'],
                    allowed_headers=['*']
                )
            ])
        
        report_lambda = _lambda.Function(
            self, 'ReportRead',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler= 'report.handler',
            code=_lambda.Code.from_asset('resources'),
            environment={
                'S3_BUCKET_NAME': bucket.bucket_name,
            }
        )
        
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=report_lambda,
        )

        bucket.grant_read_write(report_lambda)