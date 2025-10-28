# 📦 Submission Guide for Curriculum Developer Intern Assignment

## What to Submit

You need to submit **TWO items**:

### 1. GitHub Repository Link
Your GitHub repo should contain these files:
- ✅ `app.py` - Main Streamlit application
- ✅ `requirements.txt` - Python dependencies
- ✅ `README.md` - Complete documentation
- ✅ `lesson_plan.pdf` - Convert `lesson_plan.md` to PDF

### 2. Lesson Plan PDF Link
Convert the `lesson_plan.md` file to PDF format and provide a link.

---

## 📝 Steps to Submit

### Step 1: Create GitHub Repository

1. **Repository Name**: `firstname-lastname-mood2emoji`
   - Replace with your actual name (e.g., `john-smith-mood2emoji`)

2. **Initialize Repository**:
   ```bash
   git init
   git add app.py requirements.txt README.md lesson_plan.pdf
   git commit -m "Initial commit: Mood2Emoji educational app"
   git branch -M main
   git remote add origin https://github.com/yourusername/firstname-lastname-mood2emoji.git
   git push -u origin main
   ```

3. **Files to Include in GitHub**:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `lesson_plan.pdf`
   - Optional: `QUESTIONS.md` (if you have clarification questions - max 3)

### Step 2: Convert Lesson Plan to PDF

**Option A: Using Online Converter**
1. Open `lesson_plan.md` in any text editor
2. Copy all content
3. Go to https://www.markdowntopdf.com/ or similar service
4. Paste content and download PDF

**Option B: Using VS Code or Similar**
1. Open `lesson_plan.md` in VS Code
2. Install "Markdown PDF" extension
3. Right-click → "Markdown PDF: Export (pdf)"
4. Save as `lesson_plan.pdf`

**Option C: Using Pandoc (if installed)**
```bash
pandoc lesson_plan.md -o lesson_plan.pdf
```

### Step 3: Test Your App Locally

Before submitting, ensure everything works:

```bash
# Install dependencies
pip install -r requirements.txt

# Download TextBlob data (first time only)
python -m textblob.download_corpora

# Run the app
streamlit run app.py --server.port 5000
```

Test these scenarios:
- ✅ Happy sentence: "I love this project!"
- ✅ Sad sentence: "This is terrible and awful"
- ✅ Neutral sentence: "This is a sentence"
- ✅ Profanity filter: Type inappropriate word (should show neutral response)
- ✅ Teacher Mode: Open and verify diagram displays

### Step 4: Deploy to Streamlit Cloud (Optional but Recommended)

1. **Go to**: https://share.streamlit.io/
2. **Sign in** with GitHub
3. **Deploy new app**:
   - Repository: `yourusername/firstname-lastname-mood2emoji`
   - Branch: `main`
   - Main file path: `app.py`
4. **Click Deploy**
5. **Copy the public URL** (e.g., `https://yourusername-mood2emoji.streamlit.app`)

### Step 5: Final Submission

Submit via the provided form or email:

**Subject Line**: Curriculum Developer Intern Assignment - [Your Name]

**Email Body**:
```
Name: [Your Full Name]
Assignment: Kid-Safe Text-Mood Detector

GitHub Repository: https://github.com/yourusername/firstname-lastname-mood2emoji
Live Streamlit App: https://yourusername-mood2emoji.streamlit.app
Lesson Plan PDF: [Link to PDF - can be in repo or Google Drive]

Completion Time: [X hours]

Optional Notes: [Any clarifications or highlights]
```

---

## ✅ Pre-Submission Checklist

Before you submit, verify:

### Functionality (25 points)
- [ ] App runs without errors
- [ ] Text input accepts sentences
- [ ] Sentiment analysis works correctly
- [ ] Emojis display properly (😀 😐 😞)
- [ ] Profanity filter catches inappropriate words
- [ ] Teacher Mode displays and explains the process

### Code Quality (15 points)
- [ ] Code is clean and well-commented
- [ ] Variable names are descriptive
- [ ] No unnecessary complexity
- [ ] Follows Python best practices

### Logic Clarity (15 points)
- [ ] TextBlob implementation is clear
- [ ] Scoring logic makes sense (>0.1, <-0.1)
- [ ] Safety filter works as intended

### Safety (10 points)
- [ ] All responses are age-appropriate
- [ ] No offensive content possible
- [ ] Graceful handling of edge cases

### Pedagogy - Lesson Plan (30 points)
- [ ] Clear learning objectives
- [ ] 60-minute timeline included
- [ ] Topics explained in detail
- [ ] Activities are engaging
- [ ] Learning outcomes are measurable
- [ ] Age-appropriate for 12-16

### Documentation - README (5 points)
- [ ] Setup instructions are clear
- [ ] Educational value explained
- [ ] Teaching approach outlined
- [ ] Limitations documented

---

## 📏 File Size Check

Ensure your repo is under 50 MB:
```bash
du -sh .
```

Should show something like: `5.2M` (well under limit)

---

## 🚨 Common Issues to Avoid

### ❌ Don't Submit:
- Large datasets or model files
- `.git` folder (auto-excluded)
- `__pycache__` directories
- Virtual environment folders (`venv`, `env`)
- IDE-specific files (`.vscode`, `.idea`)

### ✅ Do Include:
- All 4 required files
- Clear commit messages
- Working live demo link
- Professional README

---

## 💡 Bonus Points (Optional)

Want to stand out? Consider adding:
- **QUESTIONS.md**: 1-3 thoughtful questions about scaling or improvements
- **Screenshots**: Add app screenshots to README
- **Video Demo**: 30-second screen recording of app in action
- **Extended Features**: Word highlighting, comparison mode, etc.

---

## 🕒 Deadline

**24 hours from assignment receipt**

Set a reminder to submit at least 1 hour before the deadline to handle any last-minute issues!

---

## 📧 Questions?

If you have clarification questions (max 3), create `QUESTIONS.md`:

```markdown
# Questions

1. Q: Should the profanity filter be case-sensitive?
   A: [Leave blank for evaluator to answer]

2. Q: Can we use emoji instead of text for the mood explanation?
   A: [Leave blank]

3. Q: Should we handle multiple sentences or just one?
   A: [Leave blank]
```

---

**Good luck! You've built something educational and impactful. 🚀**
