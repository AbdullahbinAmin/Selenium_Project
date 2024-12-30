# Python Selenium Project with Jenkins and GitHub Integration

This project demonstrates the integration of Python Selenium testing with Jenkins for Continuous Integration (CI) and Continuous Deployment (CD). The following steps outline how to set up and automate Selenium-based tests using Jenkins and GitHub.

---

## 1. Project Folder Structure

### Create the Project Directory:
- Create a folder named `Jenkins_Project` where all project files will reside.
- Inside `Jenkins_Project`, create a subfolder named `target`.
- Inside the `target` folder, create two subfolders: `allure-reports` and `allure-results`.

### Create a New Project in PyCharm:
- Set up a new Python project in PyCharm inside the `Jenkins_Project` directory.

### Folder Setup for Reporting:
- Ensure that the `target`, `allure-reports`, and `allure-results` folders are present for Allure reporting and test results.

---

## 2. Download WebDriver for Chrome and Firefox

### ChromeDriver:
Download the ChromeDriver: [ChromeDriver Download](https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.204/win64/chromedriver-win64.zip)

### GeckoDriver (Firefox):
Download the GeckoDriver: [GeckoDriver Download](https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-win64.zip)

---

## 3. Selenium Test Code

### Create the Test File:
Create a Python file named `Test_Selenium_Jenkins_Integration.py` and include the following code:

```python
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

def setup_function():
    global driver
    # Setup WebDriver
    path = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=path)
    driver.get("https://www.coursera.org/?authMode=login")
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('python16@gmail.com', 'python@123'),
        ('selenium19@gmail.com', 'sel@123'),
        ('pytsel@gmail.com', 'pytsel@123')
    ]

@pytest.mark.parametrize("username, password", my_cred())
def test_login(username, password):
    print("My pytest Login")
    driver.find_element(By.NAME, 'email').send_keys(username)
    time.sleep(10)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(10)
```

### Configure pytest:
Create a `pytest.ini` file and add the following configuration:
``` ini
[pytest]
addopts = -n3
markers =
    phase1
    phase2
```
---
## 4. Jenkins and Java Installation
### Download Jenkins:
Download the Jenkins: [Download Jenkins](https://get.jenkins.io/war/2.491/jenkins.war)

Place the downloaded jenkins.war in the Jenkins_Project folder.

### Download JDK 21:
Download the JDK 21 (Java): [Download JDK-21_JAVA](https://download.oracle.com/java/21/archive/jdk-21.0.4_windows-x64_bin.exe)

Install JDK 21, follow the installation wizard, keeping the default path.

### Set Java Environment Variables:
1. Navigate to `C:\Program Files\Java\jdk-21` and copy the path.
2. Open "`Environment Variables`" and create a new variable.
3. Variable Name: `JAVA_HOME`
4. Variable Value: `C:\Program Files\Java\jdk-21`
5. Add the JDK bin directory to the system Path.
6. Verify Java Installation by running the following command in the terminal:

``` bash
java -version
```
---
## 5. Running Jenkins
### Start Jenkins:
In the `Jenkins_Project` folder, open a terminal and run the following command:

``` bash
java -jar jenkins.war
```

Access Jenkins Web Interface: [https://YOUR_LOCALHOST_IPv4_ADDRESS:8080/](https://localhost:8080/) 

Put your localhost Ipv4 Address.

Use the generated password to proceed with the initial Jenkins setup.

---

## 6. Set Up Jenkins for Selenium Testing
### Create a New Jenkins Project:
In Jenkins, click on "`New Item`", name it `Selenium_Python_Jenkins`, and select "`Freestyle project`".

### Install Required Plugins:
Go to "`Manage Jenkins`" > "`Manage Plugins`".

### Install the following plugins:
1. Allure (for reporting)
2. ShiningPanda (for Python support)

### Configure the Project:
Under the `project configuration`, select "`Use custom workspace`" and point it to your `Jenkins_Project` folder.
Under Build Steps, choose "`Execute Windows batch command`" and enter the following commands:

``` bash
call ./Scripts/activate.bat
pytest -v -s Test_Selenium_Jenkins_Integration.py --alluredir=./target/allure-results
```

### Configure Post-Build Actions:
Under `Post-build Actions`, select "`Allure Report`" and set the following:

    Results directory: target/allure-results
    Report output directory: target/allure-reports

---
## 7. Integrating GitHub for Version Control

### Create a GitHub Repository:
Create a public GitHub repository named `Selenium_Project`.

### Initialize Git in Your Local Project:
Open Git Bash and run the following commands:

``` bash
git init
git add .
git commit -m "Initial commit"
git branch -M master
git remote add origin https://github.com/YourUsername/Selenium_Project.git
git push -u origin master
```

### Configure GitHub Credentials in Git Bash:
Set up your Git `username` and `email`:

``` bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```
Optionally, save credentials for future use:

``` bash
git config --global credential.helper store
```
---

## 8. Automating the Build in Jenkins
### Configure GitHub in Jenkins:
Create a new Jenkins job named `GitHub_Selenium_Project` and select "`Freestyle Project`".

Under `Source Code Management`, select `Git` and paste your GitHub repository URL:

``` bash
https://github.com/YourUsername/Selenium_Project.git
```
Add Jenkins credentials for GitHub access.

### Build Configuration in Jenkins:
Add a new Build Step: "`Execute Windows batch command`" and enter the following commands:

``` bash
python -m venv env
call ./Scripts/activate.bat
pip install -r requirements.txt
pytest -v -s Test_Selenium_Jenkins_Integration.py --alluredir=./target/allure-results
```

### Post-Build Actions:
Add Allure Report under "`Post-build Actions`".
Save and apply the configuration.

### Triggering Builds Automatically:
Configure Poll SCM with the following cron expression to trigger builds on code changes:

``` bash
* * * * *
```
---
## 9. Version Control and Continuous Integration
### Update and Commit Changes in GitHub:
Make changes to the test code, such as modifying credentials or the test case.

Commit the changes using Git Bash:

``` bash
git init
git add .
git commit -m "Updated credentials"
git push -u origin master
```

### Automatic Trigger in Jenkins:
Jenkins will automatically trigger the build due to the SCM polling configuration, running the tests and generating the Allure report.

---

## Conclusion
This project demonstrates the full CI/CD pipeline using `Selenium`, `Jenkins`, and `GitHub`, from test automation to integration with Jenkins for continuous testing and deployment. By setting up this pipeline, you ensure automated testing and reporting on every code change, significantly improving software quality and deployment efficiency.
