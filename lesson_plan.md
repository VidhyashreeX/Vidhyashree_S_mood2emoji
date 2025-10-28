# Lesson Plan: Build a Mood2Emoji App
## Introduction to Text Classification and Sentiment Analysis

---

## 📋 Lesson Overview

**Topic**: Build a Mood2Emoji App (Introduction to Text Classification)  
**Duration**: 60 minutes  
**Age Group**: 12-16 years old  
**Subject**: Computer Science / AI & Coding  
**Difficulty Level**: Beginner to Intermediate

---

## 🎯 Learning Goals

By the end of this lesson, students will be able to:

1. **Define** sentiment analysis and explain how computers detect emotions in text
2. **Identify** positive, negative, and neutral words in sentences
3. **Understand** the basic workflow of a text classification system
4. **Explore** a working sentiment analysis application hands-on
5. **Analyze** the limitations and ethical considerations of AI text analysis
6. **Apply** critical thinking to evaluate when and how AI should analyze text

---

## 📚 Topics Introduced

### Core Concepts:
- **Sentiment Analysis** - How computers understand emotions in text
- **Natural Language Processing (NLP)** - Teaching computers to understand human language
- **Text Classification** - Organizing text into categories
- **Polarity Scoring** - Measuring positive vs. negative sentiment
- **Machine Learning Applications** - Real-world uses of AI

### Technical Skills:
- Reading and interpreting code
- Understanding input-output systems
- Basic data analysis (scores, averages)
- Web application interaction

### Ethical Considerations:
- Content moderation and safety
- Privacy in text analysis
- Bias in AI systems
- Appropriate use of AI technology

---

## 📖 Topics in Detail

### 1. What is Sentiment Analysis? (10 minutes)

**Definition**: Sentiment analysis is the process of determining whether a piece of text expresses positive, negative, or neutral emotions.

**Key Concepts**:
- Computers don't "feel" emotions but can detect patterns
- Words are assigned scores based on typical emotional associations
- Positive words: love, happy, amazing, wonderful (+)
- Negative words: hate, sad, terrible, awful (-)
- Neutral words: the, is, was, and (0)

**Real-World Examples**:
- **Social Media**: Instagram and Twitter detect harmful comments
- **E-Commerce**: Amazon analyzes product reviews to help shoppers
- **Customer Service**: Companies track customer satisfaction
- **Entertainment**: Netflix understands reactions to shows

**Discussion Questions**:
- How do you express happiness in a text message?
- Can computers understand sarcasm? Why or why not?
- Why would a company want to analyze customer feedback automatically?

---

### 2. How Does the Mood2Emoji App Work? (15 minutes)

**Step-by-Step Process**:

```
User Types Sentence → Safety Check → Word Analysis → Score Calculation → Emoji Result
```

**Detailed Breakdown**:

1. **Input**: Student types a sentence (e.g., "I love learning new things!")

2. **Safety Filter**: 
   - Checks for inappropriate words
   - Protects students from harmful content
   - Returns neutral response if problematic text detected

3. **Text Processing**:
   - Sentence is broken into individual words
   - Each word is analyzed using TextBlob library
   - Library contains pre-scored dictionary of thousands of words

4. **Polarity Calculation**:
   - Each word gets a score from -1.0 (very negative) to +1.0 (very positive)
   - Scores are averaged across all words
   - Example: "I love learning" → "I"(0) + "love"(0.5) + "learning"(0.3) = Average: 0.27

5. **Decision Logic**:
   ```
   If score > 0.2  → 😀 Happy
   If score < -0.2 → 😞 Sad
   Else           → 😐 Neutral
   ```

6. **Output**: Display emoji with encouraging message

**Demonstration**:
- Teacher shows 3-4 examples live
- Students predict results before running
- Discuss why the app chose each emoji

---

### 3. Hands-On Exploration (15 minutes)

**Activity 1: Test Your Own Sentences** (7 minutes)
- Each student tests 5 different sentences
- Record results in worksheet:
  - Your sentence
  - Predicted emoji
  - Actual result
  - Mood score
  - Were you surprised?

**Example Worksheet**:
```
Sentence: "I can't wait for summer vacation!"
My Prediction: 😀
Actual Result: 😀
Mood Score: +0.65
Surprised?: No, makes sense!
```

**Activity 2: Can You Trick the Detector?** (8 minutes)
- Challenge students to find edge cases
- Examples to try:
  - Sarcasm: "Oh great, more homework"
  - Negation: "This is not bad"
  - Mixed emotions: "I'm happy but also nervous"
- Discuss why these are tricky for computers

**Class Discussion**:
- What patterns did you notice?
- Which results surprised you?
- What did the computer get wrong?

---

### 4. Understanding the Technology (12 minutes)

**Code Walkthrough** (Simplified for students):

Show key parts of `app.py`:

```python
# 1. Get user input
user_input = st.text_input("Type your sentence here:")

# 2. Analyze sentiment
blob = TextBlob(user_input)
polarity = blob.sentiment.polarity  # Score from -1 to +1

# 3. Decide which emoji
if polarity > 0.2:
    emoji = "😀"
elif polarity < -0.2:
    emoji = "😞"
else:
    emoji = "😐"
```

**Key Takeaways**:
- Libraries like TextBlob do the complex work for us
- We just need to write the logic (if/else statements)
- Real applications layer multiple technologies together

**Teacher Mode Features**:
- Open the "Teacher Mode" section in the app
- Walk through the visual diagram together
- Explain the scoring system with examples
- Show the "Behind the Scenes" metrics

---

### 5. Limitations and Ethics (8 minutes)

**Technical Limitations**:
1. **Cannot understand sarcasm**: "Yeah, right, that's just perfect" reads as positive
2. **Lacks context**: Doesn't remember previous messages in a conversation
3. **Language-specific**: Only works in English
4. **Simple model**: Professional tools use more sophisticated AI

**Ethical Discussions**:

**Question 1**: Should social media platforms automatically remove negative comments?
- **Pro**: Protects users from bullying and harm
- **Con**: Could limit free expression
- **Student Activity**: Debate in small groups (3 minutes)

**Question 2**: Is it okay for companies to analyze your messages?
- **Privacy concerns**: Who owns your words?
- **Safety benefits**: Detecting threats or harm
- **Balance**: How do we protect both privacy and safety?

**Question 3**: Can AI be biased?
- If training data contains biased examples, AI learns bias
- Example: If "professional" is associated with male names more often
- Importance of diverse data and testing

---

## 🎨 Activity Explanation

### Main Activity: Sentiment Detective (20 minutes total)

**Setup** (5 minutes):
- Divide class into groups of 3-4
- Each group gets access to the Mood2Emoji app
- Provide worksheets and writing materials

**Phase 1: Exploration** (7 minutes)
Students test sentences and record:
- Expected vs. actual results
- Mood scores
- Interesting patterns

**Phase 2: Challenge** (8 minutes)
Groups compete to:
1. Create the happiest sentence possible (highest positive score)
2. Create the saddest sentence possible (lowest negative score)
3. Find a sentence the AI gets "wrong" (explain why it's wrong)

**Sharing & Discussion** (5 minutes)
- Each group shares their best examples
- Class votes on most creative findings
- Teacher highlights learning moments

---

## 📊 Learning Outcomes

### Knowledge Outcomes:
Students will know:
- ✅ The definition of sentiment analysis
- ✅ How computers assign scores to words
- ✅ Real-world applications of text classification
- ✅ Basic structure of an AI application
- ✅ Limitations of current AI technology

### Skills Outcomes:
Students will be able to:
- ✅ Analyze text for emotional content
- ✅ Read and understand simple Python code
- ✅ Test software systematically
- ✅ Identify edge cases and limitations
- ✅ Critically evaluate AI tools

### Attitude Outcomes:
Students will:
- ✅ Feel empowered to explore AI applications
- ✅ Understand both capabilities and limitations of AI
- ✅ Think critically about ethical use of technology
- ✅ Appreciate the complexity of human language
- ✅ Be curious about how everyday apps work

---

## 📅 Detailed Lesson Timeline

| Time | Activity | Method | Materials |
|------|----------|--------|-----------|
| 0-5 min | Introduction & Hook | Demo app, ask questions | Projector, app |
| 5-10 min | Explain Sentiment Analysis | Lecture, examples | Slides, whiteboard |
| 10-20 min | How It Works | Teacher Mode walkthrough | Live app demo |
| 20-35 min | Hands-On Exploration | Individual/group work | Computers, worksheets |
| 35-45 min | Code Understanding | Code walkthrough | app.py displayed |
| 45-53 min | Ethics Discussion | Group debate | Discussion prompts |
| 53-58 min | Wrap-Up Quiz | Interactive Q&A | Quiz questions |
| 58-60 min | Reflection & Homework | Individual writing | Exit ticket |

---

## 🎯 Assessment Methods

### Formative Assessment (During Lesson):
- Observe student engagement with app
- Listen to group discussions
- Review worksheet answers
- Ask comprehension questions throughout

### Summative Assessment (End of Lesson):

**Quick Quiz** (3 minutes):
1. What is sentiment analysis? (Knowledge)
2. Name one real-world application. (Application)
3. Why can't the app understand sarcasm? (Analysis)

**Exit Ticket** (2 minutes):
Write one sentence answering:
- "The most interesting thing I learned today was..."
- "One question I still have is..."

### Homework Assignment:
**Sentiment Scavenger Hunt**:
- Find 3 apps or websites that might use sentiment analysis
- For each, explain: What might they analyze? Why?
- Due: Next class

---

## 📚 Required Materials

### Technology:
- Computer/laptop for each student (or pairs)
- Internet connection
- Mood2Emoji app running (online or local)
- Projector for teacher demonstrations

### Handouts:
- Sentiment Analysis Worksheet (testing sentences)
- Code Snippet Handout (key parts of app.py)
- Ethics Discussion Questions
- Exit Ticket template

### Optional:
- Poster with sentiment examples
- Vocabulary cards (sentiment, polarity, NLP)
- Real-world example screenshots

---

## 🔄 Differentiation Strategies

### For Advanced Students:
- Challenge: Modify the code to add a 4th emotion (surprised)
- Research: How do professional systems handle sarcasm?
- Extension: Create a word contribution visualizer

### For Struggling Students:
- Provide sentence starters for testing
- Pair with supportive partner
- Focus on hands-on exploration vs. code reading
- Simplified vocabulary list

### For English Language Learners:
- Provide sentence examples in advance
- Visual aids for emotional vocabulary
- Translation tools available
- Focus on concept understanding vs. technical terms

---

## 🏠 Homework & Extensions

### Required Homework:
Find 3 real-world examples of sentiment analysis in action

### Optional Extensions:
1. **Creative Writing**: Write a story that would confuse the detector
2. **Research Project**: How do different cultures express emotions differently?
3. **Design Challenge**: Sketch an app that analyzes images instead of text
4. **Coding Challenge**: Add a new emotion category to the app

---

## 📖 Teacher Preparation Notes

### Before Class:
- [ ] Test the Mood2Emoji app on classroom devices
- [ ] Prepare 10-15 example sentences to demonstrate
- [ ] Print worksheets and handouts
- [ ] Set up projector with app open
- [ ] Review ethical discussion questions
- [ ] Prepare contingency plan if internet fails

### Key Vocabulary to Introduce:
- **Sentiment Analysis**: Detecting emotions in text
- **Polarity**: Measure of positive vs. negative
- **Natural Language Processing (NLP)**: Teaching computers to understand human language
- **Text Classification**: Organizing text into categories
- **Algorithm**: Step-by-step instructions for computers

### Common Misconceptions to Address:
- ❌ "AI understands emotions like humans" → ✅ AI detects patterns, doesn't "feel"
- ❌ "Sentiment analysis is always accurate" → ✅ It has limitations
- ❌ "You need to be a coding expert to use AI" → ✅ Tools make it accessible

---

## 🎓 Alignment with Standards

### Computer Science Standards:
- Understanding of AI and machine learning concepts
- Application of algorithms to solve problems
- Analysis of data to make predictions
- Ethical implications of technology

### Literacy Standards:
- Understanding of author's tone and mood
- Analysis of word choice and meaning
- Critical evaluation of digital tools

### 21st Century Skills:
- Digital literacy
- Critical thinking
- Collaboration
- Creativity and innovation

---

## 📞 Parent Communication

### Suggested Email to Parents:

**Subject**: Exciting AI Lesson - Mood2Emoji App

Dear Parents,

Today your child learned about sentiment analysis - how computers detect emotions in text! We explored a kid-safe app called Mood2Emoji that analyzes sentences and returns happy, neutral, or sad emojis.

**What we learned**:
- How AI applications work
- Real-world uses in social media, reviews, and customer service
- Ethical considerations of AI technology

**At home**:
Your child has a fun homework assignment to find 3 apps that might use sentiment analysis. You might discuss together how platforms like Instagram, Amazon, or YouTube might use this technology!

**Try it yourself**: [Link to app if hosted]

Questions? Feel free to reach out!

Best regards,  
[Teacher Name]

---

## 🌟 Success Indicators

This lesson was successful if students:
- ✅ Actively engaged with the app and tested multiple sentences
- ✅ Could explain sentiment analysis in their own words
- ✅ Identified at least one limitation of the technology
- ✅ Participated in ethical discussions
- ✅ Showed curiosity about how AI works
- ✅ Connected concepts to real-world applications

---

## 📝 Reflection Questions (For Teacher)

After teaching this lesson, consider:
1. Which activities generated the most engagement?
2. Did students grasp the core concepts?
3. Were 60 minutes sufficient, or should content be adjusted?
4. Which examples resonated most with students?
5. What questions did students ask that weren't anticipated?
6. How can this lesson be improved for next time?

---

**Created for**: Curriculum Developer Intern Assignment  
**Topic**: Introduction to AI and Text Classification  
**Target Age**: 12-16 years  
**Format**: 60-minute interactive lesson with hands-on coding exploration

---

*This lesson plan is designed to be converted to PDF format for submission.*
