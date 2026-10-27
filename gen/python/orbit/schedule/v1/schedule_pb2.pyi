from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULE_STATUS_UNSPECIFIED: _ClassVar[ScheduleStatus]
    SCHEDULE_STATUS_READY: _ClassVar[ScheduleStatus]
    SCHEDULE_STATUS_PENDING_SYNC: _ClassVar[ScheduleStatus]
SCHEDULE_STATUS_UNSPECIFIED: ScheduleStatus
SCHEDULE_STATUS_READY: ScheduleStatus
SCHEDULE_STATUS_PENDING_SYNC: ScheduleStatus

class SearchGroupsRequest(_message.Message):
    __slots__ = ("query", "limit")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class SearchGroupsResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[GroupItem]
    def __init__(self, groups: _Optional[_Iterable[_Union[GroupItem, _Mapping]]] = ...) -> None: ...

class GroupItem(_message.Message):
    __slots__ = ("title", "has_regular_schedule", "has_session_schedule")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HAS_REGULAR_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    HAS_SESSION_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    title: str
    has_regular_schedule: bool
    has_session_schedule: bool
    def __init__(self, title: _Optional[str] = ..., has_regular_schedule: bool = ..., has_session_schedule: bool = ...) -> None: ...

class GetGroupScheduleRequest(_message.Message):
    __slots__ = ("group_title", "date_from", "date_to")
    GROUP_TITLE_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    group_title: str
    date_from: str
    date_to: str
    def __init__(self, group_title: _Optional[str] = ..., date_from: _Optional[str] = ..., date_to: _Optional[str] = ...) -> None: ...

class GetGroupScheduleResponse(_message.Message):
    __slots__ = ("group_title", "evening_type", "metadata", "days", "time_zone", "date_from", "date_to")
    GROUP_TITLE_FIELD_NUMBER: _ClassVar[int]
    EVENING_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    group_title: str
    evening_type: int
    metadata: ScheduleMetadata
    days: _containers.RepeatedCompositeFieldContainer[DaySchedule]
    time_zone: str
    date_from: str
    date_to: str
    def __init__(self, group_title: _Optional[str] = ..., evening_type: _Optional[int] = ..., metadata: _Optional[_Union[ScheduleMetadata, _Mapping]] = ..., days: _Optional[_Iterable[_Union[DaySchedule, _Mapping]]] = ..., time_zone: _Optional[str] = ..., date_from: _Optional[str] = ..., date_to: _Optional[str] = ...) -> None: ...

class ScheduleMetadata(_message.Message):
    __slots__ = ("last_checked_at", "last_updated_at", "is_stale", "status", "published_from", "published_to")
    LAST_CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_STALE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FROM_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_TO_FIELD_NUMBER: _ClassVar[int]
    last_checked_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    is_stale: bool
    status: ScheduleStatus
    published_from: str
    published_to: str
    def __init__(self, last_checked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_stale: bool = ..., status: _Optional[_Union[ScheduleStatus, str]] = ..., published_from: _Optional[str] = ..., published_to: _Optional[str] = ...) -> None: ...

class DaySchedule(_message.Message):
    __slots__ = ("date", "day_of_week", "lessons")
    DATE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    LESSONS_FIELD_NUMBER: _ClassVar[int]
    date: str
    day_of_week: int
    lessons: _containers.RepeatedCompositeFieldContainer[Lesson]
    def __init__(self, date: _Optional[str] = ..., day_of_week: _Optional[int] = ..., lessons: _Optional[_Iterable[_Union[Lesson, _Mapping]]] = ...) -> None: ...

class Lesson(_message.Message):
    __slots__ = ("subject", "type", "slot_number", "start_time", "end_time", "location", "auditoriums", "teachers", "e_link", "week")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    AUDITORIUMS_FIELD_NUMBER: _ClassVar[int]
    TEACHERS_FIELD_NUMBER: _ClassVar[int]
    E_LINK_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    subject: str
    type: str
    slot_number: int
    start_time: str
    end_time: str
    location: str
    auditoriums: _containers.RepeatedCompositeFieldContainer[Auditorium]
    teachers: _containers.RepeatedCompositeFieldContainer[Teacher]
    e_link: str
    week: str
    def __init__(self, subject: _Optional[str] = ..., type: _Optional[str] = ..., slot_number: _Optional[int] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., location: _Optional[str] = ..., auditoriums: _Optional[_Iterable[_Union[Auditorium, _Mapping]]] = ..., teachers: _Optional[_Iterable[_Union[Teacher, _Mapping]]] = ..., e_link: _Optional[str] = ..., week: _Optional[str] = ...) -> None: ...

class Auditorium(_message.Message):
    __slots__ = ("name", "web_url", "color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    web_url: str
    color: str
    def __init__(self, name: _Optional[str] = ..., web_url: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class Teacher(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
