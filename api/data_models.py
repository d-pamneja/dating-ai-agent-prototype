from .dependencies import *

# Data Models for Input and Output
class ChatQuery(BaseModel):
    conversation: str = Field(..., description="The entire conversation as a string")
    
class Response(BaseModel):
    response : str = Field(...,description="The final response given by the LLM of the user query")