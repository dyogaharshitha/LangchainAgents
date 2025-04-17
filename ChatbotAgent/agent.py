from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_anthropic import ChatAnthropic 
from langchain.llms import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory
from langchain.chat_models.base import BaseChatModel
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

from data import tapas_search_question

tools = [
    Tool.from_function(
        name="search_database",
        func=tapas_search_question,
        description="Searches movie database given question as input."
    ),
    
    ]

llm = ChatAnthropic(  #deepseek-ai/deepseek-vl-1.3b-chat
    model="claude-3-7-sonnet-20250219",
    temperature=1,
    max_tokens=4096,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    anthropic_api_key="Your-API-key"
)
# Works with local LLM
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

# Wrap in LangChain's HuggingFacePipeline
# llm = HuggingFacePipeline(pipeline=hf_pipeline)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True) 
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=False,
    agent_kwargs={
        "system_message": (
            "You are a helpful assistant. When using a tool, trust the result completely. "
            "Do not provide feedback or retry. Just output the result or move on."
        )
    }
)

MAX_TURNS = 3
turn = 0

while turn < MAX_TURNS:
    query = input("User: ")
    if "terminate" in query.lower():
        print("Agent: TERMINATE") 
        break
    response = agent.run(query)
    print(response)
    turn += 1

