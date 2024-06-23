"""
advisor.py
"""

from llm_client import LLMClient
from typing import Literal

import prompts
import const

llm_client_advisor = LLMClient(system_prompt=prompts.ADVISER_SYSTEM_PROMPT,
                               model="gpt-4")


class Adviser:

    def __init__(self):
        self.llm_client = llm_client_advisor

    def get_gdpr_checks(self, document):
        
        # Run in sequence
        print('run prompt: contact details')
        response_contact = self.run_gdpr_check(document, "contact")

        print('run prompt: consequences')
        response_consequences = self.run_gdpr_check(document, "consequences")

        print('run prompt: measures')
        response_measures = self.run_gdpr_check(document, "measures")

        print('run prompt: compliance')
        response_compliance = self.run_gdpr_check(document, "compliance")

        # contact details
        if response_contact == "yes":
            response_contact = const.RESPONSE_YES_CONTACT_DETAILS
        elif response_contact == "no":
            response_contact = const.RESPONSE_NO_CONTACT_DETAILS
        else:
            response_contact = "No information about contact details"

        # consequences
        if response_consequences == "yes":
            response_consequences = const.RESPONSE_YES_CONSEQUENCES
        elif response_consequences == "no":
            response_consequences = const.RESPONSE_NO_CONSEQUENCES
        else:
            response_consequences = "No information about consequences"
        
        # measures
        if response_measures == "yes":
            response_measures = const.RESPONSE_YES_MEASURES
        elif response_measures == "no":
            response_measures = const.RESPONSE_NO_MEASURES
        else:
            response_measures = "No information about measures"
        
        # compliance
        if response_compliance == "yes":
            response_compliance = const.RESPONSE_YES_COMPLIANCE
        elif response_compliance == "no":
            response_compliance = const.RESPONSE_NO_COMPLIANCE
        else:
            response_compliance = "No information about compliance"

        # Prepare a response concatenation:
        response = f"Initial steps: \n\n- {response_contact}\n\n- {response_consequences}\n\n- {response_measures}\n\n\n\nOverall judgement:\n\n- {response_compliance}"
        return response


    def run_gdpr_check(self, document: str, check_type:Literal["contact", "consequences", "measures", "compliance"]):
        
        check_gdpr_prompt = self.get_prompt(document=document, check_type=check_type)
        response = self.llm_client.send_message(check_gdpr_prompt)
        self.llm_client.reset_history()

        # check that response is not empty and only yes/no response
        if response["content"] == "":
            return "No response"
        elif response["content"].lower().strip() not in ["yes", "no"]:
            return "No response"
        
        print(response["content"].lower().strip())
        return response["content"].lower().strip()

    def generate_email(self, content):

        generate_email_prompt = prompts.CONTENT_PROMPT.format(content=content)
        response = self.llm_client.send_message(generate_email_prompt)
        self.llm_client.reset_history()
        return response["content"]
    
    def get_prompt(self, document:str, check_type:Literal["contact", "consequences", "measures", "compliance"]):

        if check_type not in ["contact", "consequences", "measures", "compliance"]:
            raise ValueError("Invalid check type")
        
        if check_type == "contact":
            check_gdpr_prompt = prompts.CHECK_CONTACT_PROMPT.format(document=document)
        elif check_type == "consequences":
            check_gdpr_prompt = prompts.CHECK_CONSEQUENCES_PROMPT.format(document=document)
        elif check_type == "measures":
            check_gdpr_prompt = prompts.CHECK_MEASURES_PROMPT.format(document=document)
        elif check_type == "compliance":
            check_gdpr_prompt = prompts.CHECK_COMPLIANCE_PROMPT.format(document=document)

        return check_gdpr_prompt