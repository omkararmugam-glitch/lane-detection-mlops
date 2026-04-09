from pydantic import BaseModel

class PredictionResponse(BaseModel):
    status: str
    inference_time: float
    lines_detected: int
    output_image: str