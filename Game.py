import os
from pickle import dump, load
import random as rand
import requests as req
from bs4 import BeautifulSoup as BS

from Scrape_quotes import scrape_quotes


def get_hint(bio_link) -> str:
    """
    This function takes a bio link and returns a hint about the author's birthdate and location.
    """
    try:
        url = "https://quotes.toscrape.com"
        response = req.get(f"{url}{bio_link}")
        soup = BS(response.text, "html.parser")
        birth_date = soup.find("span", {"class": "author-born-date"}).text
        birth_place = soup.find("span", {"class": "author-born-location"}).text
        return f"The author was born on {birth_date} {birth_place}."
    except (req.exceptions.RequestException, AttributeError) as error:
        print(f"Error: {error}")
        exit(1)


def initializing(quotes) -> tuple:
    """
        Initializes the game by randomly selecting a quote from the provided list of quotes,
        selecting the corresponding author and a list of hints, and returning all necessary
        variables for the game.

        Parameters:
        quotes (list of dict): A list of dictionaries, where each dictionary contains the quote
                               text, the name of the person who said the quote, and the href
                               of the link to the person's bio.

        Returns:
        tuple: A tuple containing the following variables:
               - random_quote (dict): A dictionary containing the quote text, author name,
                                      and bio link.
               - author (str): The name of the author of the quote.
               - bio_link (str): The href of the link to the author's bio.
               - hints (list of str): A list of three hints about the author.
               - guesses_remaining (int): The number of guesses remaining for the player.
        """

    try:
        random_index = rand.randint(0, len(quotes) - 1)
        random_quote = quotes.pop(random_index)

        author = random_quote["author"]
        bio_link = random_quote["bio_link"]
        hints = [get_hint(bio_link), f"The author's first name starts with '{author[0]}'.",
                 f"The author's last name has {len(author.split()[-1])} letters."]
        rand.shuffle(hints)

        print(random_quote["text"])
        print("Who said this quote?")
        guesses_remaining = 4

        return random_quote, author, bio_link, hints, guesses_remaining

    except (IndexError, KeyError, TypeError) as error:
        print(f"Error: {error}")
        raise error


def again() -> None:
    """
        This function asks the user if they want to play the game again and exits the program if the answer is 'n'.
    """
    play_again = input("Do you want to play again? (y/n) ")
    while play_again.lower() != "y" and play_again.lower() != "n":
        play_again = input("The answer is not valid. Please type 'y' or 'n':")
    if play_again.lower() == "n":
        print("Thanks for playing!")
        exit(0)


def play_game(to_scrape) -> None:
    """
    This function starts the game and asks the user to guess the author of a random quote.
    """

    if to_scrape.lower() == "2" and os.path.exists("Quotes.pickle"):
        try:
            with open('Quotes.pickle', 'rb') as file:
                quotes = load(file)
        except FileNotFoundError:
            print("Error: Quotes.pickle not found. Scraping website instead.")
            quotes = scrape_quotes()
        except PermissionError:
            print("Error: permission denied for Quotes.pickle. Scraping website instead.")
            quotes = scrape_quotes()
    else:
        quotes = scrape_quotes()
        with open('Quotes.pickle', 'wb') as file:
            dump(quotes, file)

    if not quotes:
        print("Sorry. There are no quotes available now.")
        exit(0)

    random_quote, author, bio_link, hints, guesses_remaining = initializing(quotes)
    while 1:
        guess = input(f"You have {guesses_remaining} guesses remaining. ")
        print()
        if guess.lower() == author.lower():
            print("Congratulations! You guessed correctly.")
            again()
            print()
            random_quote, author, bio_link, hints, guesses_remaining = initializing(quotes)
            continue
        else:
            guesses_remaining -= 1
            if not hints:
                print(f"Sorry, you're out of guesses. The author was {author}.")
                again()
                print()
                random_quote, author, bio_link, hints, guesses_remaining = initializing(quotes)
                continue
            print(f"That's incorrect. {hints.pop()}")
            if guesses_remaining > 0:
                continue
