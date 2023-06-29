from fastapi import APIRouter

from src.models.models import PredictRequest, PredictResponse
from src.calculations.predictor_engine import PredictorEngine

predictor_router = APIRouter(prefix="/predictor", tags=["Predictor"])


@predictor_router.post("/predict", response_model=PredictResponse)
def predict_code(request: PredictRequest):
    """ Анализ кода для автодополнения """
    engine = PredictorEngine()
    result = engine.predict(request.code)
    return {'result': result}
