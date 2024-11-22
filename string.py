def best_food():
  message = "I love pasta"
  message = "I love penne pasta"
  return message

print(best_food())

#personal message
def my_name():
  first_name = "rafatullah"
  last_name = "ogirima"
  full_name = f"{first_name} {last_name}"
  message = f"Hello {full_name.title()} how are you?"
  return message

print(my_name())

#Name Cases
def full_name():
  first_name = "abdulhameed"
  last_name = "Ogirima"
  full_name = f"{first_name.upper()} {last_name.title()}"
  return full_name

print(full_name())

#Famous Quote
def famous_quote():
  message = "A person who never made a mistake never tried anything new."
  authors_quote = f"albert einstein once said '{message.title()}'"
  return authors_quote

print(famous_quote())

#Famous Quote 2
def famous_quote():
  famous_person = "albert einstein"
  message = "A person who never made a mistake never tried anything new."
  authors_quote = f"{famous_person.title()} once said '{message.title()}'"
  return authors_quote

print(famous_quote())

#Stripping Names
def persons_name():
  first_name =" Aishah"
  middle_name =" Abike "
  last_name =" Badmus"
  full_name = f"{first_name.lstrip()}\t\t\n {middle_name.strip()}\n {last_name.rstrip()} "
  return full_name

print(persons_name())

#file Extensions
def file_extension():
  filename = "python_notes.txt"
  return filename.removesuffix(".txt")

print(file_extension())
