# LABORATORIO LLM
En este laboratorio vamos a explorar los LLM(Large Language Model), el cual es un tipo de modelo de inteligencia artificial diseñado para procesar y generar texto en varios idiomas. Estos modelos están entrenados en grandes cantidades de datos textuales para aprender la estructura, el significado y las reglas gramaticales del lenguaje. Pueden realizar una variedad de tareas relacionadas con el procesamiento del lenguaje natural, como traducción automática, generación de texto, respuesta a preguntas, resumen de texto y más.

# PRIMER PROGRAMA
Este código muestra un ejemplo de cómo usar la biblioteca langchain para crear un "chain" (cadena) que utiliza un "Large Language Model" (LLM) de OpenAI para responder preguntas basadas en una plantilla de pregunta y respuesta. Las bibliotecas instaladas fueron:
1. openai: proporciona acceso a estos modelos a través de una API que permite a los desarrolladores utilizar la capacidad de generación de texto de estos modelos en sus propias aplicaciones.
2. langchain: Langchain es una biblioteca que proporciona herramientas y utilidades para trabajar con modelos de lenguaje y cadenas de texto en Python
codigo: promt.py
![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/5154cc89-b4cd-4ee5-8f35-aa19eef178d7)

![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/3df444fe-708c-4fe1-950f-be52d672fe87)


# SEGUNDO PROGRAMA 
Este código muestra cómo utilizar la biblioteca langchain para construir un pipeline de procesamiento de lenguaje natural (NLP) que extrae información de un sitio web y luego utiliza un modelo de lenguaje de OpenAI para responder preguntas sobre el contenido extraído. La bibliotecas instladas fueron
1. Beautiful Soup: Es una biblioteca de Python que se utiliza para extraer datos de archivos HTML y XML.
2. chromadb: Base de datos de vectores de embedding diseñada para almacenar y recuperar vectores de representación semántica de texto.
3. tiktoken: Rápido algoritmo BPE desarrollado por OpenAI
4. langchainhub:  Módulo que proporciona acceso a diferentes modelos y recursos para el procesamiento de lenguaje natural (NLP).
codigo: rag.py

![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/6f86e7d5-622c-42af-a256-5df7cc4adefe)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/1af8624a-ca48-43e1-999e-c69da3618f4c)


# TERCER PROGRAMA
Este código carga documentos de texto, divide el texto en fragmentos, genera embeddings para estos fragmentos, indexa los embeddings en Pinecone y luego realiza búsquedas de similitud de documentos en el índice creado.
Para el archivo conocimientos.txt que usa el codigo la información esta relacionada a ataques DDoS. La biblioteca instalada fue:
1. langchain-pinecone: extensión específica entre la biblioteca langchain y el servicio Pinecone para la indexación y búsqueda eficiente de vectores de embedding generados a partir de texto
codigo pineconRag.py

![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/225c539e-dc70-421c-b010-16c98d4878ab)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/ad70ee2e-bccb-4882-bea2-79f450e6e141)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/921e83cf-8bd2-4148-bd3e-aa784292664c)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/01101d3e-eaff-49a6-9cec-90388b6dc993)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/65ec8162-913a-4dda-b256-150d69aa977b)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/39d1f0bc-36e7-450e-8813-fc1744cc3907)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/00291514-d96c-447f-b461-c8dc42fafe09)



# CUARTO PROGRAMA
el código implementa un sistema de pregunta-respuesta para el código fuente utilizando la técnica de Retriever-Augmented Generation (RAG), que combina recuperación de información y generación de texto para proporcionar respuestas más precisas y relevantes. Este script muestra cómo utilizar las bibliotecas de procesamiento de texto y aprendizaje automático para realizar la carga de documentos, la generación de embeddings, la indexación y búsqueda de información, así como la participación en conversaciones basadas en texto.
codigo: codeRag.py

![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/f749e87d-2140-422e-8a5e-4baada0eee49)


![image](https://github.com/NicolasCastro9/AREP_LABLLM/assets/98556822/0e58e24f-3f2c-4de3-a346-f0d9015817b4)


# AUTOR
Nicolás Castro Jaramillo
