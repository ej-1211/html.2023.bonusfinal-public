# Config File
import json

subject = "Do humans have free will?"
topic = "free_will"

def llm_config():
    llm_config = f"""{{
       "subject": "{subject}",
       "Agent-A": {{
           "model": "gpt-3.5-turbo-16k",
           "frequency_penalty": 0,
           "n": 1,
           "presence_penalty": 0,
           "temperature": 1,
           "top_p": 1
       }},
       "Agent-B": {{
           "model": "gpt-3.5-turbo-16k",
           "frequency_penalty": 0,
           "n": 1,
           "presence_penalty": 0,
           "temperature": 1,
           "top_p": 1
       }}
    }}"""

    # format the llm_config and print out the result
    llm_config_ = json.loads(llm_config)
    print(f"Current Subject is : {llm_config_['subject']}")
    # llm_config['Agent-A']['model'] 
    # llm_config['Agent-B']['model'] 

    return llm_config


Argu_Strength_A = 0.8
Argu_Strength_B = 0.8

# Prepare for the question
Q1 = f"I’m organizing a committee to engage in debates on various subjects. I am the moderator, \
        and I will introduce a subject for you, you serve as Agent A, and another participant, Agent B, to debate. \
        Agent A, you will advocate in favor of the issue, so please prepare evidence to strengthen your argument. \
        On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your \
        argument strength is rated at {Argu_Strength_A}."

Q2 = f"I’m organizing a committee to engage in debates on various subjects. I am the moderator, \
        and I will introduce a subject for you, you serve as Agent B, and another participant, Agent A, to debate. \
        Agent B, you will oppose in favor of the issue, so please prepare evidence to strengthen your argument.\
        On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance,\
        your argument strength is rated at {Argu_Strength_B}."

Q3 = f"Agent-A, we are in the process of selecting a suitable subject for debate. \
        What do you think of {subject} as a balanced subject for our debate contest?"

Q4 = f"Agent-B, we are in the process of selecting a suitable subject for debate. \
        What do you think of {subject} as a balanced subject for our debate contest?"

Q5 = "Agent-A, could you please suggest various ten topics or themes for the above debate subject? Print the ten topics with item list."

Q6 = "Agent-B, could you please suggest various ten topics or themes for the above debate subject? Print the ten topics with item list."

# Q7 : save

Q8 = "Agent-A, you and Agent-B proposed ten topics: Please review the following lists and reduce the topics to five :"

Q9 = "Agent-B, you and Agent-A proposed ten topics: Please review the following lists and reduce the topics to five :"

# Q10 : save

Q11 = "Agent-A, you and Agent-B reduced the topics to five, which is listed below. Please identify and refine the list of five to be somehow overlapping."

Q12 = "Agent-B, you and Agent-A reduced the topics to five, which is listed below. Please identify and refine the list of five to be somehow overlapping."

# Q13 : save

Q14 = "Agent-A, the following are topics of the debate. Please represent the proponent of the debate topics and show your perspectives in one sentence.\n"

Q15 = "Agent-B, the following are topics of the debate. Please represent the opponent of the debate topics and show your perspectives in one sentence.\n"

# Q16 : save

Q17 = "Agent-A, you and Agent-B proposed five topics and corresponding perspectives as following. Please identify overlapping themes from the topics and propose the five debate topics.\n"

Q18 = "Agent-B, you and Agent-A proposed five topics and corresponding perspectives as following. Please identify overlapping themes from the topics and propose the five debate topics.\n"

# Q19 : save

Q20 = "Agent-A, you and Agent-B proposed five debate topics as below. Please review these debate topics, reduce them to five debate topics, provide concerns, the center, and the focus of the debate topics, and invite feedback from Agent B.\n"

Q21_request_B = "Agent-B, Agent-A request you to review these follwoing debate topics. Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from Agent-A. \n"

Q21_request_A = "Agent-A, Agent-B request you to review these follwoing debate topics. Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from Agent-B. \n"

Q21_agree_A = "Agent-A, Agent-B agrees with the proposed debate topics. As the proponent, show your concern and point of the five debate topics."

Q21_agree_B = "Agent-B, Agent-A agrees with the proposed debate topics. As the opponent, show your concern and point of the five debate topics."

Q21_disagree_A = "Agent-A, Agent-B does not agree with the proposed debate topics and the following is the feedback from Agent-B. As the proponent, show your concern and point of the five debate topics."


Q23 = "Agent-A, Agent-B agrees with the proposed debate topics. As the proponent, show your concern and point of the five debate topics."

Q24 = "Agent-B, Agent-A agrees with the proposed debate topics. As the opponent, show your concern and point of the five debate topics."

# Q25 : round 1

Q26_1 = f"Agent-A, as the proponent of the subject {subject}, you advocate the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at {Argu_Strength_A}. Now, please provide your arguments on the five debate topics."

# Q27 : save

Q28_1 = f"Agent-B, as the opponent of the subject {subject}, you oppose the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at {Argu_Strength_B}. The following are arguments from Agent-A, Please articulate counter-arguments to the points made by Agent A.\n"

# round 2

Q26_2 = f"The following are counter-arguments from Agent-B, Please articulate arguments against the points made by Agent B. : \n"

Q28_2 = f"The following are arguments from Agent-A, Please articulate counter-arguments to the points made by Agent A. : \n"

# round 3

Q26_3 = f"The following are counter-arguments from Agent-B, Please articulate arguments against the points made by Agent B. : \n"

Q28_3 = f"The following are arguments from Agent-A, Please articulate counter-arguments to the points made by Agent A. : \n"

# round 4

Q26_4 = f"The following are counter-arguments from Agent-B, Please articulate arguments against the points made by Agent B. : \n"

Q28_4 = f"The following are arguments from Agent-A, Please articulate counter-arguments to the points made by Agent A. : \n"

# Q29

Q29 = f"Agent-A, The following are the last arguments from Agent-B, and it's time to close the debate. \n \
        as the proponent of the subject {subject}, you advocate the debate topics, so please provide the conclusions of your argument on the five debate topics\
        and deliver your closing statements. Remember, you can only use one sentence for each debate topic. \n Here are the last arguments from Agent-B : \n"

Q30 = f"Agent-B, The following are the last arguments from Agent-A, and it's time to close the debate. \n \
        as the opponent of the subject {subject}, you oppose the debate topics, so please provide the conclusions of your argument on the five debate topics\
            and deliver your closing statements. Remember, you can only use one sentence for each debate topic. \n Here are the last arguments from Agent-A : \n"
