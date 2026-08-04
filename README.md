# 🚀 QA Automation Framework using Playwright & Pytest

A scalable UI and API Automation Framework developed using **Python**, **Playwright**, and **Pytest** following the **Page Object Model (POM)** design pattern.

This project demonstrates modern QA Automation practices including UI testing, API testing, configuration management, HTML reporting, and CI/CD readiness.

---
Google Docs Link - https://docs.google.com/document/d/1GzW4jAekYi0jaRUBKz_3KArldaQaMRJG3xquohAMKvw/edit?usp=sharing
# 📌 Features

- ✅ UI Automation using Playwright
- ✅ API Testing using Requests
- ✅ Page Object Model (POM)
- ✅ Pytest Framework
- ✅ Configuration using Environment Variables
- ✅ HTML Test Reports
- ✅ Cross-browser Ready
- ✅ CI/CD Ready
- ✅ Easy to Extend and Maintain

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| Playwright | UI Automation |
| Pytest | Test Runner |
| Requests | API Testing |
| pytest-html | HTML Reporting |
| python-dotenv | Environment Variable Management |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
qa-automation-challenge/

├── config/
│   └── config.py
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_logout.py
│   ├── test_add_to_cart.py
│   ├── test_api.py
│   ├── test_project.py
│   └── test_sample.py
│
├── reports/
│   └── report.html
│
├── test_data/
│
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
└── README.md
```

---

# 🧪 Automated Test Scenarios

### UI Tests

- ✔ Valid Login
- ✔ Invalid Login
- ✔ Logout
- ✔ Add Product to Cart
- ✔ Inventory Validation

### API Tests

- ✔ Get Users API Validation

---

# ⚙️ Prerequisites

- Python 3.12+
- Git
- Playwright

---

# 📥 Installation

Clone the repository

```bash
git clone https://github.com/nirmalchatur/Bynery.git
```

Navigate to the project

```bash
cd Bynery
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
python -m playwright install
```

---

# ▶ Running Tests

Run all tests

```bash
python -m pytest
```

Run a specific test

```bash
python -m pytest tests/test_login.py -v
```

Run tests with HTML report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

---

# 📊 Test Report

After execution, an HTML report is generated at:

```text
reports/report.html
```

The report includes:

- Test Summary
- Pass/Fail Status
- Execution Time
- Environment Information

---

# 🏗 Framework Design

The framework follows the **Page Object Model (POM)**.

```
Test

↓

Page Object

↓

Playwright

↓

Browser
```

Benefits:

- Better code readability
- Easy maintenance
- Reusable page methods
- Reduced code duplication

---

# 🔐 Configuration Management

Environment-specific values are managed using a `.env` file.

Example:

```env
APP_BASE_URL=https://www.saucedemo.com
APP_USERNAME=standard_user
APP_PASSWORD=secret_sauce
```

Sensitive credentials are not hardcoded inside the test scripts.

---

# 📈 Current Test Status

| Test | Status |
|------|--------|
| Login | ✅ Pass |
| Invalid Login | ✅ Pass |
| Logout | ✅ Pass |
| Add to Cart | ✅ Pass |
| API Test | ✅ Pass |
| Sample Test | ✅ Pass |
| Project Flow | ✅ Pass |

**Total Tests:** **7**

**Status:** **7 Passed ✅**

---

# 🚀 CI/CD

The project is ready for integration with CI/CD tools such as:

- GitHub Actions
- Jenkins
- Azure DevOps

Typical pipeline:

```
Developer

↓

Git Push

↓

GitHub

↓

CI Pipeline

↓

Install Dependencies

↓

Run Tests

↓

Generate Reports

↓

Publish Results
```

---

# 📌 Future Enhancements

- BrowserStack Integration
- Parallel Test Execution
- Allure Reporting
- Database Validation
- Docker Support
- Jenkins Pipeline
- Mobile Automation
- Data-Driven Testing
- Retry Mechanism
- Screenshot Capture on Failure

---

# 👨‍💻 Author

**Nirmal Chaturvedi**

B.Tech – Computer Engineering

QA Automation | Python | Playwright | API Testing | SQL

GitHub: https://github.com/nirmalchatur

---

# 📄 License

This project is created for educational purposes and QA Automation practice.
