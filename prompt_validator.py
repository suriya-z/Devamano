def validate_prompt(mode: str, action: str, topic: str, level: str = None, language: str = None):
    text_actions = ["generate", "describe", "explain"]
    code_actions = ["generate", "explain", "give"]

    if mode not in ["text", "code"]:
        raise ValueError("Mode must be 'text' or 'code'")

    if mode == "text":
        # Goal dropdown removed from UI — default action to 'generate'
        if level not in ["basics", "advanced"]:
            level = "basics"
        level_label = "beginner-friendly basics" if level == "basics" else "advanced, in-depth"
        return (
            f"Write a comprehensive article about '{topic}' at a {level_label} level. "
            f"The response must be strictly 150-200 words."
        )

    if mode == "code":
        if action not in code_actions:
            raise ValueError(f"Code mode requires action: {'/'.join(code_actions)}")
        if not language:
            raise ValueError("Code mode requires a programming language")
        return f"Generate {topic} code in {language}. Provide the source code with a clear explanation."
