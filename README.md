# Agente-SQL---LLM-llma3
Imagina a quantidade de pedidos que um time de dados precisa atender todos os dias para suportar a tomada de decisão de uma empresa. Agora imagine que um Agente SQL, como o chatGPT, atendendo boa parte dessa demanda através de conhecimento dos metadados de seu banco? É isso que o Agente SQL com llma3 faz.

# O .main
Foi desenvolvido em 4 partes principais. Abra o main para identificar as funções

1. Carrega as configurações
2. Instância o modelo de embeddings e o LLM (llam3)
3. Inicializa o carregador de metadados e engine de perguntas
4. Constrói a interface interativa

O projeto foi todo modulado para que cada arquivo possa ser modificado ou alterado em seu próprio módulo.

# Funcionamento

<img width="533" height="306" alt="image" src="https://github.com/user-attachments/assets/5b2eb37c-e8f8-49e5-8325-f07eaeac3cd1" />

1. A interface é carrega com o gradio
2. O pandas é utilizado para o carregamento do CSV
3. O langchain é utilizado para transformar os dados em textos, o HuggingFaceEmbeddings para para vetorizar e o FAISS como banco de veores
4. o llma3 é utilizado como modelo de LLM com parâmetros criatividade, penalização de repetição de palavras, quantidade de tokens em contexto e outros.
