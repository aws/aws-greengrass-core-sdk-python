import asyncio
import calendar
import logging
import random
import time
import uuid

from greengrasssdk.stream_manager import (
    AssetPropertyValue,
    ExportDefinition,
    IoTSiteWiseConfig,
    MessageStreamDefinition,
    PutAssetPropertyValueEntry,
    Quality,
    ResourceNotFoundException,
    StrategyOnFull,
    StreamManagerClient,
    TimeInNanos,
    Variant,
)
from greengrasssdk.stream_manager.util import Util

# This example will create a Greengrass StreamManager stream called "SomeStream".
# It will then start writing data into that stream and StreamManager will
# automatically export the written data to the customer-created property alias.
# This example will run forever, until the program is killed.

# The size of the StreamManager stream on disk will not exceed the default (which is 256 MB).
# Any data appended after the stream reaches the size limit, will continue to be appended, and
# StreamManager will delete the oldest data until the total stream size is back under 256MB.


property_alias = "SomePropertyAlias"


# This will create a random asset property value entry and return it to the caller.
def get_random_site_wise_entry():

    # SiteWise requires unique timestamps in all messages and also needs timstamps not earlier
    # than 10 minutes in the past. Add some randomness to time and offset.

    # Note: Inorder to create a new asset property data, you should use the classes defined in the
    # greengrasssdk.stream_manager module.

    time_in_nanos = TimeInNanos(
        time_in_seconds=calendar.timegm(time.gmtime()) - random.randint(0, 60), offset_in_nanos=random.randint(0, 10000)
    )
    variant = Variant(double_value=random.random())
    asset = [AssetPropertyValue(value=variant, quality=Quality.GOOD, timestamp=time_in_nanos)]
    return PutAssetPropertyValueEntry(entry_id=str(uuid.uuid4()), property_alias=property_alias, property_values=asset)


def main(logger):
    try:
        stream_name = "SomeStream"
        client = StreamManagerClient()

        # Try deleting the stream (if it exists) so that we have a fresh start
        try:
            client.delete_message_stream(stream_name=stream_name)
        except ResourceNotFoundException:
            pass

        exports = ExportDefinition(
            iot_sitewise=[IoTSiteWiseConfig(identifier="IoTSiteWiseExport" + stream_name, batch_size=5)]
        )
        client.create_message_stream(
            MessageStreamDefinition(
                name=stream_name, strategy_on_full=StrategyOnFull.OverwriteOldestData, export_definition=exports
            )
        )

        logger.info("Now going to start writing random IoTSiteWiseEntry to the stream")
        # Now start putting in random site wise entries.
        while True:
            logger.debug("Appending new random IoTSiteWiseEntry to stream")
            client.append_message(stream_name, Util.validate_and_serialize_to_json_bytes(get_random_site_wise_entry()))
            time.sleep(1)
    except asyncio.TimeoutError:
        print("Timed out")
    except Exception as e:
        print(e)
        print(type(e))
    finally:
        if client:
            client.close()


logging.basicConfig(level=logging.INFO)
# Start up this sample code
main(logger=logging.getLogger())


# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    return
