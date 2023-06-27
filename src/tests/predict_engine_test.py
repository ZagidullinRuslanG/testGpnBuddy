import unittest

from src.calculations.predictor_engine import PredictorEngine


class PredictorEngineTest(unittest.TestCase):
    def test_something(self):
        engine = PredictorEngine()
        result = engine.predict("public bool IsStringWithUniqueSymbols(")
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
