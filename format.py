import re

# post processing of transcript.txt file
f = open("formatted.txt", "w", encoding='utf-8')
# Open the file in read mode
with open('transcription.txt', 'r', encoding='utf-8') as file:
    # Read each line in the file
    pattern = r'\?\.\! '
    for text in file:
        if (text.startswith(' ')):
            text = text[1:]
        lines = text.split('. ')

    for line in lines:
        line += "."
        f.write(line)
        f.write("\n")

f.close()