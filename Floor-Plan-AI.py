import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import matplotlib.pyplot as plt

# Function to process instructions using DistilBERT
def process_instructions(instructions):
    # Load tokenizer and model from Hugging Face model ID
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=3)

    # Tokenize the instructions
    inputs = tokenizer(instructions, return_tensors="pt")

    # Process the instructions
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()

    # Map the predicted class to a specific floor plan feature
    features_map = {
        0: {"bedrooms": 2, "living_room_size": "large", "kitchen_type": "open"},
        1: {"bedrooms": 3, "living_room_size": "medium", "kitchen_type": "closed"},
        2: {"bedrooms": 1, "living_room_size": "small", "kitchen_type": "open"},
    }

    return features_map[predicted_class]

# Function to generate the floor plan based on features
def generate_floor_plan(features):
    return features

# Function to draw the floor plan with labels
def draw_floor_plan(features):
    fig, ax = plt.subplots()

    # Drawing the living room
    if features["living_room_size"] == "large":
        ax.plot([1, 1, 6, 6, 1], [1, 5, 5, 1, 1], label='Living Room')
        ax.text(3.5, 3, 'Living Room (Large)', ha='center')
    elif features["living_room_size"] == "medium":
        ax.plot([1, 1, 5, 5, 1], [1, 4, 4, 1, 1], label='Living Room')
        ax.text(3, 2.5, 'Living Room (Medium)', ha='center')
    else:
        ax.plot([1, 1, 4, 4, 1], [1, 3, 3, 1, 1], label='Living Room')
        ax.text(2.5, 2, 'Living Room (Small)', ha='center')

    # Drawing the kitchen
    if features["kitchen_type"] == "open":
        ax.plot([6, 6, 9, 9, 6], [1, 4, 4, 1, 1], label='Kitchen')
        ax.text(7.5, 2.5, 'Kitchen (Open)', ha='center')
    else:
        ax.plot([6, 6, 8, 8, 6], [1, 3, 3, 1, 1], label='Kitchen')
        ax.text(7, 2, 'Kitchen (Closed)', ha='center')

    # Drawing the bedrooms
    if features["bedrooms"] >= 1:
        ax.plot([1, 1, 3, 3, 1], [5, 7, 7, 5, 5], label='Bedroom 1')
        ax.text(2, 6, 'Bedroom 1', ha='center')
    if features["bedrooms"] >= 2:
        ax.plot([3, 3, 5, 5, 3], [5, 7, 7, 5, 5], label='Bedroom 2')
        ax.text(4, 6, 'Bedroom 2', ha='center')
    if features["bedrooms"] == 3:
        ax.plot([5, 5, 7, 7, 5], [5, 7, 7, 5, 5], label='Bedroom 3')
        ax.text(6, 6, 'Bedroom 3', ha='center')

    # Adding toilet
    ax.plot([8, 8, 9, 9, 8], [4, 5, 5, 4, 4], label='Toilet')
    ax.text(8.5, 4.5, 'Toilet', ha='center')

    # Adding car drive-in
    ax.plot([0, 0, 10, 10, 0], [-3, -1, -1, -3, -3], label='Car Drive-In')
    ax.text(5, -2, 'Car Drive-In', ha='center')

    ax.legend()
    plt.show()

# Main function to run the entire process
def main():
    # Prompt user for instructions
    instructions = input("Please describe your desired apartment features: ")

    # Step 1: Process instructions using DistilBERT
    features = process_instructions(instructions)

    # Step 2: Generate floor plan (optional in this simplified example)
    floor_plan = generate_floor_plan(features)

    # Step 3: Draw the floor plan
    draw_floor_plan(floor_plan)

# Run the main function
if __name__ == "__main__":
    main()
