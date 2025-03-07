class ProjectRiskCalculator:
    """A class to calculate project risk based on key factors."""
    
    def __init__(self, complexity, budget, timeline, experience, team_size):
        self.complexity = complexity      # 1 (Low) to 5 (High)
        self.budget = budget              # 1 (High) to 5 (Low)
        self.timeline = timeline          # 1 (Long) to 5 (Short)
        self.experience = experience      # 1 (High) to 5 (Low)
        self.team_size = team_size        # 1 (Large) to 5 (Small)

    def calculate_risk_score(self):
        """Calculates the overall project risk score based on weighted factors."""
        score = (
            (self.complexity * 0.3) +
            (self.budget * 0.2) +
            (self.timeline * 0.2) +
            (self.experience * 0.2) +
            (self.team_size * 0.1)
        )
        return round(score, 2)

    def get_risk_level(self):
        """Determines risk level based on the score."""
        score = self.calculate_risk_score()
        if score <= 2:
            return "Low Risk"
        elif 2 < score <= 3.5:
            return "Moderate Risk"
        else:
            return "High Risk"
