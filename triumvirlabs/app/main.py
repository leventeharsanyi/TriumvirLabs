import streamlit as st
from dotenv import load_dotenv
from models import generate_voice, generate_text
from llm import llm_call

st.set_page_config(
    page_title="Triumvir Labs",
    page_icon="🩺",
    layout="centered",
)


def main():
    load_dotenv()
    st.title("Triumvir Labs")
    st.caption("A good anamnesis is half the diagnosis.")
    st.subheader("Ask something from the agent! 🙋")
    st.info("Record a question and click **Ask the agent** to get an answer.", icon="🎙️")
    audio_file = st.audio_input("Record your question here:", sample_rate=48000)
    if audio_file is not None:
        input_question = generate_text(audio_file)
        with st.chat_message("human"):
            st.markdown(f"**Transcript** 📝\n\n> {input_question}")
        if st.button("💬 Ask the agent", type="primary", use_container_width=True):
            output_text = llm_call(input_question)
            output_audio = generate_voice(output_text)
            st.write("Here is your answer:")
            st.audio(output_audio)
            with st.chat_message("ai"):
                st.markdown(f"**Transcript** 📝\n\n> {output_text}")
            if st.button("Ask another question", type="secondary", use_container_width=True):
                st.rerun()

if __name__ == "__main__":
    main()