
# CDK project example with UI

This is a project for Python development with CDK.
It contains full-stack development example with UI made in React.js, lambda function to perform storage in the static file database and AWS S3 buckets.

## Cloud Stack: 

### UI 

The front end deployed in one of the S3 buckets. It contains static page with simplistic form to enter your name and surname. Additionally there is possibility to describe a JSON file name, which then will be stored in S3 bucket. 

Before each deployment to the AWS cloud is necessary to build react webpage by running a script: 

```
npm run build
```

### S3 buckets

There are 2 buckets: 
- storing data from UI form in JSON file format
- hosting static website build in React (WARNING: the endpoint of this bucket is exposed to public)

### Lambda function handler

Lambada handler redirect RestAPI queries and save data from the UI form in the S3 bucket 