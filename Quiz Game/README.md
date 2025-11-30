# 🧠 Quiz Game

An object-oriented Python trivia game featuring computer science questions, modular design, and score tracking.

## 🎯 Features

- **True/False Questions:** Computer science and technology trivia
- **Object-Oriented Design:** Clean separation of concerns with multiple classes
- **Score Tracking:** Real-time score calculation and display
- **Question Bank System:** Easily expandable question database
- **Progressive Feedback:** Immediate answer validation and learning

## 🚀 How to Run

```bash
# Navigate to the Quiz Game directory
cd "Quiz Game"

# Run the quiz
python main.py
```

## 🎮 How to Play

1. Answer each True/False question by typing "True" or "False"
2. Get immediate feedback on your answer
3. See the correct answer and current score after each question
4. Complete all questions to see your final score

## 📁 Project Structure

```
Quiz Game/
├── main.py           # Main game controller and entry point
├── question_model.py # Question class definition
├── quiz_brain.py     # Quiz logic and game mechanics
├── data.py          # Question bank with computer science trivia
└── README.md        # This file
```

## 🛠️ Technical Implementation

### Object-Oriented Design

**`Question` Class (`question_model.py`)**
```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```
- Simple data structure for storing question and answer pairs
- Clean encapsulation of question properties

**`QuizBrain` Class (`quiz_brain.py`)**
```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
```
- Manages quiz state and progression
- Handles answer checking and scoring
- Controls game flow and user interaction

### Key Methods

- `still_has_questions()`: Checks if more questions remain
- `next_question()`: Presents questions and gets user input
- `check_answer()`: Validates answers and updates score

## 📊 Question Categories

Current question bank includes:
- **Programming Languages:** Python, C, C++, JavaScript
- **Computer History:** Ada Lovelace, computing milestones
- **Technology:** RAM, Snapchat, various tech concepts
- **Software Development:** Programming concepts and tools

## 🎓 Learning Objectives

This project demonstrates:

- **Object-Oriented Programming (OOP):** Classes, objects, encapsulation
- **Data Structures:** Lists, dictionaries for question storage
- **Control Flow:** While loops, conditionals
- **User Input Handling:** Interactive command-line interface
- **Modular Design:** Separation of data, logic, and presentation
- **Error Handling:** Case-insensitive input processing

## 🔧 Technical Features

- **Case-Insensitive Input:** Accepts "true", "TRUE", "True", etc.
- **Real-Time Scoring:** Updates and displays score after each question
- **Progress Tracking:** Shows question number and remaining questions
- **Immediate Feedback:** Shows correct answer regardless of user response
- **Clean Game Flow:** Smooth progression through all questions

## 📈 Sample Output

```
Q.1: The programming language "Python" is based off a modified version of "JavaScript". (True/False): False
You got it right
The correct answer was: False.
Your current score is: 1/1

Q.2: RAM stands for Random Access Memory. (True/False): True
You got it right
The correct answer was: True.
Your current score is: 2/2

...

You've completed the quiz
Your final score was 8/10
```

## 🚀 Future Enhancements

- [ ] Multiple choice questions support
- [ ] Different difficulty levels
- [ ] Question categories/topics selection
- [ ] Timed questions
- [ ] High score persistence
- [ ] API integration for dynamic questions
- [ ] GUI interface
- [ ] Multiplayer support

## 📚 Educational Value

Perfect for learning:
- OOP principles in Python
- Class design and interaction
- Data modeling and management
- Interactive program flow
- Code organization and modularity

---

*Part of the Python Projects Portfolio - demonstrating object-oriented programming fundamentals and interactive application development.*