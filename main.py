from helper_functions import get_args
from OpenAIClient import OpenAIClient
from dotenv import load_dotenv
from ReflectionAgent import ReflectionAgent
from system_prompt import GENERATION_SYSTEM_PROMPT, REFLECTION_SYSTEM_PROMPT
import json

def run(args):

    # Setup OpenAI client
    client = OpenAIClient(
                        args.model,
                        num_requests=1,
                        temperature=args.temperature
                        )
    

    with open("user_prompts.json","r") as file:
        input_json = json.load(file)

    agent = ReflectionAgent(
                client,
                GENERATION_SYSTEM_PROMPT,
                REFLECTION_SYSTEM_PROMPT,
                num_steps=args.num_steps,
    )

    for user_request in input_json["user_requests"]:

        agent.generate_response(user_request)



if __name__ == "__main__":

    load_dotenv()
    args = get_args()
    run(args)