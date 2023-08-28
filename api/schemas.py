from pydantic import BaseModel


class AttrsParam(BaseModel):
    total_count: int
    blank_percentage: int
    annotation_length: int
    images_count: int
    modified_annotation: str
    modified_images: str
