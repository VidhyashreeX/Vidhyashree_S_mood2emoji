import streamlit as st
from textblob import TextBlob
import re

st.set_page_config(
    page_title="Mood2Emoji - Text Mood Detector",
    page_icon="😀",
    layout="centered"
)

PROFANITY_LIST = [
    'damn', 'hell', 'crap', 'stupid', 'idiot', 'dumb', 'hate', 
    'kill', 'die', 'suck', 'shit', 'fuck', 'ass', 'bitch'
]

def contains_profanity(text):
    """Check if text contains inappropriate words"""
    text_lower = text.lower()
    for word in PROFANITY_LIST:
        if re.search(r'\b' + word + r'\b', text_lower):
            return True
    return False

def get_mood_emoji_and_message(text):
    """Analyze text and return emoji and kid-friendly message"""
    
    if not text or len(text.strip()) == 0:
        return "😐", "Please type something so I can detect the mood!"
    
    if contains_profanity(text):
        return "😐", "Let's keep our words kind and friendly! Try another sentence."
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.2:
        messages = [
            "Sounds happy! 🌟",
            "That's a positive vibe! ✨",
            "Happy thoughts detected! 🎉",
            "Sounds cheerful! 🌈"
        ]
        import random
        return "😀", random.choice(messages)
    elif polarity < -0.2:
        messages = [
            "Sounds a bit sad. 💙",
            "That seems negative. It's okay to feel this way sometimes.",
            "Sounds like you're feeling down. 🤗",
            "That's a bit gloomy, but feelings are valid!"
        ]
        import random
        return "😞", random.choice(messages)
    else:
        messages = [
            "Sounds neutral to me! 🤔",
            "Not too happy, not too sad - just neutral!",
            "Hmm, this seems pretty balanced! ⚖️",
            "Can't detect a strong mood here - sounds neutral!"
        ]
        import random
        return "😐", random.choice(messages)

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        padding: 20px 0;
    }
    h2 {
        color: #34495e;
    }
    h3 {
        color: #7f8c8d;
    }
    .emoji-result {
        font-size: 80px;
        text-align: center;
        padding: 20px;
    }
    .message-result {
        font-size: 24px;
        text-align: center;
        color: #2c3e50;
        padding: 10px;
        font-weight: 500;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin: 20px 0;
    }
    .teacher-box {
        background-color: #fff9e6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #f39c12;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Mood2Emoji Detector")
st.markdown("#### Curriculum Developer Intern — Assignment")
st.markdown("### Discover the mood in your text!")

st.markdown(
    "**How it works:** Type a sentence and I'll tell you if it sounds happy (😀), neutral (😐), or sad (😞).\n\n"
    "This is a safe space for learning about how computers understand emotions in text."
)

user_input = st.text_input(
    " Type your sentence here:",
    placeholder="Example: I love learning new things!",
    max_chars=200
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze_button = st.button(" Analyze My Text!", use_container_width=True)

if analyze_button and user_input:
    emoji, message = get_mood_emoji_and_message(user_input)
    
    st.markdown(f'<div class="emoji-result">{emoji}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="message-result">{message}</div>', unsafe_allow_html=True)
    
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    
    st.markdown("---")
    st.markdown("### Behind the Scenes")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Words Analyzed", len(user_input.split()))
    with col_b:
        st.metric("Mood Score", f"{polarity:.2f}")
    with col_c:
        mood_type = "Positive" if polarity > 0.2 else "Negative" if polarity < -0.2 else "Neutral"
        st.metric("Mood Type", mood_type)

st.markdown("---")

with st.expander("Teacher Mode - How Does This Work?"):
    st.subheader("Understanding Sentiment Analysis")
    st.markdown(
        "- Sentiment analysis helps computers estimate emotion in text.\n"
        "- This app uses a simple score from -1 (negative) to +1 (positive)."
    )
    st.markdown("#### Steps")
    st.markdown(
        "1. Text input\n"
        "2. Safety check\n"
        "3. Word analysis\n"
        "4. Mood scoring and average\n"
        "5. Emoji result"
    )
    st.markdown("#### How we pick the emoji")
    st.markdown(
        "- Score > +0.2 → Happy\n"
        "- Score < -0.2 → Sad\n"
        "- Otherwise → Neutral"
    )
    st.markdown("#### Real-world uses")
    st.markdown(
        "- Social media moderation\n"
        "- Product review insights\n"
        "- News/public opinion\n"
        "- Games reacting to feedback"
    )
    st.markdown("#### Try these examples")
    st.text("I love spending time with my friends!  → 😀")
    st.text("This is a normal sentence.           → 😐")
    st.text("I feel terrible today.               → 😞")

