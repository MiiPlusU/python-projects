# 🃏 BlackJack Capstone Project

A classic BlackJack card game implementation in Python featuring ASCII art, multiple versions, and proper game logic.

## 🎮 Game Features

- **Classic BlackJack Rules:** Hit, Stand, Bust mechanics
- **ASCII Art Interface:** Beautiful card-themed visuals
- **Dealer AI:** Automated dealer following standard casino rules
- **Score Tracking:** Real-time score calculation and display
- **Multiple Versions:** Two different implementations to compare approaches

## 🎯 How to Play

1. **Objective:** Get as close to 21 as possible without going over (busting)
2. **Card Values:**
   - Number cards (2-10): Face value
   - Face cards (J, Q, K): Worth 10
   - Aces: Worth 11 or 1 (automatically adjusted to prevent busting)

3. **Gameplay:**
   - Both player and dealer start with 2 cards
   - Player can "Hit" (take another card) or "Stand" (keep current total)
   - Dealer must hit on 16 or below, stand on 17 or above
   - Player wins if closer to 21 than dealer without busting

## 🚀 How to Run

```bash
# Navigate to the project directory
cd "BlackJack-Capstone-Project"

# Run version 1 (basic implementation)
python main_v1.py

# Run version 2 (enhanced implementation)
python main_v2.py
```

## 📁 Project Structure

```
BlackJack-Capstone-Project/
├── main_v1.py      # Basic BlackJack implementation
├── main_v2.py      # Enhanced version with improved logic
├── art.py          # ASCII art and visual elements
└── README.md       # This file
```

## 🛠️ Technical Implementation

### Version 1 (`main_v1.py`)
- Basic game loop
- Simple random card dealing
- Core win/lose logic

### Version 2 (`main_v2.py`)
- Enhanced game mechanics
- Improved user interface
- Better error handling
- More sophisticated game flow

### ASCII Art (`art.py`)
- BlackJack logo
- Card-themed visual elements
- Enhances user experience

## 🎨 Key Programming Concepts

- **Lists and Random Module:** Card deck management
- **Control Flow:** Game logic and decision making
- **Functions:** Modular code organization
- **ASCII Art Integration:** Visual programming
- **Game State Management:** Tracking player and dealer hands

## 🎲 Game Rules Implemented

- Standard 52-card deck simulation
- Ace value adjustment (11→1 when beneficial)
- Dealer must hit on 16, stand on 17
- Player bust detection
- Win/lose/tie conditions
- Multiple round capability

## 🔮 Future Enhancements

- [ ] Multiple player support
- [ ] Betting system with chips
- [ ] Card counting features
- [ ] Graphical user interface
- [ ] Statistics tracking
- [ ] Save/load game state

---

*Part of the Python Projects Portfolio - showcasing fundamental game development and logic implementation.*