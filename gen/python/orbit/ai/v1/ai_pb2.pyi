from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHUNK_STAGE_UNSPECIFIED: _ClassVar[ChunkStage]
    CHUNK_STAGE_START: _ClassVar[ChunkStage]
    CHUNK_STAGE_DELTA: _ClassVar[ChunkStage]
    CHUNK_STAGE_CITATIONS: _ClassVar[ChunkStage]
    CHUNK_STAGE_DONE: _ClassVar[ChunkStage]
    CHUNK_STAGE_ERROR: _ClassVar[ChunkStage]
    CHUNK_STAGE_CANCELLED: _ClassVar[ChunkStage]
    CHUNK_STAGE_RETRIEVAL: _ClassVar[ChunkStage]

class FeedbackRating(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEEDBACK_RATING_UNSPECIFIED: _ClassVar[FeedbackRating]
    FEEDBACK_RATING_UP: _ClassVar[FeedbackRating]
    FEEDBACK_RATING_DOWN: _ClassVar[FeedbackRating]
CHUNK_STAGE_UNSPECIFIED: ChunkStage
CHUNK_STAGE_START: ChunkStage
CHUNK_STAGE_DELTA: ChunkStage
CHUNK_STAGE_CITATIONS: ChunkStage
CHUNK_STAGE_DONE: ChunkStage
CHUNK_STAGE_ERROR: ChunkStage
CHUNK_STAGE_CANCELLED: ChunkStage
CHUNK_STAGE_RETRIEVAL: ChunkStage
FEEDBACK_RATING_UNSPECIFIED: FeedbackRating
FEEDBACK_RATING_UP: FeedbackRating
FEEDBACK_RATING_DOWN: FeedbackRating

class StudentContext(_message.Message):
    __slots__ = ("group_title", "faculty", "course")
    GROUP_TITLE_FIELD_NUMBER: _ClassVar[int]
    FACULTY_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    group_title: str
    faculty: str
    course: int
    def __init__(self, group_title: _Optional[str] = ..., faculty: _Optional[str] = ..., course: _Optional[int] = ...) -> None: ...

class SourceCitation(_message.Message):
    __slots__ = ("document_title", "section", "url", "relevance_score", "excerpt")
    DOCUMENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    EXCERPT_FIELD_NUMBER: _ClassVar[int]
    document_title: str
    section: str
    url: str
    relevance_score: float
    excerpt: str
    def __init__(self, document_title: _Optional[str] = ..., section: _Optional[str] = ..., url: _Optional[str] = ..., relevance_score: _Optional[float] = ..., excerpt: _Optional[str] = ...) -> None: ...

class ChatStreamRequest(_message.Message):
    __slots__ = ("conversation_id", "message_id", "query", "context", "model", "user_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    message_id: str
    query: str
    context: StudentContext
    model: str
    user_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., message_id: _Optional[str] = ..., query: _Optional[str] = ..., context: _Optional[_Union[StudentContext, _Mapping]] = ..., model: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ChatStreamResponse(_message.Message):
    __slots__ = ("stage", "delta_text", "citations", "error_message", "error_code", "conversation_id", "message_id", "duration_ms", "retry_after_sec")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    DELTA_TEXT_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_SEC_FIELD_NUMBER: _ClassVar[int]
    stage: ChunkStage
    delta_text: str
    citations: _containers.RepeatedCompositeFieldContainer[SourceCitation]
    error_message: str
    error_code: int
    conversation_id: str
    message_id: str
    duration_ms: int
    retry_after_sec: int
    def __init__(self, stage: _Optional[_Union[ChunkStage, str]] = ..., delta_text: _Optional[str] = ..., citations: _Optional[_Iterable[_Union[SourceCitation, _Mapping]]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[int] = ..., conversation_id: _Optional[str] = ..., message_id: _Optional[str] = ..., duration_ms: _Optional[int] = ..., retry_after_sec: _Optional[int] = ...) -> None: ...

class CancelGenerationRequest(_message.Message):
    __slots__ = ("conversation_id", "message_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    message_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., message_id: _Optional[str] = ...) -> None: ...

class CancelGenerationResponse(_message.Message):
    __slots__ = ("cancelled",)
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    cancelled: bool
    def __init__(self, cancelled: bool = ...) -> None: ...

class ConversationSummary(_message.Message):
    __slots__ = ("id", "title", "created_at", "updated_at", "messages_count", "last_message_snippet")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_SNIPPET_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    messages_count: int
    last_message_snippet: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., messages_count: _Optional[int] = ..., last_message_snippet: _Optional[str] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("id", "role", "content", "citations", "created_at", "duration_ms", "feedback_rating", "feedback_reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_RATING_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    role: str
    content: str
    citations: _containers.RepeatedCompositeFieldContainer[SourceCitation]
    created_at: _timestamp_pb2.Timestamp
    duration_ms: int
    feedback_rating: FeedbackRating
    feedback_reason: str
    def __init__(self, id: _Optional[str] = ..., role: _Optional[str] = ..., content: _Optional[str] = ..., citations: _Optional[_Iterable[_Union[SourceCitation, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[int] = ..., feedback_rating: _Optional[_Union[FeedbackRating, str]] = ..., feedback_reason: _Optional[str] = ...) -> None: ...

class GetConversationsRequest(_message.Message):
    __slots__ = ("user_id", "limit", "offset")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    limit: int
    offset: int
    def __init__(self, user_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetConversationsResponse(_message.Message):
    __slots__ = ("conversations", "total_count")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[ConversationSummary]
    total_count: int
    def __init__(self, conversations: _Optional[_Iterable[_Union[ConversationSummary, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetConversationHistoryRequest(_message.Message):
    __slots__ = ("user_id", "conversation_id", "limit")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    conversation_id: str
    limit: int
    def __init__(self, user_id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class GetConversationHistoryResponse(_message.Message):
    __slots__ = ("conversation_id", "messages")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    messages: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    def __init__(self, conversation_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ...) -> None: ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ("user_id", "conversation_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    conversation_id: str
    def __init__(self, user_id: _Optional[str] = ..., conversation_id: _Optional[str] = ...) -> None: ...

class DeleteConversationResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class SubmitFeedbackRequest(_message.Message):
    __slots__ = ("user_id", "conversation_id", "message_id", "rating", "reason", "comment")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    conversation_id: str
    message_id: str
    rating: FeedbackRating
    reason: str
    comment: str
    def __init__(self, user_id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., message_id: _Optional[str] = ..., rating: _Optional[_Union[FeedbackRating, str]] = ..., reason: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class SubmitFeedbackResponse(_message.Message):
    __slots__ = ("saved", "rating", "reason")
    SAVED_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    saved: bool
    rating: FeedbackRating
    reason: str
    def __init__(self, saved: bool = ..., rating: _Optional[_Union[FeedbackRating, str]] = ..., reason: _Optional[str] = ...) -> None: ...
