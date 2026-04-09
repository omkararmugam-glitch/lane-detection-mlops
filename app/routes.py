from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2

from app.services import detect_lanes
from app.schemas import PredictionResponse
from app.logger import logger

router = APIRouter()

@router.post("/predict/", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):

    print("🚀 ROUTE HIT")

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return PredictionResponse(
            status="error",
            inference_time=0,
            lines_detected=0,
            output_image=""
        )

    output_path, inference_time, count = detect_lanes(img)

    logger.info("Prediction done")

    return PredictionResponse(
        status="success",
        inference_time=round(inference_time, 3),
        lines_detected=count,
        output_image=output_path
    )