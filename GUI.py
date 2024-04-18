# Importamos librerías y el archivo con nuestra función de consulta
import Consulta
import streamlit as st
from streamlit_chat import message
import time

# Establecemos un css personalizado
css = """
    <style>
    span{
        color: #E900A3;
    }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

st.title("LiverBot 🤖")
st.write("¡Hazme preguntas sobre las auditorías!")

# Inicializamos el historial de chat si aún ni ha sido creado
if "messages" not in st.session_state:
    st.session_state.messages = []

# Muestra los mensajes del historial en la interfaz
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Solicita la entrada del usuario y almacena la pregunta
if prompt := st.chat_input("¿Cómo puedo ayudarte?, Ingresa tu pregunta"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Muestra un mensaje de asistente y prepara un espacio para la respuesta
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Obtiene la última pregunta del usuario
        user_message = st.session_state.messages[-1]["content"]

        # Obtiene la respuesta del modelo mediante la función de consulta
        assistant_response = Consulta.consulta(user_message)

        # Muestra la respuesta
        for char in assistant_response:
            full_response += char
            message_placeholder.text(full_response + "▌")
            time.sleep(0.05)  # Efecto delay

        # Muestra la respuesta final
        message_placeholder.text(assistant_response)

    # Agrega el mensaje del asistente al historial de chat
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response})
