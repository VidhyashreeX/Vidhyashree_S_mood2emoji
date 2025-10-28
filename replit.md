# Mood2Emoji - Text Mood Detector

## Overview

Mood2Emoji is an educational web application designed to teach students (ages 12-16) about sentiment analysis and natural language processing. The application analyzes text input and returns an emoji-based mood classification (happy 😀, neutral 😐, or sad 😞) with kid-friendly explanations. Built using Python and Streamlit, it provides a hands-on, interactive way for students to understand how computers can detect emotions in text while maintaining age-appropriate safety through content filtering.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
**Technology**: Streamlit web framework
- **Decision**: Streamlit was chosen for its simplicity and rapid prototyping capabilities, making it ideal for educational demos
- **Rationale**: Enables creation of interactive web interfaces with minimal code, perfect for a 60-minute educational session where focus should be on concepts rather than web development complexity
- **Key Components**: Single-page application with text input, emoji display, and real-time feedback
- **Layout**: Centered layout optimized for classroom presentations and student interaction

### Backend Architecture
**Technology**: Python 3.9+ with TextBlob for NLP
- **Decision**: TextBlob library handles sentiment analysis through polarity scoring
- **Rationale**: TextBlob provides simple, pre-trained sentiment analysis without requiring heavy machine learning models or training data, keeping the application lightweight and fast
- **Processing Flow**:
  1. Text input validation (empty check)
  2. Profanity filtering using regex pattern matching
  3. Sentiment polarity calculation (-1 to +1 scale)
  4. Mood classification based on polarity thresholds (>0.2 happy, <-0.2 sad, else neutral)
  5. Random kid-friendly message selection for variety

### Content Safety System
**Approach**: Rule-based profanity filtering
- **Decision**: Maintain a predefined list of inappropriate words with regex boundary matching
- **Rationale**: Ensures age-appropriate content for 12-16 year old students without requiring external moderation APIs
- **Implementation**: Pre-processing filter that intercepts inappropriate content before sentiment analysis
- **Fallback**: Returns neutral emoji with friendly redirection message when inappropriate content is detected

### Application State Management
**Pattern**: Stateless request-response model
- **Decision**: No persistent storage or session management
- **Rationale**: Each text analysis is independent, simplifying the architecture and avoiding privacy concerns with storing student input
- **Pros**: Simple, privacy-friendly, no database required
- **Cons**: No history tracking or learning analytics (acceptable trade-off for educational demo)

### Educational Design Patterns
**Pedagogical Architecture**:
- **Immediate Feedback Loop**: Real-time analysis teaches cause-and-effect
- **Visual Learning**: Emoji-based output makes abstract sentiment concrete
- **Optional Teacher Mode**: Planned feature to expose underlying mechanics (polarity scores, word weighting)
- **Transparency**: System designed to be explainable to students, not a "black box"

## External Dependencies

### Core Libraries
1. **Streamlit (v1.31.0)**
   - Purpose: Web application framework
   - Features used: Page configuration, text input widgets, layout management
   - Why required: Provides the entire UI/UX layer without HTML/CSS/JavaScript

2. **TextBlob (v0.19.0)**
   - Purpose: Natural language processing and sentiment analysis
   - Features used: Sentiment polarity scoring
   - Why required: Core NLP engine that performs the mood detection
   - Initial setup: Requires one-time download of language corpora (`python -m textblob.download_corpora`)

### Python Standard Library Dependencies
- **re (regex)**: Pattern matching for profanity filtering
- **random**: Variation in response messages for engagement

### No External Services
- **No APIs**: All processing happens locally
- **No Database**: Stateless application with no data persistence
- **No Authentication**: Public-facing educational tool with no user accounts
- **No Third-party Integrations**: Self-contained for classroom/offline use

### Deployment Considerations
- **Port Configuration**: Runs on port 5000 (Streamlit default configurable)
- **Browser Requirements**: Modern web browser with JavaScript enabled
- **Network**: Internet required only for initial TextBlob corpora download; runtime can be offline
- **Resource Requirements**: Minimal - suitable for typical student laptops or classroom computers