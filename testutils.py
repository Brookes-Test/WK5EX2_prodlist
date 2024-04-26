#IMPORTANT: DO NOT CHANGE THIS FILE!
import unittest
from main import prodlist

class TestUtils(unittest.TestCase):

  def test1(self):
    self.doTest([],1)

  def test2(self):
    self.doTest([3.5],3.5)

  def test3(testCase):
    self.doTest([3,-1.5,1],-4.5)

  def doTest(self,numList,expected):
    delta = 0.05
    actual = prodlist(numList)
    if not isinstance(actual,(int,float)):
      explanation = "Return value is not a number"
      msg = self.makeMessage(numList, expected,actual,explanation)
      testCase.fail(msg)
    if abs(expected - actual) > delta:
      msg = self.makeMessage(numList, expected,actual,"Actual and expected return values are not equal")
      testCase.fail(msg)


  def makeMessage(self, expected,actual,explanation):
    bar ="\n##################################\n"
    msg = bar + "Function call: " + self.callToStr("prodlist", numList) 
    msg += "\nExpected return value: " + repr(expected)
    msg += "\nActual return value: " + repr(actual)
    msg += "\n" + explanation + bar
    return msg

  def callToStr(self,functor,*args):
    call = functor + "("
    nbrArgs = len(args)
    for i in range(0,nbrArgs):
      call += repr(args[i])
      if i == nbrArgs-1:
        call += ")"
      else:
        call += ","
    return call

if __name__ == '__main__':
    unittest.main()
