from prompt_validator import validate_prompt
from content_generator import generate_content
from evaluator import evaluate_content

def test():
    mode = "text"
    action = "generate"
    topic = "Benefits of AI in Coding"
    level = "basics"
    language = None

    print(f"--- Running Test ---")
    print(f"Mode: {mode}")
    print(f"Action: {action}")
    print(f"Topic: {topic}")
    print(f"Level: {level}")
    print(f"Language: {language}")

    prompt = validate_prompt(mode, action, topic, level, language)
    print(f"\nGenerated Prompt: {prompt}")

    result_dict = generate_content(prompt, topic, mode)
    content = result_dict.get("generated_content")
    context = result_dict.get("knowledge_base", "") + " " + result_dict.get("reference_content", "")
    evaluation = evaluate_content(content, context, mode)

    print("\nGenerated Content:\n")
    print(content)
    print("\nEvaluation:\n", evaluation)

if __name__ == "__main__":
    test()
