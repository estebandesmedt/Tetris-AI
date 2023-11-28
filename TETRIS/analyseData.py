import os

with open("TETRIS/ai_score.txt", "r") as file:
    content = file.read()

blocks = content.split("----------------------------------------\n")

blocks = [block.strip() for block in blocks if block.strip()]

parsed_blocks = []
for block in blocks:
    lines = block.split("\n")
    score_lines = [line for line in lines if "Score" in line]
    if score_lines:
        score_line = score_lines[0]
    score = int(score_line.split(":")[1].strip())
    parsed_blocks.append((block, score))

sorted_blocks = sorted(parsed_blocks, key=lambda x: x[1], reverse=True)

script_directory = os.path.dirname(os.path.realpath(__file__))

data_directory = os.path.join(script_directory, "data")
os.makedirs(data_directory, exist_ok=True)

sorted_content = "\n".join([block[0] + "\n----------------------------------------" for block in sorted_blocks])

output_file_path = os.path.join(data_directory, "sorted_ai_scores.txt")
with open(output_file_path, "w") as file:
    file.write(sorted_content)
# print(f"Sorted content has been written to: {output_file_path}")
