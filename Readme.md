#reflection #demo #agents #llms #ai

# Reflection Pattern Demo with OpenAI Agents

This repository demonstrates the use of two agents to showcase the **Reflection Pattern**: one agent that generates code, and another agent that reflects on the generated code and suggests improvements.

### Project Overview

- **Agent 1 (Generation Agent)**: This agent generates code based on prompts or specifications.
- **Agent 2 (Reflection Agent)**: This agent reviews the code produced by the Generation Agent and provides suggestions for improvements.

This pattern mimics a cyclical process where one agent produces something and the other agent iterates upon it, improving the result over several steps.

---

## Installation

Before running the project, you'll need to install the required packages. You can install the dependencies by using the `requirements.txt` file.

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

The necessary packages to install are:

- `openai`: For interacting with the OpenAI API.
- `pydantic`: For data validation and settings management.
- `python-dotenv`: For loading environment variables.

---

## Usage

To run the demo, execute the `main.py` file with the following command:

```bash
python main.py --model <MODEL_NAME> --temperature <TEMPERATURE_VALUE> --num_steps <NUM_STEPS>
```

### Arguments:

- `--model` (`<MODEL_NAME>`): The name of the OpenAI model you wish to use for the generation and reflection agents (e.g., `text-davinci-003`).
- `--temperature` (`<TEMPERATURE_VALUE>`): Controls the randomness of the responses. A value between 0 and 1. Lower values make the output more deterministic, while higher values introduce more creativity and variability. Example: `0.7`.
- `--num_steps` (`<NUM_STEPS>`): The maximum number of reflection iterations the reflection agent will perform. Example: `3`.

---

## Example

Here's an example of how to run the demo with the `text-davinci-003` model:

```bash
python main.py --model text-davinci-003 --temperature 0.7 --num_steps 3
```

---

## How It Works

1. **Generation Agent**: The first agent generates code based on a given prompt or problem specification.
   
2. **Reflection Agent**: The second agent reviews the generated code, identifies potential areas for improvement (such as optimization, readability, etc.), and suggests improvements.

3. **Iteration**: The agents interact for a predefined number of steps (`num_steps`), where the reflection agent iterates on the output of the generation agent, refining the code further.

This interaction creates a more refined and well-optimized solution over time.

---

## Requirements

- Python 3.7 or higher
- The following Python packages:
  - `openai`
  - `pydantic`
  - `python-dotenv`

These packages are specified in the `requirements.txt` file.

---

## Environment Variables

Make sure to set up the necessary environment variables for the OpenAI API key. You can create a `.env` file in the root directory with the following content:

```
OPENAI_API_KEY=your-openai-api-key
```

Replace `your-openai-api-key` with your actual OpenAI API key.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.