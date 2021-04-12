class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
    def tearDown(self):
        pass

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount + 1

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "
    def testMethod(self):
        self.log = self.log + "testMethod "
    def tearDown(self):
        self.log = self.log + "tearDown "
    def testBrokenMethod(self):
        raise Exception

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert("1 run, 0 failed" == result.summary())
    def testResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
    def testFailedResult(self):
        result = TestResult()
        test = WasRun("testBrokenMethod")
        test.run(result)
        assert("1 run, 1 failed" == result.summary())
    def testSuite(self):
        suite = testSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())
        
class TestSuite:
    def __init__(self):
        self.tests = [] 
    def add(self, test):
        self.tests.append(test)
    def run(self, result):
        for test in self.tests:
            test.run(result)


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())

# print(TestCaseTest("testTemplateMethod").run().summary())
# print(TestCaseTest("testResult").run().summary())
# print(TestCaseTest("testFailedResult").run().summary())
# print(TestCaseTest("testResultFormatting").run().summary())

# print(TestCaseTest("testSuite").run().summary())

# TestCaseTest("testSetUp").run()
# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)

# classの整理
# TestCaseTest - テスト対象を選択して run() でテストを呼び出す
# WasRun - テスト対象？
# TestCase - テストケースのベースクラス
