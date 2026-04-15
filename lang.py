from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage


llm = ChatOllama(model='mistral',streaming=True,temperature=0.7)

history = []

while True:
    qstn = input('>>? ')

    history.append(HumanMessage(content=qstn))

    resp = ''

    cmd = qstn.strip().lower()

    if cmd in ['/exit', 'exit', 'quit', 'sair']:
        print("Encerrando o chat...")
        break

    if cmd == '/clear':
        history = []
        print("Histórico apagado.\n")
        continue

    for chunk in llm.stream(history):
        print(chunk.content,end='',flush=True)
        resp += chunk.content
    
    print()
    history.append(AIMessage(content=resp))

