
from pydantic import BaseModel, ValidationError
from typing import List


generation_format = {
    "type": "json_schema",
    "json_schema":{
        "name": "generate_code_schema",
        "description": "Schema to generate python code.",
        "strict": True,
        "schema": {
                "type": "object",
                "properties":{
                    "code": {
                                "type":"string",
                                "description":"Code generated/modified as per user's request/feedback. If user makes any non-code related request, return 'INVALID REQUEST'"
                            }     
                },
                "required":["code"],
                "additionalProperties":False
            }
    }
}

reflection_format = {
    "type": "json_schema",
    "json_schema":{
        "name": "feedback_schema",
        "description": "Schema to provide feedback for the given code.",
        "strict": True,
        "schema": {
                "type": "object",
                "properties":{
                    "status": {
                                "type":"string",
                                "description":"Status of feedback generated. 'PASS' -> If no improvements suggested else 'NEEDS IMPROVEMENT'",
                                "enum":["PASS","NEEDS IMPROVEMENT"]
                            },
                    "feedback": {
                                "type":"string",
                                "description":"Feedback to improve the given code."
                    }
                },
                "required":["status","feedback"],
                "additionalProperties":False
            }
    }
}

# Define types that match the JSON Schema using pydantic models
class Generation(BaseModel):
    code : str

class Reflection(BaseModel):
    status : str
    feedback : str
