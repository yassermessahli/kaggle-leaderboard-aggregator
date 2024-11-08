from leaderboard import LeaderboardManager
from config import COMPETITION_CONFIG
import pprint


lb_manager = LeaderboardManager()

pprint.pprint(lb_manager.calculate_global_rank(
    COMPETITION_CONFIG["teams"],
    COMPETITION_CONFIG["competitions"],
    COMPETITION_CONFIG["weights"]
))