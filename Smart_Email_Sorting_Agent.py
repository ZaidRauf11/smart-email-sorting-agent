import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.googlesearch import GoogleSearchTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# --- Define Agent ---
email_agent = Agent(
    name = "Email Agent",
    model=Groq(id="qwen/qwen3-32b"),
    role="Categorizes emails into groups like Work, Spam, Social, and Promotions",
    tools=[GoogleSearchTools()],
    instructions= "Read each email carefully and assign it to the most appropriate category based on its content.",
    show_tool_calls=True,
    markdown=True,
)


# Streamlit UI
st.set_page_config(page_title="📧 Email Agent", page_icon="📩", layout="centered")

st.markdown("""
    <h1>Smart Email Sorting Agent 📧</h1>
    <p>Try examples like: <b>"Meeting tomorrow with client"</b>, <b>"Win a FREE iPhone"</b>, or <b>"50% discount on shoes"</b>.</p>
""", unsafe_allow_html=True)

# Input form
with st.form(key="query_form"):
    query = st.text_input("🔍 Enter your Email",  placeholder="e.g. Win a FREE iPhone now!!!")
    submit = st.form_submit_button("Analyze")

# Main Processing
if submit and query:
    with st.spinner("⏳ Fetching results…"):
        try:
            response = email_agent.run(query)
            result_text = response.content if hasattr(response, "content") else str(response)

            if result_text:
                st.markdown("### 📄 Results")
                st.markdown(result_text)
            else:
                st.warning("⚠ No results found for your query.")

        except Exception as e:
            st.error(f"⚠ Something went wrong: {e}")
            st.info("Check your GROQ_API_KEY or internet connection.")




