import re, os

def create_file(file_path):
    # Create an empty file
    with open(file_path, 'w') as file:
        pass

def split_sections(input_filepath):

    # Regex pattern to identify section headers e.g., "1.1 "
    section_pattern = re.compile(r'^[5-9]\.\s*\d+ [^\d]+$')
    
    # Initialize variables
    current_section = None
    section_content = []
    
    # Read the input file
    with open(input_filepath, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        # Check if the line is a section header
        if section_pattern.match(line.strip()):
            # If there is current section data, save it
            print("match")
            if current_section is not None:
                output_folder = f'sections/{current_section.strip()}'
                os.makedirs(output_folder, exist_ok=True)
                output_filepath = os.path.join(output_folder, 'textbook.txt')
                q_filepath = os.path.join(output_folder, 'questions.txt')
                a_filepath = os.path.join(output_folder, 'answers.txt')
                create_file(q_filepath)
                create_file(a_filepath)

                with open(output_filepath, 'w') as output_file:
                    output_file.write(''.join(section_content))
                print(f"Section {current_section.strip()} saved to {output_filepath}")
            
            # Start a new section
            current_section = line.strip()
            section_content = []
        else:
            # Add line to the current section content
            # Add line to the current section content if it doesn't contain 'Salehi'
            if 'Salehi' not in line:
                section_content.append(line)
            section_content.append(line)
    
    # Save the last section encountered
    if current_section is not None:
        output_folder = f'sections/{current_section.strip()}'
        os.makedirs(output_folder, exist_ok=True)
        q_filepath = os.path.join(output_folder, 'questions.txt')
        a_filepath = os.path.join(output_folder, 'answers.txt')
        create_file(q_filepath)
        create_file(a_filepath)
        output_filepath = os.path.join(output_folder, 'textbook.txt')
        with open(output_filepath, 'w') as output_file:
            output_file.write(''.join(section_content))
        print(f"Section {current_section.strip()} saved to {output_filepath}")

# Example usage
split_sections('raw/chp6text.txt')
