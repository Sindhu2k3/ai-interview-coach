from google import genai
from config import Config

client = genai.Client(api_key=Config.OPENAI_API_KEY)


def generate_questions(role, level):

    prompt = f"""
You are an expert interviewer.

Role: {role}
Difficulty Level: {level}

Generate EXACTLY 3 interview questions.

Rules based on difficulty:

EASY:
- fundamental concepts
- simple behavioral question
- basic situational

MEDIUM:
- mix of conceptual + case based
- requires structured thinking

HARD:
- cross-domain thinking
- metrics driven
- edge cases & trade-offs

Return only numbered questions 1 to 3.
No extra text.
"""

    r = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    questions = [q.strip() for q in r.text.split("\n") if q.strip()]
    return questions[:3]



def evaluate_full(questions, answers, role, level):

    qa_text = ""
    for i in range(3):
        qa_text += f"Q{i+1}: {questions[i]}\nA{i+1}: {answers[i]}\n\n"

    prompt = f"""
You are a senior interviewer.

Role: {role}
Difficulty Level: {level}

Interview Performance:

{qa_text}

Scoring Rules:
- Easy: focus on clarity & basics
- Medium: structure + examples
- Hard: depth, metrics, trade-offs

Provide:

Overall Score: /10

Detailed Feedback:
- communication
- structure
- domain knowledge
- level appropriateness

Question-wise feedback:
- Q1:
- Q2:
- Q3:

Improved Sample Answers for each question.
"""

    r = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return r.text

