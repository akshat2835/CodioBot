# WRITE YOUR CODE HERE
import openai
import os
# Replace 'your_api_key' with your actual API key
openai.api_key = "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"# grab the env variable

def generate_website(prompt):
  response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a html expert you are going to write a html file"},
        {"role": "user", "content": prompt}
    ]
)
  website_code = response['choices'][0]['message']['content'].strip()
  return website_code

print(generate_website("create our JavaScript code that handles user input and sends requests to the ChatGPT API."))
