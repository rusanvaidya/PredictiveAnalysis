# import the webdriver package from selenium
from selenium import webdriver

# Set properties of the browser
chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Initialize the browser object
driver=webdriver.Chrome("<Provide the path of chromedriver>", options=chrome_options)

# The initial url to be opened
url = "https://www.amazon.com/Searchlight-Comics-Comic-bundle-Marvel/dp/B00VIOHOAQ/ref=sr_1_2?keywords=comics&qid=1582544333&sr=8-2"
# Open the given url in the browser
driver.get(url)

# Get the name of the comic book using its Xpath
name = driver.find_element_by_xpath('//*[@id="productTitle"]').text
print("The name of the Comic Book is:", name)

# Close the browser
driver.close()