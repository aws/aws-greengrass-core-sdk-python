#
# Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
import logging
import sys

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def handler(event, context):
    logger.info("Invoked with payload " + str(event))
    return "Invoked successfully"
