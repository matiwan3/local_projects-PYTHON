import this
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH_TO_DEV_NULL = "nul"
path = r'geckodriver.exe'
driver = webdriver.Firefox(executable_path=path, service_log_path=PATH_TO_DEV_NULL)

# here are various strategies to locate elements in a page. 
# You can use the most appropriate one for your case. 
# Selenium provides the following method to locate elements in a page:

# find_element
# To find multiple elements (these methods will return a list):

# find_elements
# Example usage:
    
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_element(By.XPATH, '//button')

# The attributes available for the By class are used to locate elements on a page. 
# These are the attributes available for By class:

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

# The ‘By’ class is used to specify which attribute is used to locate elements on a page. 
# These are the various ways the attributes are used to locate elements on a page:
driver.find_element(By.ID "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.XPATH, "xpath")
driver.find_element(By.LINK_TEXT, "link text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial libk text")
driver.find_element(By.TAG_NAME, "tag name")
driver.find_element(By.CLASS_NAME, "class name")
driver.find_element(By.CSS_SELECTOR, "css selector")

# If you want to locate several elements with the same attribute replace find_element with find_elements.

# 4.1 Locating by id

# Use this when you know the id attribute of an element.
# With this strategy, the first element with a matching id attribute will be returned. 
# If no element has a matching id attribute, a NoSuchElementException will be raised.

# For instance, consider this page source:

# <html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#   </form>
#  </body>
# </html>

# The form element can be located like this
login_form = driver.find_element(By.ID, 'loginForm')

# 4.2. Locating by Name

# Use this when you know the name attribute of an element. 
# With this strategy, the first element with a matching name attribute will be returned. 
# If no element has a matching name attribute, a NoSuchElementException will be raised.

# For instance, consider this page source:

# <html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#    <input name="continue" type="button" value="Clear" />
#   </form>
# </body>
# </html>

# The username & password elements can be located like this:

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

# This will give the "Login" button as it occurs before the "Clear" button:

continue = driver.find_element(By.NAME, 'continue')

# 4.3. Locating by XPath
# XPath is the language used for locating nodes in an XML document. 
# As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to 
# target elements in their web applications. XPath supports the simple methods of locating by id or name attributes 
# and extends them by opening up all sorts of new possibilities such as locating the third checkbox on the page.

# One of the main reasons for using XPath is when you don’t have a suitable id or name attribute for the element you wish to locate.
# You can use XPath to either locate the element in absolute terms (not advised), or relative to an element that 
# does have an id or name attribute. XPath locators can also be used to specify elements via attributes other than id and name.

# Absolute XPaths contain the location of all elements from the root (html) and as a result are 
# likely to fail with only the slightest adjustment to the application. By finding a nearby element with an id or 
# name attribute (ideally a parent element) you can locate your target element based on the relationship. 
# This is much less likely to change and can make your tests more robust.

# For instance, consider this page source:

# <html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#    <input name="continue" type="button" value="Clear" />
#   </form>
# </body>
# </html>
