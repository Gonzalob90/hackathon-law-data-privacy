import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(
        self,
        system_prompt,
        base_url=None,
        model="gpt-4o",
        temperature=0,
    ):
        api_key = os.getenv("TOGETHER_API_KEY")
        if base_url:
            if api_key:
                self.client = OpenAI(base_url=base_url, api_key=api_key)
            else:
                self.client = OpenAI(base_url=base_url)
        else:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        system_message = {"role": "system", "content": system_prompt}
        self.messages = [system_message]
        self.usage = [None]
        self.model = model
        self.temperature = temperature

    def set_system_prompt(self, new_prompt):
        self.messages[0]["content"] = new_prompt

    def add_message(self, content, role="user", name=None):
        message = {"role": role, "content": content}
        if name is not None:
            message["name"] = name
        self.messages.append(message)
        self.usage.append(None)
        return message

    def send_message(
        self,
        content,
        role="user",
        name=None,
    ):
        message = {"role": role, "content": content}
        if name is not None:
            message["name"] = name
        response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages + [message],
                temperature=self.temperature
            )
        as_dict = response.model_dump(exclude_unset=True)
        response_message = as_dict["choices"][0]["message"]
        self.messages.append(message)
        self.usage.append(None)
        self.messages.append(response_message)
        self.usage.append(as_dict["usage"])
        return response_message

    def reset_history(self):
        self.messages = [self.messages[0]]