from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    code: str = Field(title='Изначальный код для анализа', min_length=1)

    class Config:
        schema_extra = {
            "example":
                {
                    "code": "public bool IsStringWithUniqueSymbols(",
                }
        }


class PredictResponse(BaseModel):
    result: str = Field(title='Результат предиктора', min_length=1)
