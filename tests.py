import datetime
import unittest

from cdef import If, TIME, Unknown, Expression


class CdefExpressionsTestCase(unittest.TestCase):

    def test_if_simple_statement(self):
        # basic cdef expression - replace 'unknown' value with 0
        value = Expression('value')
        zero = Expression(0)
        expr = If(Unknown(value),
                  zero,
                  value)
        self.assertEqual(unicode(expr), 'value,UN,0,value,IF')

    def test_if_nested_statement(self):
        value = Expression('value')
        zero = Expression(0)
        un2zero = If(Unknown(value), zero, value)
        n = datetime.datetime(2012, 11, 14, 13, 15)
        # a little bit more complex expression:
        # alter unknown values to zero only when measurement was done after
        # given timestamp
        alter_conditionally = If(TIME > Expression(n),
                                 value,
                                 un2zero)
        self.assertEqual(unicode(alter_conditionally),
                         u'TIME,1352895300,GT,value,value,UN,0,value,IF,IF')

    def test_algebraic_expressions(self):
        expr = ((Expression(5) - Expression(2))/Expression(3) +
                Expression(2) + Expression(4) * Expression(8))
        self.assertEqual(unicode(expr), u'5,2,-,3,/,2,+,4,8,*,+')
