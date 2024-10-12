import os

question_back = {}

def parse_questions(filepath):
    f = open(filepath, "r")
    content = f.read()
    print(content)
    f.close()
    return content

d = 'sections'
subsections = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

for area in subsections:
    for subdir, dirs, files in os.walk(area):
        for file in files:
            filepath = os.path.join(subdir, file)
            
            if "questions" in file:
                parse_questions(filepath)
            elif "answers" in file:
                pass

            