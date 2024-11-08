from kaggle import KaggleApi
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any
import threading

class LeaderboardManager:
    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()
        self._cache_lock = threading.Lock()
        self._competition_cache: Dict[str, List[Dict]] = {}
        
    @lru_cache(maxsize=32)
    def fetch_competition_leaderboard(self, competition: str) -> List[Dict]:
        """
        Fetch and cache the leaderboard data of a single competition.
        Uses lru_cache for memory-efficient caching.
        """
        if competition in self._competition_cache:
            return self._competition_cache[competition]
            
        results = self.api.competition_leaderboard_view(competition=competition)
        result_fields = ["teamId", "teamName", "submissionDate", "score"]
        
        leaderboard = [
            {
                "rank": i + 1,
                **{f: str(getattr(result, f)) for f in result_fields}
            }
            for i, result in enumerate(results)
        ]
        
        with self._cache_lock:
            self._competition_cache[competition] = leaderboard
        
        return leaderboard

    def _get_team_rank(self, team: str, competition: str) -> int:
        """
        Helper function to get a team's rank in a specific competition.
        """
        results = self.fetch_competition_leaderboard(competition)
        for r in results:
            if r["teamName"] == team:
                return r["rank"]
        return len(results) + 1

    def get_all_ranks(self, team: str, competitions: List[str]) -> Dict:
        """
        Get all ranks of a team in a list of competitions using parallel processing.
        """
        with ThreadPoolExecutor() as executor:
            ranks = {
                comp: rank for comp, rank in 
                zip(competitions, executor.map(
                    lambda c: self._get_team_rank(team, c), 
                    competitions
                ))
            }
            
        return {"team": team, "ranks": ranks}

    def calculate_global_rank(self, teams: List[str], competitions: List[str], weights: List[float]) -> List[Dict]:
        """
        Calculate global ranks for all teams using parallel processing and caching.
        """
        if len(competitions) != len(weights):
            raise ValueError("The competitions list and weights list must have the same length.")
        if abs(sum(weights) - 100) > 0.001:  # Using small epsilon for float comparison
            raise ValueError("The sum of weights must be equal to 100.")

        # Pre-fetch all competition leaderboards in parallel
        with ThreadPoolExecutor() as executor:
            executor.map(self.fetch_competition_leaderboard, competitions)
        
        # Calculate ranks for all teams in parallel
        with ThreadPoolExecutor() as executor:
            team_ranks = list(executor.map(
                lambda t: (t, self.get_all_ranks(t, competitions)), 
                teams
            ))

        # Calculate global scores
        global_rank = []
        for team, ranks_data in team_ranks:
            ranks = ranks_data["ranks"]
            score = sum(1 / ranks[c] * w for c, w in zip(competitions, weights))
            global_rank.append({
                "team": team,
                "score": score,
                "all_ranks": ranks
            })

        # Sort and add final ranks
        global_rank.sort(key=lambda x: x["score"], reverse=True)
        for i, entry in enumerate(global_rank):
            entry["rank"] = i + 1

        return global_rank
