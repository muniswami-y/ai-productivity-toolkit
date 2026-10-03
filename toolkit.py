def summarize(text):
    return ask(f"Summarize this in one sentence: {text}")

def classify(text):
    return ask(f"Classify this as Positive or Negative: {text}")

def write_email(topic):
    return ask(f"Write a short professional email about: {topic}", 80)

def improve_resume_line(line):
    return ask(f"Rewrite this resume line to sound more professional: {line}", 40)

def explain_code(code):
    return ask(f"Explain what this code does in simple words: {code}", 60)
