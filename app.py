import os
import streamlit as st
from groq import Groq

# Set your API key
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

st.title("Tejas's Flirty Replies Generator")

# User input text area
user_input = st.text_area("Enter your message:")

# Generate replies button
if st.button("Generate Replies"):
    if user_input:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"You are master of flirty replies, give 3 flirty replies to this text which can impress the other person,strictly do not write anything else except the replies and keep the replies short, just keep the output in this format 1..... 2..... 3.....: '{user_input}'",
                }
            ],
            model="llama3-8b-8192",
        )

        # Get the generated flirty replies
        flirty_replies = chat_completion.choices[0].message.content.split('\n')

        # Display the replies in separate text areas
        st.subheader("Flirty Replies:")
        for i, reply in enumerate(flirty_replies):
            st.text_area(f"Reply {i + 1}", value=reply, height=50, disabled=True)
    else:
        st.warning("Please enter a message to generate replies.")