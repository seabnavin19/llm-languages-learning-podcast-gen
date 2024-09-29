import streamlit as st
from utils.Generator.podcast_generator import PodcastScriptGenerator, PodcastVoiceGenerator

st.title("Podcast Generator")


st.sidebar.header("API Key")
api_key = st.sidebar.text_input("Enter your API Key", type="password") 
language = st.sidebar.text_input("Enter the language you want to generate the podcast in")



if api_key and language:
    podcast_script_generator = PodcastScriptGenerator(model_name="gpt-4o-mini", api_key=api_key)
    podcast_voice_generator = PodcastVoiceGenerator(api_key=api_key)

    st.header("Input Vocabulary")
    vocabulary_input = st.text_area("Enter your vocabulary", height=200)


    st.header("Input Grammar")
    grammar_input = st.text_area("Enter any grammar points you want to include", height=200)

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False
    if "audio_path" not in st.session_state:
        st.session_state.audio_path = ""
    if "podcast_detail" not in st.session_state:
        st.session_state.podcast_detail = None



    if st.button("Generate Podcast"):
    
        with st.spinner("Generating podcast..."):
                if vocabulary_input:
                    try:
                        
                        st.session_state.podcast_detail = podcast_script_generator.generate_podcast(vocabulary=vocabulary_input, grammar=grammar_input,lang=language)

                        st.session_state.audio_path = "speech1.mp3"
                        audio_path= st.session_state.audio_path
                        podcast_detail = st.session_state.podcast_detail
                    
                        podcast_voice_generator.generate_voice(podcast_text=podcast_detail.podcast_lang, speech_file_path=audio_path)


                        st.subheader(f"Podcast Script (in {language} )")
                        st.write(podcast_detail.podcast_lang)

                        st.subheader("Podcast Script (in English)")
                        st.write(podcast_detail.english)  

                        st.audio(audio_path)

                        st.subheader("Questions and Answers")
                        for q_a in podcast_detail.question_and_multiple_choice_answer:
                            st.markdown("### "+q_a.question)
                            
                            st.write("Options:")
                            for ind,option in enumerate(q_a.option):
                                st.write(str(ind+1)+") "+option)
                            st.expander("See Answer").write("Answer: "+q_a.correct_answer)

                                

                        st.markdown("### Importance Words To Remember")
                        for word in podcast_detail.words_translation:
                            st.text(f"{word.word} - {word.translation}")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                
                else:
                    st.warning("Please enter vocabulary to generate a podcast.")


else:
    st.warning("Please enter your API key in the sidebar to generate a podcast.")
