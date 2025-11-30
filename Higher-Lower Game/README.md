# 📱 Higher-Lower Game

A social media follower guessing game where players compare celebrities, influencers, and brands to guess who has more followers.

## 🎮 Game Overview

Test your knowledge of social media popularity! Compare two personalities/brands and guess which one has more followers. Keep guessing correctly to build your score!

## ✨ Features

- **Celebrity Database:** 300+ celebrities, influencers, and brands
- **Follower Counts:** Real social media follower data
- **Score Tracking:** Continuous scoring system
- **ASCII Art Interface:** Visual elements for better UX
- **Multiple Versions:** Two different implementations
- **Screen Clearing:** Clean interface between rounds

## 🚀 How to Run

```bash
# Navigate to the Higher-Lower Game directory
cd "Higher-Lower Game"

# Run version 1
python main_v1.py

# Run version 2 (enhanced)
python main_v2.py
```

## 🎯 How to Play

1. **Compare:** See two personalities/brands (A and B)
2. **Guess:** Type 'A' or 'B' for who has more followers
3. **Continue:** If correct, get a new comparison with your score
4. **Game Over:** Wrong guess ends the game with final score

### Sample Gameplay
```
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.
    VS
Against B: Ariana Grande, a Musician and actress, from United States.
Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1
```

## 📁 Project Structure

```
Higher-Lower Game/
├── main_v1.py     # Basic game implementation
├── main_v2.py     # Enhanced version
├── art.py         # ASCII art and visual elements
├── game_data.py   # Celebrity/brand database
└── README.md      # This file
```

## 🛠️ Technical Implementation

### Game Logic
- **Random Selection:** Picks random celebrities from database
- **Comparison Engine:** Compares follower counts
- **Score Management:** Tracks consecutive correct guesses
- **Game Flow:** Manages turns and game state

### Data Structure
```python
{
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,
    'description': 'Footballer', 
    'country': 'Portugal'
}
```

### Key Features
- **Duplicate Prevention:** Ensures no repeat comparisons
- **Dynamic Updates:** Winner becomes next comparison base
- **Screen Management:** Clears screen between rounds
- **Input Validation:** Handles case-insensitive input

## 📊 Database Content

**Categories Include:**
- **Athletes:** Footballers, basketball players, other sports
- **Musicians:** Pop stars, rappers, international artists
- **Actors:** Movie stars, TV personalities
- **Influencers:** Social media personalities
- **Brands:** Major companies and platforms
- **Public Figures:** Politicians, celebrities

**Geographic Diversity:**
- United States, Portugal, India, United Kingdom
- South Korea, Canada, Brazil, and many more

## 🎓 Programming Concepts

This project demonstrates:
- **Data Structures:** Dictionaries and lists
- **Random Module:** Pseudo-random selection
- **Control Flow:** While loops, conditionals
- **Functions:** Modular code organization
- **File Imports:** Module system usage
- **OS Operations:** Screen clearing functionality
- **Global Variables:** Game state management

## 🎨 Visual Elements

- **ASCII Art Logo:** Game branding
- **VS Symbol:** Visual separator for comparisons
- **Clear Screen:** Clean interface updates
- **Score Display:** Real-time feedback

## 📈 Game Statistics

- **Database Size:** 300+ entries
- **Follower Range:** From thousands to hundreds of millions
- **Difficulty:** Varies based on celebrity popularity knowledge
- **Replayability:** Random selections ensure unique games

## 🚀 Future Enhancements

- [ ] Difficulty levels (easy/medium/hard)
- [ ] Category-specific modes (musicians only, athletes only)
- [ ] Multiplayer support
- [ ] High score persistence
- [ ] Real-time follower count updates
- [ ] Hint system
- [ ] Time-based challenges
- [ ] Statistics tracking

## 🎯 Educational Value

Great for learning:
- Data handling and manipulation
- Random number generation
- Game state management
- User interface design
- Modular programming
- File organization

---

*Part of the Python Projects Portfolio - showcasing data-driven game development and interactive entertainment programming.*