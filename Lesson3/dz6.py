def int_func(text):
    return text.title()

print(int_func("cat"))

def int_func(text):
  return ' '.join(word[:1].upper() + word[1:] for word in text.split(' '))
print(int_func("we will rock you"))