class Person:
  def __init__(self, emotions):
    self.mood = emotions

  def __str__(self):
    return f"Emotions: {self.mood}"

  def get_mood(self):
    for emotion, level in self.mood.items():
      if level == 1:
        print(f"I am feeling a low amount of {emotion}")
      elif level == 2:
        print(f"I am feeling a moderate amount of {emotion}")
      elif level == 3:
        print(f"I am feeling a high amount of {emotion}")
        # why does my for loop stop when i use return instead of print()?

emotions = {
  'happiness': 3,
  'sadness': 1,
  'stress': 2
}

person1 = Person(emotions)
# print(person1)
# print(person1.mood)
person1.get_mood()

