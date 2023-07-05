import unittest

from src.python.calculations.predictor_engine import PredictorEngine


class PredictorEngineTest(unittest.TestCase):
    def test_default(self):
        engine = PredictorEngine()
        result = engine.predict("public bool IsStringWithUniqueSymbols(")
        print(result)
        self.assertIsNotNone(result)

    def test_default2(self):
        engine = PredictorEngine("Codegen2_1")
        result = engine.predict2(
            "# this function check string with unique symbols on c#",
            [r"\n\n^#", "^'''", "\n\n\n"]
        )
        print(result)
        self.assertIsNotNone(result)

    def test_facebook_125(self):
        engine = PredictorEngine('facebook_125')
        result = engine.predict("Hello, i'am a programmer and ")
        print(result)
        self.assertIsNotNone(result)

    def test_question_answering(self):
        engine = PredictorEngine('t5_base')
        result = engine.answer(
            "What difference between horizontal and vertical oil wells",
            "oil")
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
