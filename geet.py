import openai

# Set your OpenAI API key
openai.api_key = "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"

# Prompt the user for input
prompt = input("Please enter a prompt: ")

# Use the GPT-3 API to generate a response to the prompt
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.5,
)

# Display the response in the terminal window
print(response["choices"][0]["text"])
