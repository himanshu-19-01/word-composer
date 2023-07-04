import speech_recognition as sr
import pyttsx3
import random
import Levenshtein
import os
def pronounce_word(word):
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.8)  # Volume level (0.0 to 1.0)
    engine.say(word)
    engine.runAndWait()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice.id)

    engine.setProperty('voice', voices[0].id)  # Set the first voice from the available options


def score_pronunciation(word, spoken_word):
    distance = Levenshtein.distance(word, spoken_word)
    max_distance = max(len(word), len(spoken_word))
    similarity = 1 - (distance / max_distance)
    score = similarity * 100
    return score

def listen_and_score(word):
    recognizer = sr.Recognizer()

    print("Please speak the word:", word)
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        spoken_word = recognizer.recognize_google(audio)
        print("You pronounced:", spoken_word)
        
        r_score = score_pronunciation(word, spoken_word)
        score=round(r_score,2)
        print("Your score:", score)
        return spoken_word,score
    except sr.UnknownValueError:
        print("Sorry, could not understand your pronunciation.")
        return "Sorry, could not understand your pronunciation."
def main():
    words = ["Pa", "Ka", "Ma", "Sa", "Co", "Ga", "Gu"]

    while True:
        sequence_length = int(input("Enter the length of the sequence: "))
        sequence = random.choices(words, k=sequence_length)
        word = "".join(sequence)

        print("Word to pronounce:", word)

        pronounce_word(word)
        listen_and_score(word)

        choice = input("Do you want to hear the correct pronunciation? (y/n): ")
        if choice.lower() == "y":
            pronounce_word(word)

        repeat = input("Do you want to try again? (y/n): ")
        if repeat.lower() != "y":
            break

if __name__ == "__main__":
    main()