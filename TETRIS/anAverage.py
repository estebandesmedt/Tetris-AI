import os

with open("TETRIS/ai_score.txt", "r") as file:
    content = file.read()

blocks = content.split("----------------------------------------\n")

blocks = [block.strip() for block in blocks if block.strip()]

parsed_blocks = []
for block in blocks:
    lines = block.split("\n")
    height_line = [line for line in lines if "Height" in line]
    lines_line = [line for line in lines if "Lines" in line]
    holes_line = [line for line in lines if "Holes" in line]
    bumps_line = [line for line in lines if "Bumps" in line]
    score_line = [line for line in lines if "Score" in line]

    if not (height_line and lines_line and holes_line and bumps_line and score_line):
        # Skip this block if any of the required lines is missing
        continue

    height = float(height_line[0].split(":")[1].strip())
    lines = float(lines_line[0].split(":")[1].strip())
    holes = float(holes_line[0].split(":")[1].strip())
    bumps = float(bumps_line[0].split(":")[1].strip())
    score = int(score_line[0].split(":")[1].strip())

    parsed_blocks.append(((height, lines, holes, bumps), score))

# Create a dictionary to store the sum and count for each combination of multipliers
average_scores = {}
for vermenigvuldigers, score in parsed_blocks:
    if vermenigvuldigers in average_scores:
        average_scores[vermenigvuldigers][0] += score
        average_scores[vermenigvuldigers][1] += 1
    else:
        average_scores[vermenigvuldigers] = [score, 1]

# Calculate the average score for each combination
for vermenigvuldigers, (total_score, count) in average_scores.items():
    average_score = total_score / count
    average_scores[vermenigvuldigers] = average_score

# Sort the combinations based on their average scores
sorted_combinations = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

script_directory = os.path.dirname(os.path.realpath(__file__))

data_directory = os.path.join(script_directory, "data")
os.makedirs(data_directory, exist_ok=True)

sorted_content = "\n".join([
    f"Height: {vermenigvuldigers[0]}\nLines : {vermenigvuldigers[1]}\nHoles : {vermenigvuldigers[2]}\nBumps : {vermenigvuldigers[3]}\nAverage Score : {average_score:.2f}\n----------------------------------------"
    for vermenigvuldigers, average_score in sorted_combinations])

output_file_path = os.path.join(data_directory, "sorted_average_ai_scores.txt")
with open(output_file_path, "w") as file:
    file.write(sorted_content)
# print(f"Sorted content has been written to: {output_file_path}")
