#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

# greengrassHelloWorldCounter.py
# Demonstrates a simple publish to a topic using Greengrass core sdk
# This lambda function will retrieve underlying platform information and send a hello world message along with the
# platform information to the topic 'hello/world/counter' along with a counter to keep track of invocations.
#
# This Lambda function requires the AWS Greengrass SDK to run on Greengrass devices.
# This can be found on the AWS IoT Console.

import json
import logging
import platform
import sys
import time

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

# Counter to keep track of invocations of the function_handler
my_counter = 0


def function_handler(event, context):
    global my_counter
    my_counter = my_counter + 1
    try:
        if not my_platform:
            client.publish(
                topic="hello/world/counter",
                queueFullPolicy="AllOrException",
                payload=json.dumps(
                    {"message": "Hello world! Sent from Greengrass Core.  Invocation Count: {}".format(my_counter)}
                ),
            )
        else:
            client.publish(
                topic="hello/world/counter",
                queueFullPolicy="AllOrException",
                payload=json.dumps(
                    {
                        "message": "Hello world! Sent from Greengrass Core running on platform: {}.".format(my_platform)
                        + "  Invocation Count: {}".format(my_counter)
                    }
                ),
            )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))
    time.sleep(20)
    return
