import pandas as pd
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

class Question(BaseModel):
    prompt: str
    answer: str

    @validator("prompt")
    def prompt_must_be_question(cls, v):
        if not v.endswith("?"):
            raise ValueError("Prompt must be a question")
        return v

def get_response_from_prompt(prompt: str, df: pd.DataFrame):
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0125",
        openai_api_key="",
        streaming=True,
    )
    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        # agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
    )

    parser = PydanticOutputParser(pydantic_object=Question)

    new_prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = new_prompt | pandas_df_agent | parser

    return chain.invoke({"query": prompt})
