Greengrass Core Python SDK
==========================

The AWS IoT Greengrass Core SDK is meant to be used by AWS Lambda functions running on an AWS IoT Greengrass Core. It will enable Lambda functions to invoke other Lambda functions deployed to the Greengrass Core, publish messages to the Greengrass Core and work with the local Shadow service.

=================================
Using AWS IoT Greengrass Core SDK
=================================

To use the AWS IoT Greengrass Core SDK, you must first import the AWS IoT Greengrass Core SDK in your Lambda function as you would with any other external libraries. You then need to create a client for 'iot-data' or 'lambda'. Use 'iot-data' if you wish to publish messages to the local Greengrass Core and interact with the local Shadow service. Use 'lambda' if you wish to invoke other Lambda functions deployed to the same Greengrass Core.

Here is an example for using the 'iot-data' client

.. code-block:: python

    import greengrasssdk

    # Let's instantiate the iot-data client
    client = greengrasssdk.client('iot-data')


Now that you have an ``iot-data`` client, you can publish requests.

.. code-block:: python

    response = client.publish(
        topic='someTopic',
        payload='some data'.encode()
    )

Here is an example for using the 'lambda' client.

.. code-block:: python

    import greengrasssdk

    client = greengrasssdk.client('lambda')

Now that you have a lambda client, you can publish requests.

.. code-block:: python

    # Define the payload to pass to the invoked lambda function
    msg = json.dumps({
        'message':"hello"
    })

    # Invoke the lambda function
    response = client.invoke(
        FunctionName='arn:<partition>:lambda:<region>:<account id>:function:<function name>',
        InvocationType='RequestResponse',
        Payload=payload,
        Qualifier='2'
    )

==============
Compatibility
==============

As new features are added to AWS IoT Greengrass, newer versions of the AWS IoT Greengrass SDK may be incompatible with older versions of the AWS IoT Greengrass core. The following table lists the compatible SDKs for all GGC releases.

+-------------+------------------------+
| GGC Version | Compatible SDK Versions|
+=============+========================+
| 1.0.x-1.6.x | 1.0.x-1.2.x            |
+-------------+------------------------+
| 1.7.x-1.8.x | 1.0.x-1.3.x            |
+-------------+------------------------+
| 1.9.x       | 1.0.x-1.4.x            |
+-------------+------------------------+
| 1.10.x      | 1.0.x-1.5.x            |
+-------------+------------------------+
| 1.11.x      | 1.0.x-1.6.x            |
+-------------+------------------------+

==============
Stream Manager
==============

Greengrass version 1.10 comes with a new optional feature, Stream Manager. This SDK supports Stream Manager, but it has additional requirements. Specifically, Stream Manager requires Python version 3.7 or above. It also has package requirements listed in the requirements.txt file. Please install these requirements and bundle it with your lambda zip package.

To install the requirements you can use pip such as :code:`pip install --target . -r requirements.txt`. This will install the requirements to the directory that you run the command in. In order to work in Greengrass the dependencies must be bundled in the zip with your lambda code.
With the pip command above, the dependencies will be installed to the current directory. The dependencies must be bundled with your lambda code, so if the current directory doesn't have your
lambda code, then simply copy the installed dependencies to the directory which contains your code.
