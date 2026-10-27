from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OAuthProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    O_AUTH_PROVIDER_UNSPECIFIED: _ClassVar[OAuthProvider]
    O_AUTH_PROVIDER_GOOGLE: _ClassVar[OAuthProvider]

class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_TYPE_UNSPECIFIED: _ClassVar[ClientType]
    CLIENT_TYPE_WEB: _ClassVar[ClientType]
    CLIENT_TYPE_MOBILE: _ClassVar[ClientType]
O_AUTH_PROVIDER_UNSPECIFIED: OAuthProvider
O_AUTH_PROVIDER_GOOGLE: OAuthProvider
CLIENT_TYPE_UNSPECIFIED: ClientType
CLIENT_TYPE_WEB: ClientType
CLIENT_TYPE_MOBILE: ClientType

class BeginOAuthLoginRequest(_message.Message):
    __slots__ = ("provider", "client_type", "initiator_binding")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_BINDING_FIELD_NUMBER: _ClassVar[int]
    provider: OAuthProvider
    client_type: ClientType
    initiator_binding: str
    def __init__(self, provider: _Optional[_Union[OAuthProvider, str]] = ..., client_type: _Optional[_Union[ClientType, str]] = ..., initiator_binding: _Optional[str] = ...) -> None: ...

class BeginOAuthLoginResponse(_message.Message):
    __slots__ = ("authorization_url", "state", "transaction_id", "expires_at")
    AUTHORIZATION_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    authorization_url: str
    state: str
    transaction_id: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, authorization_url: _Optional[str] = ..., state: _Optional[str] = ..., transaction_id: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FinishOAuthLoginRequest(_message.Message):
    __slots__ = ("provider", "code", "state", "initiator_binding", "client_ip", "user_agent")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_BINDING_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    provider: OAuthProvider
    code: str
    state: str
    initiator_binding: str
    client_ip: str
    user_agent: str
    def __init__(self, provider: _Optional[_Union[OAuthProvider, str]] = ..., code: _Optional[str] = ..., state: _Optional[str] = ..., initiator_binding: _Optional[str] = ..., client_ip: _Optional[str] = ..., user_agent: _Optional[str] = ...) -> None: ...

class FinishOAuthLoginResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "user_id", "access_token_expires_at", "refresh_token_expires_at", "is_new_user", "client_type")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_USER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    user_id: str
    access_token_expires_at: _timestamp_pb2.Timestamp
    refresh_token_expires_at: _timestamp_pb2.Timestamp
    is_new_user: bool
    client_type: ClientType
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., user_id: _Optional[str] = ..., access_token_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_token_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_new_user: bool = ..., client_type: _Optional[_Union[ClientType, str]] = ...) -> None: ...
