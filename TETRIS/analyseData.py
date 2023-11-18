import os

# Read the content of the file
with open("TETRIS/ai_score.txt", "r") as file:
    content = file.read()

# Split the content into blocks
blocks = content.split("----------------------------------------\n")

# Remove empty blocks
blocks = [block.strip() for block in blocks if block.strip()]

# Parse each block and extract the score
parsed_blocks = []
for block in blocks:
    lines = block.split("\n")
    score_line = [line for line in lines if "Score" in line][0]
    score = int(score_line.split(":")[1].strip())
    parsed_blocks.append((block, score))

# Sort the blocks based on the score in descending order
sorted_blocks = sorted(parsed_blocks, key=lambda x: x[1], reverse=True)

# Get the directory of the script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Create a 'data' directory inside the 'TETRIS' folder if it doesn't exist
data_directory = os.path.join(script_directory, "data")
os.makedirs(data_directory, exist_ok=True)

# Create a new content with sorted blocks and separators
sorted_content = "\n".join([block[0] + "\n----------------------------------------" for block in sorted_blocks])

# Write the sorted content back to the file in the 'data' directory
output_file_path = os.path.join(data_directory, "sorted_ai_scores.txt")
with open(output_file_path, "w") as file:
    file.write(sorted_content)
# print(f"Sorted content has been written to: {output_file_path}")
