*** Settings ***
Documentation    Test Suite for testing the home page
Library          SeleniumLibrary

Test Setup       Navigate to Home Page
Test Teardown    Close Browser

*** Variables ***
${TITLE}               Restful-booker-platform demo

${USERNAME_LOCATOR}    id:username
${PASSWORD_LOCATOR}    id:password

${USERNAME_VALUE}      Stefano
${PASSWORD_VALUE}      Akjsfksjg


*** Test Cases ***
Test Login 1
    [Documentation]    Test Case to check the login functionality
    
    Wait For Expected Condition          Title Is    ${TITLE}
    
    Wait Until Element Contains          xpath://*[@id='root-container']/div/nav    Shady Meadows B&B
    Click Link                           xpath://*[@id="navbarNav"]/ul/li[6]/a

    Wait Until Page Contains             Login

    Press Key                            ${USERNAME_LOCATOR}    ${USERNAME_VALUE}
    Element Attribute Value Should Be    ${USERNAME_LOCATOR}    value    ${USERNAME_VALUE}

    Press Key                            ${PASSWORD_LOCATOR}    ${PASSWORD_VALUE}
    Element Attribute Value Should Be    ${PASSWORD_LOCATOR}    value    ${PASSWORD_VALUE}

    Click Button                         id:doLogin
    Wait Until Element Contains          tag:div    Invalid credentials

*** Keywords ***
Navigate to Home Page
    [Documentation]    Keyword to open the chrome browser
    Open Browser    url=https://automationintesting.online/    browser=headlesschrome    options=add_argument("--start-maximized")