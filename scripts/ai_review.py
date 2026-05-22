import json
from openai import OpenAI

client = OpenAI()

with open("tfplan.json") as f:
    tfplan = json.load(f)

with open("infracost.json") as f:
    infracost = json.load(f)

prompt = f"""
You are a senior DevOps engineer reviewing a Terraform pull request.

Review the infrastructure changes like a human reviewer.

Focus on:
- cloud cost increases
- oversized infrastructure
- staging vs production sizing
- security concerns
- reliability risks
- unnecessary cloud spend
- bad architecture choices

Keep feedback concise, practical, and human-like.

Terraform Plan:
{json.dumps(tfplan)[:12000]}

Infracost:
{json.dumps(infracost)[:12000]}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a senior infrastructure reviewer."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

review = response.choices[0].message.content

print(review)

with open("review.md", "w") as f:
    f.write(review)