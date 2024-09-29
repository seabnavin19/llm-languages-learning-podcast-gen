from langchain_openai import ChatOpenAI
import os
from utils.Fomatter.podcast import Podcast
from pathlib import Path
from openai import OpenAI

class PodcastScriptGenerator:

    def __init__(self, model_name, api_key):
        self.llm = ChatOpenAI(model_name=model_name, api_key=api_key)

    def generate_prompt_template(self,vocabulary,grammar,lang):
        podcast_script_template = f"""
        ## you talk to your audience and make sure use use the following vocabulary and grammar in your talk, make it into 3 paragraphs in {lang} language

        vocabulary: 
        {vocabulary} 
        _________
        grammar topics: 
        {grammar}
        _________

        The podcast script should include the following elements:
        - No music or external voice needed
        - Make it more interactive and engaging with the audience

        """
        return podcast_script_template
    
    def generate_podcast(self,vocabulary,grammar,lang):
        podcast_script_template = self.generate_prompt_template(vocabulary,grammar,lang)
        structured_llm = self.llm.with_structured_output(Podcast)
        return structured_llm.invoke(podcast_script_template)


class PodcastVoiceGenerator:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_voice(self, speech_file_path, podcast_text):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=podcast_text
        )

        response.stream_to_file(speech_file_path)
        return speech_file_path