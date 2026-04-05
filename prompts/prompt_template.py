def build_prompt(context, query, mode):

    if mode == "beginner":
        instruction = "Explain in simple terms with examples."
    elif mode == "interview":
        instruction = "Give a concise, technical answer suitable for interviews."
    elif mode == "summary":
        instruction = "Summarize briefly."
    else:
        instruction = ""

    return f"""
You are an AI assistant.

Context:
{context}

Question:
{query}

Instruction:
{instruction}

If answer is not in context, say:
"I couldn't find this in the document."

Answer:
"""