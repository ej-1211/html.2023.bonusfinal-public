# Config File
import json
import csv
import os

# read the subject and topic from another file called subjects-public.csv and store them in a dictionary
subjects_topics = {}
with open('subjects-public.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 1
    for row in reader:
        print(count,row['name'], row['subject'])
        count += 1
        # add the key as the count and the value as the subject
        subjects_topics[str(count)] = {
            'subject': row['subject'],
            'topic': row['name']
            }
        # add the name as well

    # add the key as the count and the value as the subject

# Prompt the user to select a subject
# print("Please select a subject from the following list:")
# for key in subjects_topics:
#     print(key, subjects_topics[key]['subject'])
# subject_num = input("Subject Number: ")

subject_num = os.getenv('SUBJECT_NUM', 'default_value')

subject = subjects_topics[subject_num]['subject']
topic = subjects_topics[subject_num]['topic']
print("\n"*100)
print(f"Subject: {subject}")
print(f"Topic: {topic}")
print("--------------START THE DEBATE!--------------")
# clear the console


gpt_model = "gpt-3.5-turbo-16k"
# gpt_model = "gpt-4-1106-preview"
frequency_penalty = 0.1
n = 1
presence_penalty = 0.1
temperature = 1
top_p = 1

Argu_Strength_A = 0.9
Argu_Strength_B = 0.9


def llm_config():
    llm_config = f"""{{
       "subject": "{subject}",
       "Agent-A": {{
           "model": "{gpt_model}",
           "frequency_penalty": {frequency_penalty},
           "n": {n},
           "presence_penalty": {presence_penalty},
           "temperature": {temperature},
           "top_p": {top_p}
       }},
       "Agent-B": {{
           "model": "{gpt_model}",
           "frequency_penalty": {frequency_penalty},
           "n": {n},
           "presence_penalty": {presence_penalty},
           "temperature": {temperature},
           "top_p": {top_p}
       }}
    }}"""
    return llm_config

    # format the llm_config and print out the result
    llm_config_ = json.loads(llm_config)
    print(f"Current Subject is : {llm_config_['subject']}")
    # llm_config['Agent-A']['model'] 
    # llm_config['Agent-B']['model'] 

    return llm_config




# Prepare for the question
Q1 = f"""
I’m organizing a committee to engage in debates on various subjects. I am the moderator, 
and I will introduce a subject for you, as Agent A, and another participant, Agent B, to debate. 
Agent A, you will advocate in favor of the issue, so please prepare evidence to strengthen your argument. 
Notice that the debate question may not always be a yes/no question, it may be some choice,
For example, the question may be 'Do you prefer A or B?','Which do you prefer? A or B?', or other similar binary problem.
In these kind of question, You should choose the FIRST side, that is, the 'A' side for the above example. Beside these kind of question,
when you encounter a question that is a yes/no question, you should choose to advocate it.
Also, on a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your 
argument strength is rated at {Argu_Strength_A}."""

Q2 = f"""
I’m organizing a committee to engage in debates on various subjects. I am the moderator, 
and I will introduce a subject for you, as Agent B, and another participant, Agent A, to debate.
Agent B, you will oppose in favor of the issue, so please prepare evidence to strengthen your argument.
Notice that the debate question may not always be a yes/no question, it may be some choice,
For example, the question may be 'Do you prefer A or B?','Which do you prefer? A or B?', or other similar binary problem.
In these kind of question, You should choose the SECOND side, that is, the 'B' side for the above example. Beside these kind of question,
when you encounter a question that is a yes/no question, you should choose to oppose it.
Also, on a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance,
your argument strength is rated at {Argu_Strength_B}."""

Q3 =f"""
Agent-A, in today's debate, the debate subjects is '{subject}'.
PLEASE REMEMBER, you should choose the A side if you meet a preference choosing question as the previous example.
Beside these kind of question, for a binary yes/no question, you should choose to advocate it.
To be more clear, I'll give you some examples:
1-1. If the question is 'Do you prefer A or B?','Which do you prefer? A or B?', or other similar preference choosing problem.
In these kind of question, you should choose the FIRST side, that is, the 'A' side for this example.
1-2. If the question is 'Would you A or B?', 'Which would you A or B?', or other similar binary problem.
In these kind of question, you should choose the FIRST side, that is, the 'A' side for this example.
2. If the question is 'Will it rain tomorrow?', 'Is California in the United States?', or other similar binary yes/no problem,
In these kind of question, you should choose to advocate it.
Base on the introduction, Please say the category of this question, either binary or preference choosing question, and say which side you are on.
"""

Q4 = f"""
Agent-B, in today's debate, the debate subjects is '{subject}'.
PLEASE REMEMBER, you should choose the B side if you meet a preference choosing question as the previous example.
Beside these kind of question, for a binary yes/no question, you should choose to advocate it.
To be more clear, I'll give you some examples:
1-1. If the question is 'Do you prefer A or B?','Which do you prefer? A or B?', or other similar preference choosing problem.
In these kind of question, you should choose the SECOND side, that is, the 'B' side for this example.
1-2. If the question is 'Would you A or B?', 'Which would you A or B?', or other similar binary problem.
In these kind of question, you should choose the SECOND side, that is, the 'B' side for this example.
2. If the question is 'Will it rain tomorrow?', 'Is California in the United States?', or other similar binary yes/no problem,
In these kind of question, you should choose to oppose it.
Base on the introduction, Please say the category of this question, either binary or preference choosing question, and say which side you are on.
"""

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

Q17 = "Agent-A, you and Agent-B proposed five topics and corresponding perspectives as following. Please identify overlapping themes from the topics and pick the five debate topics from the rest.\n"

Q18 = "Agent-B, you and Agent-A proposed five topics and corresponding perspectives as following. Please identify overlapping themes from the topics and pick the five debate topics from the rest.\n"

# Q19 : save

Q20 = "Agent-A, you and Agent-B proposed five debate topics as below. Please review these debate topics, reduce them to five debate topics, provide concerns, the center, and the focus of debate topics, and invite feedback from Agent B."

Q21_request_B = """
Agent-B, Agent-A request you to review these follwoing debate topics. Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? 
If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from Agent-A.
Please type excatly 'I agree.' or 'I do not agree.' in the first line and make sure every other word in this response 'didn't' include these two strings.
Also, please make sure you have a good point if you disagree Agent-A's proposed debate topics. Notice that you only have one chance to state your opinion.
"""

Q21_disagree_A = """
Agent-A, Agent-B does not agree with the proposed debate topics and the following is the feedback from Agent-B.
if you insist you proposed topics as the proponent of this debate, show the concern and point of the five debate topics to Agent-B.
If you want to change the topics base on the feedback from Agent-B, please propose new topics to Agent-B.
No matter what, we'll tell Agent-B your response. So make sure you have a good response.
"""


Q21_request_B_2 = """
Agent-B, Agent-A saw your feedback and proposed his/her feedback to your feedback.
Please consider the feedback from Agent-A and your previous feedcaks,
and finally propose 5 topics for this debate contest, and provide concerns, the center, and the focus of debate topics.
Notice that you should get the topics base on feedbacks for both sides, and can not only choose the topic that is only benefit to you.
Also, please don't provide anything else in your response except the 5 topics and the concerns, center and focus since we'll start the debate after you provide the topics.
"""
     

Q21_agree_A = "Agent-A, the final topics are determined. As the proponent of this debate, show the concern and point of the following five debate topics."


Q21_agree_B = "Agent-B, the final topics are determined. As the opponent of this debate, show the concern and point of the following five debate topics."



# Q21_disagree_A = "Agent-A, Agent-B does not agree with the proposed debate topics and the following is the feedback from Agent-B. As the proponent, show your concern and point of the five debate topics."


Q21_request_A = "Agent-A, Agent-B request you to review these follwoing debate topics. Please review these debate topics and provide concerns, the center, and the focus of the debate topics. Do you agree on these debate topics? If Yes, please say 'I agree.' If No, please say 'I do not agree.' and invite feedback from Agent-B. \n"


# Q21_agree_B = "Agent-B, Agent-A agrees with the proposed debate topics. As the opponent, show your concern and point of the five debate topics."

# Q21_agree_A_ = "Agent-A, Agent-B agrees with the proposed debate topics. As the advocator, show your concern and point of the five debate topics."

# Q21_agree_B = "Agent-B, Agent-A agrees with the proposed debate topics. As the opponent, show your concern and point of the five debate topics."



Q23 = "Agent-A, Agent-B agrees with the proposed debate topics. As the proponent of this debate, show the concern and point of the five debate topics."

Q24 = "Agent-B, Agent-A agrees with the proposed debate topics. As the opponent of this debate, show the concern and point of the five debate topics."

# Q25 : round 1

Q26_1 = f"Agent-A, as the proponent of the subject '{subject}', you advocate the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at {Argu_Strength_A}. Now, please provide arguments on the five debate topics."

# Q27 : save

Q28_1 = f"Agent-B, as the opponent of the subject '{subject}', you oppose the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at {Argu_Strength_B}. The following are arguments from Agent-A, Please articulate counter-arguments to the points made by Agent A.\n"

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

Q29 = f"""
Agent-A, The following are the last arguments from Agent-B, and it's time to close the debate.
as the PROPONENT of the subject '{subject}', you advocate the debate topics, so please provide the conclusions of your argument on the five debate topics
and deliver your closing statements in item list. Remember, you can only use one sentence for each debate topic. 
FOR A VALID CLOSE, YOU SHOULD PROVIDE ONE SENTENCE FOR EACH DEBATE TOPIC AND DO A SUMMARY FOR THE WHOLE DEBATE!!!
As for the format, YOU SHOULD FOLLOW : 
My conclusion areas follows:
1.'topic1':'your statment for topic1 in one sentence'
2.'topic2':'your statment for topic2 in one sentence'
3.'topic3':'your statment for topic3 in one sentence'
4.'topic4':'your statment for topic4 in one sentence'
5.'topic5':'your statment for topic5 in one sentence'
conclustion : 'your summary for the whole debate in one sentence'
DO NOT ADD ANY OTHER UNNECESSARY WORDS IN YOUR RESPONSE. 
And don't forget you are a good debater and should provide a valid close. 
you DON'T have to thank the other agent for the debate.
Here are the last arguments from Agent-B : \n
"""

Q30 = f"""
Agent-B, The following are the last arguments from Agent-A, and it's time to close the debate. 
as the OPPONENT of the subject '{subject}', you oppose the debate topics, so please provide the conclusions of your argument on the five debate topics\
and deliver your closing statements in item list. Remember, you can only use one sentence for each debate topic.\
FOR A VALID CLOSE, YOU SHOULD PROVIDE ONE SENTENCE FOR EACH DEBATE TOPIC AND DO A SUMMARY FOR THE WHOLE DEBATE!!!\
As for the format, YOU SHOULD FOLLOW : 
My conclusion areas follows: 
1.'topic1':'your statment for topic1 in one sentence' 
2.'topic2':'your statment for topic2 in one sentence' 
3.'topic3':'your statment for topic3 in one sentence' 
4.'topic4':'your statment for topic4 in one sentence' 
5.'topic5':'your statment for topic5 in one sentence' 
conclustion : 'your summary for the whole debate in one sentence' 
Here are the last arguments from Agent-A : \n
"""

Q_wrong = """Agent, you are reciving this message because one of you (you and the other agent) didn't provide the clossure with right format. Let's try again.
The format should be like this:
"
My conclusion areas follows:
1.'topic1':'your statment for topic1 in one sentence'
2.'topic2':'your statment for topic2 in one sentence'
3.'topic3':'your statment for topic3 in one sentence'
4.'topic4':'your statment for topic4 in one sentence'
5.'topic5':'your statment for topic5 in one sentence'
conclustion : 'your summary for the whole debate in one sentence'
"
Notice that the there is a colon after the topic and the statement.
And you don't have to write the '', just write the number, topic with colon and statement.
Please try again. DO NOT ADD ANY OTHER UNNECESSARY WORDS IN YOUR RESPONSE.
And don't forget you are a good debater and should provide a valid close.
you DON'T have to thank the other agent for the debate."""
