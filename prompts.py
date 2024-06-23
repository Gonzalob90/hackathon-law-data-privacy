# Content Prompt

ADVISER_SYSTEM_PROMPT = """You are helpful GDPR advisor assistant"""


# contact details
CHECK_CONTACT_PROMPT = """Provide a Yes or No response based on whether the following notification letter contains contact details. 
For clarity, contact details should contain at least an email address. 
This is the notification letter:

{document}

RESPONSE:"""

# has consequences of breach
CHECK_CONSEQUENCES_PROMPT = """Your task is to only respond Yes or No on whether the notification letter provides a description of the likely consequences of the data breach. 
For clarity, the response should be Yes if the letter states that the consequences of the data breach could be the possible disclosure of some of the user's personal data or reporting the incident to the police. However, you should respond No if only the type of data category is provided. 
This is the notification letter:

{document}

RESPONSE:"""

# measures taken by the Data controller
CHECK_MEASURES_PROMPT = """Your task is to provide a Yes or No response to the notification letter on whether the letter contains the measures taken to address the personal data breach. 
For example, this could be reporting the incident to the police. 
This the notification letter:

{document}

RESPONSE:"""


# worty of being compliant with GDPR
CHECK_COMPLIANCE_PROMPT = """Your task is to only respond Yes or No on whether the notification letter is worth pursuing further. 
For clarity, if the notification letter states that the user's details are not affected then the response should be No. If the prompt displays that the personal data compromised are special categories of data defined in the GDPR then the response should be Yes. 
This is the notification letter:

{document}

RESPONSE:"""