import enum
from typing import List


class StrategyOnFull(enum.Enum):
    """
    StrategyOnFull is used in the MessageStreamDefinition when creating a stream.
    It defines the behavior when the stream has reached the maximum size.
    RejectNewData: any append message request after the stream is full will be rejected with an exception.
    OverwriteOldestData: the oldest stream segments will be deleted until there is room for the new message.
    """

    RejectNewData = 0
    OverwriteOldestData = 1

    @staticmethod
    def from_dict(d):
        return StrategyOnFull(d)

    def as_dict(self):
        return self.value

    def __repr__(self):
        return "<Enum StrategyOnFull. {}: {}>".format(self.name, self.value)


class Persistence(enum.Enum):
    """
    Stream persistence. If set to File, the file system will be used to persist messages long-term and is resilient to restarts.
    Memory should be used when performance matters more than durability as it only stores the stream in memory and never writes to the disk.
    """

    File = 0
    Memory = 1

    @staticmethod
    def from_dict(d):
        return Persistence(d)

    def as_dict(self):
        return self.value

    def __repr__(self):
        return "<Enum Persistence. {}: {}>".format(self.name, self.value)


class ConnectRequest:
    """
    (Internal Only) Request object to connect to the service
    """

    __slots__ = ["__request_id", "__protocol_version", "__sdk_version", "__auth_token"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "protocol_version": {"type": str, "subtype": None},
        "sdk_version": {"type": str, "subtype": None},
        "auth_token": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "protocol_version": {"required": True},
        "sdk_version": {"required": False},
        "auth_token": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        protocol_version: str = None,
        sdk_version: str = None,
        auth_token: str = None,
    ):
        pass
        self.__request_id = request_id
        self.__protocol_version = protocol_version
        self.__sdk_version = sdk_version
        self.__auth_token = auth_token

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_protocol_version(self):
        return self.__protocol_version

    def _set_protocol_version(self, value):
        if not isinstance(value, str):
            raise TypeError("protocol_version must be str")

        self.__protocol_version = value

    protocol_version = property(_get_protocol_version, _set_protocol_version)

    def _get_sdk_version(self):
        return self.__sdk_version

    def _set_sdk_version(self, value):
        if not isinstance(value, str):
            raise TypeError("sdk_version must be str")

        self.__sdk_version = value

    sdk_version = property(_get_sdk_version, _set_sdk_version)

    def _get_auth_token(self):
        return self.__auth_token

    def _set_auth_token(self, value):
        if not isinstance(value, str):
            raise TypeError("auth_token must be str")

        self.__auth_token = value

    auth_token = property(_get_auth_token, _set_auth_token)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "protocolVersion" in d:
            v["protocol_version"] = (
                str.from_dict(d["protocolVersion"])
                if hasattr(str, "from_dict")
                else d["protocolVersion"]
            )
        if "sdkVersion" in d:
            v["sdk_version"] = (
                str.from_dict(d["sdkVersion"])
                if hasattr(str, "from_dict")
                else d["sdkVersion"]
            )
        if "authToken" in d:
            v["auth_token"] = (
                str.from_dict(d["authToken"])
                if hasattr(str, "from_dict")
                else d["authToken"]
            )
        return ConnectRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__protocol_version is not None:
            d["protocolVersion"] = (
                self.__protocol_version.as_dict()
                if hasattr(self.__protocol_version, "as_dict")
                else self.__protocol_version
            )
        if self.__sdk_version is not None:
            d["sdkVersion"] = (
                self.__sdk_version.as_dict()
                if hasattr(self.__sdk_version, "as_dict")
                else self.__sdk_version
            )
        if self.__auth_token is not None:
            d["authToken"] = (
                self.__auth_token.as_dict()
                if hasattr(self.__auth_token, "as_dict")
                else self.__auth_token
            )
        return d

    def __repr__(self):
        return "<Class ConnectRequest. request_id: {}, protocol_version: {}, sdk_version: {}, auth_token: {}>".format(
            self.__request_id,
            self.__protocol_version,
            self.__sdk_version,
            self.__auth_token,
        )


class ResponseStatusCode(enum.Enum):
    """
    (Internal Only) Enum defining possible response status codes from StreamManager server.
    Success: Request succeeded.
    UnknownFailure: Encountered unknown StreamManager server failure.
    Unauthorized: Client is not authorized to perform this request.
    InvalidRequest: Client request is invalid.
    RequestPayloadTooLarge: Request payload is too large.
    ResourceNotFound: The requested resource does not exist.
    ServerTimeout: Server took too long and timed out.
    ResponsePayloadTooLarge: Server response exceeded the max allowed response payload size by the protocol.
    UnsupportedConnectVersion: Server does not support the Connect version presented by the Client.
    UnexpectedOperation: Operation presented was not expected by the Server.
    UnsupportedProtocolVersion: Protocol version presented by the Client is not compatible with the Server.
    InvalidProtocolVersion: Protocol version presented by the Client is not valid.
    FailedToConnect: Client failed to connect to the Server.
    NotEnoughMessages: There is not enough messages to return.
    MessageStoreReadError: Read messages encountered an error.
    """

    Success = 0
    UnknownFailure = 1
    Unauthorized = 2
    InvalidRequest = 3
    RequestPayloadTooLarge = 4
    ResourceNotFound = 5
    ServerTimeout = 6
    ResponsePayloadTooLarge = 7
    UnsupportedConnectVersion = 8
    UnexpectedOperation = 9
    UnsupportedProtocolVersion = 10
    InvalidProtocolVersion = 11
    FailedToConnect = 12
    NotEnoughMessages = 13
    MessageStoreReadError = 14

    @staticmethod
    def from_dict(d):
        return ResponseStatusCode(d)

    def as_dict(self):
        return self.value

    def __repr__(self):
        return "<Enum ResponseStatusCode. {}: {}>".format(self.name, self.value)


class ConnectResponse:
    """
    Internal Only
    """

    __slots__ = [
        "__request_id",
        "__status",
        "__error_message",
        "__protocol_version",
        "__supported_protocol_versions",
        "__server_version",
        "__client_identifier",
    ]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
        "protocol_version": {"type": str, "subtype": None},
        "supported_protocol_versions": {"type": list, "subtype": str},
        "server_version": {"type": str, "subtype": None},
        "client_identifier": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": False, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "status": {"required": True},
        "error_message": {"required": False},
        "protocol_version": {"required": False},
        "supported_protocol_versions": {"required": False},
        "server_version": {"required": False},
        "client_identifier": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
        protocol_version: str = None,
        supported_protocol_versions: List[str] = None,
        server_version: str = None,
        client_identifier: str = None,
    ):
        pass
        self.__request_id = request_id
        self.__status = status
        self.__error_message = error_message
        self.__protocol_version = protocol_version
        self.__supported_protocol_versions = supported_protocol_versions
        self.__server_version = server_version
        self.__client_identifier = client_identifier

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    def _get_protocol_version(self):
        return self.__protocol_version

    def _set_protocol_version(self, value):
        if not isinstance(value, str):
            raise TypeError("protocol_version must be str")

        self.__protocol_version = value

    protocol_version = property(_get_protocol_version, _set_protocol_version)

    def _get_supported_protocol_versions(self):
        return self.__supported_protocol_versions

    def _set_supported_protocol_versions(self, value):
        if not isinstance(value, list):
            raise TypeError("supported_protocol_versions must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("supported_protocol_versions list values must be str")

        self.__supported_protocol_versions = value

    supported_protocol_versions = property(
        _get_supported_protocol_versions, _set_supported_protocol_versions
    )

    def _get_server_version(self):
        return self.__server_version

    def _set_server_version(self, value):
        if not isinstance(value, str):
            raise TypeError("server_version must be str")

        self.__server_version = value

    server_version = property(_get_server_version, _set_server_version)

    def _get_client_identifier(self):
        return self.__client_identifier

    def _set_client_identifier(self, value):
        if not isinstance(value, str):
            raise TypeError("client_identifier must be str")

        self.__client_identifier = value

    client_identifier = property(_get_client_identifier, _set_client_identifier)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        if "protocolVersion" in d:
            v["protocol_version"] = (
                str.from_dict(d["protocolVersion"])
                if hasattr(str, "from_dict")
                else d["protocolVersion"]
            )
        if "supportedProtocolVersions" in d:
            v["supported_protocol_versions"] = [
                str.from_dict(p) if hasattr(str, "from_dict") else p
                for p in d["supportedProtocolVersions"]
            ]
        if "serverVersion" in d:
            v["server_version"] = (
                str.from_dict(d["serverVersion"])
                if hasattr(str, "from_dict")
                else d["serverVersion"]
            )
        if "clientIdentifier" in d:
            v["client_identifier"] = (
                str.from_dict(d["clientIdentifier"])
                if hasattr(str, "from_dict")
                else d["clientIdentifier"]
            )
        return ConnectResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        if self.__protocol_version is not None:
            d["protocolVersion"] = (
                self.__protocol_version.as_dict()
                if hasattr(self.__protocol_version, "as_dict")
                else self.__protocol_version
            )
        if self.__supported_protocol_versions is not None:
            d["supportedProtocolVersions"] = [
                p.as_dict() if hasattr(p, "as_dict") else p
                for p in self.__supported_protocol_versions
            ]
        if self.__server_version is not None:
            d["serverVersion"] = (
                self.__server_version.as_dict()
                if hasattr(self.__server_version, "as_dict")
                else self.__server_version
            )
        if self.__client_identifier is not None:
            d["clientIdentifier"] = (
                self.__client_identifier.as_dict()
                if hasattr(self.__client_identifier, "as_dict")
                else self.__client_identifier
            )
        return d

    def __repr__(self):
        return "<Class ConnectResponse. request_id: {}, status: {}, error_message: {}, protocol_version: {}, supported_protocol_versions: {}, server_version: {}, client_identifier: {}>".format(
            self.__request_id,
            self.__status,
            self.__error_message,
            self.__protocol_version,
            self.__supported_protocol_versions,
            self.__server_version,
            self.__client_identifier,
        )


class Operation(enum.Enum):
    """
    Internal Only
    """

    Unknown = 0
    Connect = 1
    CreateMessageStream = 2
    DeleteMessageStream = 3
    AppendMessage = 4
    ReadMessages = 5
    ConnectResponse = 6
    CreateMessageStreamResponse = 7
    DeleteMessageStreamResponse = 8
    AppendMessageResponse = 9
    ReadMessagesResponse = 10
    ListStreams = 11
    ListStreamsResponse = 12
    DescribeMessageStream = 13
    DescribeMessageStreamResponse = 14

    @staticmethod
    def from_dict(d):
        return Operation(d)

    def as_dict(self):
        return self.value

    def __repr__(self):
        return "<Enum Operation. {}: {}>".format(self.name, self.value)


class MessageFrame:
    """
    Internal Only
    """

    __slots__ = ["__operation", "__payload"]

    _types_map = {
        "operation": {"type": Operation, "subtype": None},
        "payload": {"type": bytes, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {"operation": {"required": True}, "payload": {"required": True}}

    def __init__(self, operation: Operation = None, payload: bytes = None):
        pass
        self.__operation = operation
        self.__payload = payload

    def _get_operation(self):
        return self.__operation

    def _set_operation(self, value):
        if not isinstance(value, Operation):
            raise TypeError("operation must be Operation")

        self.__operation = value

    operation = property(_get_operation, _set_operation)

    def _get_payload(self):
        return self.__payload

    def _set_payload(self, value):
        if not isinstance(value, bytes):
            raise TypeError("payload must be bytes")

        self.__payload = value

    payload = property(_get_payload, _set_payload)

    @staticmethod
    def from_dict(d):
        v = {}
        if "operation" in d:
            v["operation"] = (
                Operation.from_dict(d["operation"])
                if hasattr(Operation, "from_dict")
                else d["operation"]
            )
        if "payload" in d:
            v["payload"] = (
                bytes.from_dict(d["payload"])
                if hasattr(bytes, "from_dict")
                else d["payload"]
            )
        return MessageFrame(**v)

    def as_dict(self):
        d = {}
        if self.__operation is not None:
            d["operation"] = (
                self.__operation.as_dict()
                if hasattr(self.__operation, "as_dict")
                else self.__operation
            )
        if self.__payload is not None:
            d["payload"] = (
                self.__payload.as_dict()
                if hasattr(self.__payload, "as_dict")
                else self.__payload
            )
        return d

    def __repr__(self):
        return "<Class MessageFrame. operation: {}, payload: {}>".format(
            self.__operation, self.__payload
        )


class HTTPConfig:
    """
    This export destination is not supported! The interface may change at any time without notice and should not be relied on for any production use.
    There are no guarantees around its correctness.
    This configures an HTTP endpoint which sends a POST request to the provided URI. Each request contains a single message in the body of the request.
    """

    __slots__ = [
        "__identifier",
        "__uri",
        "__batch_size",
        "__batch_interval_millis",
        "__priority",
    ]

    _types_map = {
        "identifier": {"type": str, "subtype": None},
        "uri": {"type": str, "subtype": None},
        "batch_size": {"type": int, "subtype": None},
        "batch_interval_millis": {"type": int, "subtype": None},
        "priority": {"type": int, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "identifier": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
        "uri": {"required": True, "minLength": 1},
        "batch_size": {"required": False, "maximum": 500, "minimum": 1},
        "batch_interval_millis": {
            "required": False,
            "maximum": 9223372036854,
            "minimum": 60000,
        },
        "priority": {"required": False, "maximum": 10, "minimum": 1},
    }

    def __init__(
        self,
        identifier: str = None,
        uri: str = None,
        batch_size: int = None,
        batch_interval_millis: int = None,
        priority: int = None,
    ):
        """
        :param identifier: A unique identifier to identify this individual upload stream.
            Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
        :param uri: URL for HTTP endpoint which should receive the POST requests for export.
        :param batch_size: The maximum size of a batch to send to the destination. Messages will be queued until the batch size is reached, after which they will then be uploaded. If unspecified the default will be 1.
            If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
            The minimum batch size is 1 and the maximum is 500.
        :param batch_interval_millis: The time in milliseconds between the earliest un-uploaded message and the current time. If this time is exceeded, messages will be uploaded in the next batch. If unspecified messages will be eligible for upload immediately.
            If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
            The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
        :param priority: Priority for this upload stream. Lower values are higher priority. If not specified it will have the lowest priority.
        """
        pass
        self.__identifier = identifier
        self.__uri = uri
        self.__batch_size = batch_size
        self.__batch_interval_millis = batch_interval_millis
        self.__priority = priority

    def _get_identifier(self):
        return self.__identifier

    def _set_identifier(self, value):
        if not isinstance(value, str):
            raise TypeError("identifier must be str")

        self.__identifier = value

    identifier = property(_get_identifier, _set_identifier)
    """
    A unique identifier to identify this individual upload stream.
    Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
    """

    def _get_uri(self):
        return self.__uri

    def _set_uri(self, value):
        if not isinstance(value, str):
            raise TypeError("uri must be str")

        self.__uri = value

    uri = property(_get_uri, _set_uri)
    """
    URL for HTTP endpoint which should receive the POST requests for export.
    """

    def _get_batch_size(self):
        return self.__batch_size

    def _set_batch_size(self, value):
        if not isinstance(value, int):
            raise TypeError("batch_size must be int")

        self.__batch_size = value

    batch_size = property(_get_batch_size, _set_batch_size)
    """
    The maximum size of a batch to send to the destination. Messages will be queued until the batch size is reached, after which they will then be uploaded. If unspecified the default will be 1.
    If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
    The minimum batch size is 1 and the maximum is 500.
    """

    def _get_batch_interval_millis(self):
        return self.__batch_interval_millis

    def _set_batch_interval_millis(self, value):
        if not isinstance(value, int):
            raise TypeError("batch_interval_millis must be int")

        self.__batch_interval_millis = value

    batch_interval_millis = property(
        _get_batch_interval_millis, _set_batch_interval_millis
    )
    """
    The time in milliseconds between the earliest un-uploaded message and the current time. If this time is exceeded, messages will be uploaded in the next batch. If unspecified messages will be eligible for upload immediately.
    If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
    The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
    """

    def _get_priority(self):
        return self.__priority

    def _set_priority(self, value):
        if not isinstance(value, int):
            raise TypeError("priority must be int")

        self.__priority = value

    priority = property(_get_priority, _set_priority)
    """
    Priority for this upload stream. Lower values are higher priority. If not specified it will have the lowest priority.
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "identifier" in d:
            v["identifier"] = (
                str.from_dict(d["identifier"])
                if hasattr(str, "from_dict")
                else d["identifier"]
            )
        if "uri" in d:
            v["uri"] = (
                str.from_dict(d["uri"]) if hasattr(str, "from_dict") else d["uri"]
            )
        if "batchSize" in d:
            v["batch_size"] = (
                int.from_dict(d["batchSize"])
                if hasattr(int, "from_dict")
                else d["batchSize"]
            )
        if "batchIntervalMillis" in d:
            v["batch_interval_millis"] = (
                int.from_dict(d["batchIntervalMillis"])
                if hasattr(int, "from_dict")
                else d["batchIntervalMillis"]
            )
        if "priority" in d:
            v["priority"] = (
                int.from_dict(d["priority"])
                if hasattr(int, "from_dict")
                else d["priority"]
            )
        return HTTPConfig(**v)

    def as_dict(self):
        d = {}
        if self.__identifier is not None:
            d["identifier"] = (
                self.__identifier.as_dict()
                if hasattr(self.__identifier, "as_dict")
                else self.__identifier
            )
        if self.__uri is not None:
            d["uri"] = (
                self.__uri.as_dict() if hasattr(self.__uri, "as_dict") else self.__uri
            )
        if self.__batch_size is not None:
            d["batchSize"] = (
                self.__batch_size.as_dict()
                if hasattr(self.__batch_size, "as_dict")
                else self.__batch_size
            )
        if self.__batch_interval_millis is not None:
            d["batchIntervalMillis"] = (
                self.__batch_interval_millis.as_dict()
                if hasattr(self.__batch_interval_millis, "as_dict")
                else self.__batch_interval_millis
            )
        if self.__priority is not None:
            d["priority"] = (
                self.__priority.as_dict()
                if hasattr(self.__priority, "as_dict")
                else self.__priority
            )
        return d

    def __repr__(self):
        return "<Class HTTPConfig. identifier: {}, uri: {}, batch_size: {}, batch_interval_millis: {}, priority: {}>".format(
            self.__identifier,
            self.__uri,
            self.__batch_size,
            self.__batch_interval_millis,
            self.__priority,
        )


class IoTAnalyticsConfig:
    """
    Configuration object for IoT Analytics export destination.
    """

    __slots__ = [
        "__identifier",
        "__iot_channel",
        "__iot_msg_id_prefix",
        "__batch_size",
        "__batch_interval_millis",
        "__priority",
    ]

    _types_map = {
        "identifier": {"type": str, "subtype": None},
        "iot_channel": {"type": str, "subtype": None},
        "iot_msg_id_prefix": {"type": str, "subtype": None},
        "batch_size": {"type": int, "subtype": None},
        "batch_interval_millis": {"type": int, "subtype": None},
        "priority": {"type": int, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "identifier": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
        "iot_channel": {"required": True, "minLength": 1},
        "iot_msg_id_prefix": {"required": False, "maximum": 32},
        "batch_size": {"required": False, "maximum": 100, "minimum": 1},
        "batch_interval_millis": {
            "required": False,
            "maximum": 9223372036854,
            "minimum": 60000,
        },
        "priority": {"required": False, "maximum": 10, "minimum": 1},
    }

    def __init__(
        self,
        identifier: str = None,
        iot_channel: str = None,
        iot_msg_id_prefix: str = None,
        batch_size: int = None,
        batch_interval_millis: int = None,
        priority: int = None,
    ):
        """
        :param identifier: A unique identifier to identify this individual upload stream.
            Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
        :param iot_channel: The name of the IoT Analytics Channel that this exporter should upload to
        :param iot_msg_id_prefix: A string prefixed to each unique message id. After this prefix, StreamManager may append more data to make the message ID unique.
            This prefix must be less than 32 characters.
        :param batch_size: The maximum size of a batch to send to IoT Analytics. Messages will be queued until the batch size is reached, after which they will then be uploaded. If unspecified the default will be 1.
            If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
            The batch size must be between 1 and 100.
        :param batch_interval_millis: The time in milliseconds between the earliest un-uploaded message and the current time. If this time is exceeded, messages will be uploaded in the next batch. If unspecified messages will be eligible for upload immediately.
            If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
            The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
        :param priority: Priority for this upload stream. Lower values are higher priority. If not specified it will have the lowest priority.
        """
        pass
        self.__identifier = identifier
        self.__iot_channel = iot_channel
        self.__iot_msg_id_prefix = iot_msg_id_prefix
        self.__batch_size = batch_size
        self.__batch_interval_millis = batch_interval_millis
        self.__priority = priority

    def _get_identifier(self):
        return self.__identifier

    def _set_identifier(self, value):
        if not isinstance(value, str):
            raise TypeError("identifier must be str")

        self.__identifier = value

    identifier = property(_get_identifier, _set_identifier)
    """
    A unique identifier to identify this individual upload stream.
    Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
    """

    def _get_iot_channel(self):
        return self.__iot_channel

    def _set_iot_channel(self, value):
        if not isinstance(value, str):
            raise TypeError("iot_channel must be str")

        self.__iot_channel = value

    iot_channel = property(_get_iot_channel, _set_iot_channel)
    """
    The name of the IoT Analytics Channel that this exporter should upload to
    """

    def _get_iot_msg_id_prefix(self):
        return self.__iot_msg_id_prefix

    def _set_iot_msg_id_prefix(self, value):
        if not isinstance(value, str):
            raise TypeError("iot_msg_id_prefix must be str")

        self.__iot_msg_id_prefix = value

    iot_msg_id_prefix = property(_get_iot_msg_id_prefix, _set_iot_msg_id_prefix)
    """
    A string prefixed to each unique message id. After this prefix, StreamManager may append more data to make the message ID unique.
    This prefix must be less than 32 characters.
    """

    def _get_batch_size(self):
        return self.__batch_size

    def _set_batch_size(self, value):
        if not isinstance(value, int):
            raise TypeError("batch_size must be int")

        self.__batch_size = value

    batch_size = property(_get_batch_size, _set_batch_size)
    """
    The maximum size of a batch to send to IoT Analytics. Messages will be queued until the batch size is reached, after which they will then be uploaded. If unspecified the default will be 1.
    If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
    The batch size must be between 1 and 100.
    """

    def _get_batch_interval_millis(self):
        return self.__batch_interval_millis

    def _set_batch_interval_millis(self, value):
        if not isinstance(value, int):
            raise TypeError("batch_interval_millis must be int")

        self.__batch_interval_millis = value

    batch_interval_millis = property(
        _get_batch_interval_millis, _set_batch_interval_millis
    )
    """
    The time in milliseconds between the earliest un-uploaded message and the current time. If this time is exceeded, messages will be uploaded in the next batch. If unspecified messages will be eligible for upload immediately.
    If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
    The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
    """

    def _get_priority(self):
        return self.__priority

    def _set_priority(self, value):
        if not isinstance(value, int):
            raise TypeError("priority must be int")

        self.__priority = value

    priority = property(_get_priority, _set_priority)
    """
    Priority for this upload stream. Lower values are higher priority. If not specified it will have the lowest priority.
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "identifier" in d:
            v["identifier"] = (
                str.from_dict(d["identifier"])
                if hasattr(str, "from_dict")
                else d["identifier"]
            )
        if "iotChannel" in d:
            v["iot_channel"] = (
                str.from_dict(d["iotChannel"])
                if hasattr(str, "from_dict")
                else d["iotChannel"]
            )
        if "iotMsgIdPrefix" in d:
            v["iot_msg_id_prefix"] = (
                str.from_dict(d["iotMsgIdPrefix"])
                if hasattr(str, "from_dict")
                else d["iotMsgIdPrefix"]
            )
        if "batchSize" in d:
            v["batch_size"] = (
                int.from_dict(d["batchSize"])
                if hasattr(int, "from_dict")
                else d["batchSize"]
            )
        if "batchIntervalMillis" in d:
            v["batch_interval_millis"] = (
                int.from_dict(d["batchIntervalMillis"])
                if hasattr(int, "from_dict")
                else d["batchIntervalMillis"]
            )
        if "priority" in d:
            v["priority"] = (
                int.from_dict(d["priority"])
                if hasattr(int, "from_dict")
                else d["priority"]
            )
        return IoTAnalyticsConfig(**v)

    def as_dict(self):
        d = {}
        if self.__identifier is not None:
            d["identifier"] = (
                self.__identifier.as_dict()
                if hasattr(self.__identifier, "as_dict")
                else self.__identifier
            )
        if self.__iot_channel is not None:
            d["iotChannel"] = (
                self.__iot_channel.as_dict()
                if hasattr(self.__iot_channel, "as_dict")
                else self.__iot_channel
            )
        if self.__iot_msg_id_prefix is not None:
            d["iotMsgIdPrefix"] = (
                self.__iot_msg_id_prefix.as_dict()
                if hasattr(self.__iot_msg_id_prefix, "as_dict")
                else self.__iot_msg_id_prefix
            )
        if self.__batch_size is not None:
            d["batchSize"] = (
                self.__batch_size.as_dict()
                if hasattr(self.__batch_size, "as_dict")
                else self.__batch_size
            )
        if self.__batch_interval_millis is not None:
            d["batchIntervalMillis"] = (
                self.__batch_interval_millis.as_dict()
                if hasattr(self.__batch_interval_millis, "as_dict")
                else self.__batch_interval_millis
            )
        if self.__priority is not None:
            d["priority"] = (
                self.__priority.as_dict()
                if hasattr(self.__priority, "as_dict")
                else self.__priority
            )
        return d

    def __repr__(self):
        return "<Class IoTAnalyticsConfig. identifier: {}, iot_channel: {}, iot_msg_id_prefix: {}, batch_size: {}, batch_interval_millis: {}, priority: {}>".format(
            self.__identifier,
            self.__iot_channel,
            self.__iot_msg_id_prefix,
            self.__batch_size,
            self.__batch_interval_millis,
            self.__priority,
        )


class KinesisConfig:
    """
    Configuration object for Kinesis data streams export destination.
    """

    __slots__ = [
        "__identifier",
        "__kinesis_stream_name",
        "__batch_size",
        "__batch_interval_millis",
        "__priority",
    ]

    _types_map = {
        "identifier": {"type": str, "subtype": None},
        "kinesis_stream_name": {"type": str, "subtype": None},
        "batch_size": {"type": int, "subtype": None},
        "batch_interval_millis": {"type": int, "subtype": None},
        "priority": {"type": int, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "identifier": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
        "kinesis_stream_name": {"required": True, "minLength": 1},
        "batch_size": {"required": False, "maximum": 500, "minimum": 1},
        "batch_interval_millis": {
            "required": False,
            "maximum": 9223372036854,
            "minimum": 60000,
        },
        "priority": {"required": False, "maximum": 10, "minimum": 1},
    }

    def __init__(
        self,
        identifier: str = None,
        kinesis_stream_name: str = None,
        batch_size: int = None,
        batch_interval_millis: int = None,
        priority: int = None,
    ):
        """
        :param identifier: A unique identifier to identify this individual upload stream.
            Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
        :param kinesis_stream_name: The name of the Kinesis data stream that this exporter should upload to
        :param batch_size: The maximum size of a batch to send to Kinesis. Messages will be queued until the batch size is reached, after which they will then be uploaded. If unspecified the default will be 1.
            If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
            The batch size must be between 1 and 500.
        :param batch_interval_millis: The time in milliseconds between the earliest un-uploaded message and the current time. If this time is exceeded, messages will be uploaded in the next batch. If unspecified messages will be eligible for upload immediately.
            If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
            The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
        :param priority: Priority for this upload stream. Lower values are higher priority. If not specified it will have the lowest priority.
        """
        pass
        self.__identifier = identifier
        self.__kinesis_stream_name = kinesis_stream_name
        self.__batch_size = batch_size
        self.__batch_interval_millis = batch_interval_millis
        self.__priority = priority

    def _get_identifier(self):
        return self.__identifier

    def _set_identifier(self, value):
        if not isinstance(value, str):
            raise TypeError("identifier must be str")

        self.__identifier = value

    identifier = property(_get_identifier, _set_identifier)
    """
    A unique identifier to identify this individual upload stream.
    Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
    """

    def _get_kinesis_stream_name(self):
        return self.__kinesis_stream_name

    def _set_kinesis_stream_name(self, value):
        if not isinstance(value, str):
            raise TypeError("kinesis_stream_name must be str")

        self.__kinesis_stream_name = value

    kinesis_stream_name = property(_get_kinesis_stream_name, _set_kinesis_stream_name)
    """
    The name of the Kinesis data stream that this exporter should upload to
    """

    def _get_batch_size(self):
        return self.__batch_size

    def _set_batch_size(self, value):
        if not isinstance(value, int):
            raise TypeError("batch_size must be int")

        self.__batch_size = value

    batch_size = property(_get_batch_size, _set_batch_size)
    """
    The maximum size of a batch to send to Kinesis. Messages will be queued until the batch size is reached, after which they will then be uploaded. If unspecified the default will be 1.
    If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
    The batch size must be between 1 and 500.
    """

    def _get_batch_interval_millis(self):
        return self.__batch_interval_millis

    def _set_batch_interval_millis(self, value):
        if not isinstance(value, int):
            raise TypeError("batch_interval_millis must be int")

        self.__batch_interval_millis = value

    batch_interval_millis = property(
        _get_batch_interval_millis, _set_batch_interval_millis
    )
    """
    The time in milliseconds between the earliest un-uploaded message and the current time. If this time is exceeded, messages will be uploaded in the next batch. If unspecified messages will be eligible for upload immediately.
    If both batchSize and batchIntervalMillis are specified, then messages will be eligible for upload when either condition is met.
    The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
    """

    def _get_priority(self):
        return self.__priority

    def _set_priority(self, value):
        if not isinstance(value, int):
            raise TypeError("priority must be int")

        self.__priority = value

    priority = property(_get_priority, _set_priority)
    """
    Priority for this upload stream. Lower values are higher priority. If not specified it will have the lowest priority.
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "identifier" in d:
            v["identifier"] = (
                str.from_dict(d["identifier"])
                if hasattr(str, "from_dict")
                else d["identifier"]
            )
        if "kinesisStreamName" in d:
            v["kinesis_stream_name"] = (
                str.from_dict(d["kinesisStreamName"])
                if hasattr(str, "from_dict")
                else d["kinesisStreamName"]
            )
        if "batchSize" in d:
            v["batch_size"] = (
                int.from_dict(d["batchSize"])
                if hasattr(int, "from_dict")
                else d["batchSize"]
            )
        if "batchIntervalMillis" in d:
            v["batch_interval_millis"] = (
                int.from_dict(d["batchIntervalMillis"])
                if hasattr(int, "from_dict")
                else d["batchIntervalMillis"]
            )
        if "priority" in d:
            v["priority"] = (
                int.from_dict(d["priority"])
                if hasattr(int, "from_dict")
                else d["priority"]
            )
        return KinesisConfig(**v)

    def as_dict(self):
        d = {}
        if self.__identifier is not None:
            d["identifier"] = (
                self.__identifier.as_dict()
                if hasattr(self.__identifier, "as_dict")
                else self.__identifier
            )
        if self.__kinesis_stream_name is not None:
            d["kinesisStreamName"] = (
                self.__kinesis_stream_name.as_dict()
                if hasattr(self.__kinesis_stream_name, "as_dict")
                else self.__kinesis_stream_name
            )
        if self.__batch_size is not None:
            d["batchSize"] = (
                self.__batch_size.as_dict()
                if hasattr(self.__batch_size, "as_dict")
                else self.__batch_size
            )
        if self.__batch_interval_millis is not None:
            d["batchIntervalMillis"] = (
                self.__batch_interval_millis.as_dict()
                if hasattr(self.__batch_interval_millis, "as_dict")
                else self.__batch_interval_millis
            )
        if self.__priority is not None:
            d["priority"] = (
                self.__priority.as_dict()
                if hasattr(self.__priority, "as_dict")
                else self.__priority
            )
        return d

    def __repr__(self):
        return "<Class KinesisConfig. identifier: {}, kinesis_stream_name: {}, batch_size: {}, batch_interval_millis: {}, priority: {}>".format(
            self.__identifier,
            self.__kinesis_stream_name,
            self.__batch_size,
            self.__batch_interval_millis,
            self.__priority,
        )


class ExportDefinition:
    """
    Defines how and where the stream is uploaded
    """

    __slots__ = ["__http", "__iot_analytics", "__kinesis"]

    _types_map = {
        "http": {"type": list, "subtype": HTTPConfig},
        "iot_analytics": {"type": list, "subtype": IoTAnalyticsConfig},
        "kinesis": {"type": list, "subtype": KinesisConfig},
    }
    _formats_map = {}
    _validations_map = {
        "http": {"required": False},
        "iot_analytics": {"required": False},
        "kinesis": {"required": False},
    }

    def __init__(
        self,
        http: List[HTTPConfig] = None,
        iot_analytics: List[IoTAnalyticsConfig] = None,
        kinesis: List[KinesisConfig] = None,
    ):
        """
        :param http: Defines how the stream is uploaded to an HTTP endpoint
        :param iot_analytics: Defines how the stream is uploaded to IoT Analytics
        :param kinesis: Defines how the stream is uploaded to Kinesis
        """
        pass
        self.__http = http
        self.__iot_analytics = iot_analytics
        self.__kinesis = kinesis

    def _get_http(self):
        return self.__http

    def _set_http(self, value):
        if not isinstance(value, list):
            raise TypeError("http must be list")
        if not all(isinstance(i, HTTPConfig) for i in value):
            raise TypeError("http list values must be HTTPConfig")

        self.__http = value

    http = property(_get_http, _set_http)
    """
    Defines how the stream is uploaded to an HTTP endpoint
    """

    def _get_iot_analytics(self):
        return self.__iot_analytics

    def _set_iot_analytics(self, value):
        if not isinstance(value, list):
            raise TypeError("iot_analytics must be list")
        if not all(isinstance(i, IoTAnalyticsConfig) for i in value):
            raise TypeError("iot_analytics list values must be IoTAnalyticsConfig")

        self.__iot_analytics = value

    iot_analytics = property(_get_iot_analytics, _set_iot_analytics)
    """
    Defines how the stream is uploaded to IoT Analytics
    """

    def _get_kinesis(self):
        return self.__kinesis

    def _set_kinesis(self, value):
        if not isinstance(value, list):
            raise TypeError("kinesis must be list")
        if not all(isinstance(i, KinesisConfig) for i in value):
            raise TypeError("kinesis list values must be KinesisConfig")

        self.__kinesis = value

    kinesis = property(_get_kinesis, _set_kinesis)
    """
    Defines how the stream is uploaded to Kinesis
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "http" in d:
            v["http"] = [
                HTTPConfig.from_dict(p) if hasattr(HTTPConfig, "from_dict") else p
                for p in d["http"]
            ]
        if "iotAnalytics" in d:
            v["iot_analytics"] = [
                IoTAnalyticsConfig.from_dict(p)
                if hasattr(IoTAnalyticsConfig, "from_dict")
                else p
                for p in d["iotAnalytics"]
            ]
        if "kinesis" in d:
            v["kinesis"] = [
                KinesisConfig.from_dict(p) if hasattr(KinesisConfig, "from_dict") else p
                for p in d["kinesis"]
            ]
        return ExportDefinition(**v)

    def as_dict(self):
        d = {}
        if self.__http is not None:
            d["http"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__http
            ]
        if self.__iot_analytics is not None:
            d["iotAnalytics"] = [
                p.as_dict() if hasattr(p, "as_dict") else p
                for p in self.__iot_analytics
            ]
        if self.__kinesis is not None:
            d["kinesis"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__kinesis
            ]
        return d

    def __repr__(self):
        return "<Class ExportDefinition. http: {}, iot_analytics: {}, kinesis: {}>".format(
            self.__http, self.__iot_analytics, self.__kinesis
        )


class MessageStreamDefinition:
    """
    Object defining a message stream used in the CreateMessageStream API.
    """

    __slots__ = [
        "__name",
        "__max_size",
        "__stream_segment_size",
        "__time_to_live_millis",
        "__strategy_on_full",
        "__persistence",
        "__flush_on_write",
        "__export_definition",
    ]

    _types_map = {
        "name": {"type": str, "subtype": None},
        "max_size": {"type": int, "subtype": None},
        "stream_segment_size": {"type": int, "subtype": None},
        "time_to_live_millis": {"type": int, "subtype": None},
        "strategy_on_full": {"type": StrategyOnFull, "subtype": None},
        "persistence": {"type": Persistence, "subtype": None},
        "flush_on_write": {"type": bool, "subtype": None},
        "export_definition": {"type": ExportDefinition, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "name": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
        "max_size": {
            "required": False,
            "maximum": 9223372036854775807,
            "minimum": 1024,
        },
        "stream_segment_size": {
            "required": False,
            "maximum": 2147483647,
            "minimum": 1024,
        },
        "time_to_live_millis": {
            "required": False,
            "maximum": 9223372036854,
            "minimum": 60000,
        },
        "strategy_on_full": {"required": True},
        "persistence": {"required": False},
        "flush_on_write": {"required": False},
        "export_definition": {"required": False},
    }

    def __init__(
        self,
        name: str = None,
        max_size: int = 268435456,
        stream_segment_size: int = 16777216,
        time_to_live_millis: int = None,
        strategy_on_full: StrategyOnFull = None,
        persistence: Persistence = None,
        flush_on_write: bool = None,
        export_definition: ExportDefinition = None,
    ):
        """
        :param name: The unique name of the stream.
            Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
        :param max_size: The maximium size in bytes for the entire stream. Set to 256MB by default with a minimum of 1KB and a maximum of 8192PB.
        :param stream_segment_size: The size of each segment of the stream. Set to 16MB by default with a minimum of 1KB and a maximum of 2GB.
            Data is only deleted segment by segment, so the segment size is the smallest amount of data which can be deleted.
        :param time_to_live_millis: Time to live for each message in milliseconds. Data may be deleted at any time after the TTL expires; deletion is not guaranteed to occur immediately when the TTL expires.
            The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
        :param strategy_on_full: What to do when the maximum size of the stream is reached.
            RejectNewData: any append message request after the stream is full will be rejected with an exception.
            OverwriteOldestData: the oldest stream segments will be deleted until there is room for the new message.
        :param persistence: Stream persistence. If set to File, the file system will be used to persist messages long-term and is resilient to restarts.
            Memory should be used when performance matters more than durability as it only stores the stream in memory and never writes to the disk.
        :param flush_on_write: This only applies when Persistence is set to File mode.
            Waits for the filesystem to complete the write for every message. This is safer, but slower. Default is false.
        :param export_definition: Defines how and where the stream is uploaded. See the definition of the ExportDefinition object for more detail.
        """
        pass
        self.__name = name
        self.__max_size = max_size
        self.__stream_segment_size = stream_segment_size
        self.__time_to_live_millis = time_to_live_millis
        self.__strategy_on_full = strategy_on_full
        self.__persistence = persistence
        self.__flush_on_write = flush_on_write
        self.__export_definition = export_definition

    def _get_name(self):
        return self.__name

    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value

    name = property(_get_name, _set_name)
    """
    The unique name of the stream.
    Must be an alphanumeric string including spaces, commas, periods, hyphens, and underscores with length between 1 and 255.
    """

    def _get_max_size(self):
        return self.__max_size

    def _set_max_size(self, value):
        if not isinstance(value, int):
            raise TypeError("max_size must be int")

        self.__max_size = value

    max_size = property(_get_max_size, _set_max_size)
    """
    The maximium size in bytes for the entire stream. Set to 256MB by default with a minimum of 1KB and a maximum of 8192PB.
    """

    def _get_stream_segment_size(self):
        return self.__stream_segment_size

    def _set_stream_segment_size(self, value):
        if not isinstance(value, int):
            raise TypeError("stream_segment_size must be int")

        self.__stream_segment_size = value

    stream_segment_size = property(_get_stream_segment_size, _set_stream_segment_size)
    """
    The size of each segment of the stream. Set to 16MB by default with a minimum of 1KB and a maximum of 2GB.
    Data is only deleted segment by segment, so the segment size is the smallest amount of data which can be deleted.
    """

    def _get_time_to_live_millis(self):
        return self.__time_to_live_millis

    def _set_time_to_live_millis(self, value):
        if not isinstance(value, int):
            raise TypeError("time_to_live_millis must be int")

        self.__time_to_live_millis = value

    time_to_live_millis = property(_get_time_to_live_millis, _set_time_to_live_millis)
    """
    Time to live for each message in milliseconds. Data may be deleted at any time after the TTL expires; deletion is not guaranteed to occur immediately when the TTL expires.
    The minimum value is 60000 milliseconds and the maximum is 9223372036854 milliseconds.
    """

    def _get_strategy_on_full(self):
        return self.__strategy_on_full

    def _set_strategy_on_full(self, value):
        if not isinstance(value, StrategyOnFull):
            raise TypeError("strategy_on_full must be StrategyOnFull")

        self.__strategy_on_full = value

    strategy_on_full = property(_get_strategy_on_full, _set_strategy_on_full)
    """
    What to do when the maximum size of the stream is reached.
    RejectNewData: any append message request after the stream is full will be rejected with an exception.
    OverwriteOldestData: the oldest stream segments will be deleted until there is room for the new message.
    """

    def _get_persistence(self):
        return self.__persistence

    def _set_persistence(self, value):
        if not isinstance(value, Persistence):
            raise TypeError("persistence must be Persistence")

        self.__persistence = value

    persistence = property(_get_persistence, _set_persistence)
    """
    Stream persistence. If set to File, the file system will be used to persist messages long-term and is resilient to restarts.
    Memory should be used when performance matters more than durability as it only stores the stream in memory and never writes to the disk.
    """

    def _get_flush_on_write(self):
        return self.__flush_on_write

    def _set_flush_on_write(self, value):
        if not isinstance(value, bool):
            raise TypeError("flush_on_write must be bool")

        self.__flush_on_write = value

    flush_on_write = property(_get_flush_on_write, _set_flush_on_write)
    """
    This only applies when Persistence is set to File mode.
    Waits for the filesystem to complete the write for every message. This is safer, but slower. Default is false.
    """

    def _get_export_definition(self):
        return self.__export_definition

    def _set_export_definition(self, value):
        if not isinstance(value, ExportDefinition):
            raise TypeError("export_definition must be ExportDefinition")

        self.__export_definition = value

    export_definition = property(_get_export_definition, _set_export_definition)
    """
    Defines how and where the stream is uploaded. See the definition of the ExportDefinition object for more detail.
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "name" in d:
            v["name"] = (
                str.from_dict(d["name"]) if hasattr(str, "from_dict") else d["name"]
            )
        if "maxSize" in d:
            v["max_size"] = (
                int.from_dict(d["maxSize"])
                if hasattr(int, "from_dict")
                else d["maxSize"]
            )
        if "streamSegmentSize" in d:
            v["stream_segment_size"] = (
                int.from_dict(d["streamSegmentSize"])
                if hasattr(int, "from_dict")
                else d["streamSegmentSize"]
            )
        if "timeToLiveMillis" in d:
            v["time_to_live_millis"] = (
                int.from_dict(d["timeToLiveMillis"])
                if hasattr(int, "from_dict")
                else d["timeToLiveMillis"]
            )
        if "strategyOnFull" in d:
            v["strategy_on_full"] = (
                StrategyOnFull.from_dict(d["strategyOnFull"])
                if hasattr(StrategyOnFull, "from_dict")
                else d["strategyOnFull"]
            )
        if "persistence" in d:
            v["persistence"] = (
                Persistence.from_dict(d["persistence"])
                if hasattr(Persistence, "from_dict")
                else d["persistence"]
            )
        if "flushOnWrite" in d:
            v["flush_on_write"] = (
                bool.from_dict(d["flushOnWrite"])
                if hasattr(bool, "from_dict")
                else d["flushOnWrite"]
            )
        if "exportDefinition" in d:
            v["export_definition"] = (
                ExportDefinition.from_dict(d["exportDefinition"])
                if hasattr(ExportDefinition, "from_dict")
                else d["exportDefinition"]
            )
        return MessageStreamDefinition(**v)

    def as_dict(self):
        d = {}
        if self.__name is not None:
            d["name"] = (
                self.__name.as_dict()
                if hasattr(self.__name, "as_dict")
                else self.__name
            )
        if self.__max_size is not None:
            d["maxSize"] = (
                self.__max_size.as_dict()
                if hasattr(self.__max_size, "as_dict")
                else self.__max_size
            )
        if self.__stream_segment_size is not None:
            d["streamSegmentSize"] = (
                self.__stream_segment_size.as_dict()
                if hasattr(self.__stream_segment_size, "as_dict")
                else self.__stream_segment_size
            )
        if self.__time_to_live_millis is not None:
            d["timeToLiveMillis"] = (
                self.__time_to_live_millis.as_dict()
                if hasattr(self.__time_to_live_millis, "as_dict")
                else self.__time_to_live_millis
            )
        if self.__strategy_on_full is not None:
            d["strategyOnFull"] = (
                self.__strategy_on_full.as_dict()
                if hasattr(self.__strategy_on_full, "as_dict")
                else self.__strategy_on_full
            )
        if self.__persistence is not None:
            d["persistence"] = (
                self.__persistence.as_dict()
                if hasattr(self.__persistence, "as_dict")
                else self.__persistence
            )
        if self.__flush_on_write is not None:
            d["flushOnWrite"] = (
                self.__flush_on_write.as_dict()
                if hasattr(self.__flush_on_write, "as_dict")
                else self.__flush_on_write
            )
        if self.__export_definition is not None:
            d["exportDefinition"] = (
                self.__export_definition.as_dict()
                if hasattr(self.__export_definition, "as_dict")
                else self.__export_definition
            )
        return d

    def __repr__(self):
        return "<Class MessageStreamDefinition. name: {}, max_size: {}, stream_segment_size: {}, time_to_live_millis: {}, strategy_on_full: {}, persistence: {}, flush_on_write: {}, export_definition: {}>".format(
            self.__name,
            self.__max_size,
            self.__stream_segment_size,
            self.__time_to_live_millis,
            self.__strategy_on_full,
            self.__persistence,
            self.__flush_on_write,
            self.__export_definition,
        )


class MessageStreamInfo:
    """
    Message stream information including its definition, storage status and export status
    """

    class storageStatus:
        """
            Stream status including oldest/newest sequence number and total bytes
            """

        __slots__ = [
            "__oldest_sequence_number",
            "__newest_sequence_number",
            "__total_bytes",
        ]

        _types_map = {
            "oldest_sequence_number": {"type": int, "subtype": None},
            "newest_sequence_number": {"type": int, "subtype": None},
            "total_bytes": {"type": int, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "oldest_sequence_number": {"required": False},
            "newest_sequence_number": {"required": False},
            "total_bytes": {"required": False},
        }

        def __init__(
            self,
            oldest_sequence_number: int = None,
            newest_sequence_number: int = None,
            total_bytes: int = None,
        ):
            """
                :param oldest_sequence_number: The sequence number of the first message which is still accessible in the stream.
                :param newest_sequence_number: The sequence number of the last appended message.
                :param total_bytes: The current total size of the stream in bytes.
                """
            pass
            self.__oldest_sequence_number = oldest_sequence_number
            self.__newest_sequence_number = newest_sequence_number
            self.__total_bytes = total_bytes

        def _get_oldest_sequence_number(self):
            return self.__oldest_sequence_number

        def _set_oldest_sequence_number(self, value):
            if not isinstance(value, int):
                raise TypeError("oldest_sequence_number must be int")

            self.__oldest_sequence_number = value

        oldest_sequence_number = property(
            _get_oldest_sequence_number, _set_oldest_sequence_number
        )
        """
            The sequence number of the first message which is still accessible in the stream.
            """

        def _get_newest_sequence_number(self):
            return self.__newest_sequence_number

        def _set_newest_sequence_number(self, value):
            if not isinstance(value, int):
                raise TypeError("newest_sequence_number must be int")

            self.__newest_sequence_number = value

        newest_sequence_number = property(
            _get_newest_sequence_number, _set_newest_sequence_number
        )
        """
            The sequence number of the last appended message.
            """

        def _get_total_bytes(self):
            return self.__total_bytes

        def _set_total_bytes(self, value):
            if not isinstance(value, int):
                raise TypeError("total_bytes must be int")

            self.__total_bytes = value

        total_bytes = property(_get_total_bytes, _set_total_bytes)
        """
            The current total size of the stream in bytes.
            """

        @staticmethod
        def from_dict(d):
            v = {}
            if "oldestSequenceNumber" in d:
                v["oldest_sequence_number"] = (
                    int.from_dict(d["oldestSequenceNumber"])
                    if hasattr(int, "from_dict")
                    else d["oldestSequenceNumber"]
                )
            if "newestSequenceNumber" in d:
                v["newest_sequence_number"] = (
                    int.from_dict(d["newestSequenceNumber"])
                    if hasattr(int, "from_dict")
                    else d["newestSequenceNumber"]
                )
            if "totalBytes" in d:
                v["total_bytes"] = (
                    int.from_dict(d["totalBytes"])
                    if hasattr(int, "from_dict")
                    else d["totalBytes"]
                )
            return MessageStreamInfo.storageStatus(**v)

        def as_dict(self):
            d = {}
            if self.__oldest_sequence_number is not None:
                d["oldestSequenceNumber"] = (
                    self.__oldest_sequence_number.as_dict()
                    if hasattr(self.__oldest_sequence_number, "as_dict")
                    else self.__oldest_sequence_number
                )
            if self.__newest_sequence_number is not None:
                d["newestSequenceNumber"] = (
                    self.__newest_sequence_number.as_dict()
                    if hasattr(self.__newest_sequence_number, "as_dict")
                    else self.__newest_sequence_number
                )
            if self.__total_bytes is not None:
                d["totalBytes"] = (
                    self.__total_bytes.as_dict()
                    if hasattr(self.__total_bytes, "as_dict")
                    else self.__total_bytes
                )
            return d

        def __repr__(self):
            return "<Class storageStatus. oldest_sequence_number: {}, newest_sequence_number: {}, total_bytes: {}>".format(
                self.__oldest_sequence_number,
                self.__newest_sequence_number,
                self.__total_bytes,
            )

    class exportStatuses:
        """
            Export status including the export identifier and the last exported sequence number for that export task
            """

        __slots__ = [
            "__export_config_identifier",
            "__last_exported_sequence_number",
            "__last_export_time",
            "__error_message",
        ]

        _types_map = {
            "export_config_identifier": {"type": str, "subtype": None},
            "last_exported_sequence_number": {"type": int, "subtype": None},
            "last_export_time": {"type": int, "subtype": None},
            "error_message": {"type": str, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "export_config_identifier": {"required": False},
            "last_exported_sequence_number": {"required": True},
            "last_export_time": {"required": False},
            "error_message": {"required": False},
        }

        def __init__(
            self,
            export_config_identifier: str = None,
            last_exported_sequence_number: int = None,
            last_export_time: int = None,
            error_message: str = None,
        ):
            """
                :param export_config_identifier: The unique export identifier.
                :param last_exported_sequence_number: The sequence number of the last message which was successfully exported.
                :param last_export_time: The last time an export was attempted. Data is Unix epoch time in milliseconds.
                :param error_message: Error message from the last export attempt if it failed.
                """
            pass
            self.__export_config_identifier = export_config_identifier
            self.__last_exported_sequence_number = last_exported_sequence_number
            self.__last_export_time = last_export_time
            self.__error_message = error_message

        def _get_export_config_identifier(self):
            return self.__export_config_identifier

        def _set_export_config_identifier(self, value):
            if not isinstance(value, str):
                raise TypeError("export_config_identifier must be str")

            self.__export_config_identifier = value

        export_config_identifier = property(
            _get_export_config_identifier, _set_export_config_identifier
        )
        """
            The unique export identifier.
            """

        def _get_last_exported_sequence_number(self):
            return self.__last_exported_sequence_number

        def _set_last_exported_sequence_number(self, value):
            if not isinstance(value, int):
                raise TypeError("last_exported_sequence_number must be int")

            self.__last_exported_sequence_number = value

        last_exported_sequence_number = property(
            _get_last_exported_sequence_number, _set_last_exported_sequence_number
        )
        """
            The sequence number of the last message which was successfully exported.
            """

        def _get_last_export_time(self):
            return self.__last_export_time

        def _set_last_export_time(self, value):
            if not isinstance(value, int):
                raise TypeError("last_export_time must be int")

            self.__last_export_time = value

        last_export_time = property(_get_last_export_time, _set_last_export_time)
        """
            The last time an export was attempted. Data is Unix epoch time in milliseconds.
            """

        def _get_error_message(self):
            return self.__error_message

        def _set_error_message(self, value):
            if not isinstance(value, str):
                raise TypeError("error_message must be str")

            self.__error_message = value

        error_message = property(_get_error_message, _set_error_message)
        """
            Error message from the last export attempt if it failed.
            """

        @staticmethod
        def from_dict(d):
            v = {}
            if "exportConfigIdentifier" in d:
                v["export_config_identifier"] = (
                    str.from_dict(d["exportConfigIdentifier"])
                    if hasattr(str, "from_dict")
                    else d["exportConfigIdentifier"]
                )
            if "lastExportedSequenceNumber" in d:
                v["last_exported_sequence_number"] = (
                    int.from_dict(d["lastExportedSequenceNumber"])
                    if hasattr(int, "from_dict")
                    else d["lastExportedSequenceNumber"]
                )
            if "lastExportTime" in d:
                v["last_export_time"] = (
                    int.from_dict(d["lastExportTime"])
                    if hasattr(int, "from_dict")
                    else d["lastExportTime"]
                )
            if "errorMessage" in d:
                v["error_message"] = (
                    str.from_dict(d["errorMessage"])
                    if hasattr(str, "from_dict")
                    else d["errorMessage"]
                )
            return MessageStreamInfo.exportStatuses(**v)

        def as_dict(self):
            d = {}
            if self.__export_config_identifier is not None:
                d["exportConfigIdentifier"] = (
                    self.__export_config_identifier.as_dict()
                    if hasattr(self.__export_config_identifier, "as_dict")
                    else self.__export_config_identifier
                )
            if self.__last_exported_sequence_number is not None:
                d["lastExportedSequenceNumber"] = (
                    self.__last_exported_sequence_number.as_dict()
                    if hasattr(self.__last_exported_sequence_number, "as_dict")
                    else self.__last_exported_sequence_number
                )
            if self.__last_export_time is not None:
                d["lastExportTime"] = (
                    self.__last_export_time.as_dict()
                    if hasattr(self.__last_export_time, "as_dict")
                    else self.__last_export_time
                )
            if self.__error_message is not None:
                d["errorMessage"] = (
                    self.__error_message.as_dict()
                    if hasattr(self.__error_message, "as_dict")
                    else self.__error_message
                )
            return d

        def __repr__(self):
            return "<Class exportStatuses. export_config_identifier: {}, last_exported_sequence_number: {}, last_export_time: {}, error_message: {}>".format(
                self.__export_config_identifier,
                self.__last_exported_sequence_number,
                self.__last_export_time,
                self.__error_message,
            )

    __slots__ = ["__definition", "__storage_status", "__export_statuses"]

    _types_map = {
        "definition": {"type": MessageStreamDefinition, "subtype": None},
        "storage_status": {"type": storageStatus, "subtype": None},
        "export_statuses": {"type": list, "subtype": exportStatuses},
    }
    _formats_map = {}
    _validations_map = {
        "definition": {"required": True},
        "storage_status": {"required": True},
        "export_statuses": {"required": False},
    }

    def __init__(
        self,
        definition: MessageStreamDefinition = None,
        storage_status: storageStatus = None,
        export_statuses: List[exportStatuses] = None,
    ):
        """
        :param storage_status: Stream status including oldest/newest sequence number and total bytes
        """
        pass
        self.__definition = definition
        self.__storage_status = storage_status
        self.__export_statuses = export_statuses

    def _get_definition(self):
        return self.__definition

    def _set_definition(self, value):
        if not isinstance(value, MessageStreamDefinition):
            raise TypeError("definition must be MessageStreamDefinition")

        self.__definition = value

    definition = property(_get_definition, _set_definition)

    def _get_storage_status(self):
        return self.__storage_status

    def _set_storage_status(self, value):
        if not isinstance(value, MessageStreamInfo.storageStatus):
            raise TypeError("storage_status must be MessageStreamInfo.storageStatus")

        self.__storage_status = value

    storage_status = property(_get_storage_status, _set_storage_status)
    """
    Stream status including oldest/newest sequence number and total bytes
    """

    def _get_export_statuses(self):
        return self.__export_statuses

    def _set_export_statuses(self, value):
        if not isinstance(value, list):
            raise TypeError("export_statuses must be list")
        if not all(isinstance(i, MessageStreamInfo.exportStatuses) for i in value):
            raise TypeError(
                "export_statuses list values must be MessageStreamInfo.exportStatuses"
            )

        self.__export_statuses = value

    export_statuses = property(_get_export_statuses, _set_export_statuses)

    @staticmethod
    def from_dict(d):
        v = {}
        if "definition" in d:
            v["definition"] = (
                MessageStreamDefinition.from_dict(d["definition"])
                if hasattr(MessageStreamDefinition, "from_dict")
                else d["definition"]
            )
        if "storageStatus" in d:
            v["storage_status"] = (
                MessageStreamInfo.storageStatus.from_dict(d["storageStatus"])
                if hasattr(MessageStreamInfo.storageStatus, "from_dict")
                else d["storageStatus"]
            )
        if "exportStatuses" in d:
            v["export_statuses"] = [
                MessageStreamInfo.exportStatuses.from_dict(p)
                if hasattr(MessageStreamInfo.exportStatuses, "from_dict")
                else p
                for p in d["exportStatuses"]
            ]
        return MessageStreamInfo(**v)

    def as_dict(self):
        d = {}
        if self.__definition is not None:
            d["definition"] = (
                self.__definition.as_dict()
                if hasattr(self.__definition, "as_dict")
                else self.__definition
            )
        if self.__storage_status is not None:
            d["storageStatus"] = (
                self.__storage_status.as_dict()
                if hasattr(self.__storage_status, "as_dict")
                else self.__storage_status
            )
        if self.__export_statuses is not None:
            d["exportStatuses"] = [
                p.as_dict() if hasattr(p, "as_dict") else p
                for p in self.__export_statuses
            ]
        return d

    def __repr__(self):
        return "<Class MessageStreamInfo. definition: {}, storage_status: {}, export_statuses: {}>".format(
            self.__definition, self.__storage_status, self.__export_statuses
        )


class Message:
    """
    Message object containing metadata and the user's payload
    """

    __slots__ = ["__stream_name", "__sequence_number", "__ingest_time", "__payload"]

    _types_map = {
        "stream_name": {"type": str, "subtype": None},
        "sequence_number": {"type": int, "subtype": None},
        "ingest_time": {"type": int, "subtype": None},
        "payload": {"type": bytes, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "stream_name": {"required": True},
        "sequence_number": {"required": False},
        "ingest_time": {"required": False},
        "payload": {"required": True},
    }

    def __init__(
        self,
        stream_name: str = None,
        sequence_number: int = None,
        ingest_time: int = None,
        payload: bytes = None,
    ):
        """
        :param stream_name: The name of the stream which this message is in.
        :param sequence_number: The sequence number of this message within the stream.
        :param ingest_time: The time that the message was ingested to Stream Manager. Data is Unix epoch time in milliseconds.
        :param payload: The binary message data.
        """
        pass
        self.__stream_name = stream_name
        self.__sequence_number = sequence_number
        self.__ingest_time = ingest_time
        self.__payload = payload

    def _get_stream_name(self):
        return self.__stream_name

    def _set_stream_name(self, value):
        if not isinstance(value, str):
            raise TypeError("stream_name must be str")

        self.__stream_name = value

    stream_name = property(_get_stream_name, _set_stream_name)
    """
    The name of the stream which this message is in.
    """

    def _get_sequence_number(self):
        return self.__sequence_number

    def _set_sequence_number(self, value):
        if not isinstance(value, int):
            raise TypeError("sequence_number must be int")

        self.__sequence_number = value

    sequence_number = property(_get_sequence_number, _set_sequence_number)
    """
    The sequence number of this message within the stream.
    """

    def _get_ingest_time(self):
        return self.__ingest_time

    def _set_ingest_time(self, value):
        if not isinstance(value, int):
            raise TypeError("ingest_time must be int")

        self.__ingest_time = value

    ingest_time = property(_get_ingest_time, _set_ingest_time)
    """
    The time that the message was ingested to Stream Manager. Data is Unix epoch time in milliseconds.
    """

    def _get_payload(self):
        return self.__payload

    def _set_payload(self, value):
        if not isinstance(value, bytes):
            raise TypeError("payload must be bytes")

        self.__payload = value

    payload = property(_get_payload, _set_payload)
    """
    The binary message data.
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "streamName" in d:
            v["stream_name"] = (
                str.from_dict(d["streamName"])
                if hasattr(str, "from_dict")
                else d["streamName"]
            )
        if "sequenceNumber" in d:
            v["sequence_number"] = (
                int.from_dict(d["sequenceNumber"])
                if hasattr(int, "from_dict")
                else d["sequenceNumber"]
            )
        if "ingestTime" in d:
            v["ingest_time"] = (
                int.from_dict(d["ingestTime"])
                if hasattr(int, "from_dict")
                else d["ingestTime"]
            )
        if "payload" in d:
            v["payload"] = (
                bytes.from_dict(d["payload"])
                if hasattr(bytes, "from_dict")
                else d["payload"]
            )
        return Message(**v)

    def as_dict(self):
        d = {}
        if self.__stream_name is not None:
            d["streamName"] = (
                self.__stream_name.as_dict()
                if hasattr(self.__stream_name, "as_dict")
                else self.__stream_name
            )
        if self.__sequence_number is not None:
            d["sequenceNumber"] = (
                self.__sequence_number.as_dict()
                if hasattr(self.__sequence_number, "as_dict")
                else self.__sequence_number
            )
        if self.__ingest_time is not None:
            d["ingestTime"] = (
                self.__ingest_time.as_dict()
                if hasattr(self.__ingest_time, "as_dict")
                else self.__ingest_time
            )
        if self.__payload is not None:
            d["payload"] = (
                self.__payload.as_dict()
                if hasattr(self.__payload, "as_dict")
                else self.__payload
            )
        return d

    def __repr__(self):
        return "<Class Message. stream_name: {}, sequence_number: {}, ingest_time: {}, payload: {}>".format(
            self.__stream_name,
            self.__sequence_number,
            self.__ingest_time,
            self.__payload,
        )


class ReadMessagesOptions:
    """
    Options for the ReadMessages API. All fields are optional.
    """

    __slots__ = [
        "__desired_start_sequence_number",
        "__min_message_count",
        "__max_message_count",
        "__read_timeout_millis",
    ]

    _types_map = {
        "desired_start_sequence_number": {"type": int, "subtype": None},
        "min_message_count": {"type": int, "subtype": None},
        "max_message_count": {"type": int, "subtype": None},
        "read_timeout_millis": {"type": int, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "desired_start_sequence_number": {
            "required": False,
            "maximum": 9223372036854775807,
            "minimum": 0,
        },
        "min_message_count": {"required": False, "maximum": 2147483647, "minimum": 1},
        "max_message_count": {"required": False, "maximum": 2147483647, "minimum": 1},
        "read_timeout_millis": {
            "required": False,
            "maximum": 9223372036854,
            "minimum": 0,
        },
    }

    def __init__(
        self,
        desired_start_sequence_number: int = None,
        min_message_count: int = 1,
        max_message_count: int = None,
        read_timeout_millis: int = 0,
    ):
        """
        :param desired_start_sequence_number: The desired beginning sequence number to start reading from. If the desired sequence number is less than the current minimum of the stream, then it will instead start reading from the current minimum.
        :param min_message_count: The minimum number of messages that will be returned. If not enough messages are available for reading, then NotEnoughMessages exception will be thrown.
            The minimum values is 1 and the maximum value is 2147483647.
        :param max_message_count: The maximum number of messages that will be returned.
            The minimum values is the value of the minimum message count and the maximum value is 2147483647.
        :param read_timeout_millis: The time to wait for messages in milliseconds. Default is 0, meaning that the server will not wait for messages.
            If it can fulfill the minimum messages it will return them, but otherwise NotEnoughMessages exception will be thrown.
            If the timeout is greater than zero, then the server will wait up to that time for more messages to be appended to the stream, waiting until the minimum number of messages is reached.
            The maximum value is the value of the client timeout.
        """
        pass
        self.__desired_start_sequence_number = desired_start_sequence_number
        self.__min_message_count = min_message_count
        self.__max_message_count = max_message_count
        self.__read_timeout_millis = read_timeout_millis

    def _get_desired_start_sequence_number(self):
        return self.__desired_start_sequence_number

    def _set_desired_start_sequence_number(self, value):
        if not isinstance(value, int):
            raise TypeError("desired_start_sequence_number must be int")

        self.__desired_start_sequence_number = value

    desired_start_sequence_number = property(
        _get_desired_start_sequence_number, _set_desired_start_sequence_number
    )
    """
    The desired beginning sequence number to start reading from. If the desired sequence number is less than the current minimum of the stream, then it will instead start reading from the current minimum.
    """

    def _get_min_message_count(self):
        return self.__min_message_count

    def _set_min_message_count(self, value):
        if not isinstance(value, int):
            raise TypeError("min_message_count must be int")

        self.__min_message_count = value

    min_message_count = property(_get_min_message_count, _set_min_message_count)
    """
    The minimum number of messages that will be returned. If not enough messages are available for reading, then NotEnoughMessages exception will be thrown.
    The minimum values is 1 and the maximum value is 2147483647.
    """

    def _get_max_message_count(self):
        return self.__max_message_count

    def _set_max_message_count(self, value):
        if not isinstance(value, int):
            raise TypeError("max_message_count must be int")

        self.__max_message_count = value

    max_message_count = property(_get_max_message_count, _set_max_message_count)
    """
    The maximum number of messages that will be returned.
    The minimum values is the value of the minimum message count and the maximum value is 2147483647.
    """

    def _get_read_timeout_millis(self):
        return self.__read_timeout_millis

    def _set_read_timeout_millis(self, value):
        if not isinstance(value, int):
            raise TypeError("read_timeout_millis must be int")

        self.__read_timeout_millis = value

    read_timeout_millis = property(_get_read_timeout_millis, _set_read_timeout_millis)
    """
    The time to wait for messages in milliseconds. Default is 0, meaning that the server will not wait for messages.
    If it can fulfill the minimum messages it will return them, but otherwise NotEnoughMessages exception will be thrown.
    If the timeout is greater than zero, then the server will wait up to that time for more messages to be appended to the stream, waiting until the minimum number of messages is reached.
    The maximum value is the value of the client timeout.
    """

    @staticmethod
    def from_dict(d):
        v = {}
        if "desiredStartSequenceNumber" in d:
            v["desired_start_sequence_number"] = (
                int.from_dict(d["desiredStartSequenceNumber"])
                if hasattr(int, "from_dict")
                else d["desiredStartSequenceNumber"]
            )
        if "minMessageCount" in d:
            v["min_message_count"] = (
                int.from_dict(d["minMessageCount"])
                if hasattr(int, "from_dict")
                else d["minMessageCount"]
            )
        if "maxMessageCount" in d:
            v["max_message_count"] = (
                int.from_dict(d["maxMessageCount"])
                if hasattr(int, "from_dict")
                else d["maxMessageCount"]
            )
        if "readTimeoutMillis" in d:
            v["read_timeout_millis"] = (
                int.from_dict(d["readTimeoutMillis"])
                if hasattr(int, "from_dict")
                else d["readTimeoutMillis"]
            )
        return ReadMessagesOptions(**v)

    def as_dict(self):
        d = {}
        if self.__desired_start_sequence_number is not None:
            d["desiredStartSequenceNumber"] = (
                self.__desired_start_sequence_number.as_dict()
                if hasattr(self.__desired_start_sequence_number, "as_dict")
                else self.__desired_start_sequence_number
            )
        if self.__min_message_count is not None:
            d["minMessageCount"] = (
                self.__min_message_count.as_dict()
                if hasattr(self.__min_message_count, "as_dict")
                else self.__min_message_count
            )
        if self.__max_message_count is not None:
            d["maxMessageCount"] = (
                self.__max_message_count.as_dict()
                if hasattr(self.__max_message_count, "as_dict")
                else self.__max_message_count
            )
        if self.__read_timeout_millis is not None:
            d["readTimeoutMillis"] = (
                self.__read_timeout_millis.as_dict()
                if hasattr(self.__read_timeout_millis, "as_dict")
                else self.__read_timeout_millis
            )
        return d

    def __repr__(self):
        return "<Class ReadMessagesOptions. desired_start_sequence_number: {}, min_message_count: {}, max_message_count: {}, read_timeout_millis: {}>".format(
            self.__desired_start_sequence_number,
            self.__min_message_count,
            self.__max_message_count,
            self.__read_timeout_millis,
        )


class CreateMessageStreamRequest:
    """
    (Internal Only) Request object for creating a message stream
    """

    __slots__ = ["__request_id", "__definition"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "definition": {"type": MessageStreamDefinition, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "definition": {"required": True},
    }

    def __init__(
        self, request_id: str = None, definition: MessageStreamDefinition = None
    ):
        pass
        self.__request_id = request_id
        self.__definition = definition

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_definition(self):
        return self.__definition

    def _set_definition(self, value):
        if not isinstance(value, MessageStreamDefinition):
            raise TypeError("definition must be MessageStreamDefinition")

        self.__definition = value

    definition = property(_get_definition, _set_definition)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "definition" in d:
            v["definition"] = (
                MessageStreamDefinition.from_dict(d["definition"])
                if hasattr(MessageStreamDefinition, "from_dict")
                else d["definition"]
            )
        return CreateMessageStreamRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__definition is not None:
            d["definition"] = (
                self.__definition.as_dict()
                if hasattr(self.__definition, "as_dict")
                else self.__definition
            )
        return d

    def __repr__(self):
        return "<Class CreateMessageStreamRequest. request_id: {}, definition: {}>".format(
            self.__request_id, self.__definition
        )


class CreateMessageStreamResponse:
    """
    Internal Only
    """

    __slots__ = ["__request_id", "__status", "__error_message"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "status": {"required": True},
        "error_message": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
    ):
        pass
        self.__request_id = request_id
        self.__status = status
        self.__error_message = error_message

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        return CreateMessageStreamResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        return d

    def __repr__(self):
        return "<Class CreateMessageStreamResponse. request_id: {}, status: {}, error_message: {}>".format(
            self.__request_id, self.__status, self.__error_message
        )


class DeleteMessageStreamRequest:
    """
    (Internal Only) Request object for deleting a message stream
    """

    __slots__ = ["__request_id", "__name"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "name": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "name": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
    }

    def __init__(self, request_id: str = None, name: str = None):
        pass
        self.__request_id = request_id
        self.__name = name

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_name(self):
        return self.__name

    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value

    name = property(_get_name, _set_name)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "name" in d:
            v["name"] = (
                str.from_dict(d["name"]) if hasattr(str, "from_dict") else d["name"]
            )
        return DeleteMessageStreamRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__name is not None:
            d["name"] = (
                self.__name.as_dict()
                if hasattr(self.__name, "as_dict")
                else self.__name
            )
        return d

    def __repr__(self):
        return "<Class DeleteMessageStreamRequest. request_id: {}, name: {}>".format(
            self.__request_id, self.__name
        )


class DeleteMessageStreamResponse:
    """
    Internal Only
    """

    __slots__ = ["__request_id", "__status", "__error_message"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "status": {"required": True},
        "error_message": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
    ):
        pass
        self.__request_id = request_id
        self.__status = status
        self.__error_message = error_message

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        return DeleteMessageStreamResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        return d

    def __repr__(self):
        return "<Class DeleteMessageStreamResponse. request_id: {}, status: {}, error_message: {}>".format(
            self.__request_id, self.__status, self.__error_message
        )


class DescribeMessageStreamRequest:
    """
    (Internal Only) Request object for describing a message stream
    """

    __slots__ = ["__request_id", "__name"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "name": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "name": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
    }

    def __init__(self, request_id: str = None, name: str = None):
        pass
        self.__request_id = request_id
        self.__name = name

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_name(self):
        return self.__name

    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value

    name = property(_get_name, _set_name)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "name" in d:
            v["name"] = (
                str.from_dict(d["name"]) if hasattr(str, "from_dict") else d["name"]
            )
        return DescribeMessageStreamRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__name is not None:
            d["name"] = (
                self.__name.as_dict()
                if hasattr(self.__name, "as_dict")
                else self.__name
            )
        return d

    def __repr__(self):
        return "<Class DescribeMessageStreamRequest. request_id: {}, name: {}>".format(
            self.__request_id, self.__name
        )


class DescribeMessageStreamResponse:
    """
    (Internal Only) Response object for describing a message stream
    """

    __slots__ = ["__request_id", "__status", "__error_message", "__message_stream_info"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
        "message_stream_info": {"type": MessageStreamInfo, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "status": {"required": True},
        "error_message": {"required": False},
        "message_stream_info": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
        message_stream_info: MessageStreamInfo = None,
    ):
        pass
        self.__request_id = request_id
        self.__status = status
        self.__error_message = error_message
        self.__message_stream_info = message_stream_info

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    def _get_message_stream_info(self):
        return self.__message_stream_info

    def _set_message_stream_info(self, value):
        if not isinstance(value, MessageStreamInfo):
            raise TypeError("message_stream_info must be MessageStreamInfo")

        self.__message_stream_info = value

    message_stream_info = property(_get_message_stream_info, _set_message_stream_info)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        if "messageStreamInfo" in d:
            v["message_stream_info"] = (
                MessageStreamInfo.from_dict(d["messageStreamInfo"])
                if hasattr(MessageStreamInfo, "from_dict")
                else d["messageStreamInfo"]
            )
        return DescribeMessageStreamResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        if self.__message_stream_info is not None:
            d["messageStreamInfo"] = (
                self.__message_stream_info.as_dict()
                if hasattr(self.__message_stream_info, "as_dict")
                else self.__message_stream_info
            )
        return d

    def __repr__(self):
        return "<Class DescribeMessageStreamResponse. request_id: {}, status: {}, error_message: {}, message_stream_info: {}>".format(
            self.__request_id,
            self.__status,
            self.__error_message,
            self.__message_stream_info,
        )


class AppendMessageRequest:
    """
    (Intenral Only) Request object for appending to a message stream
    """

    __slots__ = ["__request_id", "__name", "__payload"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "name": {"type": str, "subtype": None},
        "payload": {"type": bytes, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "name": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
        "payload": {"required": True, "minLength": 1},
    }

    def __init__(self, request_id: str = None, name: str = None, payload: bytes = None):
        pass
        self.__request_id = request_id
        self.__name = name
        self.__payload = payload

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_name(self):
        return self.__name

    def _set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value

    name = property(_get_name, _set_name)

    def _get_payload(self):
        return self.__payload

    def _set_payload(self, value):
        if not isinstance(value, bytes):
            raise TypeError("payload must be bytes")

        self.__payload = value

    payload = property(_get_payload, _set_payload)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "name" in d:
            v["name"] = (
                str.from_dict(d["name"]) if hasattr(str, "from_dict") else d["name"]
            )
        if "payload" in d:
            v["payload"] = (
                bytes.from_dict(d["payload"])
                if hasattr(bytes, "from_dict")
                else d["payload"]
            )
        return AppendMessageRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__name is not None:
            d["name"] = (
                self.__name.as_dict()
                if hasattr(self.__name, "as_dict")
                else self.__name
            )
        if self.__payload is not None:
            d["payload"] = (
                self.__payload.as_dict()
                if hasattr(self.__payload, "as_dict")
                else self.__payload
            )
        return d

    def __repr__(self):
        return "<Class AppendMessageRequest. request_id: {}, name: {}, payload: {}>".format(
            self.__request_id, self.__name, self.__payload
        )


class AppendMessageResponse:
    """
    Internal Only
    """

    __slots__ = ["__request_id", "__status", "__error_message", "__sequence_number"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
        "sequence_number": {"type": int, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "status": {"required": True},
        "error_message": {"required": False},
        "sequence_number": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
        sequence_number: int = None,
    ):
        pass
        self.__request_id = request_id
        self.__status = status
        self.__error_message = error_message
        self.__sequence_number = sequence_number

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    def _get_sequence_number(self):
        return self.__sequence_number

    def _set_sequence_number(self, value):
        if not isinstance(value, int):
            raise TypeError("sequence_number must be int")

        self.__sequence_number = value

    sequence_number = property(_get_sequence_number, _set_sequence_number)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        if "sequenceNumber" in d:
            v["sequence_number"] = (
                int.from_dict(d["sequenceNumber"])
                if hasattr(int, "from_dict")
                else d["sequenceNumber"]
            )
        return AppendMessageResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        if self.__sequence_number is not None:
            d["sequenceNumber"] = (
                self.__sequence_number.as_dict()
                if hasattr(self.__sequence_number, "as_dict")
                else self.__sequence_number
            )
        return d

    def __repr__(self):
        return "<Class AppendMessageResponse. request_id: {}, status: {}, error_message: {}, sequence_number: {}>".format(
            self.__request_id,
            self.__status,
            self.__error_message,
            self.__sequence_number,
        )


class ReadMessagesRequest:
    """
    (Internal Only) Request object for reading from a message stream. readMessagesOptions is optional.
    """

    __slots__ = ["__request_id", "__stream_name", "__read_messages_options"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "stream_name": {"type": str, "subtype": None},
        "read_messages_options": {"type": ReadMessagesOptions, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "stream_name": {
            "required": True,
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^[\w ,.\-_]*$",
        },
        "read_messages_options": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        stream_name: str = None,
        read_messages_options: ReadMessagesOptions = None,
    ):
        pass
        self.__request_id = request_id
        self.__stream_name = stream_name
        self.__read_messages_options = read_messages_options

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_stream_name(self):
        return self.__stream_name

    def _set_stream_name(self, value):
        if not isinstance(value, str):
            raise TypeError("stream_name must be str")

        self.__stream_name = value

    stream_name = property(_get_stream_name, _set_stream_name)

    def _get_read_messages_options(self):
        return self.__read_messages_options

    def _set_read_messages_options(self, value):
        if not isinstance(value, ReadMessagesOptions):
            raise TypeError("read_messages_options must be ReadMessagesOptions")

        self.__read_messages_options = value

    read_messages_options = property(
        _get_read_messages_options, _set_read_messages_options
    )

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "streamName" in d:
            v["stream_name"] = (
                str.from_dict(d["streamName"])
                if hasattr(str, "from_dict")
                else d["streamName"]
            )
        if "readMessagesOptions" in d:
            v["read_messages_options"] = (
                ReadMessagesOptions.from_dict(d["readMessagesOptions"])
                if hasattr(ReadMessagesOptions, "from_dict")
                else d["readMessagesOptions"]
            )
        return ReadMessagesRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__stream_name is not None:
            d["streamName"] = (
                self.__stream_name.as_dict()
                if hasattr(self.__stream_name, "as_dict")
                else self.__stream_name
            )
        if self.__read_messages_options is not None:
            d["readMessagesOptions"] = (
                self.__read_messages_options.as_dict()
                if hasattr(self.__read_messages_options, "as_dict")
                else self.__read_messages_options
            )
        return d

    def __repr__(self):
        return "<Class ReadMessagesRequest. request_id: {}, stream_name: {}, read_messages_options: {}>".format(
            self.__request_id, self.__stream_name, self.__read_messages_options
        )


class ReadMessagesResponse:
    """
    Internal Only
    """

    __slots__ = ["__request_id", "__messages", "__status", "__error_message"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "messages": {"type": list, "subtype": Message},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": False, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "messages": {"required": False},
        "status": {"required": False},
        "error_message": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        messages: List[Message] = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
    ):
        pass
        self.__request_id = request_id
        self.__messages = messages
        self.__status = status
        self.__error_message = error_message

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_messages(self):
        return self.__messages

    def _set_messages(self, value):
        if not isinstance(value, list):
            raise TypeError("messages must be list")
        if not all(isinstance(i, Message) for i in value):
            raise TypeError("messages list values must be Message")

        self.__messages = value

    messages = property(_get_messages, _set_messages)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "messages" in d:
            v["messages"] = [
                Message.from_dict(p) if hasattr(Message, "from_dict") else p
                for p in d["messages"]
            ]
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        return ReadMessagesResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__messages is not None:
            d["messages"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__messages
            ]
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        return d

    def __repr__(self):
        return "<Class ReadMessagesResponse. request_id: {}, messages: {}, status: {}, error_message: {}>".format(
            self.__request_id, self.__messages, self.__status, self.__error_message
        )


class ListStreamsRequest:
    """
    (Internal Only) Request object to list all available streams. There are no options.
    """

    __slots__ = ["__request_id"]

    _types_map = {"request_id": {"type": str, "subtype": None}}
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"}
    }

    def __init__(self, request_id: str = None):
        pass
        self.__request_id = request_id

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        return ListStreamsRequest(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        return d

    def __repr__(self):
        return "<Class ListStreamsRequest. request_id: {}>".format(self.__request_id)


class ListStreamsResponse:
    """
    Internal Only
    """

    __slots__ = ["__request_id", "__status", "__error_message", "__streams"]

    _types_map = {
        "request_id": {"type": str, "subtype": None},
        "status": {"type": ResponseStatusCode, "subtype": None},
        "error_message": {"type": str, "subtype": None},
        "streams": {"type": list, "subtype": str},
    }
    _formats_map = {}
    _validations_map = {
        "request_id": {"required": True, "minLength": 1, "pattern": "^[\w ,.\-_]*$"},
        "status": {"required": True},
        "error_message": {"required": False},
        "streams": {"required": False},
    }

    def __init__(
        self,
        request_id: str = None,
        status: ResponseStatusCode = None,
        error_message: str = None,
        streams: List[str] = None,
    ):
        pass
        self.__request_id = request_id
        self.__status = status
        self.__error_message = error_message
        self.__streams = streams

    def _get_request_id(self):
        return self.__request_id

    def _set_request_id(self, value):
        if not isinstance(value, str):
            raise TypeError("request_id must be str")

        self.__request_id = value

    request_id = property(_get_request_id, _set_request_id)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, ResponseStatusCode):
            raise TypeError("status must be ResponseStatusCode")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_error_message(self):
        return self.__error_message

    def _set_error_message(self, value):
        if not isinstance(value, str):
            raise TypeError("error_message must be str")

        self.__error_message = value

    error_message = property(_get_error_message, _set_error_message)

    def _get_streams(self):
        return self.__streams

    def _set_streams(self, value):
        if not isinstance(value, list):
            raise TypeError("streams must be list")
        if not all(isinstance(i, str) for i in value):
            raise TypeError("streams list values must be str")

        self.__streams = value

    streams = property(_get_streams, _set_streams)

    @staticmethod
    def from_dict(d):
        v = {}
        if "requestId" in d:
            v["request_id"] = (
                str.from_dict(d["requestId"])
                if hasattr(str, "from_dict")
                else d["requestId"]
            )
        if "status" in d:
            v["status"] = (
                ResponseStatusCode.from_dict(d["status"])
                if hasattr(ResponseStatusCode, "from_dict")
                else d["status"]
            )
        if "errorMessage" in d:
            v["error_message"] = (
                str.from_dict(d["errorMessage"])
                if hasattr(str, "from_dict")
                else d["errorMessage"]
            )
        if "streams" in d:
            v["streams"] = [
                str.from_dict(p) if hasattr(str, "from_dict") else p
                for p in d["streams"]
            ]
        return ListStreamsResponse(**v)

    def as_dict(self):
        d = {}
        if self.__request_id is not None:
            d["requestId"] = (
                self.__request_id.as_dict()
                if hasattr(self.__request_id, "as_dict")
                else self.__request_id
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__error_message is not None:
            d["errorMessage"] = (
                self.__error_message.as_dict()
                if hasattr(self.__error_message, "as_dict")
                else self.__error_message
            )
        if self.__streams is not None:
            d["streams"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__streams
            ]
        return d

    def __repr__(self):
        return "<Class ListStreamsResponse. request_id: {}, status: {}, error_message: {}, streams: {}>".format(
            self.__request_id, self.__status, self.__error_message, self.__streams
        )
