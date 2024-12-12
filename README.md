# LinkedIn Job Application Automation

This script automates the process of logging into LinkedIn, navigating to the jobs page, and applying to jobs using the 'Easy Apply' feature. It uses Selenium for web automation.

# Features
- *Login to LinkedIn*: Automates the login process using your credentials.
- *Navigate to Jobs Page*: Directly navigates to a pre-defined LinkedIn jobs search page.
- *Apply to Jobs*: Automatically processes job listings and interacts with the 'Easy Apply' button where available.

# Prerequisites

1. *Python*: Make sure Python is installed on your system.
2. *Selenium*: Install the Selenium library for Python.
3. *Webdriver Manager*: Install the Webdriver Manager for Chrome.
4. *Google Chrome*: Ensure Google Chrome is installed.

# Installation

1. Clone this repository or download the script.
2. Install the required Python packages:
   ```bash
   pip install selenium webdriver-manager
   ```

# Usage

1. Update the script with your LinkedIn credentials in the `linkedin_login` function:
   ```python
   linkedin_login(driver, "your_email", "your_password")
   ```

2. Run the script:
   ```bash
   python script_name.py
   ```

# How It Works

# Functions:

1. *linkedin_login(driver, email, password)*:
   - Logs into LinkedIn using the provided email and password.

2. *navigate_to_jobs_page(driver)*:
   - Navigates to a pre-defined LinkedIn jobs search page.
   - Waits until the jobs list is loaded.

3. *process_jobs(driver)*:
   - Iterates through job listings on the current page.
   - Clicks on the job title, applies using 'Easy Apply' (if available), and navigates back to the job list.
   - Moves to the next page if available.

# Workflow:
1. The script initializes a Selenium WebDriver instance with Chrome.
2. Logs in to LinkedIn using the provided credentials.
3. Navigates to the jobs page URL specified in the `navigate_to_jobs_page` function.
4. Processes job cards on the page and interacts with the 'Easy Apply' button.
5. Moves to the next page of job results until no more pages are available.
6. Closes the browser upon completion.

# Customization

- *Change Job Search Parameters**: Update the `jobs_url` in the `navigate_to_jobs_page` function to modify the job search criteria.
- *Error Handling**: Customize exception handling for different sections of the script as per your requirements.

# Notes

- This script interacts with live web pages, so LinkedIn's layout changes may affect its functionality.
- Ensure compliance with LinkedIn's [terms of service](https://www.linkedin.com/legal/user-agreement) while using this script.

# Disclaimer

This script is intended for educational purposes only. Use it responsibly and avoid violating any policies or terms of use of LinkedIn.

---

Enjoy automating your job applications!

