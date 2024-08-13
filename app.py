import streamlit as st
from src.helper get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain


def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrieval System ")

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = pdf_text(pdf_docs)

                st.success("Done")
       # Process the uploaded PDF files


if __name__ == "__main__":
    main()


