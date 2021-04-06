class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
    def tearDown(self):
        pass

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "
    def testMethod(self):
        self.log = self.log + "testMethod "
    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

TestCaseTest("testTemplateMethod").run()
# TestCaseTest("testSetUp").run()
# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)

# classの整理
# TestCaseTest - テスト対象を選択して run() でテストを呼び出す
# WasRun - テスト対象？
# TestCase - テストケースのベースクラス
