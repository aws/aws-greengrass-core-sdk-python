=========
CHANGELOG
=========

1.6.1
=====
Stream manager support for Python 3.10.

1.6.0
=====
Stream manager supports automatic data export to AWS S3 and AWS IoT SiteWise, provides new API method to update existing streams, and pause or resume exporting.
Support Python3.8 lambda runtime. 

1.5.0
=====

SDK supports StreamManager client.

1.4.0
======

Added support for Python 3.7 Lambda runtime. Lambda functions that use Python 3.7 can now run on an AWS IoT Greengrass core. (AWS IoT Greengrass continues to support Python 2.7 runtime.)


1.3.0
======

SDK supports SecretsManager client.


1.2.0
======

SDK and GGC compatibility check takes place in the background.


1.1.0
======
Lambda only accepted payload in JSON format. With this update, Invoking or publishing binary payload to a lambda is supported.
