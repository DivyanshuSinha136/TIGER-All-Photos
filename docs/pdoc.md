![Pythonaibrain](https://raw.githubusercontent.com/DivyanshuSinha136/TIGER-All-Photos/main/TIGER-Photos/pythonaibrain.png)

# Pythonaibrain

Pythonaibrain is a versatile, plug-and-play Python package designed to help you build offline intelligent AI assistants and applications effortlessly. With modules covering speech recognition, text-to-speech, natural language understanding, `LLM support`, and more, Pythonaibrain lets you create powerful AI solutions without deep expertise or complex setup. Whether you’re a beginner or an experienced developer, get ready to bring your AI ideas to life quickly and efficiently.

---

## Installation

Install the `Pythonaibrain` package:

```bash
pip install pythonaibrain==1.1.9
```

---

## About Pythonaibrain Package

Pythonaibrain package consists of `pyaitk` (which means `Python AI Toolkit`) module and `PyAgent` modules, `pyaitk` provides you methods to create your AI models/chatbots where as `PyAgent` provides best `GUI` and `Web` supports for intrection with models/chatbots. It also provide best contorl on your device. In this package you got default pre-trained models.

---

### pyaitk (`Python AI ToolKit`)

`pyaitk` provides various type of methods and functions to create an advance AI.

---

#### How to import pyaitk

After `pythonaibrain` installations run this code for importing pyaitk

```python
import pyaitk
```

On importing the module it internally train built-in models to work more smootly and fast.

> Note : It takes few minutes to train model.

---

Built-in methods, modules and function in pyaitk :

---

## Methods & Functions

* Camera
* TTS (Text To Speech)
* PTT (PDF To Text)
* ITT (Image To Text)
* STT (Speech To Text)
* MathAI
* Search
* Memory
* Contexts
* Brain
* Advance Brain

---

## Camera Method

The `pyaitk` toolkit supports Camera to click photos and make videos. It can save photos/videos and send them to `pyaitk` `Brain method` for processing.

### Example: Start your camera

```python
import pyaitk
from pyaitk import Camera
import tkinter as tk

root = tk.Tk()          # Create GUI
Camera(root)            # Start camera and pass root as master
root.mainloop()         # Run the GUI
```

Or simply:

```python
from pyaitk.Camera import Start
Start()
```

Or via Brain module:

```python
from pyaitk import Brain

brain = Brain()
brain.load()
brain.process_messages('Click Photo')
```

---

## TTS (Text To Speech) Method

Converts text to speech in male or female voice.

### Example

```python
from pyaitk import TTS

tts = TTS(text='Hello World')
tts.say(voice='david')    # Male voice in windows
tts.say(voice='zira')  # Female voice in windows
tts.say(voice= 'alex') # Male voice in macos
tts.say(voice= 'samantha') # Female voice in macos
tts.say(voice= 'english') # for linux
```

By default, `tts.say()` uses the male voice of windows so agrest with your device type, also see the TTS __doc__.

---

You should know the voice for different OS

|Voice|Gender|style|OS|
|:--:|:--:|:--:|:--:|
|David|Male|en-US|Windows|
|Mark|Male|en-US|Windows|
|Zira|Female|en-US|Windows|
|Alex|Male|en-US|MacOS|
|Samantha|Female|en-US|MacOS|
|Victoria|Female|en-US|MacOS|
|Fred|Male|robotic|MacOS|
|Daniel|Male|en-GB|MacOS|
|Fiona|Female|en-GB|MacOS|
|English|None|Default espeak voice|Linux|
|English-US|None|American English|Linux|
|English-UK|None|British English|Linux|
|MB-EN1|None|MBROLA English 1|Linux|
|MB-FR1|None|MBROLA French 1|Linux|

---

Other ways to use TTS.

```python
from pyaitk import speak

text = "Hello World" # Taking a text
speak(text) # speak functions speak the given text without doing all the setup of TTS method.
```

#### Syntax for speak function

```text
speak(text: str = 'Hi', voice: str = <accordind to device type>):
```

#### What speak function returns?

`speak` function returns `None`.

> Note: You can also set voice according to your choice

## PTT (PDF To Text) Function

PTT (`PPT To Text`) function extract text from the given `.pdf` file.

### Example

```python
import pyaitk
from pyaitk import PTT

ptt = PTT(path='example.pdf')  # Provide your file path
print(ptt)                     # Extracted text output
```

---

#### What PPT function returns?

The PPT function return the extracted text in the string formate.

---

## STT (Speech To Text) Method.

STT (`Speech To Text`) method is use to convert speech to text.

### Example

```python
from pyaitk import STT # Import the method form pyaitk module

stt = STT()

text = stt.listen() # Listen the voice and convert into text and return
print(text)

```

### What STT().listen() return?

`STT().listen()` retuens `string.`

### Why do we use it?

We use it to convert speech to text.

> Note: It works with Internet.

---

## MathAI Function

It is a `built-in function` in `pyaitk` for solving `complex`, and `symbolic` math problems.

### Way to use MathAI function

#### Steps

* First `import MathAI` function from `pyaitk module`.

```python
from pyaitk import MathAI
```

* Create a variable for storing query in string formate.

```python
query = "X + Y - 2X + 3Y" # let's take a query
```

* Now get the answer from the `MathAI` function for the query.

```python
answer = MathAI(query= query) # MathAI gives the answer in string formate.
```

* After that print the answer.

```python
print(answer)
```

From this way we can ask any query of math with `MathAI`.

#### Full Code

```python
from pyaitk import MathAI

query = "X + Y - 2X + 3Y" # let's take a query
answer = MathAI(query= query) # MathAI gives the answer in string formate.

print(answer)
```

> Note: MathAI have fixed pattern of prompts, means you can ask question in direct form not question with string like,
>
> ```python
>query = "Solve X + Y - 2X + 3Y"
>```
>
>Try to ask direct questions only.

### Prompts for MathAI

#### Solve normal numeric problems.

```c
1 + 2 + 3 + 4 - 5 (1 - 55) + 10
```

#### Solve symbolic methamatic.

```c
X + 2Y - X + 10Z * (10 - 100)X
```

#### Matrix

```c
Matrix([[1, 0], [0, 1]])

Matrix([[1,2,3], [2, 3, 10]])
```

#### Trigonometric Functions

##### sin

```c
sin(0)
sin(30)
sin(45)
sin(60)
sin(90)
...
sin(180)
...
```

###### Syntax

```c
sin(<value of theata>)
```

##### cos

```c
cos(0)
cos(30)
cos(45)
cos(60)
cos(90)
...
cos(180)
...
```

###### Syntax

```c
cos(<value of theata>)
```

##### tan

```c
tan(0)
tan(30)
tan(45)
tan(60)
tan(90)
...
tan(180)
...
```

###### Syntax

```c
tan(<value of theata>)
```

##### cosec

```cpp
csc(0)
csc(30)
csc(45)
csc(60)
csc(90)
...
csc(180)
...
```

###### Syntax

```cpp
csc(<value of theata>)
```

##### sec

```cpp
sec(0)
sec(30)
sec(45)
sec(60)
sec(90)
...
sec(180)
...
```

###### Syntax

```cpp
sec(<value of theata>)
```

##### cot

```cpp
cot(0)
cot(30)
cot(45)
cot(60)
cot(90)
...
cot(180)
...
```

###### Syntax

```cpp
cot(<value of theata>)
```

#### Limit

```cpp
limit('2X')
limit('2X + 3Y')
```

##### Syntax

```cpp
limit(<symbolic and trigonometric values in string formate>)
```

#### Determinants

```cpp
det(Matrix([[10]]))
det(Matrix([[10], [20]]))
det(Matrix([[10], [30], [40]]))
det(Matrix([[10], [100], [0], [50]]))
det(Matrix([[10], [97], [95], [1], [99]]))
det(Matrix([[10], [11], [100], [3], [2], [150]]))
det(Matrix([[10, 20]]))
det(Matrix([[10, 20], [20, 30]]))
det(Matrix([[10, 20], [60, 70], [80, 100]]))
det(Matrix([[10, 20, 30]]))
det(Matrix([[10, 20, 30], [40, 50, 60]]))
det(Matrix([[10, 20, 30], [40, 50, 60], [90, 100, 102]]))
det(Matrix([[10, 20, 30], [40, 50, 60], [90, 100, 102], [95, 101, 1000]]))
...
```

#### Log

```cpp
log(10)
log(20)
log(0)
log(100)
...
```

#### Ln

```cpp
ln(0)
ln(1)
ln(10)
ln(100)
ln(1000)
ln(102)
ln(3)
ln(90)
ln(893)
ln(9)
...
```

#### E

```cpp
e()
```

`↑` Get the value of `e`.

```cpp
e(10)
e(3)
e(21)
e(38)
e(0)
...
```

#### ⊼ (`pi`)

```cpp
pi()
```

`↑` Get the value of `⊼`

#### Square

Get all square of the value.

```cpp
sqrt(10)
sqrt(2)
sqrt(30)
sqrt(28039)
sqrt(19)
sqrt(289843190)
...
```

#### Differential

```cpp
diff('2x')
diff('x')
diff('y')
...
```

Give all the values in string formate.

#### Integration (`∫`)

Give all the values in string formate.

```cpp
integrate('dx')
integrate('x dx')
integrate('2x dx')
integrate('2x dy')
integrate('x dy')
integrate('2x + 3y - 3y dx')
...
```

#### Factor

Get all the factors of the numbers

```cpp
factor(10)
factor(213)
factor(389)
factor(1983)
factor(0)
factor(12)
...
```

---

## Search Method

`Search` method is for searching queries from internate, and gives top five answers, links, summaries.

### Ways to use Search method

#### Steps

* First `import Search` method from `pyaitk module`.

```python
from pyaitk import Search
```

* Assigne a varible for query

```python
query = 'pythonaibrain'
```

* Assigne a varible, and pass query in it.

```python
search = Search(query = query)
```

* > If no query given it by default takes 'pythonaibrain' as a query.

* Run the run funcition inside Search to get all top five answers, links, summaries.

```python
search.run()
```

* Get answer.

```python
search.get_results_str()
```

* > Note: It return all the answer in string formate, so we will try to fetch all the answers in a variable.

* Fetch answer.

```python
answer = search.get_results_str()
```

* At last print all the fetch answers.

```python
print(answer)
```

#### Full code

```python
from pyaitk import Search

query = 'pythonaibrain'

search = Search(query)
search.run()

# Get answer.

answer = search.get_results_str()

# print the fetched answer.

print(answer)
```

---

## Memory Method

It is use for `LTM` (`Long-Term-Memory`) ans `STM` (`Short-Term-Memory`), or we can say `LSTM` (`Long-Short-Term-Memory`)

### Way to use Memory Method

#### Steps

* First we will `import Memory` method from `pyaitk module`.

```python
from pyaitk import memory
```

* After that.

```python
memory = Memory() # you can pass name of your memory file otherwise it by default takes memory.json
```

* > Note : The memory file extention should be `.json`

* Now we will remember function for remember.

```python
memory.remember('user', 'Hi') # It takes key value pairs as a parameter.
```

* Now we recall the messages.

```python
memory.recall('user') # It takes key as a peremeter.
```

* Now we save the memory for LTM.

```python
memory.save_memory() # It saves the memory for long time.
```

* Now we load our LTM.

```python
memory.load_memory() # It load our saved memory, but if the memory is not saved it takes empty dict.
```

* If we want to delete our existing memory we will use  `clear_memory` function.

```python
memory.clear_memory() # It cleare all the data to our memory.
```

* > Remember : It will not delete the file.

---

## Contexts Method

`Contexts` method extract sutable answer asked by user from the given context.

### Example

```python
from pyaitk import Contexts

context = '''
Patanjali Ayurved is an Indian company. It was founded by Baba Ramdev and Acharya Balkrishna in 2006.
'''

question = 'Who founded Patanjali Ayurved?'
contexts = Contexts()
answer = contexts.ask(context=context, question=question)
print(answer)
```

---

#### What Contexts method returns?

The `Contexts` method itself rethurn nothing, but it's ask attribute returns `answers` in `string` formate.

---

## Brain Method

It is a powerfull method which allow you to create a smart `AI` `models` and `chatbots`. It gives you better flexibility to work on your model.

You can also give your dataset to train it. It also supports `function mapping`.

You can also download `pre-trained` models from it.

> Note: Not all models, you can download models which supports pythonaibrain.

### Ways to use Brain Method

#### Steps

* First we will `import Brain` from `pyaitk module`.

```python
from pyaitk import Brain
```

* Let's create brain of our chatbot.

```python
brain = Brain() # You can pass your intents path, and functions for function mapping.
```

* Let's load our default model.

```python
brain.load() # It loads the default model
```

* If you give your dataset then you should train and save your model.

```python
brain = Brain('intents.json')

brain.train() # It takes few minutes or may be hour, it depends you dataset size.
brain.save()
```

* Let's start chatting with default model (in basic style).

```python
while True:
    message = input('Message : ')
    answer = brain.process_messages(answer)
    brain.pyai_say(answer)
```

* Other ways to talk with our model (in advance style).

```python
while True:
    message = input('Message : ')
    answer = brain.talk(answer, grammer= False, TTS= True) # You can also close TTS by passing TTS= False.
    brain.write(answer)
```

#### Full Code

```python
from pyaitk import Brain

brain = Brain()

# def Hello():
#     return "Hello"
# brain = Brain(intents_path= 'intents.json', hello= Hello)
# brain.train()
# brain.save()

brain.load()

while True:
    message = input("Message : ")
    # answer = brain.process_messages(message)
    answer = brain.talk(message, grammer= False, TTS= True)
    # brain.pyai_say(answer)
    brain.write(answer)

# for more detail about functions run:
# print(brain.__all__)
```

#### Functions of `Brain` method

```python
from pyaitk import Brain

brain = Brain()
```

* If you want to know the model is loaded or not, then use `is_loaded` function.

```python
brain.is_loaded()
```

It returns True/ False.

* If you want to know the model is saved or not, then use `is_saved` function.

```python
brain.is_saved()
```

It also returns True/ False.

* Or, if you want to konw the model is trained or not, then use `is_trained` function.

```python
brain.is_trained()
```

It also returns True/ False.

* If you want to know type of inputed message then use `predict_message_type` function.

```python
brain.predict_message_type('What is your name?') # Returns -> Question.
```

##### What `predict_message_type` function can returns for the message

* Question
* Answer
* Command
* Shutdown
* Make Directory
* Statement
* Name
* Know
* Start

###### Notes:

* `Shutdown` and `Start` commands require terminal support and
**do not work on Android or iOS.**

* `Make Directory` creates folders on your device.
* `Statement` is any plain text that is not a command/question.
* `Name` detects if a message contains a person's name.

### How to create `intents.json`

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "What's up?", "Howdy"],
      "responses": ["Hello! How can I help you today?", "Hey there!", "Hi! What can I do for you?"]
    },
    {
      "tag": "bye",
      "patterns": ["Bye", "See you soon", "Take care"],
      "responses": ["Bye! Have a great day", "See you"]
    }
  ]
}
```

Save this as a `.json` file and provide it to the Brain module.

### Other way

```python
from pyaitk import Brain

brain = Brain(intents_path='intents.json')  # or Brain() with default
brain.train()
brain.save()
message = input('Message: ')
message_type = brain.predict_message_type(message=message)

if message_type in ['Question', 'Answer']:
    print(f'Answer: {brain.process_messages(message=message)}')
```

Note : train and save the file when use first time or change the default intents.json with your intents.json otherwise use load function by writting,

```python
brain.load() # it returns bool
```

And also don't forgot to load otherwise it through an error
Or,

```python
from pyaitk import Brain

brain = Brain()
brain.load()
message = input('Message: ')
message_type = brain.predict_message_type(message=message)

if message_type in ['Question', 'Answer']:
    print(f'Answer: {brain.process_messages(message=message)}')
```

---

## Advance Brain Module

An advanced version of the Brain module with smarter classification and better entity recognition. It also suport LLMs for better responce.

### Usage

```python
from pyaitk import AdvanceBrain

advance_brain = AdvanceBrain(intents_path='intents.json')  # or AdvanceBrain()

message = input('Message: ')
message_type = advance_brain.predict_message_type(message=message)

if message_type in ['Question', 'Answer']:
    print(f'Answer: {advance_brain.process_messages(message=message)}')
```

### Same limitations apply as Brain module for commands.

---

## Pythonaibrain Summary.

| Module Name  | Description                                 |
| ------------ | ------------------------------------------- |
| Brain        | Basic Smart AI brain using `.json` knowledge base |
| AdvanceBrain | Advanced AI brain with better understanding and LLM supports |
| TTS          | Text to speech                              |
| MathAI       | Use to solve complex and symbolic math problems|
| PTT          | It extract text from pdf                    |
| ITT          | Image to text extraction                    |
| Camera       | Capture photos and videos                   |
| Context      | Get answers from text contexts              |
| Search       | It search top five result from internet     |

---

## Built-in AI Assistant - PyAgent

If you prefer not to code your own AI, use the built-in **PyAgent** GUI or web assistant.

### GUI

```python
import PyAgent
PyAgent.App()
```

### Web Server

```python
from PyAgent import PYAS
PYAS.app.run(debug=False)
```

Or

```python
from PyAgent import Server
server = Server()
server.run()
```

### Socket Client-AI Server

Make your own client-AI server for handling multiples client togeather, for client side we use `pythonaibrain-client` module.

#### Install pythonaibrain-client

```bash
pip install pythonaibrain-client
```

After that,

```python
from pyaibrain.client import ClientServer

cServer = ClientServer()
cServer.serve()
```

This will create client side in cli (`Command Line Interface`).

Also,

```bash
client-server
```


### Socket Server

```python
from pyaitk import server

server()
```

From this way we can make main server for which handle clients.

---

### Console Scripts

```bash
download-nlu       # Downloads NLTK Data
tiger-server       # Starts AI Agent Chat Server
tiger-web-server   # Starts Web-based AI Server
```

---

## Visit [PyPI](https://pypi.org/project/pythonaibrain) for installation and more details.

## Visit [GitHub](https://github.com/DivyanshuSinha136/TIGER-All-Photos/) for more detail about package.

## Visit [Pythonaibrain Issues](https://github.com/DivyanshuSinha136/TIGER-All-Photos/issues) for any issues.

---

**Start building your AI assistant today with Pythonaibrain!**
**Try to ask your doubt with AI releated to this package!**
