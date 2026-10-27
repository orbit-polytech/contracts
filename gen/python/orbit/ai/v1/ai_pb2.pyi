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
CHUNK_STAGE_UNSPECIFIED: ChunkStage
CHUNK_STAGE_START: ChunkStage
CHUNK_STAGE_DELTA: ChunkStage
CHUNK_STAGE_CITATIONS: ChunkStage
CHUNK_STAGE_DONE: ChunkStage
CHUNK_STAGE_ERROR: ChunkStage

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
    __slots__ = ("conversation_id", "message_id", "query", "context")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    message_id: str
    query: str
    context: StudentContext
    def __init__(self, conversation_id: _Optional[str] = ..., message_id: _Optional[str] = ..., query: _Optional[str] = ..., context: _Optional[_Union[StudentContext, _Mapping]] = ...) -> None: ...

class ChatStreamResponse(_message.Message):
    __slots__ = ("stage", "delta_text", "citations", "error_message", "error_code", "conversation_id", "message_id")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    DELTA_TEXT_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    stage: ChunkStage
    delta_text: str
    citations: _containers.RepeatedCompositeFieldContainer[SourceCitation]
    error_message: str
    error_code: int
    conversation_id: str
    message_id: str
    def __init__(self, stage: _Optional[_Union[ChunkStage, str]] = ..., delta_text: _Optional[str] = ..., citations: _Optional[_Iterable[_Union[SourceCitation, _Mapping]]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[int] = ..., conversation_id: _Optional[str] = ..., message_id: _Optional[str] = ...) -> None: ...

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
