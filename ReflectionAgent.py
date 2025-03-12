from enums import Role
import json
from output_format import generation_format, reflection_format
from pydantic import BaseModel, ValidationError
from typing import List

from output_format import Generation, Reflection

from logger import setup_logger

# Create a logger specific to this module
logger = setup_logger('Reflection')

class ReflectionAgent:

    def __init__(self,
                client,
                gen_prompt,
                ref_prompt,
                num_steps,
                verbose=True
                ):

        self.client = client
        self.sys_generation_prompt = gen_prompt
        self.sys_reflection_prompt = ref_prompt
        self.num_steps = num_steps
        self.verbose=verbose

        self.generation_history = [
            self.build_prompt(Role.SYSTEM.value,self.sys_generation_prompt)
        ]

        self.reflection_history = [
            self.build_prompt(Role.SYSTEM.value,self.sys_reflection_prompt)
        ]

    def llm_call(self,messages,response_format):

        response = self.client.generate_response(messages=messages,
                                response_format=response_format)

        return json.loads(response.choices[0].message.content)

    def build_prompt(self,role,message,action=None):

        if(action=="improve"):
            return {"role":role,
                    "content":"Following is feedback for the above code:\n"+message}
        elif(action=="reflect"):
            return {"role":role,
                    "content":"Provide feedback for following code:\n"+message}
        elif(action=="generate"):
            return {"role":role,
                    "content":"Following is user request:\n"+message}
        else:
            return {"role":role,
                    "content":message}

    def generate(self):

        generation = self.llm_call(self.generation_history,generation_format)

        try:
            # Parse and validate the response content
            generation = Generation.model_validate(generation)
        except ValidationError as e:
            # Handle validation errors
            print(e.json())

        self.generation_history.append(
            self.build_prompt(role=Role.ASSISTANT.value,message=generation.code)
            )

        self.reflection_history.append(
            self.build_prompt(role=Role.USER.value,message=generation.code,action="reflect")
        )

        return generation
        

    def reflect(self):

        reflection = self.llm_call(self.reflection_history,reflection_format)

        try:
            # Parse and validate the response content
            reflection = Reflection.model_validate(reflection)
        except ValidationError as e:
            # Handle validation errors
            print(e.json())

        self.reflection_history.append(
            self.build_prompt(role=Role.ASSISTANT.value,message=reflection.feedback)
        )

        self.generation_history.append(
            self.build_prompt(role=Role.USER.value,message=reflection.feedback,action="improve")
        )

        return reflection


    def generate_response(self,usr_msg):

        # Generate response from generator
        self.generation_history.append(
            self.build_prompt(Role.USER.value,usr_msg,"generate")
        )

        logger.info(f"User request \n {usr_msg}")


        for step in range(self.num_steps):

            generation = self.generate()

            if(self.verbose):
                logger.info("Generated/Improved Code : \n")
                logger.info(f"\n\n {generation.code}")

            reflection = self.reflect()

            if(self.verbose):
                logger.info("Reflection Generated : \n")
                logger.info(f"Status : {reflection.status}\n")
                logger.info("Feedback : \n")
                logger.info(reflection.feedback+"\n")

            if(reflection.status=="PASS"):
                break
