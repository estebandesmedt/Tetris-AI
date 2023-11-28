import os
import matplotlib.pyplot as plt

# Read scores from the file
with open("TETRIS/ai_score.txt", "r") as file:
    content = file.read()

# Split the content into blocks
blocks = content.split("----------------------------------------\n")

# Remove empty blocks
blocks = [block.strip() for block in blocks if block.strip()]

parsed_blocks = []
for block in blocks:
    lines = block.split("\n")
    score_lines = [line for line in lines if "Score" in line]
    if score_lines:
        score_line = score_lines[0]
        score = int(score_line.split(":")[1].strip())
        parsed_blocks.append(score)

# Create a directory for data if it doesn't exist
script_directory = os.path.dirname(os.path.realpath(__file__))
data_directory = os.path.join(script_directory, "data")
os.makedirs(data_directory, exist_ok=True)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(parsed_blocks, bins=20, color='blue', edgecolor='black')
plt.title('Histogram of AI Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# Save the histogram plot to a new file
histogram_plot_file_path = os.path.join(data_directory, "ai_scores_histogram.png")
plt.savefig(histogram_plot_file_path)

# Display the plot (uncomment the line below if you want to display the plot)
# plt.show()

print(f"Histogram plot has been saved to: {histogram_plot_file_path}")
