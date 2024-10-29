---

# Gen_AI Chatbot

This repository hosts the code for **Gen_AI**, an interactive AI chatbot created using Large Language Models (LLMs) via LangChain and HuggingFace. The chatbot interface is built with Gradio and deployed on Hugging Face Spaces for easy access. [Try out the Gen_AI Chatbot here](https://huggingface.co/spaces/Dilleswari/Gen-AI)!

## Features

- **Interactive Chatbot**: Created using LangChain for chaining LLM tasks, allowing complex interactions and natural conversations.
- **Gradio Interface**: A user-friendly web interface for interacting with the chatbot.
- **Deployed on Hugging Face Spaces**: Easily accessible for anyone with the link above.

## Installation

Ensure you have [Python 3.x](https://www.python.org/) or [Anaconda](https://www.anaconda.com/) installed, then install the necessary dependencies:

```bash
pip install langchain-huggingface huggingface_hub transformers accelerate bitsandbytes langchain gradio
```

## How to Run Locally

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dilleswari1234/Gen_AI.git
   cd Gen_AI
   ```

2. **Run the Application**:

   Run the main application with:

   ```bash
   python app.py
   ```

   Alternatively, you can access the chatbot directly on [Hugging Face Spaces](https://huggingface.co/spaces/Dilleswari/Gen-AI) without any local setup and start interacting with the chatbot directly in your browser.

## Project Structure

```
Gen_AI/
├── dilli_chatbot.ipynb    #run this notebook to get .pkl files
├── app.py                 # Main application file for running locally
├── README.md              # Project documentation
└── requirements.txt       # Dependencies required to run the project
```

- **`app.py`**: Runs the main application locally if preferred over the web version.
- **`notebooks/`**: Contains notebooks for model experimentation.

## Notes

- Make sure dependencies are up to date. All required packages are listed in `requirements.txt` for convenience.
- The Hugging Face Space allows anyone to use the chatbot without needing local resources, but you may still run it locally if preferred.

## Contact

For questions or contributions, please reach out through GitHub issues or contact [bathularajadilleswari06639@gmail.com].

---

This `README.md` now includes all your information, from deployment details on Hugging Face Spaces to setup instructions, making it easy for anyone to get started with Gen_AI!


![Screenshot 2024-10-29 193737](https://github.com/user-attachments/assets/f6a7820b-920b-487a-8168-09f6f2551eb8)
