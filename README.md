# S3-hosted site with password protection

This template goes with [the blog post on the Cevo website](https://cevo.com.au/post/2018-11-01-password-protected-s3-websites/).

It creates a stack which provides a password-protected front end to a static S3-hosted website.
Unlike hosting a site directly from S3, this has the advantage of:

* HTTP to HTTPS redirection
* HTTPS (SSL) protection of content in transit, with automated SSL certificate generation and
  management
* Serverless authentication (pay only if there's demand)
* A global CDN for rapid, cached delivery of content

## Creating the stack

1. Create a Route53 zone for the site
1. Update the `parameters.json` with the domain, site prefix (eg `www`), username and password to
   limit visitors
1. Create the stack in the `us-east-1` region (for now, it has to be, but it hardly matters
   because the content all comes via CloudFront anyhow)

