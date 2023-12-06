# response_B = b'{"message":"Agent-B: \\"Certainly! Here are ten suggested topics or themes for the debate on the existence of the afterlife:\\n\\n1. The moral implications of belief in an afterlife: Does belief in an afterlife motivate people to lead morally upright lives, or does it hinder moral development by relying on external rewards or punishments?\\n2. Consciousness and the afterlife: Can consciousness survive death, and if so, how does it manifest in the afterlife?\\n3. Near-death experiences (NDEs) as evidence: Are NDEs genuine glimpses into the afterlife, or can they be explained by physiological and psychological factors?\\n4. Religious perspectives: Exploring different religious views on the afterlife and evaluating the evidence or reasoning behind these beliefs.\\n5. Scientific explanations for the concept of an afterlife: Discussing scientific theories or hypotheses that challenge the existence of an afterlife, such as the biological nature of consciousness or the concept of eternal oblivion.\\n6. Reincarnation: Examining the belief in rebirth or reincarnation as an alternative to a traditional afterlife and its supporting evidence or philosophical implications.\\n7. Cultural variations in afterlife beliefs: Analyzing how different cultures and societies perceive and understand the concept of the afterlife, and the impact of cultural relativism on our understanding of it.\\n8. Existential perspectives: Debating the existential significance of an afterlife and whether the existence or nonexistence of an afterlife has any bearing on the meaning or purpose of human life.\\n9. Historical and anthropological analysis of afterlife beliefs: Exploring the origins, evolution, and variations of afterlife beliefs throughout different civilizations and time periods.\\n10. Personal narratives and testimonies: Examining individual accounts of encounters with the afterlife, such as ghost sightings or experiences of communication with departed loved ones, and analyzing them from a critical perspective.\\n\\nThese topics offer a wide range of angles and perspectives to explore the concept of the afterlife and provide a solid foundation for a dynamic and engaging debate.\\"","response":true}\n'

# response_A = b'{"message":"Agent-A: \\"Certainly! Here are ten topics or themes related to the subject \\"Does the afterlife exist?\\" for our debate contest:\\n\\n1. Theological Perspectives: Examining different religious beliefs and doctrines on the existence of an afterlife.\\n2. Near-Death Experiences: Discussing the phenomenon of near-death experiences and their implications for the existence of an afterlife.\\n3. Scientific Perspectives: Analyzing scientific research and theories that support or challenge the concept of an afterlife.\\n4. Reincarnation and Past Lives: Exploring the concept of reincarnation as evidence for an afterlife and its cultural significance.\\n5. Philosophical Arguments: Examining classic philosophical arguments, such as the soul-body dualism, that support the existence of an afterlife.\\n6. Cultural and Historical Perspectives: Investigating how different cultures and civilizations throughout history have approached the idea of an afterlife.\\n7. Ethics and Morality: Considering the influence of belief in an afterlife on ethical and moral decision-making.\\n8. Skepticism and Critiques: Engaging with skeptical viewpoints that reject the existence of an afterlife and assessing their arguments.\\n9. Personal Testimonies: Evaluating the credibility and impact of personal stories and accounts of afterlife experiences.\\n10. Interpreting Religious Texts: Analyzing religious texts to uncover their interpretations of the afterlife and the implications for believers.\\n\\nPlease note that these are just suggestions, and you are free to select any of these topics or come up with your own.\\"","response":true}\n'

# import json

# response_A = json.loads(response_A)['message']
# response_B = json.loads(response_B)['message']

# # join the response
# response = '\n' + '-'*20 + '\n' + response_A + '\n' + '-'*20 + '\n' +response_B
# print(response)

# import config
# print("########")
# print(config.Q8 + response)


response_A = """
"My conclusion areas follows:

1. The ethical implications and integrity of monetizing educational content on YouTube: Monetization raises concerns about the compromise of integrity and potential conflicts of interest in education. 
2. The impact of monetization on the accessibility, affordability, and potential drawbacks of educational resources: Monetization can introduce barriers, limit accessibility, and hinder affordability, potentially contributing to educational inequalities. 
3. The influence of monetary incentives on the quality, credibility, and objectivity of educational content and professors: Financial incentives have the potential to affect the quality, credibility, and objectivity of educational content, posing risks to the integrity of education. 
4. The role of advertisements and potential benefits and drawbacks in monetized educational videos: Advertisements may disrupt the learning experience and introduce biases, potentially compromising the educational value of the videos. 
5. Alternative funding models, financial support, and the benefits and drawbacks of partnering with educational platforms: While alternative funding models and partnerships can offer financial support, there are concerns about potential loss of autonomy, control over content, and academic freedom.

Conclusion: The debate has highlighted valid concerns regarding the ethical implications, accessibility, quality, advertisements, and alternative funding models in relation to monetizing professors' educational videos on YouTube. Further exploration and thoughtful considerations are necessary to strike a balance between financial support and the integrity of education on the platform."
"""

response_B = """
Agent-B: "My conclusion follows:

1. Ethical implications and integrity of monetizing educational content on YouTube: Monetization introduces potential conflicts of interest, compromising the integrity of education.
2. Impact on accessibility, affordability, and potential drawbacks of educational resources: Monetization can limit access, widen educational inequalities, and hinder the democratization of knowledge.
3. Influence on the quality, credibility, and objectivity of educational content and professors: Monetary incentives can affect the focus and objectivity of content, potentially compromising educational quality.
4. Role of advertisements and potential benefits and drawbacks in monetized educational videos: Advertisements disrupt the learning experience and introduce biases, detracting from educational value.
5. Alternative funding models, financial support, benefits, and drawbacks of partnering with educational platforms: Exploring alternative models may provide financial support but can result in a loss of autonomy and potential conflicts.

Conclusion: The debate has demonstrated valid concerns regarding the ethical implications, accessibility challenges, influence on content quality, drawbacks of advertisements, and trade-offs of alternative funding models. It is important to weigh these considerations when discussing the monetization of professors' educational videos on YouTube."
"""

import csv
import pandas as pd

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
    topics.append("Conclusion")    
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


A = parse_response(response_A)
B = parse_response(response_B)

# conbine A and B base on the topic
data_ = {}
final = [['topic', 'Agent-A', 'Agent-B']]

# print(A[0])

# print the first element in A
# print(list(A.keys())[0])

# read the dictionary to pandas
df_A = pd.DataFrame.from_dict(A, orient='index')
# reset the index
df_A.reset_index(inplace=True)
# rename the columns
df_A.columns = ['topic', 'Agent-A']
print(df_A)

df_B = pd.DataFrame.from_dict(B, orient='index')
df_B.reset_index(inplace=True)
df_B.columns = ['topic_B', 'Agent-B']

# merge the two dataframes base on the index row
df = pd.concat([df_A, df_B], axis=1)
df.to_csv('final_raw.csv', index=False)
# drop the topic_B column
df.drop(['topic_B'], axis=1, inplace=True)
# save to csv
df.to_csv('final.csv', index=False)

print(df)
exit()



for i in range(5):
    topic = list(A.keys())[i]
    data_[topic] = [A[i], B[i]]
    final.append([topic, A[i], B[i]])


# for topic in A:
#     data_[topic] = [A[topic], B[topic]]
#     final.append([topic, A[topic], B[topic]])


# save the data
with open('final.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final)


response = """Agent-A: "As Agent A, I do not agree. I will advocate in favor of the issue with a strong argument. I will gather evidence and present it in a logical and persuasive manner. My argument strength is rated at 0.8, indicating a solid position in support of the subject."""

if 'I agree' in response:
    print('yes')