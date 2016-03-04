C:\Anaconda2\python.exe D:/learnpython27/qiwsirPython/ex1-8.py
2016-03-03
Help on built-in module datetime:

NAME
    datetime - Fast implementation of the datetime type.

FILE
    (built-in)

CLASSES
    __builtin__.object
        date
            datetime
        time
        timedelta
        tzinfo
    
    class date(__builtin__.object)
     |  date(year, month, day) --> date object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  fromordinal(...)
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  fromtimestamp(...)
     |      timestamp -> local date from a POSIX timestamp (like time.time()).
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  replace(...)
     |      Return date with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  today(...)
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  day
     |  
     |  month
     |  
     |  year
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  max = datetime.date(9999, 12, 31)
     |  
     |  min = datetime.date(1, 1, 1)
     |  
     |  resolution = datetime.timedelta(1)
    
    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |  
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints or longs.
     |  
     |  Method resolution order:
     |      datetime
     |      date
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |  
     |  combine(...)
     |      date, time -> datetime with same date and time fields
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  date(...)
     |      Return date object with same year, month and day.
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  fromtimestamp(...)
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].
     |      
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |  
     |  now(...)
     |      [tz] -> new datetime with tz's local day and time.
     |  
     |  replace(...)
     |      Return datetime with new specified fields.
     |  
     |  strptime(...)
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcfromtimestamp(...)
     |      timestamp -> UTC datetime from a POSIX timestamp (like time.time()).
     |  
     |  utcnow(...)
     |      Return a new datetime representing UTC day and time.
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |  
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  fromordinal(...)
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  today(...)
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |  
     |  day
     |  
     |  month
     |  
     |  year
    
    class time(__builtin__.object)
     |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
     |  
     |  All arguments are optional. tzinfo may be None, or an instance of
     |  a tzinfo subclass. The remaining arguments may be ints or longs.
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM].
     |  
     |  replace(...)
     |      Return time with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  max = datetime.time(23, 59, 59, 999999)
     |  
     |  min = datetime.time(0, 0)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
    
    class timedelta(__builtin__.object)
     |  Difference between two datetime values.
     |  
     |  Methods defined here:
     |  
     |  __abs__(...)
     |      x.__abs__() <==> abs(x)
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __div__(...)
     |      x.__div__(y) <==> x/y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __floordiv__(...)
     |      x.__floordiv__(y) <==> x//y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __pos__(...)
     |      x.__pos__() <==> +x
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rdiv__(...)
     |      x.__rdiv__(y) <==> y/x
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __rfloordiv__(...)
     |      x.__rfloordiv__(y) <==> y//x
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  total_seconds(...)
     |      Total seconds in the duration.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  days
     |      Number of days.
     |  
     |  microseconds
     |      Number of microseconds (>= 0 and less than 1 second).
     |  
     |  seconds
     |      Number of seconds (>= 0 and less than 1 day).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  max = datetime.timedelta(999999999, 86399, 999999)
     |  
     |  min = datetime.timedelta(-999999999)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
    
    class tzinfo(__builtin__.object)
     |  Abstract base class for time zone info objects.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __reduce__(...)
     |      -> (cls, state)
     |  
     |  dst(...)
     |      datetime -> DST offset in minutes east of UTC.
     |  
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |  
     |  tzname(...)
     |      datetime -> string name of time zone.
     |  
     |  utcoffset(...)
     |      datetime -> minutes east of UTC (negative for west of UTC).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

DATA
    MAXYEAR = 9999
    MINYEAR = 1
    datetime_CAPI = <capsule object "datetime.datetime_CAPI">


None

Process finished with exit code 0
