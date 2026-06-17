def clean_text(text):
    text = text.lower()
    text = text.strip()

    return text


sample = " PAYING SWETHA MOBILES "

print(clean_text(sample))