#
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

import logging
import sys

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

client = greengrasssdk.client("iot-data")


def uptime_handler(event, context):
    logger.info("Received message!")
    if "state" in event:
        if event["state"] == "on":
            try:
                client.publish(topic="/topic/metering", queueFullPolicy="AllOrException", payload="Robot arm turned ON")
                logger.info("Triggering publish to topic " "/topic/metering with ON state")
            except Exception as e:
                logger.error("Failed to trigger publish to topic " "/topic/metering with ON state: " + repr(e))
        elif event["state"] == "off":
            try:
                client.publish(
                    topic="/topic/metering", queueFullPolicy="AllOrException", payload="Robot arm turned OFF"
                )
                logger.info("Triggering publish to topic " "/topic/metering with OFF state")
            except Exception as e:
                logger.error("Failed to trigger publish to topic " "/topic/metering with OFF state: " + repr(e))
