# 📣 EchoPost
*Let your ideas echo across LinkedIn.*

EchoPost is an AI-powered LinkedIn Post Generator built with Python, LangChain, and Groq LLMs.  
It analyzes example posts, extracts metadata, and generates engaging LinkedIn posts in English or Hinglish with customizable length.

---

## 🚀 Features
- 🔍 **Metadata Extraction** – Detects line count, language, and tags from raw LinkedIn posts.  
- 📝 **Post Generation** – Creates LinkedIn-ready posts on any topic with emojis for better engagement.  
- 🎯 **Few-Shot Learning** – Uses filtered real examples to fine-tune writing style.  
- 🌐 **Language Support** – English + Hinglish (mix of Hindi and English).  
- ⚡ **Configurable Lengths** – Short (1–5 lines), Medium (6–10 lines), Long (11–15 lines).  

---

## 📂 Project Structure
EchoPost/
│── .venv/ # Virtual environment
│── pycache/ # Python cache files
│── data/ # Raw and processed post data (JSON)
│── .env # Environment variables (API keys etc.)
│── few_shot.py # Few-shot examples handler
│── llm_helper.py # LLM configuration & initialization
│── main.py # Entry point for the project
│── post_generator.py # Core LinkedIn post generator
│── preprocess.py # Preprocess raw LinkedIn posts
│── requirements.txt # Project dependencies

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/EchoPost.git
   cd EchoPost

2 **Create and activate a virtual environment**
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3 **Install dependencies**
pip install -r requirements.txt

4 **Set environment variables**
- Create a .env file in the root directory:
GROQ_API_KEY=your_api_key_here
- Add any other required keys (e.g., OpenAI API key if you switch models).

▶️ Usage
1. **Preprocess raw posts**
python preprocess.py
This extracts metadata (line count, language, tags) from data/raw_posts.json
and saves it to data/processed_posts.json.

2. **Generate a LinkedIn Post**
python post_generator.py
Inside post_generator.py, you can try:
print(GeneratePost("Self Improvement", "Short", "English"))

3. **Run the main script**
python main.py

🛠️ Tech Stack
Python 3.10+
LangChain
Groq LLM(or OpenAI-compatible API)
Pandas for data processing

🤝 Contributing
Contributions are welcome!
Feel free to fork this repo, create a branch, and submit a pull request.

📜 License
This project is licensed under the MIT License.

✨ Acknowledgements
Inspired by the need for creators to simplify LinkedIn content writing.
Built with ❤️ using LangChain + Groq.
