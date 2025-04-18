*** Settings ***
Documentation    Test Suite for testing the home page
Library          SeleniumLibrary

Test Setup       Navigate to Home Page
Test Teardown    Close Browser

*** Variables ***

*** Test Cases ***
Test Title
    [Documentation]    Test Case to check the title of the home page
    Title Should Be    Restful-booker-platform demo

*** Keywords ***
Navigate to Home Page
    [Documentation]    Keyword to open the chrome browser
    Open Browser    url=https://automationintesting.online/    browser=headlesschrome

