import datetime as __datetime

__all__ = ["Interval", "IntervalList"]


# Intervals are represented as two-element tuple holding two datetime objects:
# The first datetime object represents the start time, while the latter represents the end time.
Interval = tuple[__datetime.datetime, __datetime.datetime]

# A list of intervals as defined above.
IntervalList = list[Interval]
