import pandas as pd
from pandasai.llm import OpenAI
from pandasai import SmartDataframe


def get_response_from_prompt(openai_api_token: str, prompt: str, df: pd.DataFrame):
    llm = OpenAI(
        temperature=0,
        api_token=openai_api_token,
        model="gpt-3.5-turbo-0125",
    )
    smart_df = SmartDataframe(
        df,
        description="A dataframe with a collection of game reviews by a group of friends (crias)",
        config={"llm": llm, "verbose": True},
    )
    return smart_df.chat(prompt + " responda em português brasileiro")
