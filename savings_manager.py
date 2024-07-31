import json

SAVINGS_GOAL_FILE = 'savings_goal.json'

def load_savings_goal():
    try:
        with open(SAVINGS_GOAL_FILE, 'r') as file:
            data = json.load(file)
            return data.get('goal', 0.0)
    except FileNotFoundError:
        return 0.0

def save_savings_goal(goal):
    with open(SAVINGS_GOAL_FILE, 'w') as file:
        json.dump({'goal': goal}, file)
