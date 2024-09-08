from fastapi import APIRouter, HTTPException, status
from schemas.fatsia import GrowthStageData
from services.fatsia_services import process_growth_stage

# Initialize the router
router = APIRouter(
    prefix="/fatsia",
    tags=["fatsia"],
    responses={404: {"description": "Not found"}},
)

@router.post("/growth", status_code=status.HTTP_202_ACCEPTED)
async def submit_growth_stage(data: GrowthStageData):
    """
    Submit detected growth stage data, including object detections.
    """
    if not process_growth_stage(data):
        raise HTTPException(status_code=500, detail="Error processing data")
    return {"status": "success", "detail": "Data accepted"}