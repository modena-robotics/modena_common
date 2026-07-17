from enum import IntEnum


class JogType(IntEnum):
    JOG_JOINT = 0x00
    JOG_WORLD = 0x01
    JOG_TOOL = 0x02
    JOG_NONE = 0x03


class JogIndex(IntEnum):
    JOG_INDEX_1 = 0
    JOG_INDEX_2 = 1
    JOG_INDEX_3 = 2
    JOG_INDEX_4 = 3


class JogDirection(IntEnum):
    JOG_POS = 1
    JOG_NEG = -1