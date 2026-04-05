def build_prompt(context, query, mode):

    if mode == "beginner":
        instruction = """Explain the answer in simple, clear language that a non-expert can understand.
- Use everyday examples where relevant
- Break complex ideas into smaller parts
- Avoid jargon unless necessary, and define it if used"""
    elif mode == "interview":
        instruction = """Provide a concise, technical answer suitable for technical interviews.
- Be precise and specific
- State key concepts clearly
- Keep answer under 150 words
- Highlight important details"""
    elif mode == "summary":
        instruction = """Provide a brief, concise summary of the key points.
- Extract only the most important information
- Keep to 2-3 main points maximum
- Be direct and avoid repetition"""
    else:
        instruction = "Provide a clear, direct answer based directly on the context provided."

    return f"""You are an expert assistant tasked with answering questions using ONLY the provided context.

CRITICAL RULES:
1. Answer ONLY based on the context given below
2. Do NOT add information from your training data
3. If the answer is not in the context, say: "I couldn't find this information in the provided document."
4. Be precise and factual
5. Cite relevant parts of the context when appropriate

CONTEXT:
{context}

QUESTION:
{query}

RESPONSE MODE:
{instruction}

ANSWER:
"""