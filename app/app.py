from flask import Flask, render_template
from leaderboard import LeaderboardManager
from config import COMPETITION_CONFIG
from datetime import datetime, timezone
import time

app = Flask(__name__)

# Create a single instance of LeaderboardManager
leaderboard_manager = LeaderboardManager()

def get_leaderboard(teams, competitions, weights):
    timestamp = time.time()
    rankings = leaderboard_manager.calculate_global_rank(teams, competitions, weights)
    return rankings, competitions, timestamp

def get_competition_status():
    start_time = datetime.fromisoformat(COMPETITION_CONFIG.get("start_time", "2024-01-01T00:00:00+00:00"))
    end_time = datetime.fromisoformat(COMPETITION_CONFIG.get("end_time", "2024-01-02T00:00:00+00:00"))
    now = datetime.now(timezone.utc)
    
    competition_status = {
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "is_active": start_time <= now <= end_time,
        "has_ended": now > end_time,
        "has_started": now >= start_time
    }
    return competition_status

@app.route('/')
def leaderboard():
    try:
        teams = COMPETITION_CONFIG["teams"]
        competitions = COMPETITION_CONFIG["competitions"]
        weights = COMPETITION_CONFIG["weights"]
        
        rankings, competitions, timestamp = get_leaderboard(teams=teams, competitions=competitions, weights=weights)
        last_update = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        competition_status = get_competition_status()
        
        return render_template('leaderboard.html', 
                             rankings=rankings,
                             competitions=competitions,
                             last_update=last_update,
                             competition_name=COMPETITION_CONFIG["competition_name"],
                             competition_status=competition_status)
    except Exception as e:
        return render_template('errors.html')

if __name__ == '__main__':
    app.run(debug=True)