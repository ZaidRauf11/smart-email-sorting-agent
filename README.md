# 📧 SmartInbox AI – Email Sorting Agent

This project is an **AI-powered Email Sorting Agent** built using **Agno** and **Streamlit**.
It classifies emails into categories like **Work, Spam, Social, and Promotions** using the **Groq LLM** model.

## 🚀 Features

* Categorizes emails into:

  * 📂 **Work** → e.g., "Meeting with client tomorrow"
  * 🗑 **Spam** → e.g., "Win a FREE iPhone now!!!"
  * 👥 **Social** → e.g., "Your friend tagged you in a photo"
  * 🛍 **Promotions** → e.g., "50% discount on clothes"
* Built with **Streamlit** for a simple and interactive UI.
* Uses **Agno Agents** to handle email classification logic.
* Loads **GROQ API Key** securely from `.env` file using `python-dotenv`.

---

## 🛠 Requirements

Install the required dependencies:

```txt
streamlit
agno
python-dotenv
```

---

## 📂 Project Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ZaidRauf11/smartinbox-ai.git
   cd smartinbox-ai
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your **GROQ API Key** to a `.env` file:

   ```
   GROQ_API_KEY=your_api_key_here
   ```

---

## 🎯 How It Works

1. User enters an email text into the **Streamlit UI**.
2. The **AI Agent** (via Agno + Groq LLM) analyzes the text.
3. The email is categorized into the correct group (**Work, Spam, Social, Promotions**).
4. The result is displayed neatly in the Streamlit interface.

---

## 💻 Interface

The app is powered by **Streamlit** and has a clean, user-friendly design:

* 📩 Input box to enter an email.
* ⚡ Analyze button to classify the email.
* 📄 Results section shows the predicted category.

Example inputs:

* `"Meeting scheduled with client tomorrow"` → **Work**
* `"Win a FREE iPhone now!!!"` → **Spam**
* `"Your friend tagged you in a photo"` → **Social**
* `"50% discount on electronics"` → **Promotions**

---

## 📌 Run the App

Start the app locally:

```bash
streamlit run app.py
```

Then open in browser: [http://localhost:8501](http://localhost:8501)

---

📸 App Preview

<img width="846" height="859" alt="3" src="https://github.com/user-attachments/assets/09bcda1d-371f-4036-ad67-a40430d15f65" />

---

✨ **SmartInbox AI** makes email organization easy, fast, and intelligent!

