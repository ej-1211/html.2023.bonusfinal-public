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


# response_A = """
# Agent-A: "Closing statements:

# 1. Near-Death Experiences: While near-death experiences may have alternative explanations, the consistent elements reported across cultures suggest the possibility of transcendent experiences that point towards an afterlife.

# 2. Philosophical Arguments: Philosophical discussions provide a foundation for contemplating the existence of an afterlife, acknowledging that while conclusive proof may be elusive, reasoned exploration expands our understanding of the possibilities of an afterlife beyond empirical evidence.

# 3. Scientific Evidence: While scientific research operates within empirical boundaries, the existence of anomalies and emerging understandings highlights the need for open-mindedness and continued exploration to expand our understanding of the afterlife.

# 4. Skepticism and Critiques: Skepticism promotes critical thinking and rigorous evaluation, which I advocate for. However, maintaining a balance between skepticism and open-mindedness allows for a comprehensive examination of evidence and arguments surrounding the existence of an afterlife.

# 5. Cultural Perspectives: Cultural beliefs offer insights into human experience and the afterlife, reflecting our shared yearning for meaning and continuity. While cultural perspectives may not be empirical evidence, they contribute to the wider understanding of the afterlife.

# In conclusion, through the consideration of near-death experiences, philosophical reasoning, scientific exploration, skepticism, and cultural perspectives, I assert that the existence of an afterlife warrants further examination and encourages an open dialogue that embraces diverse perspectives and an ongoing pursuit of knowledge."
# """

# response_B = """
# Agent-B: "Conclusions on the five debate topics:

# 1. Near-Death Experiences: Although near-death experiences share common elements, their subjective nature and alternative explanations caution against using them as conclusive evidence for an afterlife.
# 2. Philosophical Arguments: While philosophical discussions provide insights, they remain speculative and subjective, lacking empirical proof of the existence of an afterlife.
# 3. Scientific Evidence: The lack of conclusive scientific evidence limits its support for the existence of an afterlife, as the current understanding of the natural world does not align with supernatural claims.
# 4. Skepticism and Critiques: Skepticism is vital for critical thinking, requiring careful evaluation of evidence and logical reasoning to maintain an intellectually honest approach to the debate.
# 5. Cultural Perspectives: Cultural beliefs provide insights into human experiences and aspirations but do not provide objective evidence for the existence of an afterlife due to their subjective nature and varying cultural influences.

# Closing Statement:
# In conclusion, while the subject of the afterlife is profound and captivating, the arguments presented in opposition highlight the need for rigorous evidence, logical reasoning, and skepticism. By critically evaluating near-death experiences, philosophical reasoning, scientific evidence, skepticism, and cultural perspectives, we can foster a comprehensive and balanced approach to understanding the concept of an afterlife. Such nuanced explorati
# """

# import csv

# # Function to parse responses
# def parse_response(response):
#     # Split the response into points
#     points = response.split('\n')
#     # remove empty lines
#     points = [point for point in points if point != '']
#     # keep the data that starts with a number
#     content = [point for point in points if point[0].isdigit()]
#     # Extract the main content from each point using the colon
#     main_content = [point.split(': ', 1)[-1] for point in content]
#     # Store the topic as well
#     topics = [point.split(': ', 1)[0] for point in content]
#     # remove the number and the dot in the topic
#     topics = [topic[3:] for topic in topics]
#     # add the conclusion base on the last point in points
#     topics.append("Conclusion")    
#     conclusion = points[-1]
#     main_content.append(conclusion)

#     if len(topics) != 6:
#         print("Error: the number of topics is not 5+1.")
#         exit()
#         return None
#     print(topics)

#     # Store the data in a dictionary
#     data = dict(zip(topics, main_content))
#     return data


# A = parse_response(response_A)
# B = parse_response(response_B)

# # conbine A and B base on the topic
# data_ = {}
# final = [['topic', 'Agent-A', 'Agent-B']]
# for topic in A:
#     data_[topic] = [A[topic], B[topic]]
#     final.append([topic, A[topic], B[topic]])


# # save the data
# with open('final.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(final)


response = """Agent-A: "As Agent A, I do not agree. I will advocate in favor of the issue with a strong argument. I will gather evidence and present it in a logical and persuasive manner. My argument strength is rated at 0.8, indicating a solid position in support of the subject."""

if 'I agree' in response:
    print('yes')