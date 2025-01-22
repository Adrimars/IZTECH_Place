from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

from database import pixels_collection
from models import PixelModel

router = APIRouter()

@router.get("/pixels",response_model = List[PixelModel])
async def get_all_pixels():
    cursor = pixels_collection.find({})
    pixels = []
    async for doc in cursor:
        pixels.append(PixelModel(**doc))
    return pixels


@router.get("/pixels/{x}/{y}",response_model = PixelModel)
async def get_pixe_by_coordinates(x: int, y: int):
    pixel = await pixels_collection.find_one({"x":x,"y":y})
    if not pixel:
        raise HTTPException(status_code=404,detail = "Pixel cannot be found")
    return PixelModel(**pixel)


@router.post("/pixels",response_model = PixelModel)
async def create_or_update_pixel(pixel: PixelModel):
    existing = await pixels_collection.find_one({"x": pixel.x, "y": pixel.y})
    if existing:
        updated_data = {
            "color" : pixel.color,
            "userId" : pixel.userId,
            "lastUpdatedAt" : datetime.utcnow().isoformat()
        }
        await pixels_collection.update_one({"x": pixel.x, "y": pixel.y},{"$set":updated_data})
        return {"detail": "Pixel updated successfully"}
    else:
        new_pixel = pixel.dict(exclude = {"id"})
        new_pixel["lastUpdatedAt"] = datetime.utcnow().isoformat()
        await pixels_collection.insert_one(new_pixel)
        return {"detail": "Pixel created successfully"}



