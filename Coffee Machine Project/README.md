# ☕ Coffee Machine Project

A comprehensive coffee vending machine simulator with resource management, payment processing, and menu system.

## 🎯 Project Overview

Simulate a real coffee machine experience! Order drinks, process payments, manage resources, and maintain the machine - all through an interactive command-line interface.

## ✨ Features

- **Multiple Coffee Types:** Espresso, Latte, Cappuccino
- **Resource Management:** Water, milk, coffee beans tracking
- **Payment System:** Coin processing and change calculation
- **Admin Functions:** Machine reports and maintenance
- **Object-Oriented Design:** Clean, modular architecture
- **Multiple Versions:** Different implementation approaches
- **Realistic Simulation:** Authentic coffee machine experience

## 🚀 How to Run

```bash
# Navigate to the Coffee Machine Project directory
cd "Coffee Machine Project"

# Run version 1 (basic)
python main_v1.py

# Run version 2 (intermediate) 
python main.v2.py

# Run version 3 (advanced OOP)
python main_v3.py
```

## 📁 Project Structure

```
Coffee Machine Project/
├── main_v1.py      # Basic procedural implementation
├── main.v2.py      # Intermediate version
├── main_v3.py      # Advanced OOP implementation
├── coffee_maker.py # Coffee machine class
├── menu.py         # Menu and drink definitions
├── money_machine.py# Payment processing class
└── README.md       # This file
```

## ☕ Available Drinks

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|----- |
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 100ml | 24g | $3.00 |

## 🎮 How to Use

### Customer Operations
```bash
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
Here is $2.50 in change.
Here is your latte ☕️. Enjoy!
```

### Maintenance Commands
- `report` - View current resource levels and money
- `off` - Turn off the machine (admin only)

## 🛠️ Technical Implementation

### Version 1 (Procedural)
- Simple function-based approach
- Global variables for resources
- Basic input/output handling

### Version 3 (Object-Oriented)
```python
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
```

### Key Classes (v3)
- **`CoffeeMaker`**: Resource management and drink preparation
- **`Menu`**: Drink definitions and menu operations
- **`MoneyMachine`**: Payment processing and change calculation

## 💰 Payment System

**Accepted Coins:**
- Quarters ($0.25)
- Dimes ($0.10) 
- Nickels ($0.05)
- Pennies ($0.01)

**Features:**
- Exact change calculation
- Insufficient funds detection
- Money tracking and reporting

## 📊 Resource Management

**Starting Resources:**
- Water: 300ml
- Milk: 200ml
- Coffee: 100g
- Money: $0.00

**Smart Features:**
- Automatic resource checking before drink preparation
- "Sorry" messages for insufficient ingredients
- Resource consumption tracking

## 🎓 Programming Concepts

This project demonstrates:
- **Object-Oriented Programming:** Classes, methods, encapsulation
- **Data Structures:** Dictionaries for resources and menu items
- **Error Handling:** Resource availability checking
- **User Interface:** Interactive command-line design
- **State Management:** Persistent resource tracking
- **Modular Design:** Separate classes for different responsibilities

## 🔧 Advanced Features (v3)

- **Resource Validation:** Ensures sufficient ingredients before preparation
- **Payment Validation:** Checks payment adequacy before processing
- **Change Calculation:** Accurate money handling with multiple coin types
- **Report Generation:** Detailed resource and financial reporting
- **Extensible Menu:** Easy addition of new drinks and prices

## 📈 Sample Reports

```
Water: 250ml
Milk: 50ml 
Coffee: 76g
Money: $2.50
```

## 🚀 Future Enhancements

- [ ] Drink customization (size, strength)
- [ ] Loyalty card system
- [ ] Inventory restocking alerts
- [ ] Multiple payment methods (card, mobile)
- [ ] Drink history and analytics
- [ ] GUI interface
- [ ] Multi-machine management
- [ ] Temperature control simulation

## 🎯 Educational Value

Excellent for learning:
- Object-oriented design principles
- Real-world system simulation
- Resource management algorithms
- Payment processing logic
- User experience design
- Code evolution and refactoring

---

*Part of the Python Projects Portfolio - demonstrating progression from procedural to object-oriented programming through practical simulation.*