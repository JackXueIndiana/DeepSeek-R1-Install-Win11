# DeepSeek-R1-Install-Win11
This is the note I took when I try to install DeepSeek R1 on my laptop.

I follow this [blog](https://www.thewindowsclub.com/how-to-run-deepseek-locally-on-windows#:~:text=We%20will%20show%20you%20how%20to%20host%20the,the%20installer%20file%20to%20install%20the%20Chatbox%20AI.)

## Install Ollama
The first step is to install Ollama on your computer. You can download it from its [official website](https://ollama.com/). Run the installer file to install Ollama on your computer. After installing Ollama, visit its official website again and click on the Models tab on the top.

## Install DeepSeek R1 model with cmd
I select the smallest model, deepseek-r1:1.5b, by in a CMD window running this command:
~~~
ollama run deepseek-r1:1.5b
~~~

## Try out
Upon successfully installation, you can start chat with the model:
~~~
(base) C:\Users\xinxue\deepseek-r1>ollama run deepseek-r1:1.5b
>>> hello
<think>

</think>

Hello! How can I assist you today? 😊

>>> what's your name?
<think>

</think>

Hello! My name is DeepSeek-R1-Lite-Preview. I'm currently an AI assistant created by DeepSeek, available to help with various inquiries and
tasks. Let me know how I can assist you!
~~~
