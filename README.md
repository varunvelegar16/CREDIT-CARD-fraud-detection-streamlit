

🛡️ Rule-Based Credit Card Fraud Detection
📌 Project Overview
This project implements a Deterministic Fraud Detection System. Unlike AI-based systems that "guess" based on probability, this system uses a strict set of financial compliance rules and expert-defined logic to flag suspicious transactions instantly.

This approach is widely used in banking as the "First Line of Defense" because it is 100% transparent, easy to audit, and executes with near-zero latency.

⚙️ How It Works (The Logic Layer)
The system evaluates every transaction against a predefined Risk Matrix. If a transaction meets any of the following criteria, it is automatically flagged:

High-Velocity Rule: More than 5 transactions from the same account within 10 minutes.

Threshold Rule: Any single transaction exceeding $10,000 without prior authorization.

Balance Depletion Rule: Any "CASH_OUT" transaction that leaves the origin account with exactly $0.00 (a common sign of account takeover).

Impossible Travel: Transactions occurring in two different geographic locations faster than a plane can fly between them.

🚀 Features
Zero "Black Box" Issues: Every flag comes with a specific reason code (e.g., ERR-VELOCITY).

Instant Execution: No heavy model loading; just fast, efficient Python logic.

Customizable: Rules can be updated by a human analyst in seconds without retraining.

📂 Project Structure
Plaintext
├── app.py             # Streamlit/Flask UI for manual entry
├── rules_engine.py    # The core "If-Then" logic functions
├── config.json        # Threshold settings (e.g., MAX_AMOUNT: 10000)
└── requirements.txt   # Dependencies (Streamlit, Pandas)
🛠️ Installation
Clone the repo:

Bash
git clone https://github.com/your-username/non-ai-fraud-detection.git
Run the application:

Bash
streamlit run app.py
📝 Example Logic
Python
def check_fraud(amount, old_balance):
    if amount > 10000:
        return "FLAGGED: High Value"
    if old_balance == amount:
        return "FLAGGED: Account Clearing"
    return "SAFE"

