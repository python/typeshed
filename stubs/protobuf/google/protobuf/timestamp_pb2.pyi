"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.well_known_types
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Timestamp(google.protobuf.message.Message, google.protobuf.internal.well_known_types.Timestamp):
    """A Timestamp represents a point in time independent of any time zone or local
    calendar, encoded as a count of seconds and fractions of seconds at
    nanosecond resolution. The count is relative to an epoch at UTC midnight on
    January 1, 1970, in the proleptic Gregorian calendar which extends the
    Gregorian calendar backwards to year one.

    All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap
    second table is needed for interpretation, using a [24-hour linear
    smear](https://developers.google.com/time/smear).

    The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By
    restricting to that range, we ensure that we can convert to and from [RFC
    3339](https://www.ietf.org/rfc/rfc3339.txt) date strings.

    # Examples

    Example 1: Compute Timestamp from POSIX `time()`.

        Timestamp timestamp;
        timestamp.set_seconds(time(NULL));
        timestamp.set_nanos(0);

    Example 2: Compute Timestamp from POSIX `gettimeofday()`.

        struct timeval tv;
        gettimeofday(&tv, NULL);

        Timestamp timestamp;
        timestamp.set_seconds(tv.tv_sec);
        timestamp.set_nanos(tv.tv_usec * 1000);

    Example 3: Compute Timestamp from Win32 `GetSystemTimeAsFileTime()`.

        FILETIME ft;
        GetSystemTimeAsFileTime(&ft);
        UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

        // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
        // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
        Timestamp timestamp;
        timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
        timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

    Example 4: Compute Timestamp from Java `System.currentTimeMillis()`.

        long millis = System.currentTimeMillis();

        Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
            .setNanos((int) ((millis % 1000) * 1000000)).build();


    Example 5: Compute Timestamp from Java `Instant.now()`.

        Instant now = Instant.now();

        Timestamp timestamp =
            Timestamp.newBuilder().setSeconds(now.getEpochSecond())
                .setNanos(now.getNano()).build();


    Example 6: Compute Timestamp from current time in Python.

        timestamp = Timestamp()
        timestamp.GetCurrentTime()

    # JSON Mapping

    In JSON format, the Timestamp type is encoded as a string in the
    [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the
    format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z"
    where {year} is always expressed using four digits while {month}, {day},
    {hour}, {min}, and {sec} are zero-padded to two digits each. The fractional
    seconds, which can go up to 9 digits (i.e. up to 1 nanosecond resolution),
    are optional. The "Z" suffix indicates the timezone ("UTC"); the timezone
    is required. A proto3 JSON serializer should always use UTC (as indicated by
    "Z") when printing the Timestamp type and a proto3 JSON parser should be
    able to accept both UTC and other timezones (as indicated by an offset).

    For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past
    01:30 UTC on January 15, 2017.

    In JavaScript, one can convert a Date object to this format using the
    standard
    [toISOString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
    method. In Python, a standard `datetime.datetime` object can be converted
    to this format using
    [`strftime`](https://docs.python.org/2/library/time.html#time.strftime) with
    the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java, one can use
    the Joda Time's [`ISODateTimeFormat.dateTime()`](
    http://www.joda.org/joda-time/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime%2D%2D
    ) to obtain a formatter capable of generating timestamps in this format.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SECONDS_FIELD_NUMBER: builtins.int
    NANOS_FIELD_NUMBER: builtins.int
    seconds: builtins.int
    """Represents seconds of UTC time since Unix epoch
    1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to
    9999-12-31T23:59:59Z inclusive.
    """

    nanos: builtins.int
    """Non-negative fractions of a second at nanosecond resolution. Negative
    second values with fractions must still have non-negative nanos values
    that count forward in time. Must be from 0 to 999,999,999
    inclusive.
    """

    def __init__(self,
        *,
        seconds: builtins.int = ...,
        nanos: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nanos",b"nanos","seconds",b"seconds"]) -> None: ...
global___Timestamp = Timestamp
