# IPL Match Winner Predictor AI

## Project Overview

IPL Match Winner Predictor AI is a Machine Learning-powered web application that predicts the winning probability of teams during the second innings of an IPL match.

The application analyzes the current match situation, including score, wickets, overs completed, target score, venue, batting team, and bowling team, and then predicts the probability of each team winning the match.

The project combines Machine Learning, Data Analysis, Cricket Analytics, Interactive Visualizations, and a modern Streamlit Dashboard to provide real-time match insights.

## 🚀 Live Demo

[Click Here to Open the App](https://ipl-match-winner-predictor-otfgeuz46an6kb3ffyg3yp.streamlit.app/)

---

# Features

### Team Selection

* Searchable Batting Team dropdown
* Searchable Bowling Team dropdown
* Validation to prevent selecting the same team

### Venue Selection

* Searchable Venue dropdown
* Supports all venues available in the training dataset

### Match Situation Inputs

Users can enter:

* Target Score
* Current Score
* Overs Completed
* Wickets Fallen

The application automatically calculates:

* Runs Left
* Balls Left
* Wickets Left
* Current Run Rate (CRR)
* Required Run Rate (RRR)

---

# Machine Learning Model

The prediction engine is built using:

* Scikit-Learn
* Random Forest Classifier

### Features Used for Prediction

* Venue
* Batting Team
* Bowling Team
* Runs Left
* Balls Left
* Wickets Left
* Current Run Rate
* Required Run Rate

The model generates:

* Batting Team Win Probability
* Bowling Team Win Probability

---

# Winner Prediction Engine

The dashboard highlights:

### Predicted Winner Card

Displays:

* Predicted Winning Team
* Win Probability
* Confidence Level

This allows users to quickly identify the likely winner without interpreting raw probabilities.

---

# Visual Analytics Dashboard

## Win Probability Distribution

Interactive Donut Chart showing:

* Batting Team Probability
* Bowling Team Probability

Features:

* Dynamic percentage display
* Highlighted dominant team
* Interactive visualization

---

## Match Win Probability Breakdown

Progress bars display:

* Batting Team win percentage
* Bowling Team win percentage

Provides an easy-to-understand comparison of winning chances.

---

## Run Rate Analysis

Current Run Rate vs Required Run Rate comparison.

Interactive Bar Chart displays:

* Current RR
* Required RR

Additional trend line helps users compare scoring pace and chase difficulty.

---

# Match Summary Card

Displays important match metrics:

* Target Score
* Current Score
* Wickets Fallen
* Runs Needed
* Balls Remaining
* Current RR
* Required RR

Provides a complete snapshot of the match situation.

---

# User Interface Features

### Premium Dashboard Design

* Stadium Background Image
* Glassmorphism Design
* Dark Theme Layout
* Team-specific IPL Colors
* Responsive Dashboard
* Modern Visualization Components

### User Experience Improvements

* Searchable dropdowns
* Input validation
* Real-time predictions
* Clean layout
* Easy-to-understand analytics

---

# Tech Stack

## Frontend

* Streamlit
* HTML
* CSS

## Backend

* Python

## Machine Learning

* Scikit-Learn
* Random Forest Classifier

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly

---

# ⚙️ Installation

### Clone Repository

```bash
git clone <repository-link>
cd IPL-Match-Winner-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# Future Improvements

Potential future enhancements:

* Live IPL API Integration
* Ball-by-ball Prediction Updates
* Team Logos
* Historical Match Analysis
* Player Statistics Integration
* Match Simulation Engine
* Mobile Optimized UI

---

# Author

**Shivam Ahirwar**

Machine Learning & Data Science Enthusiast

Built with Python, Machine Learning, Cricket Analytics, and Streamlit.
