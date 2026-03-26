from prompt_validator import validate_prompt
from content_generator import generate_content
from evaluator import evaluate_content

def run():
    mode = input("Enter mode (text/code): ")
    action = input("Enter action (generate/describe/explain/give): ")
    topic = input("Enter topic: ")
    level = None
    language = None
    if mode == "text":
        level = input("Enter level (basics/advanced): ")
    elif mode == "code":
        language = input("Enter language (e.g. Python, JavaScript): ")

    prompt = validate_prompt(mode, action, topic, level, language)
    content, links, context = generate_content(prompt, topic, mode)
    evaluation = evaluate_content(content, context, mode)

    print("\nGenerated Content:\n")
    print(content)
    print("\nEvaluation:\n", evaluation)
    print("\nVerification Links:\n", "\n".join(links))

if __name__ == "__main__":
    run()
