import cv2
import numpy as np
import time
import os
import mlflow

# ✅ MLflow setup
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("lane-detection")

# ✅ Enable system metrics (IMPORTANT)
mlflow.enable_system_metrics_logging()

# Output folder
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def detect_lanes(image):

    print("🔥 FUNCTION CALLED")

    with mlflow.start_run():

        print("🔥 MLFLOW STARTED")

        start_time = time.time()

        # Resize
        img = cv2.resize(image, (640, 480))

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Edge detection
        edges = cv2.Canny(gray, 50, 150)

        # Hough Transform
        lines = cv2.HoughLinesP(
            edges,
            1,
            np.pi / 180,
            100,
            minLineLength=50,
            maxLineGap=10
        )

        count = 0

        if lines is not None:
            count = len(lines)
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # Save output image
        output_path = os.path.join(OUTPUT_DIR, f"output_{int(time.time())}.jpg")
        cv2.imwrite(output_path, img)

        # Time taken
        inference_time = time.time() - start_time

        # ✅ Metrics
        mlflow.log_metric("inference_time", inference_time)
        mlflow.log_metric("lines_detected", count)
        mlflow.log_metric("execution_time", inference_time)

        # ✅ Tags (for traces)
        mlflow.set_tag("stage", "inference")
        mlflow.set_tag("endpoint", "/predict")

        # ✅ Artifact
        mlflow.log_artifact(output_path)

        print("✅ MLFLOW LOGGED")

        return output_path, inference_time, count