import datetime as __datetime
import re as __re

__all__ = [
    "inclinations",
    "parse_stk_date",
    "unparse_stk_date",
    "collected_data",
]


__stk_date_fmt = "%d %b %Y %H:%M:%S.%f"
__stk_date_re = __re.compile(
    r"^(\d{1,2}\s[A-Z][a-z]{2}\s\d{4} \d{2}:\d{2}:)(\d{2}\.\d{1,})$"
)

inclinations = [27, 50, 76, 86]


def __truncate_to_microseconds(match: __re.Match) -> str:
    """Truncates the seconds in a STK date string to microseconds. To be used with `re.sub` and `__stk_date_re`."""
    return f"{match.group(1)}{round(float(match.group(2)), 6)}"


def parse_stk_date(s: str) -> __datetime.datetime:
    """Creates a datetime object from a given STK date string."""
    return __datetime.datetime.strptime(
        __re.sub(__stk_date_re, __truncate_to_microseconds, s), __stk_date_fmt
    )


def unparse_date_stk(d: __datetime.datetime) -> str:
    """Creates a string representation as returned by STK for a given datetime object."""
    return d.strftime(__stk_date_fmt)


def collected_data(
    start: __datetime.datetime,
    end: __datetime.datetime,
    offset=__datetime.timedelta(seconds=20),
    rate: float = 100.0,
) -> float:
    """Calculates the amount of data (in kb) the satellite can collect between `start` and `end`.
    `offset` specifies the time required for synchronization, `rate` the data rate (in kb/s).
    """
    return rate * max(0.0, (end - start - offset).total_seconds())
