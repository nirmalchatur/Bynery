# Automation Framework Architecture

# Overview

This project follows the **Page Object Model (POM)** architecture using **Python**, **Playwright**, and **Pytest**.

The framework is designed to separate test logic from page interactions, making it scalable, reusable, and easy to maintain.

---

# High-Level Architecture

```
                    +----------------------+
                    |    GitHub Actions    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |       Pytest         |
                    +----------+-----------+
                               |
                 Executes Test Cases
                               |
                               v
                    +----------------------+
                    |      Test Files      |
                    | (tests/*.py)         |
                    +----------+-----------+
                               |
                     Uses Page Objects
                               |
                               v
                    +----------------------+
                    |    Page Objects      |
                    | (pages/*.py)         |
                    +----------+-----------+
                               |
                  Playwright API Calls
                               |
                               v
                    +----------------------+
                    |     Playwright       |
                    +----------+-----------+
                               |
                        Browser Automation
                               |
                               v
                    +----------------------+
                    |     Chromium         |
                    +----------------------+
```

---

# Folder Structure

```
qa-automation-challenge/

config/
pages/
tests/
utils/
reports/

README.md
TestPlan.md
Architecture.md
requirements.txt
pytest.ini
conftest.py
```

---

# Component Description

## 1. Test Layer

Location

```
tests/
```

Responsibilities

- Executes automation scripts
- Validates expected behaviour
- Uses reusable page methods
- Contains assertions

Example

```
test_login.py
test_logout.py
test_add_to_cart.py
```

---

## 2. Page Object Layer

Location

```
pages/
```

Responsibilities

- Stores page locators
- Encapsulates page actions
- Keeps UI logic separate from test logic

Example

```
LoginPage.login()

InventoryPage.add_first_product()

DashboardPage.verify_inventory_page()
```

---

## 3. Configuration Layer

Location

```
config/
```

Responsibilities

- Stores application URL
- Stores credentials
- Reads environment variables
- Supports multiple environments

Example

```
APP_BASE_URL

APP_USERNAME

APP_PASSWORD
```

---

## 4. Utility Layer

Location

```
utils/
```

Responsibilities

- Helper methods
- Logging
- API utilities
- Common reusable functions

---

## 5. Reporting Layer

Location

```
reports/
```

Responsibilities

- Stores HTML execution reports
- Displays pass/fail summary
- Execution duration
- Environment details

Generated using

```
pytest-html
```

---

# Test Execution Flow

```
Developer

↓

GitHub

↓

GitHub Actions

↓

Checkout Repository

↓

Install Dependencies

↓

Install Playwright

↓

Execute Pytest

↓

Page Objects

↓

Playwright

↓

Chromium Browser

↓

HTML Report Generated
```

---

# Design Principles

The framework follows the following software engineering principles:

- Separation of Concerns
- Reusability
- Maintainability
- Scalability
- Readability

---

# Why Page Object Model?

Benefits include:

- Reduced code duplication
- Easy locator maintenance
- Improved readability
- Better test organization
- Reusable page methods

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| UI Automation | Playwright |
| Test Framework | Pytest |
| API Testing | Requests |
| Reporting | pytest-html |
| CI/CD | GitHub Actions |
| Version Control | Git |

---

# Continuous Integration

Every push to the repository automatically triggers GitHub Actions.

Pipeline Steps

```
Push Code

↓

Checkout Repository

↓

Install Python

↓

Install Dependencies

↓

Install Playwright

↓

Run Tests

↓

Generate HTML Report

↓

Upload Report
```

---

# Future Improvements

The framework can be extended with:

- BrowserStack Integration
- Parallel Execution
- Docker
- Allure Reporting
- Jenkins Pipeline
- Data-Driven Testing
- Retry Mechanism
- Screenshot Capture on Failure
- Cross Browser Execution

---

# Conclusion

The framework provides a modular and scalable automation solution by combining Playwright, Pytest, and the Page Object Model. The architecture is designed to support future enhancements while maintaining clean, reusable, and maintainable test code.
