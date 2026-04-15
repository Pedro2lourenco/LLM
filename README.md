# Chat CLI com LangChain + Ollama (Streaming + Memória)

Este projeto é um chatbot simples em terminal que utiliza **LangChain** com **Ollama (modelo Mistral)**, suportando:

*  Respostas em streaming
*  Memória de conversa (histórico)
* Comandos de saída e limpeza de histórico

---

## Requisitos

* Python 3.9+
* Ollama instalado e rodando
* Modelo `mistral` baixado

---

## Instalação

Instale as dependências:

```bash id="a1b2c3"
pip install langchain langchain-community
```

---

## Baixar o modelo

```bash id="d4e5f6"
ollama pull mistral
```
---

## Como usar

Digite normalmente suas perguntas no terminal:

```text id="m4n5o6"
>>? O que é física quântica?
```

A resposta será gerada em tempo real (streaming).

---

## Comandos disponíveis

Durante a execução, você pode usar:

* `/exit` → encerra o programa
* `/clear` → limpa o histórico da conversa

Exemplo:

```text id="p7q8r9"
>>? /clear
Histórico apagado.
```

---

## Como funciona

* O modelo `mistral` é carregado via Ollama
* Cada mensagem do usuário é armazenada no `history`
* O histórico é enviado ao modelo para manter contexto
* A resposta é exibida em **streaming (token por token)**
* A conversa continua até o usuário sair

---

## 🚀 Possíveis melhorias

* Limitar tamanho do histórico (evitar consumo de memória)
* Adicionar salvamento em arquivo (`.json` ou `.txt`)
* Criar interface web (Flask / FastAPI)
* Adicionar comandos como `/save`, `/load`
* Suporte a múltiplos modelos do Ollama

---

## 📚 Observação

Se o streaming não funcionar corretamente:

* Verifique se o Ollama está ativo:

```bash
ollama run mistral
```
---

Feito para estudo de LLMs locais com Python + LangChain ⚡
