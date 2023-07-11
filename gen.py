import random
import string
import base64

for key in range(1, 10001):
  prefix = "sk-"
  random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
  encoded_string = base64.b64encode(random_string.encode()).decode()

  generated_string = prefix + encoded_string.replace("=", "")
  print(f"Key {key} : {generated_string}")
  with open("keys_1", "a") as f:
    f.write(generated_string + "\n")