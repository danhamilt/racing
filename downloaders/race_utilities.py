from enum import StrEnum
from typing import NewType

# ENUMS
class StateEnum(StrEnum):
    NSW = 'nsw'
    VIC = 'vic'
    QLD = 'qld'
    WA = 'wa'
    SA = 'sa'
    TAS = 'tas'
    ACT = 'act'
    NT = 'nt'

class HttpRequestEnum(StrEnum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'

# Custom Type Hint Classes
RequestTypes = NewType('RequestTypes', HttpRequestEnum)
StateTypes = NewType('StateTypes', StateEnum)