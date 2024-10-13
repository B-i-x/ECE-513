import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


# completion = openai.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)

d = 'sections'
subsections = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

for area in subsections:
    for subdir, dirs, files in os.walk(area):
        for file in files:
            filepath = os.path.join(subdir, file)

            with open(filepath, 'r') as f:
                content = f.read()

            print(content)