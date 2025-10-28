antworten = {}
with open("antworten.txt", "r", encoding="utf-8") as f:
    for line in f:
        if ";" in line:
            eingabe, antwort = line.strip().split(";", 1)
            antworten[eingabe.lower()] = antwort

print("Hallo! Ich bin dein Lern-Chatbot. Schreibe 'exit', um zu beenden.")

while True:
    user_input = input("Du: ").lower()

    if user_input == "exit":
        print("Chatbot: Tschüss! Bis bald.")
        break

    # Antwort suchen
    gefunden = False
    for key in antworten:
        if key in user_input:
            print("Chatbot:", antworten[key])
            gefunden = True
            break

    if not gefunden:
        print("Chatbot: Interessant! Wie soll ich darauf antworten?")
        neue_antwort = input("Deine Antwort: ")
        antworten[user_input] = neue_antwort

        # Neue Antwort speichern
        with open("antworten.txt", "a", encoding="utf-8") as f:
            f.write(f"{user_input};{neue_antwort}\n")
        print("Chatbot: Danke! Ich habe dazu gelernt.")
