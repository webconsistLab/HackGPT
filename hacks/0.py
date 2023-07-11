import openai

keys = open("keys/keys_0").read().splitlines()

it = 0
openai.api_key = ''  # Replace with your OpenAI API key

def chat_with_bot(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the most recent engine available
        prompt=message,
        max_tokens=50,  # Adjust the response length as needed
        temperature=0.7,  # Adjust the creativity of the responses (lower values are more focused, higher values are more random)
        n=1,  # Generate a single response
        stop=None,  # Stop generating after a certain token is reached (optional)
    )
    return response.choices[0].text.strip()

input("")

for key in keys:
  it += 1
  openai.api_key = key
  print(f"{it}", end=" ")
  try:
    chat_with_bot("Write a hello world program in C++")
    print(f"0 FOUND : {key}")
    open("valids", "a").write(key+"\n")
  except openai.error.AuthenticationError:
    print(f"0 Invalid : {key}")

