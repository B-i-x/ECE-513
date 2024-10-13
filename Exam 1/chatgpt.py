import openai
import os
import json
import time
import re

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Directory containing the textbook sections
d = 'sections'
subsections = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d, o))]

def extract_section_numbers(path):
    # Assuming the directory names are formatted like '1', '2', '1.1', '1.2', etc.
    # Adjust the regex pattern based on your directory naming convention
    pattern = r'(\d+)(?:\.(\d+))?'
    matches = re.findall(pattern, path)
    section = matches[0][0] if matches else '0'
    subsection = matches[0][1] if matches and matches[0][1] else '0'
    return section, subsection

# Iterate over each subsection
for area in subsections:
    for subdir, dirs, files in os.walk(area):
        for file in files:
            
            if "questions" in file or "answers" in file:
                continue
            
            filepath = os.path.join(subdir, file)
            print(f"Processing {filepath}...")
            # Read the textbook content from the file
            with open(filepath, 'r') as f:
                file_textbook_content = f.read()
            # print(len(file_textbook_content))

            # Truncate content if it's too long (adjust based on the model's token limit)
            max_content_length = 50000  # Approximately 6000 tokens
            if len(file_textbook_content) > max_content_length:
                file_textbook_content = file_textbook_content[:max_content_length]
            # Extract section and subsection numbers
            relative_path = os.path.relpath(subdir, d)
            section, subsection = extract_section_numbers(relative_path)
            # Build the prompt for the AI model
            prompt = f"""Based on the following content, please create 10 questions, they can be Multiple choice, Multiple answers, Short answer, or Fill in the blank. Do not make true/false questions. Provide the correct answers as well. 

            For each question, assign an ID in the format [{section}.{subsection}.question_number], where question_number starts from 1 and increments for each question.

            Please format the questions and answers exactly as shown in the following example:

            questions:
            ---

            [1.2.1] Multiple Choice: Which tag is used to define an independent, self-contained content that could be syndicated?
            - (A) <div>
            - (B) <section>
            - (C) <article>
            - (D) <span>

            ---

            [1.2.2] Multiple Choice: What does the <link> tag primarily use within an HTML document?
            - (A) To link JavaScript files
            - (B) To establish connections between different HTML pages
            - (C) To connect the document to external stylesheets
            - (D) To embed responsive meta tags

            ---

            answers:
            [1.2.1] (C) <article>
            [1.2.2] (C) To connect the document to external stylesheets
            The content is:

            {file_textbook_content}
            """
            # print(prompt)
            # Prepare the messages for the ChatCompletion API
            messages = [
                {"role": "system", "content": "You are a helpful assistant that creates test questions based on provided textbook content."},
                {"role": "user", "content": prompt}
            ]
            # Call the OpenAI API to generate questions
            try:
                completion = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=16384,  # Adjust as needed
                )

                response = completion.choices[0].message.content
                print(response)
                # Separate questions and answers

                # Call the OpenAI API to generate questions
                try:
                    # Split the response into 'questions' and 'answers' sections
                    questions_part = ''
                    answers_part = ''
                    if 'questions:' in response and 'answers:' in response:
                        parts = response.split('answers:')
                        questions_part = parts[0].strip()
                        questions_part = questions_part.replace('questions:', '')
                        answers_part = parts[1].strip()
                    else:
                        print(f"Unexpected format in response for {filepath}. Saving entire response as questions.")
                        questions_part = response

                    # Save the questions to a file in the same directory
                    questions_filename = os.path.join(subdir, f'questions_{section}.{subsection}')
                    with open(questions_filename, 'w', encoding='utf-8') as f_out:
                        f_out.write(questions_part)

                    # Save the answers to a separate file
                    answers_filename = os.path.join(subdir, f'answers_{section}.{subsection}')
                    with open(answers_filename, 'w', encoding='utf-8') as f_out:
                        f_out.write(answers_part)

                    print(f"Generated questions and answers for {filepath}")

                except Exception as e:
                    print(f"Error processing response for {filepath}: {e}")


            except Exception as e:
                print(f"Error processing {filepath}: {e}")