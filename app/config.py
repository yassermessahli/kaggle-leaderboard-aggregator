# config.py for competition configuration
# used by app.py

COMPETITION_NAME = "Mini Datathon - SOAI"

START_TIME = "2024-11-07T19:00:00+00:00"
END_TIME = "2024-11-08T18:00:00+00:00"

TEAMS = [
    "kurtosis",
    "Vgaith",
    "Megatron"
]

COMPETITIONS = [
    "pcbm-challge",
    "jumia-purchase-prediction",
    "instadeep-challenge-soai"
]

WEIGHTS = [40, 35, 25]


# ==================================================================================

COMPETITION_CONFIG = {
    "competition_name": COMPETITION_NAME,
    "start_time": START_TIME,
    "end_time": END_TIME,
    "teams": TEAMS,
    "competitions": COMPETITIONS,
    "weights": WEIGHTS
}