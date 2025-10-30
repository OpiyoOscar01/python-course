class Dog:
  def __init__(self,name,action):
    self.name=name
    self.action=action
  def instruct(self):
    print(f"Hello {self.name} {self.action}")
  def assign_trainer(self,trainer):
    print(f"Hi {self.name},your trainer is {trainer}")

dog1=Dog("Bob","Jump")
dog1.instruct()
dog1.assign_trainer("Steve")