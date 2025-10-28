# Mood2Emoji - Kid-Safe Text Mood Detector 

A simple, educational web application that teaches students (ages 12-16) about sentiment analysis and natural language processing through an interactive mood detection tool.

##  What Does This App Do?

Mood2Emoji takes a sentence you type and tells you whether it sounds **happy** 😀, **neutral** 😐, or **sad** 😞. It's a fun, hands-on way for students to learn how computers can understand emotions in text!

### Key Features:
- **Simple Text Analysis**: Type any sentence and get instant mood feedback
- **Kid-Friendly Emojis**: Visual results that are easy to understand
- **Safety First**: Built-in filter for inappropriate words
- **Teacher Mode**: Educational section explaining how sentiment analysis works
- **Real-Time Learning**: See the "mood score" behind each analysis

##  Setup and Run Instructions

### Prerequisites
- Python 3.9 or higher

### Installation Steps

1. **Clone or Download this repository**
   ```bash
   git clone <your-repo-url>
   cd mood2emoji
   ```

2. **Install Dependencies**
   ```bash
   pip install streamlit textblob
   ```

3. **Download TextBlob Language Data** (First time only)
   ```bash
   python -m textblob.download_corpora
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py --server.port 5000
   ```

5. **Open in Browser**
   - The app will automatically open at `http://localhost:5000`
   - If not, manually navigate to the URL shown in your terminal

##  How Kids Learn From This

### Learning Objectives:
1. **Introduction to AI/ML**: Understand how computers can "read" emotions
2. **Text Processing**: Learn how text is broken down into words and analyzed
3. **Data Science Basics**: See how scores and averages work in real applications
4. **Critical Thinking**: Explore why certain words are positive or negative
5. **Ethical AI**: Understand the importance of content safety filters

### What Students Discover:
- Computers don't "feel" emotions but can detect patterns in words
- Positive words like "love," "happy," "great" have positive scores
- Negative words like "sad," "terrible," "bad" have negative scores
- Context matters: "not good" is different from "good"
- Real-world applications: social media moderation, customer reviews, chatbots

## Teaching This in 60 Minutes

### Lesson Structure:

**Minutes 0-10: Introduction & Demo**
- Show the app and demonstrate with 3-4 examples
- Ask students: "How do you think computers understand emotions?"
- Discuss real-world applications (social media, reviews, customer service)

**Minutes 10-20: How It Works**
- Open "Teacher Mode" and walk through the step-by-step process
- Explain the mood scoring system (-1 to +1 scale)
- Show how positive and negative words affect the overall score

**Minutes 20-35: Hands-On Exploration**
- Students test their own sentences
- Challenge: Can you trick the detector?
- Worksheet: Record 5 sentences and their results

**Minutes 35-45: Understanding the Code**
- Open `app.py` and show key sections:
  - Text input (Streamlit)
  - Sentiment analysis (TextBlob)
  - Safety filter (profanity check)
  - Emoji assignment (if/else logic)
- Explain that libraries like TextBlob do the "heavy lifting"

**Minutes 45-55: Extension Activities**
- Discuss limitations: sarcasm, context, cultural differences
- Brainstorm: What other text analysis tools could we build?
- Ethics discussion: Should all messages be monitored? Privacy vs. safety

**Minutes 55-60: Wrap-Up & Reflection**
- Quiz: What is sentiment analysis?
- Share: One surprising thing you learned
- Homework: Find 3 apps that might use sentiment analysis

##  How It Works (Technical Overview)

### Architecture:
```
User Input → Safety Check → TextBlob Analysis → Polarity Score → Emoji Output
```

### Technology Stack:
- **Streamlit**: Web interface and user interaction
- **TextBlob**: Natural language processing and sentiment analysis
- **Python**: Core programming language

### Sentiment Scoring:
- TextBlob analyzes text and returns a polarity score from -1.0 (very negative) to +1.0 (very positive)
- Thresholds:
  - Score > 0.2 → Happy 😀
  - Score < -0.2 → Sad 😞
  - Score between -0.2 and 0.2 → Neutral 😐



##  Known Limitations

### Technical Limitations:
1. **Sarcasm Detection**: Cannot understand sarcasm or irony
   - Example: "Oh great, another rainy day" might be detected as happy
   
2. **Context Understanding**: Analyzes individual sentences, not full conversations
   - Cannot remember previous messages
   
3. **Language**: Only works with English text
   - Other languages will not be analyzed correctly
   
4. **Slang & Emojis**: May not recognize very new slang or interpret existing emojis
   - Works best with standard English words

5. **Simple Profanity Filter**: Basic word list, not comprehensive
   - Could miss creative misspellings or new inappropriate terms


### Design Decisions:
- Intentionally simple to keep focus on learning concepts
- Trade-off: Accuracy vs. Understandability (we chose understandability)
- No data storage or user tracking (privacy-first for students)

## Learning Outcomes

After using this app, students should be able to:
-  Explain what sentiment analysis is in their own words
-  Identify positive, negative, and neutral text examples
-  Understand how computers use math to analyze text
-  Recognize real-world applications of sentiment analysis
- Discuss ethical considerations of AI text analysis
- Appreciate the limitations of current AI technology

## Project Structure

```
mood2emoji/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── lesson_plan.pdf    # 60-minute lesson plan for teachers
```



##  References

- **TextBlob Documentation**: https://textblob.readthedocs.io/
- **Streamlit Documentation**: https://docs.streamlit.io/
-


**Built by Vidhyashree S. As a pert of my curriculum Developer Intern — Assignment**
