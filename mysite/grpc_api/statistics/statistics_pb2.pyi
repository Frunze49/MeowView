from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Post(_message.Message):
    __slots__ = ("post_id", "author", "description", "image", "likes", "views")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    author: str
    description: str
    image: bytes
    likes: int
    views: int
    def __init__(self, post_id: _Optional[int] = ..., author: _Optional[str] = ..., description: _Optional[str] = ..., image: _Optional[bytes] = ..., likes: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("likes", "author")
    LIKES_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    likes: int
    author: str
    def __init__(self, likes: _Optional[int] = ..., author: _Optional[str] = ...) -> None: ...

class StatisticRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class StatisticResponse(_message.Message):
    __slots__ = ("likes", "views")
    LIKES_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    likes: int
    views: int
    def __init__(self, likes: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class TopPostsRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: str
    def __init__(self, filter: _Optional[str] = ...) -> None: ...

class TopPostsResponse(_message.Message):
    __slots__ = ("posts",)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[Post]
    def __init__(self, posts: _Optional[_Iterable[_Union[Post, _Mapping]]] = ...) -> None: ...

class TopUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TopUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...
