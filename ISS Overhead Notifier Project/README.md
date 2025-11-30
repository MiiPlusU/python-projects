# 🛰️ ISS Overhead Notifier Project

A real-time International Space Station (ISS) tracking application that sends email notifications when the ISS passes overhead during nighttime for optimal viewing conditions.

## 🌟 Project Overview

Never miss the ISS again! This automated system tracks the International Space Station's location and sends you email alerts when it's visible from your location during nighttime hours.

## ✨ Features

- **Real-Time ISS Tracking:** Fetches current ISS coordinates from NASA API
- **Location-Based Alerts:** Customizable latitude/longitude monitoring
- **Nighttime Detection:** Uses sunrise/sunset API to determine optimal viewing
- **Email Notifications:** Automated SMTP email alerts
- **Continuous Monitoring:** Runs indefinitely with periodic checks
- **API Integration:** Multiple REST API services

## 🚀 How to Run

```bash
# Navigate to the ISS Overhead Notifier Project directory
cd "ISS Overhead Notifier Project"

# Install required packages
pip install requests pandas

# Update your coordinates and email in main.py
# Set MY_LAT, MY_LONG, MY_EMAIL, MY_PASSWORD

# Run the notifier
python main.py
```

## 🛰️ How It Works

1. **ISS Position Check:** Queries ISS location API every 60 seconds
2. **Proximity Detection:** Checks if ISS is within ±5° of your coordinates
3. **Night Verification:** Confirms it's nighttime for optimal visibility
4. **Email Alert:** Sends notification when both conditions are met
5. **Continuous Loop:** Repeats monitoring process indefinitely

### Viewing Conditions
- **ISS Overhead:** Within ±5° latitude/longitude of your location
- **Nighttime:** During dark hours for maximum visibility
- **Clear Skies:** Best viewing (not detected by app)

## 📁 Project Structure

```
ISS Overhead Notifier Project/
├── main.py       # Main tracking and notification script
└── README.md     # This file
```

## 🛠️ Technical Implementation

### APIs Used
```python
# ISS Current Location
"http://api.open-notify.org/iss-now.json"

# Sunrise/Sunset Times  
"https://api.sunrise-sunset.org/json"
```

### Core Functions
```python
def is_above():
    # Check if ISS is within viewing range
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG:
        return True

def is_night():
    # Verify it's nighttime for optimal viewing
    # Compare current time with sunrise/sunset data
```

### Email System
- **SMTP Integration:** Automated email sending
- **Gmail Support:** Works with Gmail SMTP servers
- **Secure Authentication:** Uses app passwords for security

## 🌍 Location Setup

**Configure Your Coordinates:**
```python
MY_LAT = 33.162689    # Your latitude
MY_LONG = -96.937622  # Your longitude  
MY_EMAIL = "your-email@gmail.com"
MY_PASSWORD = "your-app-password"
```

**Find Your Coordinates:**
- Google Maps: Right-click → "What's here?"
- GPS devices or smartphone apps
- Online coordinate lookup tools

## 📧 Email Configuration

**Gmail Setup:**
1. Enable 2-factor authentication
2. Generate app-specific password
3. Use app password in `MY_PASSWORD`
4. Update `MY_EMAIL` with your Gmail address

## 🛰️ ISS Facts

**International Space Station:**
- **Altitude:** ~408 km (254 miles) above Earth
- **Speed:** 28,000 km/h (17,500 mph)
- **Orbit Time:** 90 minutes per orbit
- **Visibility:** Appears as bright moving star
- **Size:** Football field-sized solar arrays

**Viewing Tips:**
- Look for steady, bright light moving across sky
- No blinking (distinguishes from aircraft)
- Visible for 2-5 minutes per pass
- Best seen during dawn/dusk transitions

## 🎓 Programming Concepts

This project demonstrates:
- **API Integration:** Multiple REST API consumption
- **JSON Processing:** Parsing API responses
- **Email Automation:** SMTP protocol usage
- **Datetime Handling:** Time zone and scheduling
- **Geolocation Math:** Coordinate proximity calculations
- **Error Handling:** Network request exception management
- **Infinite Loops:** Continuous monitoring systems

## 📊 Technical Specifications

- **Update Frequency:** Every 60 seconds
- **Detection Range:** ±5° latitude/longitude
- **Email Service:** SMTP (Gmail optimized)
- **Dependencies:** requests, pandas, smtplib, datetime
- **Runtime:** Continuous (until manually stopped)

## 🌙 Night Detection Logic

Uses sunrise-sunset.org API to determine:
- Current local time vs sunrise/sunset
- Astronomical twilight periods
- Optimal viewing windows
- Seasonal daylight variations

## 🚀 Future Enhancements

- [ ] Mobile app notifications (push notifications)
- [ ] Weather API integration (cloud cover check)
- [ ] Multiple location monitoring
- [ ] ISS pass prediction (upcoming passes)
- [ ] Viewing angle calculations
- [ ] Historical pass logging
- [ ] GUI interface for easier configuration
- [ ] Social media posting integration

## 🔧 Troubleshooting

**Common Issues:**
- **Email not sending:** Check app password and 2FA
- **API errors:** Verify internet connection
- **Wrong notifications:** Confirm coordinates accuracy
- **No notifications:** Check ISS pass times for your area

## 🌟 Educational Value

Perfect for learning:
- REST API consumption
- Real-time data processing
- Email automation
- Astronomical calculations
- Continuous monitoring systems
- Error handling and reliability
- Geospatial programming

## 📡 Space Technology

**NASA APIs:**
- Open Notify API for ISS tracking
- Real-time positional data
- Public access, no authentication required
- High reliability and accuracy

---

*Part of the Python Projects Portfolio - showcasing real-time API integration, automation, and space technology applications.*