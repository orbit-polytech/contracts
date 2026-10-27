import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from orbit.auth.v1 import identity_pb2 as _identity_pb2
from orbit.auth.v1 import oauth_pb2 as _oauth_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendCodeRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class SendCodeResponse(_message.Message):
    __slots__ = ("retry_after_seconds", "expires_in_seconds")
    RETRY_AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    retry_after_seconds: int
    expires_in_seconds: int
    def __init__(self, retry_after_seconds: _Optional[int] = ..., expires_in_seconds: _Optional[int] = ...) -> None: ...

class VerifyCodeRequest(_message.Message):
    __slots__ = ("email", "code", "client_ip", "user_agent")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    email: str
    code: str
    client_ip: str
    user_agent: str
    def __init__(self, email: _Optional[str] = ..., code: _Optional[str] = ..., client_ip: _Optional[str] = ..., user_agent: _Optional[str] = ...) -> None: ...

class VerifyCodeResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "user_id", "access_token_expires_at", "refresh_token_expires_at", "is_new_user")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_USER_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    user_id: str
    access_token_expires_at: _timestamp_pb2.Timestamp
    refresh_token_expires_at: _timestamp_pb2.Timestamp
    is_new_user: bool
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., user_id: _Optional[str] = ..., access_token_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_token_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_new_user: _Optional[bool] = ...) -> None: ...

class RefreshTokenRequest(_message.Message):
    __slots__ = ("refresh_token", "client_ip", "user_agent")
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    client_ip: str
    user_agent: str
    def __init__(self, refresh_token: _Optional[str] = ..., client_ip: _Optional[str] = ..., user_agent: _Optional[str] = ...) -> None: ...

class RefreshTokenResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "access_token_expires_at", "refresh_token_expires_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    access_token_expires_at: _timestamp_pb2.Timestamp
    refresh_token_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_token_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_token_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
