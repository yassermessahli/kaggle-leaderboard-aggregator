# Global Leaderboard Aggregator (For kaggle competitions)

A dynamic web application that aggregates and displays real-time leaderboard data from multiple Kaggle competitions. Originally built with Django, now migrated to Flask for improved performance and simplicity.

## 🔄 Leaderboard Aggregator is now with Flask!

This project has been successfully migrated from `Django` to `Flask` framework, bringing several improvements:

- **Lighter Weight**: Reduced dependencies and simpler architecture
- **Faster Response Time**: Streamlined data processing pipeline
- **Easier Deployment**: Simplified configuration and setup process
- **Better Resource Usage**: More efficient memory management

![screenshot](https://github.com/yassermessahli/kaggle-leaderboard-aggregator/blob/main/assets/images/screenshot.png)

## ✨ New Features

Since the migration, we've added several enhancements:

- **Real-time Competition Countdown**: Dynamic timer showing competition status and remaining time
- **Animated UI Components**: Smooth animations for leaderboard updates
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS
- **Visual Score Indicators**: Progress bars showing relative performance
- **Auto-updating Rankings**: Real-time score updates
- **Competition Status Tracking**: Clear indicators for competition phases (upcoming/active/ended)

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip
- Kaggle API credentials

### Installation

1. Clone the repository:
```bash
git clone git@github.com:yassermessahli/TrainIt-datathon-leaderboard.git
cd kaggle-leaderboard-aggregator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your competition settings in `config.py`:
```python
COMPETITION_CONFIG = {
    "competition_name": "Your Competition Name",
    "start_time": "2024-11-14T19:00:00+00:00",  # Competition start time
    "end_time": "2024-11-15T19:00:00+00:00",    # Competition end time
    "teams": [
        "team1",
        "team2",
        # Add your team names
    ],
    "competitions": [
        "competition1",
        "competition2",
        # Add your Kaggle competition IDs
    ],
    "weights": {
        "competition1": 0.5,
        "competition2": 0.5,
        # Add weights for each competition (must sum to 1)
    }
}
```

5. Run the application:
```bash
python .\app\app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## 🔧 Configuration

### Adding Teams

Add team names to the `teams` list in `config.py`. These should match exactly with the team names on Kaggle.

### Adding Competitions

1. Add competition IDs to the `competitions` list
2. Add corresponding weights in the `weights` dictionary
3. Ensure weights sum to 1.0

Example:
```python
"competitions": ["competition1", "competition2", "competition3"],
"weights": {
    "competition1": 0.4,
    "competition2": 0.3,
    "competition3": 0.3
}
```

## 📊 Features Explanation

### Global Score Calculation

The global score for each team is calculated as:
```
Global Score = Σ (1 / Competition_ranking × Competition_Weight)
```

### Real-time Updates

The leaderboard automatically updates to show:
- Current rankings
- Individual competition scores
- Global aggregated scores
- Competition status and remaining time

### Visual Elements

- **Progress Bars**: Show relative performance compared to top score
- **Rank Badges**: Special styling for top 3 positions
- **Status Indicators**: Show competition phase (upcoming/active/completed)
- **Countdown Timer**: Real-time updates for competition duration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


