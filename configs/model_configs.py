"""
Model configurations such as model name, type and output paths
model_name:
model_type:
model_output_path:
model_artifacts
"""

from pathlib import Path

@staticmethod
class ModelConfig:
    BASE_DIR = Path(__file__).resolve.parent.parent

    MODEL_NAME = "xgboost"

    MODEL_TYPE = "classification"

    # directories
    MODEL_DIR = BASE_DIR/"models"

    ARTIFACTS_DIR = BASE_DIR/"artifacts"

    # model paths 
    MODEL_PATH = MODEL_DIR/"model.pkl"
    BEST_MODEL_PATH = MODEL_DIR/"best_model.pkl"

    # encoder 
    LABEL_ENCODER_PATH = MODEL_DIR/"label_encoder.pkl"

    # storing artifacts
    METRICS_PATH = ARTIFACTS_DIR/"metrics.json"
    BEST_PARAMS_PATH = ARTIFACTS_DIR/"best_params.json"


    SUBMISSION_PATH = ARTIFACTS_DIR/"submission.csv"


