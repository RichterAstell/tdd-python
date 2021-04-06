class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        self.test.run()
        assert(test.wasRun)
    def testSetUp(self):
        self.test.run()
        assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)

# classの整理
# TestCaseTest - テスト対象を選択して run() でテストを呼び出す
# WasRun - テスト対象？
# TestCase - テストケースのベースクラス
