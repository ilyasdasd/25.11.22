import os

b_dir = os.getcwd()
dir_name = "Flies"

file_path = os.path.join(b_dir, dir_name)
files = os.listdir(file_path)


file_dict = {}
for f in files:
    name = os.path.join(file_path,f)
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        text = []
        len_text = len(lines)
        for line in lines:
            text.append(line.strip())
        file_dict[f] = (len_text, text)

sorted_values = sorted(file_dict.values())
sorted_dict = {}

for i in sorted_values:
    for j in file_dict.keys():
        if file_dict[j] == i:
            sorted_dict[j] = file_dict[j]
            break

with open('sort_text.txt', "w", encoding='utf-8') as file:
    for key, value in sorted_dict.items():
        file.write(f"{key}\n")
        file.write(f"{value[0]}\n")
        for val in value[1]:
            file.write(f"{val}\n")