# 💰 Personal Finance Manager CLI

A simple command-line Python application to help users manage personal finances. You can track **expenses**, **incomes**, **investments**, and **set a monthly budget** without needing a database — all data is saved in a local JSON file.

---

## 🚀 Features

- 📌 Add & view **expenses**, **incomes**, and **investments**
- 🧾 Set and check **monthly budget**
- 🗑️ Delete specific entries by category/source/description
- 🧠 Simple CLI with clear commands using [Click](https://click.palletsprojects.com/)
- 💾 Data persistence using JSON (no external database required)

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/personal-finance-cli.git
   cd personal-finance-cli
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install click
⚙️ How to Use
Run the CLI app with:

bash
Copy
Edit
python finance_manage.py COMMAND [OPTIONS]
✅ Commands:
Command	Description	Example
add-expense	Add a new expense	--amount 100 --category Food
add-income	Add a new income	--amount 500 --source Job
add-investment	Add an investment	--amount 200 --description Stocks
set-budget	Set a monthly budget	--budget 1500
show-summary	Show full financial summary	(no options)
delete-expense	Delete expenses by category	Prompted input
delete-income	Delete incomes by source	Prompted input
delete-investment	Delete investment by description	Prompted input

📁 File Structure
bash
Copy
Edit
.
├── finance_manage.py    # Main CLI application
├── finance_data.json    # Auto-generated data storage (created at runtime)
└── README.md            # Project documentation
📌 Dependencies
Python 3.6+

click

Install dependencies with:

bash
Copy
Edit
pip install -r requirements.txt
(Create requirements.txt with: click==8.1.3)

👨‍💻 Author
Tanvir