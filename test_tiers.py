import sys
sys.path.append('C:\\Users\\Admin\\Desktop\\genai_project')
from content_generator import evaluate_domain_tier

urls = [
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://ischoolonline.berkeley.edu/blog/what-is-machine-learning/",
    "https://www.geeksforgeeks.org/machine-learning/types-of-machine-learning/",
    "https://www.ibm.com/think/topics/machine-learning-types",
    "https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html",
    "https://www.khanacademy.org/science/computer-science",
    "https://someblog.org/article"
]

print(f"{'URL':<70} | {'Tier':<4} | {'Weight':<6}")
print("-" * 85)
for url in urls:
    tier, weight = evaluate_domain_tier(url)
    print(f"{url:<70} | {tier:<4} | {weight:<6}")
