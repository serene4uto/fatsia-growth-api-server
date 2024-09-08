from pydantic import BaseModel, Field
from typing import List

class BoundingBox(BaseModel):
    x_min: int
    y_min: int
    x_max: int
    y_max: int

class Detection(BaseModel):
    object_id: str
    confidence: float
    bounding_box: BoundingBox

class GrowthStageData(BaseModel):
    device_id: str
    timestamp: str
    detections: List[Detection]
