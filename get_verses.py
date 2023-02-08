import json
import requests
import config

class BibleVerse():
    def __init__(self, book, chapter, verse):
        self.url = "https://ajith-holy-bible.p.rapidapi.com/GetVerseOfaChapter"
        self.headers = {
	      "X-RapidAPI-Key": config.bible_api_key,
	      "X-RapidAPI-Host": "ajith-holy-bible.p.rapidapi.com"
        }

        self.book = book
        self.chapter = chapter
        self.verse = verse

    def result(self):
        query = {
            "Book": self.book,
            "chapter": self.chapter,
            "Verse": self.verse,
        }
        response = requests.request("GET", self.url, headers=self.headers, params=query)

        return f"{eval(response.text)['Output']}\n{self.book.capitalize()} {self.chapter}:{self.verse}"



# print(BibleVerse("john","3","16").result())