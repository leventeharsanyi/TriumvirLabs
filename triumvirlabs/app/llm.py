import os
import anthropic
from dotenv import load_dotenv

# Parameters
model_type = "claude-haiku-4-5-20251001" # "claude-3-haiku-20240307" "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307" # Choose from here: https://docs.anthropic.com/en/docs/about-claude/models
api_call_sleep_sec = 70
max_output_tokens = 1_000
max_input_tokens = 20_000
temperature = 0

# Setup
load_dotenv()
client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Import data
f = open('app/input_ehr.txt', 'r')
ehr_medical_history_example = f.read()

def llm_call(question: str) -> str:
    prompt = f"""
    You are a helpful medical assistant that answers questions using text from the reference medical history included below.
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information.
    Strike a friendly and converstional tone. If the medical history is irrelevant to the answer, you may ignore it. 
    In case of timestamps or date-times just use the day without the exact time.

    QUESTION: {question}
    MEDICAL HISTORY: {ehr_medical_history_example}
    """

    message = client.messages.create(
        model=model_type,
        max_tokens=max_output_tokens,
        temperature=temperature,
        system="""
    You are a helpful medical assistant that answers questions using text from the reference medical history included below.
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information.
    strike a friendly and converstional tone. If the medical history is irrelevant to the answer, you may ignore it.
    In case of timestamps or date-times just use the day without the exact time.
    """,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    generated_answer = message.content[0].text
    return generated_answer


if __name__ == "__main__":
    generated_answer = llm_call(question="Has the patient ever smoked tobacco?")
