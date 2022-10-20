"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol Buffers - Google's data interchange format
Copyright 2008 Google Inc.  All rights reserved.
https://developers.google.com/protocol-buffers/

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution.
    * Neither the name of Google Inc. nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.well_known_types
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Duration(google.protobuf.message.Message, google.protobuf.internal.well_known_types.Duration):
    """A Duration represents a signed, fixed-length span of time represented
    as a count of seconds and fractions of seconds at nanosecond
    resolution. It is independent of any calendar and concepts like "day"
    or "month". It is related to Timestamp in that the difference between
    two Timestamp values is a Duration and it can be added or subtracted
    from a Timestamp. Range is approximately +-10,000 years.

    # Examples

    Example 1: Compute Duration from two Timestamps in pseudo code.

        Timestamp start = ...;
        Timestamp end = ...;
        Duration duration = ...;

        duration.seconds = end.seconds - start.seconds;
        duration.nanos = end.nanos - start.nanos;

        if (duration.seconds < 0 && duration.nanos > 0) {
          duration.seconds += 1;
          duration.nanos -= 1000000000;
        } else if (duration.seconds > 0 && duration.nanos < 0) {
          duration.seconds -= 1;
          duration.nanos += 1000000000;
        }

    Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.

        Timestamp start = ...;
        Duration duration = ...;
        Timestamp end = ...;

        end.seconds = start.seconds + duration.seconds;
        end.nanos = start.nanos + duration.nanos;

        if (end.nanos < 0) {
          end.seconds -= 1;
          end.nanos += 1000000000;
        } else if (end.nanos >= 1000000000) {
          end.seconds += 1;
          end.nanos -= 1000000000;
        }

    Example 3: Compute Duration from datetime.timedelta in Python.

        td = datetime.timedelta(days=3, minutes=10)
        duration = Duration()
        duration.FromTimedelta(td)

    # JSON Mapping

    In JSON format, the Duration type is encoded as a string rather than an
    object, where the string ends in the suffix "s" (indicating seconds) and
    is preceded by the number of seconds, with nanoseconds expressed as
    fractional seconds. For example, 3 seconds with 0 nanoseconds should be
    encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should
    be expressed in JSON format as "3.000000001s", and 3 seconds and 1
    microsecond should be expressed in JSON format as "3.000001s".
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECONDS_FIELD_NUMBER: builtins.int
    NANOS_FIELD_NUMBER: builtins.int
    seconds: builtins.int
    """Signed seconds of the span of time. Must be from -315,576,000,000
    to +315,576,000,000 inclusive. Note: these bounds are computed from:
    60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years
    """
    nanos: builtins.int
    """Signed fractions of a second at nanosecond resolution of the span
    of time. Durations less than one second are represented with a 0
    `seconds` field and a positive or negative `nanos` field. For durations
    of one second or more, a non-zero value for the `nanos` field must be
    of the same sign as the `seconds` field. Must be from -999,999,999
    to +999,999,999 inclusive.
    """
    def __init__(
        self,
        *,
        seconds: builtins.int | None = ...,
        nanos: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nanos", b"nanos", "seconds", b"seconds"]) -> None: ...

global___Duration = Duration
