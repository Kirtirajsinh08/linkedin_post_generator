from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def Get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def GeneratePost(topic, length, language):
    prompt = GetPrompt(topic, length, language)
    response = llm.invoke(prompt)
    return response.content

def GetPrompt(topic, length, language):
    length_str = Get_length_str(length)
    
    # Base prompt (points 1–3)
    prompt = f"""Generate a LinkedIn Post using the below given information. No Preamble.
    1) Topic: {topic}
    2) Length: {length} ({length_str})
    3) Language: {language}"""

    # If examples exist → add point 4
    examples = few_shot.get_filtered_posts(length, language, topic)
    if len(examples) > 0:
        prompt += f"""
    4) Use the writing style as per the following examples."""
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"""\n\n     Example {i+1} : {post_text}"""
            if i == 1:  # limit to 2 examples
                break

    # Add Hinglish + emoji instructions always at the end
    prompt += f"""
    
    If the language is Hinglish then it means it is a mix of Hindi and English.
    The script for the generated post should always be in English.
    You are allowed to add some emojis related to the content of the post in between the content so that the content looks more attractive.
    """

    return prompt

if __name__ == "__main__":
    print(GetPrompt("Self Improvement", "Short", "English"))
    print('\n')
    print(GeneratePost("Self Improvement", "Short", "English"))
