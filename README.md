rrd-cdef
========

Trivial DSL for RRD CDEF epressions (http://oss.oetiker.ch/rrdtool/tut/cdeftutorial.en.html). I've covered only part of CDEF - if you need something more just add an issue or make pull request with your patch :-P

USAGE
-----

    >>> # Alter unknown value of x to 0:
    >>> from cdef import Expression, If, TIME, Unknown
    >>> x = Expression('x')
    >>> zero = Expression(0)
    >>> unknow2zero = lambda v: If(Unknown(v), zero, v)
    >>> unicode(unknow2zero(x))
    x,UN,0,x,IF
    >>> # Alter unknown value of x to 0 when it was measured before given timestamp:
    >>> import datetime
    >>> dt = datetime.datetime(2012, 11, 27, 13, 15)
    >>> unicode(If(TIME > dt, x, unknown2zero(x)))
    TIME,1352895300,GT,x,value,UN,0,x,IF,IF
    >>> # Alter x,y and z to 0 when unknown and before given timestamp and sum them up together:
    >>> unicode(sum((If(TIME > dt, v, unknown2zero(v)) for v in [Expression('x'), Expression('y'), Expression('z')]), zero))
    u'0,TIME,1354018500,GT,x,x,UN,0,x,IF,IF,+,TIME,1354018500,GT,y,y,UN,0,y,IF,IF,+,TIME,1354018500,GT,z,z,UN,0,z,IF,IF,+'
