from Xlib.protocol import rq

# TODO: Complete all classes using WindowValues and GCValues
# Currently *object is used to represent the ValueList instead of the possible attribute types
def WindowValues(arg: str) -> rq.ValueList: ...
def GCValues(arg: str) -> rq.ValueList: ...

TimeCoord: rq.Struct
Host: rq.Struct
CharInfo: rq.Struct
FontProp: rq.Struct
ColorItem: rq.Struct
RGB: rq.Struct
Point: rq.Struct
Segment: rq.Struct
Rectangle: rq.Struct
Arc: rq.Struct
