import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write(f"**User:** {message.content}")
        else:
            st.write(f"**System:** {message.content}")

def main():
    st.set_page_config(page_title="Academic Research Paper Information Retrieval", layout="wide")

    st.markdown("<h1 style='text-align: center;'>Academic Research Paper Information Retrieval System 📚</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Efficiently Search and Interact with Your Academic PDFs</h3>", unsafe_allow_html=True)
    
    st.write("---")

    user_question = st.text_input("🔍 **Ask a Question** about the contents of the uploaded PDF files")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None

    if user_question:
        st.markdown("### Conversation History")
        user_input(user_question)

    with st.sidebar:
        st.title("📁 Menu")
        st.markdown("### Upload Your Research Papers")
        st.markdown("Upload your academic research papers (PDF files) to enable the system to extract and retrieve information.")
        pdf_docs = st.file_uploader("Upload PDF Files", accept_multiple_files=True)

        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing your documents..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    st.session_state.conversation = get_conversational_chain(vector_store)
                    st.success("Your documents have been successfully processed! You can now ask questions.")
            else:
                st.error("Please upload at least one PDF file.")

    st.write("---")
    st.markdown("<small style='text-align: center; display: block;'>© 2024 Academic Research Paper Information Retrieval System | Contact: duttapragyanjyoti@gmail.com</small>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
