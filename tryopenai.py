import os
import openai

openai.api_key = os.getenv("")

response = openai.Completion.create(
  engine="davinci",
  prompt="Topic: Breakfast\nTwo-Sentence Horror Story: He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton.\n###\nTopic: Wind\nTwo-Sentence Horror Story:",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["###"]
)
