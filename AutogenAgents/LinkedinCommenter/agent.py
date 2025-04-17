from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat, BaseGroupChat
from autogen_agentchat.agents import AssistantAgent,  UserProxyAgent
from autogen_ext.models.anthropic import AnthropicChatCompletionClient
from autogen_core.model_context import UnboundedChatCompletionContext
from autogen_core.tools import FunctionTool  
from autogen_agentchat.ui import Console
import asyncio 
from custom_tools import get_url_content 

# === TOOLS ===
tools = [
    FunctionTool(name="get_url_content", func=get_url_content, description="Get contents of website url provided."),
]

# === LLM ===
model_client = AnthropicChatCompletionClient(model="claude-3-7-sonnet-20250219",
    api_key="Your API key",
    max_tokens=4096, max_retries=1,temperature=0.95,
    config={
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 4096,
        "temperature": 0.95,
        "api_key": "Your API key"
    }
)



# === AGENTS ===

# 1. Healthcare Domain Researcher
healthcare_researcher = AssistantAgent(
    name="HealthcareResearcher",
    system_message="""
    You are an expert in healthcare content analysis.
    Tasks:
    - Summarize healthcare content
    - Extract keywords and medical terms
    - Identify key points
    - Fact-check any claims (simulate using known facts)
    """,
    model_client=model_client,
    tools=tools
)

# 2. Post Researcher
post_researcher = AssistantAgent(
    name="PostResearcher",
    system_message="""
    You are a post analyst.
    Tasks:
    - Determine theme (e.g., innovation, policy, product launch)
    - Analyze tone (positive, critical, neutral)
    - Flag for sensitivity or misinformation
    """,
    model_client=model_client,
    tools=tools 
)

# 3. Client Researcher
client_researcher = AssistantAgent(
    name="ClientResearcher",
    system_message="""
    You find relevant content and posts from client profiles based on the given post's keywords and key points.
    Tasks:
    - Match post to clients interests.
    - Assess relevance between post and client content
    """,
     model_client=model_client,
     tools=tools
)

# 4. Commenter
commenter = AssistantAgent(
    name="Commenter",
    system_message="""
    You are a professional LinkedIn commenter.
    Tasks:
    - Generate insightful and on-brand comments for the post (one or two sentences)
    - Evaluate a comment’s clarity and tone
    - Improve comments to increase engagement
    - If cooment is appropriate, say APPROVE
    """,
     model_client=model_client
)

#-------------------
# orchestration
#-------------------

# Simulated user agent
user_proxy = UserProxyAgent(
    name="User",
    #system_message="You provide LinkedIn post content or a URL and instructions.",
    #code_execution_config={"use_docker": False}
)

max_msg_termination = MaxMessageTermination(max_messages=10)
text_termination = TextMentionTermination("APPROVE")
combined_termination = max_msg_termination | text_termination
agents=[ healthcare_researcher, post_researcher, client_researcher, commenter]

round_robin_team = SelectorGroupChat(agents,model_client=model_client,termination_condition=combined_termination) 


#---------------
# Example
#---------------
sample_post = """
The future of telemedicine is here. With AI-powered diagnostics and remote monitoring, 
patients in rural areas are finally getting the care they need. #healthtech #AI #telemedicine
"""
client_profie = """
Here's a sample LinkedIn profile and posts for a healthcare professional:

---

### **LinkedIn Profile**

**Name**: Dr. Priya Mehra  
**Title**: Compassionate Healthcare Leader | Expert in Patient-Centered Care | Advocate for Community Health  

**About**:  
"As a dedicated healthcare professional with over 10 years of experience, I am passionate about delivering holistic, patient-centered care. My expertise spans general medicine, preventive healthcare, and community outreach. I have successfully led cross-functional teams to improve patient outcomes and implement innovative care strategies. I’m deeply committed to making healthcare more accessible and equitable for all.  

I believe in the power of education and collaboration to inspire healthier communities. Outside the clinic, I enjoy mentoring young medical professionals, speaking at health seminars, and volunteering with community health initiatives."

**Skills**:  
- Patient Care  
- Preventive Medicine  
- Leadership & Team Management  
- Community Health Advocacy  
- Healthcare Technology Integration  

**Experience**:  
- **Senior Physician, Community Health Hospital** *(2018 - Present)*  
  - Spearheaded a telemedicine program, increasing access to care for rural patients by 45%.  
  - Led a team of 15 healthcare professionals, improving patient satisfaction scores by 25%.  

- **Resident Physician, City General Hospital** *(2013 - 2018)*  
  - Delivered exceptional patient care with a focus on diagnostics and disease prevention.  
  - Developed a successful health awareness campaign, reaching over 10,000 community members.  

**Education**:  
- MD, Internal Medicine, XYZ Medical College  
- MBBS, ABC University  

**Interests**: Holistic Wellness | Digital Health | Public Speaking  

---

### **Sample LinkedIn Posts**

**Post 1: Inspirational Moment**  
_"Witnessing a patient's recovery is a constant reminder of why I chose this profession. Today, I saw a patient walk out of the clinic with renewed hope and health. Moments like these fuel my passion for patient-centered care. To my fellow healthcare professionals: What moment recently inspired you in your practice?"_  

**Post 2: Healthcare Tip**  
_"In honor of World Health Day, let's talk preventive care. Did you know that routine check-ups can reduce the risk of serious illnesses by up to 30%? Let's empower our patients and communities with the knowledge they need to stay healthy. Share your favorite preventive health tips below!"_  

**Post 3: Celebrating Success**  
_"I'm thrilled to share that our new telemedicine initiative has successfully connected over 1,000 rural patients to quality care in just six months. This achievement is a testament to teamwork and innovation in healthcare. Here's to breaking barriers and building healthier communities."_  

**Post 4: Industry Insight**  
_"As healthcare professionals, we are at the forefront of incredible technological advancements. AI is transforming diagnostics, telemedicine is expanding access, and digital tools are enhancing patient engagement. How do you see these changes shaping our field in the coming years?"_  

"""


message=f"""Analyze this LinkedIn post: "{sample_post} and comment on behalf of client: {client_profie}"

Goals:
- Understand the main message and medical relevance
- Extract keywords and any healthcare trends
- Assess whether this is relevant for a client focused on digital health
- Suggest a comment that is insightful but concise

When done say TERMINATE
"""


async def chat(message):
    await Console(round_robin_team.run_stream(task=str(message)))

if __name__ == "__main__":
    asyncio.run(chat(message))
