from langchain_openai import OpenAI

llm = OpenAI(streaming=True)

# prompt = "Conte uma historia sobre aprendizado de máquina"

# print(llm.invoke(prompt)) // Responde a uma unica pergunta


# for trecho in llm.stream(prompt):
#     print(trecho, end = "")

from langchain.prompts import PromptTemplate


questions = [
    "",
    "O que é memoria ram?",
    "O que é cpu?",
    "",
]


def soma2():
    return 2


llm2 = OpenAI()

print(llm2.batch(questions))
