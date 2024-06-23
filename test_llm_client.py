from llm_client import LLMClient

llm_client = LLMClient("You're a helpful AI legal assistant", 
                       base_url='https://api.together.xyz/v1', 
                       model='meta-llama/Llama-3-8b-chat-hf', 
                       max_tokens=2048)

def generate_answer_no_context(llm_client, doc, q):
    '''Placeholder approach here - we are sending the question only, no document context'''
    answer = llm_client.send_message(q)
    return answer['content']


print(generate_answer_no_context(llm_client= llm_client, doc="", q='Tell me a joke'))