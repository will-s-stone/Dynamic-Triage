import anthropic
from config import LLM_API_KEY

client = anthropic.Anthropic(api_key=LLM_API_KEY)


def query_llm(patient_info):
    """
    Sends the patient's information to the LLM and returns the response.
    Uses the Anthropic API (Claude) to process patient information.
    """
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2048,
            temperature=0.5,
            system="You are assisting a non-medical expert in triaging patients. Collect necessary information for "
                   "diagnosis.",
            messages=[
                {
                    "role": "user",
                    "content": f"Patient information: {patient_info}. What additional info do you need for diagnosis?"
                }
            ]
        )

        return response.content
    except Exception as e:
        # Handle any errors that may occur during the API call
        return {"error": str(e)}






