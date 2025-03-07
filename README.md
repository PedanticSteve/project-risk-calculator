# 📊 Project Risk Calculator

A Python-based tool that helps assess project risk based on key factors such as complexity, budget, timeline, team experience, and team size. This calculator provides a **risk score** and categorizes the project as **Low Risk, Moderate Risk, or High Risk**.

## 🚀 Features
✅ User-friendly **CLI input system**  
✅ Calculates a **weighted risk score**  
✅ Provides a **risk level assessment** (Low, Moderate, High)  
✅ Modular design with a **separate risk calculation module**  

## 📁 Project Structure
project-risk-calculator/ 
│── risk_calculator.py # Module for risk calculation 
│── main.py # Main script for user input and execution 
│── README.md # Documentation


## 🛠 Installation & Usage
### 🔹 1. Clone the Repository

```
sh
git clone https://github.com/yourusername/project-risk-calculator.git
cd project-risk-calculator
```

### 🔹 2. Run the Program
Ensure you have Python installed (Python 3.x recommended).
Run the script using:
```
python main.py
```
### 🔹 3. Enter Project Risk Factors
The program will prompt you to rate five project factors from 1 (Best) to 5 (Worst):

Project Complexity (1: Simple – 5: Very Complex)
Budget Availability (1: High – 5: Very Low)
Project Timeline (1: Long – 5: Very Short)
Team Experience Level (1: High – 5: Low)
Team Size (1: Large – 5: Small)

### 🔹 4. View Risk Score & Assessment
After entering your values, the program calculates the Project Risk Score and categorizes it as Low Risk, Moderate Risk, or High Risk.

📌 Example Output
```
🔹 Project Risk Calculator 🔹
Rate each factor from 1 (Best) to 5 (Worst).
Project Complexity (1: Simple - 5: Very Complex): 4
Budget Availability (1: High - 5: Very Low): 3
Project Timeline (1: Long - 5: Very Short): 5
Team Experience Level (1: High - 5: Low): 2
Team Size (1: Large - 5: Small): 3

📊 Project Risk Score: 3.4
⚠️ Risk Level: Moderate Risk
```
### 🎯 Future Improvements
✅ Implement a GUI version with a web interface
✅ Save risk assessments to CSV or JSON files
✅ Provide risk mitigation suggestions based on score

📜 License
This project is open-source and available under the MIT License.
