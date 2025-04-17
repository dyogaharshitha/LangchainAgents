# CommentGeneratorAgent
Generates custom comments on linkedin posts

Sure! Here's a well-structured `README.md` file for your multi-agent LinkedIn comment generator system, based on the code you shared:

---

# 🤖 Multi-Agent LinkedIn Comment Generator (Healthcare Focus)

This project leverages an **Autogen-based agent framework** to analyze LinkedIn posts related to healthcare and generate **insightful, on-brand comments** from the perspective of a client. It uses **Claude 3 Sonnet** via Anthropic API and integrates multiple AI agents, each specialized in distinct tasks.

---

## 🧠 How It Works

The system uses a **SelectorGroupChat** to orchestrate communication between the following agents:

### 👥 Agents

1. **HealthcareResearcher**  
   - Extracts healthcare-related keywords and medical relevance.
   - Summarizes posts and fact-checks medical claims.

2. **PostResearcher**  
   - Determines the **theme** and **tone** of the post.
   - Flags any **sensitive topics** or **misinformation**.

3. **ClientResearcher**  
   - Matches content to client’s **interests**, **profile**, and **past posts**.
   - Checks for **relevance** to the client.

4. **Commenter**  
   - Generates **LinkedIn-ready comments**.
   - Evaluates tone, improves clarity, and ensures engagement.
   - Marks comments as `APPROVE` if they’re suitable.

5. **User (Simulated)**  
   - Provides the initial **LinkedIn post** and **client profile**.

---

## 🛠️ Features

- 🧩 Modular agent design using `autogen_agentchat`
- 🔗 Custom function tool `get_url_content()` to scrape URLs (extendable)
- 🧠 Contextual memory and multi-agent reasoning
- 💬 Asynchronous streaming chat interface via `Console()`
- ✅ Stops when a comment is marked as `APPROVE` or after 10 rounds

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/healthcare-linkedin-commenter.git
cd healthcare-linkedin-commenter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Ensure you have Python 3.8+ and an Anthropic API key.

### 3. Add Your Anthropic API Key

Update the `api_key` field in the `AnthropicChatCompletionClient`:

```python
api_key="Your API key"
```

> Or load it from environment variables for better security.

### 4. Run the Bot

```bash
python main.py
```

The agents will begin collaborating and stream output to the console.

---

## 📦 Project Structure

```
.
├── custom_tools.py         # Custom tools like `get_url_content`
├── agent.py                 # Main execution script
├── README.md               # This file
├── requirements.txt        # Python dependencies
```

---

## ✨ Example Output

Given a post about **AI in telemedicine**, the system might generate:

> _"Impressive shift toward equitable healthcare! As someone who led a telemedicine rollout, I truly appreciate how AI is bridging care gaps in underserved communities. Exciting times for healthtech."_  
> → `APPROVE`

---

## 🔧 Customization

- 💡 Add more agents for sentiment scoring, influencer matching, etc.
- 🌐 Enable real-time web tools to fact-check or fetch current content
- 🗂 Extend tools with company profile matchers or regulatory compliance checkers

---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

Built with [Autogen](https://github.com/microsoft/autogen), [Anthropic Claude](https://www.anthropic.com/index/claude), and Python asyncio.
