*** Settings ***
Library           testCh_report.py

*** Variables ***
${COLLECTION_PATH}    API\FakeRESTApi.Web V1.postman_collection.json
${ENVIRONMENT_PATH}    API\FakeRestAPI.postman_environment.json

*** Test Cases ***
Execute Postman Collection Using Newman
    [Documentation]    Runs a Postman collection using Newman and generates an json report.
    ${stdout}    ${stderr}    ${retcode}=    Run Newman    ${COLLECTION_PATH}    ${ENVIRONMENT_PATH}
    Log    "STDOUT: ${stdout}"
    Log    "STDERR: ${stderr}"
    Run Keyword If    ${retcode} != 0    Log    Test completed with errors, check STDOUT and STDERR for details.
    Log    Newman run completed Check the JSON report at POC_Robot_Newman\\JSON\\report.json
