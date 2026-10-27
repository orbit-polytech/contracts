import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from orbit.auth.v1 import oauth_pb2 as _oauth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinkedIdentity(_message.Message):
    __slots__ = ("id", "provider", "provider_subject", "email", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    provider: _oauth_pb2.OAuthProvider
    provider_subject: str
    email: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., provider: _Optional[_Union[_oauth_pb2.OAuthProvider, str]] = ..., provider_subject: _Optional[str] = ..., email: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BeginIdentityLinkRequest(_message.Message):
    __slots__ = ("user_id", "provider", "client_type", "initiator_binding", "reauth_proof")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_BINDING_FIELD_NUMBER: _ClassVar[int]
    REAUTH_PROOF_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    provider: _oauth_pb2.OAuthProvider
    client_type: _oauth_pb2.ClientType
    initiator_binding: str
    reauth_proof: str
    def __init__(self, user_id: _Optional[str] = ..., provider: _Optional[_Union[_oauth_pb2.OAuthProvider, str]] = ..., client_type: _Optional[_Union[_oauth_pb2.ClientType, str]] = ..., initiator_binding: _Optional[str] = ..., reauth_proof: _Optional[str] = ...) -> None: ...

class BeginIdentityLinkResponse(_message.Message):
    __slots__ = ("authorization_url", "state", "transaction_id", "expires_at")
    AUTHORIZATION_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    authorization_url: str
    state: str
    transaction_id: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, authorization_url: _Optional[str] = ..., state: _Optional[str] = ..., transaction_id: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FinishIdentityLinkRequest(_message.Message):
    __slots__ = ("provider", "code", "state", "initiator_binding")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_BINDING_FIELD_NUMBER: _ClassVar[int]
    provider: _oauth_pb2.OAuthProvider
    code: str
    state: str
    initiator_binding: str
    def __init__(self, provider: _Optional[_Union[_oauth_pb2.OAuthProvider, str]] = ..., code: _Optional[str] = ..., state: _Optional[str] = ..., initiator_binding: _Optional[str] = ...) -> None: ...

class FinishIdentityLinkResponse(_message.Message):
    __slots__ = ("identity",)
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    identity: LinkedIdentity
    def __init__(self, identity: _Optional[_Union[LinkedIdentity, _Mapping]] = ...) -> None: ...

class ListLinkedIdentitiesRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ListLinkedIdentitiesResponse(_message.Message):
    __slots__ = ("identities",)
    IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    identities: _containers.RepeatedCompositeFieldContainer[LinkedIdentity]
    def __init__(self, identities: _Optional[_Iterable[_Union[LinkedIdentity, _Mapping]]] = ...) -> None: ...

class UnlinkIdentityRequest(_message.Message):
    __slots__ = ("user_id", "provider", "reauth_proof")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REAUTH_PROOF_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    provider: _oauth_pb2.OAuthProvider
    reauth_proof: str
    def __init__(self, user_id: _Optional[str] = ..., provider: _Optional[_Union[_oauth_pb2.OAuthProvider, str]] = ..., reauth_proof: _Optional[str] = ...) -> None: ...

class UnlinkIdentityResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
