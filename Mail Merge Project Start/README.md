# 📧 Mail Merge Project

An automated mail merge system that personalizes template letters with individual names, generating custom letters for mass mailings.

## 📋 Project Overview

Automate the tedious process of personalizing mass mailings! This project reads a list of names and a letter template, then generates individual personalized letters for each recipient.

## ✨ Features

- **Template-Based System:** Single template for multiple personalized letters
- **Batch Processing:** Handles multiple recipients automatically
- **File I/O Operations:** Reads from and writes to multiple file formats
- **Name Placeholder Replacement:** Seamless name substitution
- **Organized Output:** Clean file structure for generated letters
- **Cross-Platform Compatibility:** Works on different operating systems

## 🚀 How to Run

```bash
# Navigate to the Mail Merge Project directory
cd "Mail Merge Project Start"

# Run the mail merge
python main.py
```

## 📁 Project Structure

```
Mail Merge Project Start/
├── main.py                    # Main mail merge script
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt    # Letter template
│   └── Names/
│       └── invited_names.txt      # List of recipient names
├── Output/
│   └── ReadyToSend/
│       └── letter_for_[name].txt  # Generated personalized letters
└── README.md                  # This file
```

## 🛠️ How It Works

1. **Read Names:** Load recipient names from `invited_names.txt`
2. **Read Template:** Load letter template from `starting_letter.txt`
3. **Process Each Name:** Replace `[name]` placeholder with actual name
4. **Generate Letters:** Create individual letter file for each person
5. **Save Output:** Store personalized letters in `ReadyToSend` folder

### Input Files

**Names File (`invited_names.txt`):**
```
Alice Smith
Bob Johnson
Charlie Brown
Diana Wilson
```

**Template File (`starting_letter.txt`):**
```
Dear [name],

You are invited to my birthday party on Saturday.

Hope you can make it!

Best regards,
Your Friend
```

### Output Result
Generates individual files:
- `letter_for_Alice Smith.txt`
- `letter_for_Bob Johnson.txt`
- `letter_for_Charlie Brown.txt`
- `letter_for_Diana Wilson.txt`

## 💻 Technical Implementation

### Core Logic
```python
place_holder = "[name]"

# Read all names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read template
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Generate personalized letters
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(place_holder, stripped_name)
    
    # Save individual letter
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
```

### Key Operations
- **File Reading:** Multiple file input handling
- **String Processing:** Placeholder replacement and whitespace handling
- **Loop Processing:** Batch operations on name list
- **File Writing:** Dynamic filename generation and content output

## 🎓 Programming Concepts

This project demonstrates:
- **File I/O Operations:** Reading from and writing to files
- **String Manipulation:** Replace operations and text processing
- **Loops and Iteration:** Processing multiple items
- **File Path Management:** Working with directory structures
- **List Processing:** Handling data collections
- **Error Handling:** Robust file operations
- **Template Systems:** Placeholder-based content generation

## 📊 Use Cases

**Perfect For:**
- **Party Invitations:** Birthday parties, weddings, events
- **Business Communications:** Marketing letters, announcements
- **Educational:** Student notifications, parent communications
- **Non-Profits:** Fundraising letters, volunteer coordination
- **Personal:** Holiday cards, thank you notes

## 🔧 Customization Options

**Easy Modifications:**
```python
# Different placeholder
place_holder = "{{NAME}}"

# Multiple placeholders
letter_contents.replace("[name]", name)
letter_contents.replace("[date]", current_date)
letter_contents.replace("[event]", event_name)

# Different file formats
# Save as HTML, CSV, or other formats
```

## 📈 Sample Use Case

**Wedding Invitation Scenario:**
- **Names:** 150 wedding guests
- **Template:** Formal invitation with RSVP details
- **Output:** 150 personalized invitation files
- **Time Saved:** Hours of manual work reduced to seconds

## 🚀 Future Enhancements

- [ ] Multiple placeholder support (`[name]`, `[date]`, `[location]`)
- [ ] CSV input for structured data (name, address, email)
- [ ] Email integration for direct sending
- [ ] HTML template support for rich formatting
- [ ] GUI interface for non-programmers
- [ ] PDF generation for professional output
- [ ] Template validation and error checking
- [ ] Batch email sending with SMTP
- [ ] Mail merge for different document types

## 💡 Business Applications

**Professional Use Cases:**
- **HR Communications:** Employee notifications, policy updates
- **Sales Outreach:** Personalized sales letters
- **Customer Service:** Personalized responses and follow-ups
- **Marketing Campaigns:** Targeted promotional materials
- **Legal Notifications:** Contract updates, policy changes

## 🎯 Educational Value

Perfect for learning:
- File handling and I/O operations
- String manipulation techniques
- Directory and path management
- Batch processing concepts
- Template-based programming
- Automation principles
- Real-world business applications

## 📋 File Management Best Practices

**Demonstrated Concepts:**
- **Organized Structure:** Separate input and output directories
- **Descriptive Naming:** Clear file naming conventions
- **Error Prevention:** File existence checking
- **Resource Management:** Proper file closing with context managers

---

*Part of the Python Projects Portfolio - showcasing file I/O operations, string processing, and business automation applications.*