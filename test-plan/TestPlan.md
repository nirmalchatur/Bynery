# Test Plan

# QA Automation Challenge

## Author

**Nirmal Chaturvedi**

---

# 1. Objective

The objective of this project is to validate the core functionality of the application using automated UI and API tests.

The automation framework is built using **Python**, **Playwright**, and **Pytest** while following the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and code reusability.

---

# 2. Scope

The automation suite covers the following functional areas:

### UI Testing

- User Login
- Invalid Login Validation
- Logout Functionality
- Product Selection
- Cart Validation

### API Testing

- User API Response Validation

---

# 3. Test Strategy

The project follows a layered automation approach.

```

Test Cases

↓

Page Objects

↓

Playwright

↓

Browser

```

The framework separates test logic from page interactions, making it easier to maintain and extend.

---

# 4. Automation Framework

Framework Type:

- Playwright
- Pytest
- Page Object Model (POM)

Supporting Libraries:

- requests
- python-dotenv
- pytest-html

---

# 5. Test Environment

| Item | Value |
|------|-------|
| Language | Python 3.12 |
| Automation Tool | Playwright |
| Test Framework | Pytest |
| Browser | Chromium |
| Operating System | Windows 11 / Ubuntu (GitHub Actions) |
| Version Control | Git |
| CI/CD | GitHub Actions |

---

# 6. Test Scenarios

## Login

Objective:

Verify that a valid user can successfully log in.

Expected Result:

- Login successful
- Inventory page displayed

---

## Invalid Login

Objective:

Verify that invalid credentials display an error.

Expected Result:

- Error message displayed
- User remains on login page

---

## Add Product to Cart

Objective:

Verify that a product can be added to the shopping cart.

Expected Result:

- Cart badge displays correct item count

---

## Logout

Objective:

Verify that the user can successfully log out.

Expected Result:

- Login page displayed
- Login form visible

---

## API Validation

Objective:

Verify the Users API returns a successful response.

Expected Result:

- Status Code = 200
- Response contains user data

---

# 7. Test Data

| Parameter | Value |
|-----------|-------|
| Username | standard_user |
| Password | secret_sauce |

---

# 8. Assumptions

- Application is available during execution.
- Internet connection is stable.
- Test users remain active.
- Browser launches successfully.

---

# 9. Risks

- Application downtime
- Network latency
- Changes in UI locators
- Third-party API changes

---

# 10. Reporting

Test execution generates an HTML report using **pytest-html**.

Report Location:

```

reports/report.html

```

The report contains:

- Test Summary
- Execution Time
- Pass/Fail Status
- Environment Details

---

# 11. CI/CD

GitHub Actions is configured to automatically execute the automation suite on every push and pull request.

Pipeline Flow:

```

Developer

↓

Git Push

↓

GitHub Actions

↓

Install Dependencies

↓

Install Playwright

↓

Execute Tests

↓

Generate HTML Report

↓

Upload Report

```

---

# 12. Folder Structure

```

qa-automation-challenge/

config/
pages/
tests/
reports/
utils/

README.md
TestPlan.md
requirements.txt
pytest.ini
conftest.py

```

---

# 13. Test Execution

Run all tests

```bash
python -m pytest
```

Generate HTML Report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

---

# 14. Results

| Test Case | Status |
|-----------|--------|
| Login | ✅ Pass |
| Invalid Login | ✅ Pass |
| Add Product to Cart | ✅ Pass |
| Logout | ✅ Pass |
| API Validation | ✅ Pass |
| Sample Test | ✅ Pass |
| Project Flow | ✅ Pass |

---

# 15. Future Improvements

- Cross-browser execution
- Parallel execution
- BrowserStack integration
- Docker support
- Allure reporting
- Jenkins integration
- Data-driven testing
- Retry mechanism
- Screenshot capture on failure

---

# Conclusion

The automation framework successfully validates the application's primary UI and API workflows using modern automation practices.

The framework is modular, scalable, CI/CD-ready, and designed to be easily extended for future test scenarios.
