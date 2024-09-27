from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import get_chrome_driver

# Initialize the driver using the custom configuration
driver = get_chrome_driver()

try:
    # Visit the website
    driver.get("https://magento.softwaretestingboard.com/")
    
    # Wait until the "Mens" menu is clickable and click it
    mens_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Men"))
    )
    mens_menu.click()
    
    # Wait until the "Tops" submenu is visible and click it
    tops_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Tops"))
    )
    tops_menu.click()
    
    # Wait until the products are visible and select the first product
    first_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item-info"))
    )
    first_product.click()
    
    # Wait until the size options are visible and select the first size
    first_size = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".swatch-option.text"))
    )
    first_size.click()
    
    # Wait until the color options are visible and select the first color
    first_color = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".swatch-option.color"))
    )
    first_color.click()
    
    # Wait until the "Add to Cart" button is clickable and click it
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "product-addtocart-button"))
    )
    add_to_cart_button.click()
    
finally:
    # Close the driver
    driver.quit()