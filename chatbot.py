from msilib.schema import Class
import openai

openai.api_key = "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"
completion = openai.Completion()

#name1 = 'Bob'
#name2 = 'John'

class Chatbot :
    def __init__(self, userName, agentName):
        self.name1 = userName
        self.name2 = agentName

    def talk(self, input, keywords) : 
        append = ''
        for k in keywords.keys():
            append += ' ' + k
        prompt = f'{self.name1}:{input}{append}\n{self.name2}:'
        response = completion.create(
            prompt = prompt,engine = "davinci",
            stop = [f"{self.name1}:"],
            temperature = 0.1,
            top_p =1, best_of=1,
            max_tokens=50
        )
        answer = response.choices[0].text.strip().split(f"{self.name1}:", 1)[0].split(f"{self.name2}:", 1)[0]

        return answer

    def set_user_name(self, name):
        self.name1 = name

    def set_agent_name(self, name):
        self.name2 = name
