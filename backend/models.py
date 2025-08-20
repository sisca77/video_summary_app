from pydantic import BaseModel, Field
from typing import Optional


class VideoUploadResponse(BaseModel):
    task_id: str
    message: str


class ProcessingStatus(BaseModel):
    task_id: str
    status: str  # "processing", "extracting_transcript", "splitting_file", "generating_outline", "completed", "failed"
    progress: int  # 0-100
    message: str
    transcript: Optional[str] = None
    outline: Optional[str] = None
    detailed_explanation: Optional[str] = None
    error: Optional[str] = None


class VideoSummaryResult(BaseModel):
    task_id: str
    file_name: str
    transcript: str
    outline: str
    processing_time: float
