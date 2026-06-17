def clean_text(text):
    text = text.lower()
    text = " ".join(text.split())

    return text


sample = "   PAYING    SWETHA      MOBILES   "

print(clean_text(sample))
