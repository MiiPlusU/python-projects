# 🎯 The Number Guessing Game

A classic number guessing game with difficulty levels, attempt tracking, and interactive gameplay.

## 🎮 Game Overview

Guess the computer's secret number between 1 and 100! Choose your difficulty level and test your guessing skills with limited attempts.

## ✨ Features

- **Difficulty Levels:** Easy (10 attempts) and Hard (5 attempts)
- **Smart Feedback:** "Too high" or "Too low" hints
- **Attempt Tracking:** Real-time remaining attempts display
- **ASCII Art:** Visual game logo and interface
- **Multiple Versions:** Two implementations with different approaches
- **Input Validation:** Handles user input and game flow

## 🚀 How to Run

```bash
# Navigate to the Number Guessing Game directory
cd "The Number Guessing Game"

# Run version 1
python main_v1.py

# Run version 2 (enhanced)
python main_v2.py
```

## 🎯 How to Play

1. **Start:** Game generates a random number between 1-100
2. **Choose Difficulty:**
   - Easy: 10 attempts
   - Hard: 5 attempts
3. **Guess:** Enter your number guess
4. **Get Feedback:** "Too high", "Too low", or "You got it!"
5. **Win/Lose:** Guess correctly or run out of attempts

### Sample Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number
```

## 📁 Project Structure

```
The Number Guessing Game/
├── main_v1.py     # Basic implementation
├── main_v2.py     # Enhanced version
├── art.py         # ASCII art logo
└── README.md      # This file
```

## 🛠️ Technical Implementation

### Core Game Logic
- **Random Number Generation:** `random.randint(1, 100)`
- **Difficulty Selection:** Dynamic attempt allocation
- **Comparison Logic:** Greater than/less than feedback
- **Loop Control:** While loop with attempt counter
- **Input Handling:** Integer conversion and validation

### Game Flow
1. Display welcome message and logo
2. Generate secret number
3. Get difficulty choice from user
4. Set attempt limit based on difficulty
5. Main guessing loop with feedback
6. Win/lose condition checking

## 🎓 Programming Concepts

This project demonstrates:
- **Random Module:** Pseudo-random number generation
- **Control Flow:** While loops, if/elif/else statements
- **Functions:** Code organization and modularity
- **Variables:** Global and local variable management
- **User Input:** Interactive command-line interface
- **Type Conversion:** String to integer conversion
- **Boolean Logic:** Game state management

## 🎯 Game Strategy Tips

- **Binary Search Approach:** Start with 50, then adjust by halves
- **Easy Mode:** More forgiving, good for learning
- **Hard Mode:** Requires strategic thinking and luck
- **Pattern Recognition:** Learn from "too high/low" feedback

## 📊 Difficulty Analysis

**Easy Mode (10 attempts):**
- Success rate: ~90% with good strategy
- Allows for experimental guesses
- Good for beginners

**Hard Mode (5 attempts):**
- Success rate: ~60% with optimal strategy
- Requires efficient guessing strategy
- Challenging for experienced players

## 🚀 Future Enhancements

- [ ] Custom number ranges
- [ ] Score/statistics tracking
- [ ] Multiplayer support
- [ ] Hint system
- [ ] Time-based challenges
- [ ] Leaderboard system
- [ ] GUI interface
- [ ] Sound effects

## 🎨 Educational Value

Perfect for learning:
- Basic Python syntax
- Control structures and loops
- Random number generation
- User input handling
- Function definition and calling
- Game logic implementation

---

*Part of the Python Projects Portfolio - showcasing fundamental programming concepts through interactive game development.*