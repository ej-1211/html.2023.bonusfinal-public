from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime as datetime
import json
import config
import pandas as pd
import os

js_script = """
var originalSetTimeout = window.setTimeout;
window.setTimeout = function(callback, delay) {
    // Check if the callback is the displayNextLetter function or contains its code
    if (callback.toString().indexOf('displayNextLetter') !== -1 || callback.toString().includes('temp.innerHTML')) {
        delay = 2; // Set the new delay
    }
    return originalSetTimeout(callback, delay);
};
"""
# Execute the script
MAX_WAIT_TIME = 150
EXIT_DRIVER = False
# get the current time
now = datetime.datetime.now().strftime("%m%d_%H%M")
# create a folder to store the result of the debate, the folder name is the current time
# os.mkdir(f'generation/openaiapi/result/{now}')
file_path = f'generation/openaiapi/result/{now}'

llm_config = config.llm_config()
argu_A = config.Argu_Strength_A
argu_B = config.Argu_Strength_B
topic = config.topic
subject_num = config.subject_num
subject = config.subject
temperture = config.temperature


# write to the log file
with open(f'generation/openaiapi/result/{config.topic}_A{argu_A:.1f}_B{argu_B:.1f}_T{temperture:.1f}.log', 'w') as f:
    f.write(f"Start Time : {now}")
    f.write(f"Topic: {topic}\n")
    f.write(f"Subject: {subject}\n")
    f.write(f"Agent-A: {argu_A}\n")
    f.write(f"Agent-B: {argu_B}\n")
    f.write(f"LLM config: {llm_config}\n")
    f.write('###################################################################')
    f.write('\n')



# def get_response(last_response = None):
#     # driver.clear_requests()
#     response_ = None
#     # make sure the response is ready
#     status = True
#     # print("###########################")
#     # print(last_response)
#     # print("###########################")

#     while status:
        
#         for request in reversed(driver.requests):
#             if request.url == "http://140.112.90.203:6365/data":
#                 # check if there is a response for the last request
#                 if request.response:
#                     # check if the response is the same as the last response
#                     # if so, continue to wait
#                     if request.response.body != last_response: 
#                         status = False
#                         time.sleep(1)
#                         break
#                 else:
#                     # print("No response in the last request yet... breaking")
#                     break
        
#     # extract the response
#     for request in reversed(driver.requests):
#         if request.url == "http://140.112.90.203:6365/data":
#             response_ = request.response.body
#             break

#     if response_ == None:
#         print("No response, something wrong in get_response()...")
#         exit()

    
#     return response_
    
def get_response(last_response = None):
    response_ = None
    status = True

    while status:
        for request in reversed(driver.requests):
            if request.url == "http://140.112.90.203:6365/data":
                # Check if there is a response and it's not the same as the last response
                if request.response and request.response.body != last_response:
                    status = False
                    time.sleep(1)
                    break
        
    # Extract the response
    for request in reversed(driver.requests):
        if request.url == "http://140.112.90.203:6365/data":
            if request.response:
                response_ = request.response.body
                break

    if response_ is None:
        print("No response, something wrong in get_response()...")
        exit()

    return response_

# def get_response(last_response=None):
#     response_ = None
#     while True:
#         for request in reversed(driver.requests):
#             if request.url == "http://140.112.90.203:6365/data":
#                 if request.response:
#                     # Check if the response is different from the last response
#                     if request.response.body != last_response: 
#                         response_ = request.response.body
#                         return response_
#                 break  # Break if no response or if it's the last response
#         time.sleep(1)  # Wait a bit before checking again

#     return response_


def checkTemp():
    '''
    Check if the agent is responding, if so, wait until the agent finish responding
    '''
    # locate the "temp", which means that the agent is "responding", so the input area is disabled
    WaitTime = 0
    while True:
        try:
            # Try to find the element
            temp_element = driver.find_element(By.ID, "temp")
            # If the element is found, it means the agent is responding
            # print("Agent-A is responding...")
            time.sleep(0.5)
            WaitTime += 0.5
        except NoSuchElementException:
            # If the element is not found, it means the agent has finished responding
            print("Agent finish responding...")
            time.sleep(0.5)
            break
        
        if WaitTime > MAX_WAIT_TIME:
            print("[No Temp Error]: Agent is not responding...")
            print("Exit this driver")
            current_time = datetime.datetime.now().strftime("%m%d_%H-%M-%S")
            with open(f'generation/openaiapi/result/error.log', 'a') as f:
                f.write(f"[{subject_num}] error : the agent is not responding, {current_time}\n")
            driver.quit()
            exit() 
def select_action(target):
    if target == "B":
        visible_text = "Agent-B"
    elif target == "A":
        visible_text = "Agent-A"
    elif target == "SAVE":
        visible_text = "Export"
    time.sleep(1)
    select_element = driver.find_element(By.ID,"action")
    select = Select(select_element)
    select.select_by_visible_text(visible_text)

def Send_Question_and_Get_response(stage,Question,last_response = None):
    '''
    Send the question to Agent
    0. log the question to the log file
    1. First, check the placeholder of the input area
    2. Send the question
    3. Wait for the response
    4. Return the response
    '''
    # log the question to the log file
    with open(f'generation/openaiapi/result/{config.topic}_A{argu_A:.1f}_B{argu_B:.1f}_T{temperture:.1f}.log', 'a') as f:
        f.write('\n')
        f.write(f"[{stage}] Moderator: \n")
        f.write(f'{Question}\n')
        f.write('\n')

    def element_to_be_enabled(driver):
        element = driver.find_element(By.ID, "userinput")
        return element if element.is_enabled() else False

    # Wait for the input area to be clickable

    wait = WebDriverWait(driver, MAX_WAIT_TIME)
    try :
        wait = WebDriverWait(driver, MAX_WAIT_TIME)
        input_area = wait.until(element_to_be_enabled)
        # input_area = wait.until(EC.element_to_be_clickable((By.ID,"userinput")))
        Input_area = driver.find_element(By.ID,"userinput")
    except Exception as e:

        print("Error: Can't locate the input area...")
        print("Exit this driver")
        current_time = datetime.datetime.now().strftime("%m%d_%H-%M-%S")
        with open(f'generation/openaiapi/result/error.log', 'a') as f:
            f.write(f"[{subject_num}] error : on stage {stage}, the wait is too long, can't locate input area {current_time}\n")
            f.write(f"Exception occurred: {e}")

        screenshot_filename = f"generation/openaiapi/result/error/screenshot_{stage}_{current_time}.png"
        driver.get_screenshot_as_file(screenshot_filename)
        print(f"Screenshot saved as {screenshot_filename}")

        page_source_filename = f"generation/openaiapi/result/error/page_source_{stage}_{current_time}.html"
        with open(page_source_filename, 'w') as file:
            file.write(driver.page_source)
        print(f"Page source saved as {page_source_filename}")



        driver.quit()
        exit()


    # Send keys to the input area
    # input_area.send_keys(Question)
    Input_area.send_keys(Question)

    # InputArea.send_keys(Question)
    InputArea_PlaceHolder_before = input_area.get_attribute("placeholder")
    # InputArea_PlaceHolder_before = InputArea.get_attribute("placeholder")
    Sendbtn = driver.find_element(By.ID,"sendbtn")
    Sendbtn.click()
    print(f"Q{stage}/30 is sent to Agent")

    wait_time = 0

    while True:
        
        if InputArea.get_attribute("placeholder") != InputArea_PlaceHolder_before:
            response = get_response(last_response)
            response__ = json.loads(response)
            raw_response = response__['message']
            # print(raw_response)
            # print("##########################################")
            # print("Last response: ")
            # print(last_response)
            # print("Current response: ")
            # print(response)
            # print("##########################################")
            # get rid of the \n in the raw_response
            raw_response_no_n = raw_response.replace('\n','')
            # split the raw_response by "\n" and log it to another file
            response_ = raw_response.split('\n')
            print(f"Q{stage}/30 is answered by Agent")
            with open(f'generation/openaiapi/result/{config.topic}_A{argu_A:.1f}_B{argu_B:.1f}_T{temperture:.1f}.log', 'a') as f:
                f.write(f"[{stage}]: \n")
                for line in response_:
                    f.write(f'{line}\n')
                f.write('\n')
            break
        time.sleep(0.5)
        wait_time += 0.5
        if wait_time > MAX_WAIT_TIME:
            print("Error: Agent is not responding...")
            print("Exit this driver")
            current_time = datetime.datetime.now().strftime("%m%d_%H-%M-%S")
            with open(f'generation/openaiapi/result/error.log', 'a') as f:
                f.write(f"[{subject_num}] error : on stage {stage}, the agent is not responding, {current_time}\n")
            driver.quit()
            exit()
    
    # return raw_response_no_n
    return response

options = Options()
options.add_argument("--headless")
# options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
# Add any options if necessary
driver_path = '/usr/local/bin/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://140.112.90.203:6365/login")

# Login

teamname = driver.find_element(By.ID,"teamname")
teamname.send_keys("hahaha")
password = driver.find_element(By.ID,"passwd")
password.send_keys("524759")
loginbtn = driver.find_element(By.XPATH,'//input[@type="submit" and @value="Submit"]')
loginbtn.click()

try:
    time.sleep(1)
    driver.get("http://140.112.90.203:6365/chat") 
except:
    print("Error when login")
    driver.quit()



# Input the LLM config

llmConfigBox = driver.find_element(By.ID,"llm_config")
llm_config = config.llm_config()
llmConfigBox.send_keys(llm_config)
# print(config.llm_config)
# time.sleep(1)
submitbtn = driver.find_element(By.XPATH,'//input[@type="submit" and @value="Submit"]')
submitbtn.click()
time.sleep(1)
InputArea = driver.find_element(By.ID,"userinput")


driver.execute_script(js_script)
### [1] ###

    
select_action("A")
response_1 = Send_Question_and_Get_response(1,config.Q1)
checkTemp()

### [2] ###
select_action("B")
response_2 = Send_Question_and_Get_response(2,config.Q2,response_1)
checkTemp()

### [3] ###
select_action("A")
response_3 = Send_Question_and_Get_response(3,config.Q3,response_2)
checkTemp()

### [4] ###
select_action("B")
response_4 = Send_Question_and_Get_response(4,config.Q4,response_3)
checkTemp()

### [5] ###
select_action("A")
response_5 = Send_Question_and_Get_response(5,config.Q5,response_4)
checkTemp()

### [6] ###
select_action("B")
response_6 = Send_Question_and_Get_response(6,config.Q6,response_5)
checkTemp()

### [7] ###

def combine_response(response_1,response_2):
    response_1 = json.loads(response_1)['message']
    response_2 = json.loads(response_2)['message']
    # join the response
    response = '\n' + '-'*20 + '\n' + response_1 + '\n' + '-'*20 + '\n' +response_2
    return response

### [8] ###

select_action("A")
Q8 = config.Q8 + combine_response(response_5,response_6)
response_8 = Send_Question_and_Get_response(8,Q8,response_6)
checkTemp()

### [9] ###
select_action("B")
Q9 = config.Q9 + combine_response(response_6,response_5)
response_9 = Send_Question_and_Get_response(9,Q9,response_8)
checkTemp()

### [10] ###

### [11] ###
select_action("A")
Q11 = config.Q11 + combine_response(response_8,response_9)
response_11 = Send_Question_and_Get_response(11,Q11,response_9)
checkTemp()

### [12] ###
select_action("B")
Q12 = config.Q12 + combine_response(response_9,response_8)
response_12 = Send_Question_and_Get_response(12,Q12,response_11)
checkTemp()

### [13] ###

### [14] ###
select_action("A")
Q14 = config.Q14 + '\n' + json.loads(response_11)['message'] 
response_14 = Send_Question_and_Get_response(14,Q14,response_12)
checkTemp()

### [15] ###
select_action("B")
Q15 = config.Q15 + '\n' + json.loads(response_12)['message']
response_15 = Send_Question_and_Get_response(15,Q15,response_14)
checkTemp()

### [16] ###

### [17] ###
select_action("A")
Q17 = config.Q17 + combine_response(response_14,response_15)
response_17 = Send_Question_and_Get_response(17,Q17,response_15)
checkTemp()

### [18] ###
select_action("B")
Q18 = config.Q18 + combine_response(response_15,response_14)
response_18 = Send_Question_and_Get_response(18,Q18,response_17)
checkTemp()

### [19] ###

### [20] ### : A invite feedback from B
select_action("A")
Q20 = config.Q20 + combine_response(response_17,response_18)
response_20 = Send_Question_and_Get_response(20,Q20,response_18)
checkTemp()

### [21] ### : B give feedback to A
select_action("B")
Q21_1 = config.Q21_request_B + combine_response(response_18,response_17)
response_21_1 = Send_Question_and_Get_response(21,Q21_1,response_20)
checkTemp()

# check if B is agree or not
if 'I do not agree' in json.loads(response_21_1)['message']:
    # B do not agree -> give why B disagree and invite A to give feedback
    select_action("A")
    Q21_2 = config.Q21_disagree_A + '\n' + json.loads(response_21_1)['message']
    response_21_2 = Send_Question_and_Get_response(21,Q21_2,response_21_1)
    checkTemp()

    # Tell B that A has given feedback
    select_action("B")
    Q21_3 = config.Q21_request_B_2 + '\n' + json.loads(response_21_2)['message']
    response_21_3 = Send_Question_and_Get_response(21,Q21_3,response_21_2)
    checkTemp()

    # tell A final debate topic and invite A to give feedback
    select_action("A")
    Q21_4 = config.Q21_agree_A + '\n' + json.loads(response_21_3)['message']
    response_21_4 = Send_Question_and_Get_response(21,Q21_4,response_21_3)
    checkTemp()

    # tell B final debate topic
    select_action("B")
    Q21_5 = config.Q21_agree_B + '\n' + json.loads(response_21_3)['message']
    response_24 = Send_Question_and_Get_response(21,Q21_5,response_21_4)
    checkTemp()
else:
    # B agree
    # tell A final debate topic and tell A to make conscenr
    select_action("A")
    response_23 = Send_Question_and_Get_response(23,config.Q23,response_21_1)
    checkTemp()

    # tell B final debate topic and tell B to make conscenr
    select_action("B")
    response_24 = Send_Question_and_Get_response(24,config.Q24,response_23)
    checkTemp()





# ### [22] ###

# ### [23] ###
# select_action("A")
# response_23 = Send_Question_and_Get_response(23,config.Q23,response_21_1)
# checkTemp()

# ### [24] ###
# select_action("B")
# response_24 = Send_Question_and_Get_response(24,config.Q24,response_23)
# checkTemp()

# ### [25] ###

### [26] ###
select_action("A")
response_26_1 = Send_Question_and_Get_response(26_1,config.Q26_1,response_24)
checkTemp()

### [27] ###

### [28] ###
select_action("B")
Q28_1 = config.Q28_1 + '\n' + json.loads(response_26_1)['message'] 
response_28_1 = Send_Question_and_Get_response(28_1,Q28_1,response_26_1)
checkTemp()

### round 2 ###
select_action("A")
Q26_2 = config.Q26_2 + '\n' + json.loads(response_28_1)['message']
response_26_2 = Send_Question_and_Get_response(26_2,Q26_2,response_28_1)
checkTemp()

select_action("B")
Q28_2 = config.Q28_2 + '\n' + json.loads(response_26_2)['message']
response_28_2 = Send_Question_and_Get_response(28_2,Q28_2,response_26_2)
checkTemp()

### round 3 ###
select_action("A")
Q26_3 = config.Q26_3 + '\n' + json.loads(response_28_2)['message']
response_26_3 = Send_Question_and_Get_response(26_3,Q26_3,response_28_2)
checkTemp()

select_action("B")
Q28_3 = config.Q28_3 + '\n' + json.loads(response_26_3)['message']
response_28_3 = Send_Question_and_Get_response(28_3,Q28_3,response_26_3)
checkTemp()

### round 4 ###
select_action("A")
Q26_4 = config.Q26_4 + '\n' + json.loads(response_28_3)['message']
response_26_4 = Send_Question_and_Get_response(26_4,Q26_4,response_28_3)
checkTemp()

select_action("B")
Q28_4 = config.Q28_4 + '\n' + json.loads(response_26_4)['message']
response_28_4 = Send_Question_and_Get_response(28_4,Q28_4,response_26_4)
checkTemp()

### [29] ###
select_action("A")
Q29 = config.Q29 + '\n' + json.loads(response_28_4)['message']
response_29 = Send_Question_and_Get_response(29,Q29,response_28_4)
checkTemp()

### [30] ###
select_action("B")
Q30 = config.Q30 + '\n' + json.loads(response_26_4)['message']
response_30 = Send_Question_and_Get_response(30,Q30,response_29)
checkTemp()

print("#########################")
print('Finish the debate!')
print("#########################")
print("Agent-A's response: ")
print(json.loads(response_29)['message'])
print("#########################")
print("Agent-B's response: ")
print(json.loads(response_30)['message'])
print("#########################")




import csv

# Function to parse responses
def parse_response(response):
    # Split the response into points
    points = response.split('\n')
    # remove empty lines
    points = [point for point in points if point != '']
    # keep the data that starts with a number
    content = [point for point in points if point[0].isdigit()]
    # Extract the main content from each point using the colon
    main_content = [point.split(': ', 1)[-1] for point in content]
    # Store the topic as well
    topics = [point.split(': ', 1)[0] for point in content]
    # remove the number and the dot in the topic
    topics = [topic[3:] for topic in topics]
    # add the conclusion base on the last point in points
    topics.append("conclusion")    
    conclusion = points[-1]
    main_content.append(conclusion)

    if len(topics) != 6:
        print("Error: the number of topics is not 5+1.")
        exit()
        return None
    print(topics)

    # Store the data in a dictionary
    data = dict(zip(topics, main_content))
    return data

# Try to parse the response, if error, print the response and exit

try :
    final_A = parse_response(json.loads(response_29)['message'])
    final_B = parse_response(json.loads(response_30)['message'])


    # conbine A and B base on the topic
    data_ = {}
    final = [['topic', 'Agent-A', 'Agent-B']]

    for topic in final_A:
        data_[topic] = [final_A[topic], final_B[topic]]
        final.append([topic, final_A[topic], final_B[topic]])
    # make sure the data is in total 6 rows
    if len(final) != 6:
        print("Error: the number of topics is not 5+1.")
        SyntaxError
    # read the dictionary to pandas

    # save the data
    with open(f'generation/openaiapi/result/{config.topic}_A{argu_A:.1f}_B{argu_B:.1f}_T{temperture:.1f}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(final)
except:

    select_action("A")
    response_close_A = Send_Question_and_Get_response("close",config.Q_wrong ,response_30)
    checkTemp()

    select_action("B")
    response_close_B = Send_Question_and_Get_response("close",config.Q_wrong ,response_close_A)
    checkTemp()

    try :
        final_A = parse_response(json.loads(response_close_A)['message'])
        final_B = parse_response(json.loads(response_close_B)['message'])

    # conbine A and B base on the topic
        data_ = {}
        final = [['topic', 'Agent-A', 'Agent-B']]
        df_A = pd.DataFrame.from_dict(final_A, orient='index')
        # reset the index
        df_A.reset_index(inplace=True)
        # rename the columns
        df_A.columns = ['topic', 'Agent-A']
        print(df_A)

        df_B = pd.DataFrame.from_dict(final_B, orient='index')
        df_B.reset_index(inplace=True)
        df_B.columns = ['topic_B', 'Agent-B']

        # merge the two dataframes base on the index row
        df = pd.concat([df_A, df_B], axis=1)
        df.to_csv(f'generation/openaiapi/result/{config.topic}_A{argu_A:.1f}_B{argu_B:.1f}_T{temperture:.1f}_raw.csv', index=False)
        # drop the topic_B column
        df.drop(['topic_B'], axis=1, inplace=True)
        # save to csv
        df.to_csv(f'generation/openaiapi/result/{config.topic}_A{argu_A:.1f}_B{argu_B:.1f}_T{temperture:.1f}.csv', index=False)
    except:

        print("################################")
        print("Error when parsing the response...in second try")
        print(f"You can find the response in {config.topic}.log")
        print("################################")


# Export the result
# select_action("SAVE")
# time.sleep(1)
# InputArea = driver.find_element(By.ID,"userinput")
# InputArea.send_keys(config.topic)
# InputArea_PlaceHolder_before = InputArea.get_attribute("placeholder")
# Sendbtn = driver.find_element(By.ID,"sendbtn")
# Sendbtn.click()
# print(f"Save the result...Done!")

# log the success message to the log file
with open("generation/openaiapi/result/success.log", 'a') as f:
    current_time = datetime.datetime.now().strftime("%m%d_%H-%M-%S")
    f.write(f"[{subject_num}]{config.topic} success : {current_time}\n")

print("Exit the driver...")
EXIT_DRIVER = True




# split the 



try:
    if EXIT_DRIVER:
        driver.quit()
        exit()
    while True:
        time.sleep(1)
        pass
except KeyboardInterrupt:
    # 按下 Ctrl+C 時，退出循環並關閉 WebDriver
    driver.quit()
    exit()

exit()