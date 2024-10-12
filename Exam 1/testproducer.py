import os

question_back = {}
d = 'sections'
subsections = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

for area in subsections:
    for subdir, dirs, files in os.walk(area):
        for file in files:
            print(os.path.join(subdir, file))