# DeepSeek-R1-Install-Win11
Running LLM locally is very appealling as it could address many concerns regarding security and IP protection. This is the note I took when I try to install DeepSeek R1 on my laptop.

I follow this [blog](https://www.thewindowsclub.com/how-to-run-deepseek-locally-on-windows#:~:text=We%20will%20show%20you%20how%20to%20host%20the,the%20installer%20file%20to%20install%20the%20Chatbox%20AI.)

## Install Ollama
The first step is to install Ollama on your computer. You can download it from its [official website](https://ollama.com/). Run the installer file to install Ollama on your computer. After installing Ollama, visit its official website again and click on the Models tab on the top.

## Install DeepSeek R1 model with cmd
I select the smallest model, deepseek-r1:1.5b, by in a CMD window running this command:
~~~
ollama run deepseek-r1:1.5b
~~~

## Try out
Upon successfully installation, you can start chat with the model. The speed of response generation is amazingly good even on a pretty elementary laptop. 
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

### Test the model in Python App
You can try to run tryme.py.
~~~
$ C:/python.exe c:/Users/xinxue/deepseek-r1/tryme.py
You:What is your name?
DeepSeek: <think>

</think>

Greetings! I'm DeepSeek-R1, an artificial intelligence assistant created by DeepSeek. I'm at your service and would be delighted to assist you with any inquiries or tasks you may have.
~~~

### Test the model in async call
You can try out to run async.py
~~~
$ C:/python.exe c:/Users/xinxue/deepseek-r1/async.py
<think>

</think>

The color of the sky, also known as the atmospheric color, is primarily due to the scattering and absorption of light in the Earth's atmosphere. When sunlight passes through these layers, it is both scattered and absorbed by various particles, including molecules and small water droplets, which are illuminated from all directions by the Sun. This process causes the colors of the visible spectrum that would otherwise be seen as a single color to appear as multiple hues or colors when observed directly by humans.

~~~

### Test the model in Smantic Kernel
In SK, we load in the model through ollama connector (sk version 1.21.3).
YOu can try out to run sk.py
~~~
$ C:/python.exe c:/Users/xinxue/deepseek-r1/sk.py
<think>
Okay, so I need to give a TLDR from these three points about robots and human life. Let's break it down. 

Point 1 says the robot can't injure anyone or let another harm if not doing so themselves. That sounds like the Third Law of Thermodynamics, which says no law breaks in physics without a reason. So that covers safety and preventing harm.

Point 2 mentions obeying human orders unless they conflict with laws. That's more about ethics and consequences. If someone violates a rule, the robot has to follow it instead because breaking one is not allowed.

Point 3 talks about protecting itself as long as no conflict with other laws. So that relates to safety and existence beyond just preventing harm to humans.

Putting it together: The robot can't hurt anyone unless doing so themselves, must obey orders without breaking laws, and must protect itself while complying with both human and non-human laws. But wait, the user asked for exactly five words, so maybe I can combine some parts.

Perhaps "Robots cannot harm humans or others, obey instructions when safe, and must exist safely." That's seven words. Maybe shorten it further to five: "Robots must obey, protect themselves, prevent harm from humans."
</think>

Robots must obey, protect themselves, prevent harm from humans.
~~~
