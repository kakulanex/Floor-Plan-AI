# Floor-Plan-AI
"Imagine designing customized, space-efficient floor plans in seconds — not hours. Our AI-powered Floor Plan Generator leverages natural language processing and machine learning to instantly translate everyday instructions like 'two-bedroom apartment with an open kitchen' into functional, visual floor plans. Tailored for housing authorities like the Kano State Housing Corporation, this tool streamlines architectural planning, reduces design costs, and enhances customer satisfaction through automation and smart design suggestions. It's the future of real estate planning — fast, flexible, and fully intelligent."

# 🏠 Floor Plan AI: About the Project

## HOW TO INSTALL

 - git clone https://github.com/kakulanex/Floor-Plan-AI.git
 - cd Floor-Plan-AI
 - pip install requirements.txt
 - python Floor-Plan-AI.py
  
## 🚀 Inspiration
The inspiration for this project came from observing the time-consuming and costly process of designing residential floor plans in public housing systems, particularly at the **Kano State Housing Corporation**. I wanted to explore how **Artificial Intelligence** could simplify architectural planning by automatically generating floor layouts based on natural language instructions.

## 🧠 What I Learned
Through this project, I deepened my understanding of:
- **Natural Language Processing (NLPgit)** with `DistilBERT`
- **Supervised fine-tuning** for classification tasks
- **PyTorch and Transformers** for training custom AI models
- **Matplotlib** for drawing 2D architectural plans
- **Handling real-world datasets** and converting user input into structured formats

## 🛠️ How I Built It
1. **Dataset Creation**: I created a dummy dataset of floor plan requests and corresponding labels to simulate user needs. I also researched real datasets (e.g., ROBIN, RentHop, and SESYD).
2. **Model Development**: I fine-tuned a `DistilBERT` model to classify user instructions into predefined floor plan templates.
3. **Tokenization and Prediction**: I used Hugging Face’s tokenizer and model to process and predict the layout features.
4. **Visualization**: I used `matplotlib` to draw simplified floor plans based on model output (e.g., bedrooms, kitchen type, living room size).
5. **Integration**: I wrote a main script to handle dataset loading, model training, prediction, and drawing — all in one.

## ⚠️ Challenges Faced
- **Fine-tuning NLP models** with limited data required careful preprocessing and multiple iterations.
- **Token dimension mismatches** during training led to debugging and adjustments in `DataLoader` logic.
- **Dataset acquisition**: Real-world labeled architectural data is scarce or unstructured, so I had to simulate meaningful examples.
- **Drawing logic**: Translating abstract room features into coordinate plots demanded creativity in spatial mapping.

## 💡 What's Next?
I plan to:
- Integrate a **web interface** where users can input instructions and receive real-time floor plan sketches.
- Use **real-world datasets** for improved accuracy and generalization.
- Add **room dimension scaling** and **multiple floor support**.

> This project combines AI, architecture, and automation — making design smarter, faster, and accessible.
