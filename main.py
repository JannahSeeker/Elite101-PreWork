import random
greetings = [
    "Hello", "Hi", "Good morning", "Good afternoon", "Good evening",
    "Welcome", "Greetings", "Hey there", "Howdy", "Salutations",
    "Top of the morning to you", "Pleased to meet you", "Yo", "What's up",
    "Nice to see you", "G'day", "Bonjour", "Hola", "Ciao", "Namaste",
    "How's it going", "Hey", "Guten Tag", "Kon'nichiwa", "Shalom",
    "Sawubona", "Ahlan", "What's happening", "Hey ya", "Well, hello there"
]
prompts = {
  "age": "How young are you? ",
  "name": "May I have your name, please? "
}
help_phrases = [
  "How can I assist you?",
  "What can I do for you?",
  "How may I be of service?",
  "What do you need help with?",
  "Is there anything I can help with?",
  "What assistance do you require?",
  "How can I lend a hand?",
  "How may I assist you today?",
  "Is there something you need help with?",
  "How can I support you?",
  "Can I help you with something?",
  "What can I do to help?",
  "In what way can I be of help?",
  "How may I be of assistance?",
  "What do you need assistance with?",
  "How can I aid you?",
  "How can I assist you today?",
  "How may I assist you?",
  "Can I help you with anything?",
  "How can I be of assistance to you?"
]
thankyou_phrases = [
    "Thank you so much!",
    "I really appreciate it, thank you!",
    "Thanks a bunch!",
    "I can't thank you enough!",
    "You're the best, thank you!",
    "Thanks a million!",
    "Many thanks!",
    "I'm grateful, thank you!",
    "I owe you one, thanks!",
    "Thanks for everything!"
]
bye_phrases = [
    "Goodbye!",
    "See you later!",
    "Take care!",
    "Farewell!",
    "Until next time!",
    "Bye now!",
    "Have a good one!",
    "Catch you later!",
    "Adios!",
    "So long!",
    "Until we meet again!"
]
options = [
    ['Purchase a product', 'print("placeholder")'],
    ['Return an item', 'print("placeholder")'],
    ['Check store hours', 'print("placeholder")'],
    ['Speak with a representative', 'print("placeholder")'],
    ['Exit the store', 'print(random.choice(bye_phrases))']
]


bye_phrases = [
    "Goodbye!",
    "See you later!",
    "Take care!",
    "Farewell!",
    "Until next time!",
    "Bye now!",
    "Have a good one!",
    "Catch you later!",
    "Adios!",
    "So long!",
    "Until we meet again!"
]
happy_phrases = [
    "Well, I'll be darned!",
    "Oh my goodness, that's fantastic!",
    "Goodness gracious, that's wonderful!",
    "Wow, that's amazing!",
    "Oh wow, that's delightful!",
    "Great Scott, that's terrific!",
    "Holy moly, that's outstanding!",
    "Oh my, that's marvelous!",
    "Gee whiz, that's superb!",
    "Well I'll be, that's excellent!"
]
class Customer:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.email = '' 
        self.choice = 0
    def collectinformation(self):
      print(random.choice(greetings) + "!") #Welcomes user
      self.name = input(prompts['name']) #collects name and age
      self.age = input(prompts['age']) 
    def welcomemenu(self):
      print("Welcome to the store, " + self.name + "!\n" + random.choice(happy_phrases),"I'd like to be", self.age,"again!\n" + "Here are the services we offer at the moment:\n")
    def printmenu(self):
      for i, option in enumerate(options):
        print(f"{i+1}. {option[0]}")
    def get_user_choice(self):
      self.choice = int(input("Please enter a number corresponding to the service you would like to use: "))
      while True:
        if self.choice < 1 or self.choice > len(options):
          print("Invalid choice. Please try again.")
          self.choice = int(input("Please enter a number corresponding to the service you would like to use: "))
        else:
          print(random.choice(thankyou_phrases))
          break 
    def act(self):
      exec(options[self.choice-1][1])  
          
        
        



customer1 = Customer()

customer1.collectinformation()
customer1.welcomemenu()
customer1.printmenu()
customer1.get_user_choice()
customer1.act()