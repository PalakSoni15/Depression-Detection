import requests

payload = {
  "name": "string",
  "email": "string",
  "dob": "string",
  "gender": "Male",
  "password": "string"
}

payload = {"text": "some random depressive text"}

# res = requests.get("http://127.0.0.1:8000/")
res = requests.post("http://127.0.0.1:8000/depression/", json=payload)


print(res)
