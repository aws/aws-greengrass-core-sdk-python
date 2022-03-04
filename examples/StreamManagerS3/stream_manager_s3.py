import asyncio
import logging
import time

from greengrasssdk.stream_manager import (
    ExportDefinition,
    MessageStreamDefinition,
    ReadMessagesOptions,
    ResourceNotFoundException,
    S3ExportTaskDefinition,
    S3ExportTaskExecutorConfig,
    Status,
    StatusConfig,
    StatusLevel,
    StatusMessage,
    StrategyOnFull,
    StreamManagerClient,
    StreamManagerException,
)
from greengrasssdk.stream_manager.util import Util

# This example creates a local stream named "SomeStream", and a status stream named "SomeStatusStream.
# It adds 1 S3 Export task into the "SomeStream" stream and then stream manager automatically exports
# the data to a customer-created S3 bucket named "SomeBucket".
# This example runs until the customer-created file at URL "SomeURL" has been uploaded to the S3 bucket.


def main(logger):
    try:
        stream_name = "SomeStream"
        status_stream_name = "SomeStatusStreamName"
        bucket_name = "SomeBucket"
        key_name = "SomeKey"
        file_url = "file:/path/to/some/file.someExtension"
        client = StreamManagerClient()

        # Try deleting the status stream (if it exists) so that we have a fresh start
        try:
            client.delete_message_stream(stream_name=status_stream_name)
        except ResourceNotFoundException:
            pass

        # Try deleting the stream (if it exists) so that we have a fresh start
        try:
            client.delete_message_stream(stream_name=stream_name)
        except ResourceNotFoundException:
            pass

        exports = ExportDefinition(
            s3_task_executor=[
                S3ExportTaskExecutorConfig(
                    identifier="S3TaskExecutor" + stream_name,  # Required
                    # Optional. Add an export status stream to add statuses for all S3 upload tasks.
                    status_config=StatusConfig(
                        status_level=StatusLevel.INFO,  # Default is INFO level statuses.
                        # Status Stream should be created before specifying in S3 Export Config.
                        status_stream_name=status_stream_name,
                    ),
                )
            ]
        )

        # Create the Status Stream.
        client.create_message_stream(
            MessageStreamDefinition(name=status_stream_name, strategy_on_full=StrategyOnFull.OverwriteOldestData)
        )

        # Create the message stream with the S3 Export definition.
        client.create_message_stream(
            MessageStreamDefinition(
                name=stream_name, strategy_on_full=StrategyOnFull.OverwriteOldestData, export_definition=exports
            )
        )

        # Append a S3 Task definition and print the sequence number
        s3_export_task_definition = S3ExportTaskDefinition(input_url=file_url, bucket=bucket_name, key=key_name)
        logger.info(
            "Successfully appended S3 Task Definition to stream with sequence number %d",
            client.append_message(stream_name, Util.validate_and_serialize_to_json_bytes(s3_export_task_definition)),
        )

        # Read the statuses from the export status stream
        stop_checking = False
        next_seq = 0
        while not stop_checking:
            try:
                messages_list = client.read_messages(
                    status_stream_name,
                    ReadMessagesOptions(
                        desired_start_sequence_number=next_seq, min_message_count=1, read_timeout_millis=1000
                    ),
                )
                for message in messages_list:
                    # Deserialize the status message first.
                    status_message = Util.deserialize_json_bytes_to_obj(message.payload, StatusMessage)

                    # Check the status of the status message. If the status is "Success",
                    # the file was successfully uploaded to S3.
                    # If the status was either "Failure" or "Cancelled", the server was unable to upload the file to S3.
                    # We will print the message for why the upload to S3 failed from the status message.
                    # If the status was "InProgress", the status indicates that the server has started uploading
                    # the S3 task.
                    if status_message.status == Status.Success:
                        logger.info("Successfully uploaded file at path " + file_url + " to S3.")
                        stop_checking = True
                    elif status_message.status == Status.InProgress:
                        logger.info("File upload is in Progress.")
                        next_seq = message.sequence_number + 1
                    elif status_message.status == Status.Failure or status_message.status == Status.Canceled:
                        logger.info(
                            "Unable to upload file at path " + file_url + " to S3. Message: " + status_message.message
                        )
                        stop_checking = True
                if not stop_checking:
                    time.sleep(5)
            except StreamManagerException:
                logger.exception("Exception while running")
                time.sleep(5)
    except asyncio.TimeoutError:
        logger.exception("Timed out while executing")
    except Exception:
        logger.exception("Exception while running")
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
