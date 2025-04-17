from langchain_core.runnables import RunnableMap
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

from data import tapas_search_question

model_name = "microsoft/phi-2"  # Or your local path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype="auto")

# Create HuggingFace pipeline
hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=1024,
    temperature=0.7,
    do_sample=True,
)

# HuggingFace LLM (enhancer)
llm_enhancer = HuggingFacePipeline(pipeline=hf_pipeline)

# OpenAI responder LLM
llm_responder = HuggingFacePipeline(pipeline=hf_pipeline)

# Prompts
enhancer_prompt = PromptTemplate.from_template("""
You are a prompt enhancer. Based on the history and user input, rephrase the input if necessary to make it self sufficient.

History:
{history}

User Input:
{question}

Enhanced Prompt:
""")

responder_prompt = PromptTemplate.from_template("""
Context:
{context}

You are as friendly chatbot. Use context to respond to the user in a sentence or two. 

User:
{enhanced_prompt}

Bot Response:""")

# Memory for conversation history
memory = ConversationBufferMemory(return_messages=True)

# Enhancer pipeline
enhancer_chain = (
    RunnableMap({
        "history": lambda x: memory.load_memory_variables({})["history"] if memory else "",
        "question": lambda x: x["question"]
    })
    | enhancer_prompt
    | llm_enhancer
    | (lambda x: {"enhanced_prompt": x[len(enhancer_prompt.template):]})  # Wrap output
)

# Responder pipeline
responder_chain = (
    RunnableMap({
        "enhanced_prompt": lambda x: x["enhanced_prompt"],
        "context": lambda x: x["context"]
    })
    | responder_prompt
    | llm_responder
)

# Combined pipeline
def run_pipeline(question: str, context: str):
    enhanced = enhancer_chain.invoke({"question": question})
    knowledge = tapas_search_question(enhanced) 
    response = responder_chain.invoke({
        "enhanced_prompt": enhanced["enhanced_prompt"],
        "context": knowledge 
    })

    memory.save_context({"input": question}, {"output": response})
    return response

# 🧪 Example
if __name__ == "__main__":
  for i in range(3):  
    question = input("User: ") #"Who is the director of the movie avatar?"
    context = tapas_search_question(question) #"AI can analyze large sets of medical images to detect early signs of tumors more accurately than traditional methods."
    print(run_pipeline(question, context))
