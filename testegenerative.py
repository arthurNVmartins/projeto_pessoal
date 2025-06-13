from google import genai
client=genai.Client(api_key='AIzaSyDNIxqy6DfKkExD0nN0v26vVxzN52xMIEo')
response=client.models.generate_content(
    model="gemini=2.0-flash",contents="Me diga as histórias do homem aranha escritas por J.Michael Straczynski"
)
print(response.text)