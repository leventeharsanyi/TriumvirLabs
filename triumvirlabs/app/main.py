import streamlit as st
from dotenv import load_dotenv
from models import generate_voice, generate_text

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
    audio_file = st.audio_input("Record your question here:", sample_rate=48000)
    input_question = ""
    if audio_file is not None:
        input_question = generate_text(audio_file)
        with st.chat_message("human"):
            st.markdown(f"**Transcript** 📝\n\n> {input_question}")
    if st.button("Ask"):
        # TODO: Implement the Anthropic API here.
        output_text = " ".join(input_question.split()[::-1])
        output_audio = generate_voice(output_text)
        st.write("Here is your answer:")
        st.audio(output_audio)
        with st.chat_message("bot"):
            st.markdown(f"**Transcript** 📝\n\n> {output_text}")

if __name__ == "__main__":
    main()