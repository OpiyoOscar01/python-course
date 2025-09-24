def greet_user_with_default(name="Guest",title="Mr./Ms."):
  print(f"Hello, {title} {name}!")
  print("Welcome to functional programming in Python")

#Using default title
greet_user_with_default("Alice","Dr.")
greet_user_with_default()