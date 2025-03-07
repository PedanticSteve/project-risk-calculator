from risk_calculator import ProjectRiskCalculator

def get_user_input(prompt, min_val=1, max_val=5):
    """Helper function to get valid user input between min and max values."""
    while True:
        try:
            value = int(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("\n🔹 Project Risk Calculator 🔹")
    print("Rate each factor from 1 (Best) to 5 (Worst).")

    complexity = get_user_input("Project Complexity (1: Simple - 5: Very Complex)")
    budget = get_user_input("Budget Availability (1: High - 5: Very Low)")
    timeline = get_user_input("Project Timeline (1: Long - 5: Very Short)")
    experience = get_user_input("Team Experience Level (1: High - 5: Low)")
    team_size = get_user_input("Team Size (1: Large - 5: Small)")

    calculator = ProjectRiskCalculator(complexity, budget, timeline, experience, team_size)
    
    risk_score = calculator.calculate_risk_score()
    risk_level = calculator.get_risk_level()

    print(f"\n📊 Project Risk Score: {risk_score}")
    print(f"⚠️ Risk Level: {risk_level}")

if __name__ == "__main__":
    main()
