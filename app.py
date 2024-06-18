import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain import PromptTemplate
import gradio as gr

# Set HuggingFace API token (replace 'your_huggingface_api_token' with your actual token)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

# Define the HuggingFace model
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(repo_id=repo_id,
                          max_length=128,
                          temperature=0.7,
                          token=os.environ["HUGGINGFACEHUB_API_TOKEN"])

# Define the prompt template and LLM chain
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

# Function to invoke the model
def get_answer(question):
    llm_chain = prompt | llm
    response = llm_chain.invoke(question)
    return response

# Create a Gradio interface
interface = gr.Interface(
    fn=get_answer,  # Function to invoke
    inputs="text",  # Input type
    outputs="text",  # Output type
    title="Generative AI Question Answering",
    description="Ask a question and get a detailed answer step by step.",
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch(share=True)
