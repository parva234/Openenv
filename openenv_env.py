import random

class SupportRoutingEnv:

    def __init__(self):
        self.tickets = {
            "easy": [
                "Password reset not working",
                "Unable to login",
                "Forgot account password"
            ],
            "medium": [
                "Payment failed but money deducted",
                "App crashes on checkout",
                "Unable to update profile"
            ],
            "hard": [
                "Data breach suspected in account",
                "Unauthorized transactions detected",
                "System vulnerability report"
            ]
        }

    def reset(self, difficulty):
        text = random.choice(self.tickets[difficulty])
        return {"text": text}

    def step(self, action):
        
        if action["priority"] == "high":
            reward = 1.0
        else:
            reward = 0.5

        return {"reward": reward}


class BaselineAgent:

    def predict(self, text):
        text = text.lower()


        if "password" in text or "login" in text:
            department = "IT Support"
        elif "payment" in text:
            department = "Finance"
        elif "security" in text or "breach" in text:
            department = "Security"
        else:
            department = "General"

        if "breach" in text or "unauthorized" in text:
            priority = "high"
        elif "failed" in text or "crash" in text:
            priority = "medium"
        else:
            priority = "low"

        return {
            "department": department,
            "priority": priority
        }