import unittest

from predictorEngine import PredictorEngine


class PredictorEngineWithoutParameters(unittest.TestCase):
    def test_something(self):
        engine = PredictorEngine(None, None)
        result = engine.predict("public bool IsStringWithUniqueSymbols(")
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
