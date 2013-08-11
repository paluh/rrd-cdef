import datetime
import time


def _coerce(v):
    return v if isinstance(v, Expression) else Expression(v)

class Expression(object):

    def __init__(self, value):
        if isinstance(value, datetime.datetime):
            self.value = int(time.mktime(value.timetuple()))
        else:
            self.value = value

    def __gt__(self, other):
        return Greater(self, other)

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mult(self, other)

    def __div__(self, other):
        return Div(self, other)

    def __unicode__(self):
        return unicode(self.value)


class BinaryOperator(Expression):

    operator = None

    def __init__(self, value1, value2):
        self.value1 = _coerce(value1)
        self.value2 = _coerce(value2)

    def __unicode__(self):
        return u'%s,%s,%s' % (self.value1, self.value2, self.operator)


class UnaryOperator(Expression):

    operator = None

    def __init__(self, value):
        self.value = _coerce(value)

    def __unicode__(self):
        return u'%s,%s' % (self.value, self.operator)


class Add(BinaryOperator):

    operator = '+'


class Sub(BinaryOperator):

    operator = '-'


class Mult(BinaryOperator):

    operator = '*'


class Div(BinaryOperator):

    operator = '/'


class Greater(BinaryOperator):

    operator = 'GT'


class Lesser(BinaryOperator):

    operator = 'LT'


class If(Expression):

    def __init__(self, condition, then, else_):
        self.condition = condition
        self.then = _coerce(then)
        self.else_ = _coerce(else_)

    def __unicode__(self):
        return u'%s,%s,%s,IF' % (self.condition, self.then, self.else_)


class Unknown(UnaryOperator):

    operator = 'UN'


class Ceil(UnaryOperator):

    operator = 'CEIL'


class Floor(UnaryOperator):

    operator = 'FLOOR'


class Min(BinaryOperator):

    operator = 'MIN'


class Max(BinaryOperator):

    operator = 'MAX'


# set operations

class Minimum(UnaryOperator):

    operator = 'MINIMUM'


class Average(UnaryOperator):

    operator = 'AVERAGE'


class Maximum(UnaryOperator):

    operator = 'MAXIMUM'


class Last(UnaryOperator):

    operator = 'LAST'

TIME = Expression('TIME')
UNKNOWN = Expression('UNKN')

