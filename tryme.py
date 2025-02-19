import ollama

model = "deepseek-r1:1.5b"

while True:
    Myprompt = input("You:")
    answer = ollama.generate(model=model, prompt=Myprompt)
    print("DeepSeek:", answer["response"])