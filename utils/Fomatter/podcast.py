from typing import Optional,List,Dict

from pydantic import BaseModel, Field


class Questions(BaseModel):
    """question and multiple choice answers for the podcast to test audience comprehension"""
    question: str = Field(description="The question to ask the audience")
    option: List[str] = Field(description="The list of the answer option")
    correct_answer: str = Field(description="The correct answer to the question")

class WordTranslation(BaseModel):
    """Model for a word and its translation."""
    word: str = Field(description="The word to translate")
    translation: str = Field(description="The correct translation of the word in english")



class Podcast(BaseModel):
    """Podcast information with a question and multiple choice answers."""
    
    podcast_lang: str = Field(description="The Target language content of the podcast (if grammar and vocabulary are in the target language)")
    english: str = Field(description="The English content of the podcast , it is like the translation of the target language content")
    question_and_multiple_choice_answer: List[Questions]= Field(
        description="generate 5 questions and multiple choice answers for the podcast to test audience comprehension"
    ),
    words_translation:List[WordTranslation]=Field(
        description="select some importance words in the podcast and provide the translation of the word in english"
    )