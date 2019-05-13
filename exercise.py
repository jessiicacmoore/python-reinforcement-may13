class Person:
  def __init__(self, emotions):
    self.mood = emotions

  def __str__(self):
    return f"Emotions: {self.emotions}"

  def get_mood(self):
    for emotion, level in self.mood.items():
      if level == 3:
        return f"I am feeling a high amount of {emotion}"
      elif level == 2:
        return f"I am feeling a moderate amount of {emotion}"
      elif level == 1:
        return f"I am feeling a low amount of {emotion}"

emotions = {
  'happiness': 3,
  'sadness': 1,
  'stress': 2
}

person1 = Person(emotions)
# print(person1)
print(person1.mood)
print(person1.get_mood())
