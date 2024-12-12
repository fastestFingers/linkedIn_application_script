from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def linkedin_login(driver, email, password):
    """Logs in to LinkedIn using the provided credentials."""
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)
    
    # Enter login credentials
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    time.sleep(3)
    print("Logged into LinkedIn.")

def navigate_to_jobs_page(driver):
    """Navigates to the LinkedIn jobs page."""
    jobs_url = "https://www.linkedin.com/jobs/search/?currentJobId=4084895950&f_AL=true&f_WT=2&keywords=remote&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true&spellCorrectionEnabled=true"
    driver.get(jobs_url)
    
    try:
        # Wait until the jobs list is loaded (timeout set to 60 seconds)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list"))
        )
        print("Jobs page loaded successfully.")
    except Exception as e:
        print(f"Error loading jobs page: {e}")

def process_jobs(driver):
    """Processes job listings and interacts with each job's 'Easy Apply' button."""
    page_number = 1  # Start from page 1
    job_counter = 1  # Initialize job counter

    while True:
        try:
            # Find all the job cards on the page
            job_cards = driver.find_elements(By.CSS_SELECTOR, '.job-card-container')
            
            for job_card in job_cards:
                try:
                    # Locate and click on the job title, which is dynamically placed
                    job_title_element = job_card.find_element(By.CSS_SELECTOR, 'h3.job-card-list__title, h1.t-24.t-bold.inline a')
                    job_title = job_title_element.text
                    print(f"Found job title: {job_title}")
                    
                    # Click on the job title to view more details
                    job_title_element.click()
                    
                    # Wait for the job details page to load
                    time.sleep(10)
                    
                    # Now, look for the 'Easy Apply' button and click it
                    apply_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Easy Apply')]"))
                    )
                    apply_button.click()
                    print(f"Applied to {job_title} successfully.")
                    
                    # After applying, go back to the search results
                    driver.back()
                    time.sleep(2)
                    
                except Exception as e:
                    print(f"Error processing job card: {e}")
                    
            # Check if there's a next page and navigate to it
            next_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-pagination__button--next')
            if next_button and next_button[0].is_enabled():
                next_button[0].click()
                print(f"Moving to page {page_number + 1}...")
                time.sleep(5)  # Wait for the next page to load
                page_number += 1
            else:
                print("No more pages to process.")
                break

        except Exception as e:
            print(f"Error processing the job cards: {e}")
            break

if __name__ == "__main__":
    # Set up Chrome options and driver
    chrome_options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Login to LinkedIn
    # Make sure to put your own credentials
    linkedin_login(driver, "", "")
    
    # Navigate to jobs page
    navigate_to_jobs_page(driver)
    
    # Process jobs and apply
    process_jobs(driver)

    # Close the browser after the process
    driver.quit()
