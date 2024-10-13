import os, re, csv

question_back = {}

def parse_questions(filepath):
    with open(filepath, "r", encoding='utf-8') as f:
        content = f.read()

    # Split the content into individual questions using '---' as delimiter
    questions_raw = content.strip().split('---')

    questions = {}

    for question_raw in questions_raw:
        question_raw = question_raw.strip()
        if not question_raw:
            continue  # Skip empty entries

        # Extract the question ID and the rest of the content
        id_match = re.match(r'\[(.*?)\]\s*(.*)', question_raw, re.DOTALL)
        if id_match:
            qid = id_match.group(1).strip()
            qtext = id_match.group(2).strip()
            # Store the question text with its ID
            questions[qid] = qtext
        else:
            print(f"Could not parse question in file {filepath}: {question_raw[:50]}...")

    return questions

def parse_answers(filepath):
    with open(filepath, "r", encoding='utf-8') as f:
        lines = f.readlines()


    answers = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Attempt to match ID with square brackets
        id_match = re.match(r'\[(.*?)\]\s*(.*)', line)
        if id_match:
            qid = id_match.group(1).strip()
            ans_text = id_match.group(2).strip()
            answers[qid] = ans_text
            continue

        # Attempt to match ID without square brackets
        id_match = re.match(r'(\d+\.\d+\.\d+)\s+(.*)', line)
        if id_match:
            qid = id_match.group(1).strip()
            ans_text = id_match.group(2).strip()
            answers[qid] = ans_text
            continue

        print(f"Could not parse answer in file {filepath}: {line[:50]}...")

    return answers

# Collect all questions and answers from the 'sections' directory
all_questions = {}
all_answers = {}

d = 'sections'
subsections = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

for area in subsections:
    for subdir, dirs, files in os.walk(area):
        for file in files:
            filepath = os.path.join(subdir, file)
            
            if "questions" in file:
                questions = parse_questions(filepath)
                all_questions.update(questions)
            elif "answers" in file:
                answers = parse_answers(filepath)
                all_answers.update(answers)

# Combine questions and answers based on question ID
combined_data = []

for qid in all_questions:
    question_text = all_questions[qid]
    answer_text = all_answers.get(qid, "Answer not found")
    combined_data.append({
        'ID': qid,
        'Question': question_text,
        'Answer': answer_text
    })

# Define CSV columns
csv_columns = ['ID', 'Question', 'Answer']

# Write the combined data into a CSV file
with open('questions_answers.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in combined_data:
        writer.writerow(data)           