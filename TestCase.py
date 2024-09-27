from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Import the custom driver initialization function
from config import get_chrome_driver

# Initialize the driver using the custom configuration
driver = get_chrome_driver()

try:
    # Visit the website
    driver.get("https://magento.softwaretestingboard.com/")
    
    # Wait until the 'Mens' menu is visible and hover over it
    mens_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Men']"))
    )
    ActionChains(driver).move_to_element(mens_menu).perform()
    
    # Wait until the 'Tops' submenu is visible and hover over it
    tops_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Tops']"))
    )
    ActionChains(driver).move_to_element(tops_menu).perform()
    
    # Wait until the 'Tees' option is visible and click it
    tees_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Tees']"))
    )
    tees_option.click()
    
    # Wait until the product grid is visible and select the first product
    first_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item-info"))
    )
    first_product.click()
    
    # Wait until the 'Add to Cart' button is clickable and click it
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "product-addtocart-button"))
    )
    add_to_cart_button.click()
    
finally:
    # Close the driver
    driver.quit()
