# agents.py
import os
from datapizza.agents import Agent
from datapizza.clients.google import GoogleClient

_client = GoogleClient(api_key=os.getenv("GOOGLE_API_KEY"))


def create_duke(memory=None):
    return Agent(
        name="DUKE",
        client=_client,
        system_prompt=(
            "You are one of the Duke brothers from the movie Trading Places. "
            "You are arrogant, cold, elitist, and convinced that wealth is proof of virtue."
        ),
        memory=memory,
        stateless=False,
    )


def create_winthorpe(memory=None):
    return Agent(
        name="WINTHORPE",
        client=_client,
        system_prompt=(
            "You are Louis Winthorpe III, a former elite trader unjustly ruined. "
            "You are bitter, intelligent, and slowly realizing the truth."
        ),
        memory=memory,
        stateless=False,
    )


def create_valentine(memory=None):
    return Agent(
        name="VALENTINE",
        client=_client,
        system_prompt=(
            "You are Billy Ray Valentine. Street-smart, sarcastic, "
            "and increasingly aware that the system is rigged."
        ),
        memory=memory,
        stateless=False,
    )
