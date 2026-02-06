🤖 AI Operations Assistant

An agent-based AI system that accepts natural language tasks, creates an execution plan using LLM reasoning, calls real-world APIs, verifies results, and returns structured output.

This project demonstrates multi-agent architecture, LLM orchestration, and real API integrations, all running locally.

🚀 Features

Multi-agent design (Planner, Executor, Verifier)

LLM-powered structured reasoning (JSON planning)

Tool-based architecture

3 real API integrations

Graceful fallback when LLM is unavailable

Runs locally via FastAPI

Structured, verifiable output

🧠 System Architecture
User → API → Planner Agent → Executor Agent → Verifier Agent → Final Output

🔹 Planner Agent

Converts natural language tasks into structured JSON plans

Selects which tools to call

Uses LLM reasoning

Includes rule-based fallback if LLM fails

🔹 Executor Agent

Executes steps sequentially

Calls external APIs through tools

Handles unknown tool errors

🔹 Verifier Agent

Uses LLM to validate structure and completeness

Ensures final output is clean and structured

Fallback verification if LLM unavailable

🛠️ Integrated APIs
Tool	API Used	Purpose
WeatherTool	OpenWeatherMap API	Fetch real-time weather data
GitHubTool	GitHub REST API	Search top repositories
NewsTool	NewsAPI	Fetch latest news articles
📂 Project Structure
ai_ops_assistant/
│
├── agents/
│   ├── planner.py
│   ├── executor.py
│   ├── verifier.py
│
├── tools/
│   ├── github_tool.py
│   ├── weather_tool.py
│   ├── news_tool.py
│
├── llm/
│   ├── llm_client.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md

⚙️ Setup Instructions

1️⃣ Clone Repository
git clone  https://github.com/opyash218/AI-Operations-Assistant-.git
cd ai_ops_assistant

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

API keys are required but not included for security reasons. Use .env.example as reference.

🔐 API Keys Setup (Required)

This project uses external APIs. You must generate your own free keys.

1️⃣ OpenAI API Key

• Go to: https://platform.openai.com/

• Sign in → API Keys → Create new key
• Add to .env

2️⃣ Weather API Key (OpenWeatherMap)

• Go to: https://openweathermap.org/api

• Sign up → Get API Key
• Add to .env

3️⃣ News API Key (Optional)

• Go to: https://newsapi.org/

• Register → Get key


Create .env file using:

OPENAI_API_KEY=your_openai_key
WEATHER_API_KEY=your_openweather_key
NEWS_API_KEY=your_newsapi_key

▶️ Run Locally
uvicorn main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs


Use POST /run-task

🧪 Example Prompts

Get weather in Mumbai

Find top AI repositories on GitHub

Latest news about Artificial Intelligence

Check weather in London and show ML GitHub repos

Top headlines about India economy

🧩 LLM Usage

Planner Agent generates structured JSON execution plans

Verifier Agent ensures output correctness

No monolithic prompts used

Fallback rule-based planning when API quota exceeded

❗ Error Handling

LLM failure fallback planning

Unknown tool handling

API error detection

Partial result support

Prevents server crash (graceful degradation)

⚖️ Limitations / Tradeoffs

Sequential execution (not parallel)

No caching

Free API rate limits apply

LLM latency depends on provider

🌟 Future Improvements

Parallel tool execution

API caching

Cost/token tracking

More tools (Finance, Maps, Stocks)

Conversation memory

🏁 Evaluation Criteria Coverage
Requirement	Implementation
Multi-agent architecture	Planner, Executor, Verifier
LLM usage	Structured planning + verification
API integrations	Weather + GitHub + News
Local execution	FastAPI server
Structured outputs	JSON planning + responses

✅ Conclusion

This project demonstrates an end-to-end AI agent system capable of:

Planning tasks

Using tools

Integrating APIs

Handling failures gracefully

Producing structured outputs
