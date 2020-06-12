# Data Mining and Machine Learning 2020
# Group Number 2    ->  [Raz Malka | Shoham Yamin | Raz Itzhak Afriat]
# Research Subject  ->  One-Class SVMs for Document Classification

# This file is meant to represent simple constants for the whole system
from enum import Enum

version = "v0.13"

# MAIN
root_title = "One-Class SVMs for Document Classification - G2"
root_width = 900
root_height = 588

# WINDOW
about_title = "About"
about_header = "\nOne-Class SVM Document Classification\nVersion - " + version
repository_link = "https://github.com/RazMalka/SVM-DC"
about_footer = "MIT License © 2020\n\nRaz Malka\tShoham Yamin\tRaz Itzhak Afriat"
about_width = 400
about_height = 180

representations = ["Binary", "Frequency", "TF-IDF", "Hadamard"]
kernel_types    = ["Linear", "Radial"]
#training_sets = ["-", "Harry Potter", "Game of Thrones"]

# REPRESENT
m       = 10    # Amount of Keywords Taken
special = [".", ",", "’", "“", "”", "—", "?", "!", "|", "-", ";", ":", '\'', "`",
            "said", "look", "get", "have", "had", "has", "page", "chapter", "got", "no",
            "yes", "know", "dont", "do", "did", "didnt", "thing", "us", "we", "them"]

class BookSet(Enum):
    ALL = 1
    HARRY_POTTER = 2
    GAME_OF_THRONES = 3
    THE_HUNGER_GAMES = 4
    GODS_OF_SPACE = 5
    FORSYTE_SAGA = 6
    CHILD_OF_THE_SUN = 7

# Book List

books = ["Book 1 - The Philosopher's Stone (A).txt_1000.txt",
"Book 1 - The Philosopher's Stone (A).txt_10000.txt",
"Book 1 - The Philosopher's Stone (A).txt_11000.txt",
"Book 1 - The Philosopher's Stone (A).txt_12000.txt",
"Book 1 - The Philosopher's Stone (A).txt_13000.txt",
"Book 1 - The Philosopher's Stone (A).txt_14000.txt",
"Book 1 - The Philosopher's Stone (A).txt_15000.txt",
"Book 1 - The Philosopher's Stone (A).txt_16000.txt",
"Book 1 - The Philosopher's Stone (A).txt_2000.txt",
"Book 1 - The Philosopher's Stone (A).txt_3000.txt",
"Book 1 - The Philosopher's Stone (A).txt_4000.txt",
"Book 1 - The Philosopher's Stone (A).txt_5000.txt",
"Book 1 - The Philosopher's Stone (A).txt_6000.txt",
"Book 1 - The Philosopher's Stone (A).txt_7000.txt",
"Book 1 - The Philosopher's Stone (A).txt_8000.txt",
"Book 1 - The Philosopher's Stone (A).txt_9000.txt",
'Book 2 - The Chamber of Secrets (A).txt_1000.txt',
'Book 2 - The Chamber of Secrets (A).txt_10000.txt',
'Book 2 - The Chamber of Secrets (A).txt_11000.txt',
'Book 2 - The Chamber of Secrets (A).txt_12000.txt',
'Book 2 - The Chamber of Secrets (A).txt_13000.txt',
'Book 2 - The Chamber of Secrets (A).txt_14000.txt',
'Book 2 - The Chamber of Secrets (A).txt_15000.txt',
'Book 2 - The Chamber of Secrets (A).txt_16000.txt',
'Book 2 - The Chamber of Secrets (A).txt_17000.txt',
'Book 2 - The Chamber of Secrets (A).txt_2000.txt',
'Book 2 - The Chamber of Secrets (A).txt_3000.txt',
'Book 2 - The Chamber of Secrets (A).txt_4000.txt',
'Book 2 - The Chamber of Secrets (A).txt_5000.txt',
'Book 2 - The Chamber of Secrets (A).txt_6000.txt',
'Book 2 - The Chamber of Secrets (A).txt_7000.txt',
'Book 2 - The Chamber of Secrets (A).txt_8000.txt',
'Book 2 - The Chamber of Secrets (A).txt_9000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_1000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_10000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_11000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_12000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_13000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_14000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_15000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_16000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_17000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_18000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_19000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_2000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_20000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_21000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_22000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_3000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_4000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_5000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_6000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_7000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_8000.txt',
'Book 3 - The Prisoner of Azkaban (A).txt_9000.txt',
'Book 4 - The Goblet of Fire (A).txt_1000.txt',
'Book 4 - The Goblet of Fire (A).txt_10000.txt',
'Book 4 - The Goblet of Fire (A).txt_11000.txt',
'Book 4 - The Goblet of Fire (A).txt_12000.txt',
'Book 4 - The Goblet of Fire (A).txt_13000.txt',
'Book 4 - The Goblet of Fire (A).txt_14000.txt',
'Book 4 - The Goblet of Fire (A).txt_15000.txt',
'Book 4 - The Goblet of Fire (A).txt_16000.txt',
'Book 4 - The Goblet of Fire (A).txt_17000.txt',
'Book 4 - The Goblet of Fire (A).txt_18000.txt',
'Book 4 - The Goblet of Fire (A).txt_19000.txt',
'Book 4 - The Goblet of Fire (A).txt_2000.txt',
'Book 4 - The Goblet of Fire (A).txt_20000.txt',
'Book 4 - The Goblet of Fire (A).txt_21000.txt',
'Book 4 - The Goblet of Fire (A).txt_22000.txt',
'Book 4 - The Goblet of Fire (A).txt_23000.txt',
'Book 4 - The Goblet of Fire (A).txt_24000.txt',
'Book 4 - The Goblet of Fire (A).txt_25000.txt',
'Book 4 - The Goblet of Fire (A).txt_26000.txt',
'Book 4 - The Goblet of Fire (A).txt_27000.txt',
'Book 4 - The Goblet of Fire (A).txt_28000.txt',
'Book 4 - The Goblet of Fire (A).txt_29000.txt',
'Book 4 - The Goblet of Fire (A).txt_3000.txt',
'Book 4 - The Goblet of Fire (A).txt_30000.txt',
'Book 4 - The Goblet of Fire (A).txt_31000.txt',
'Book 4 - The Goblet of Fire (A).txt_32000.txt',
'Book 4 - The Goblet of Fire (A).txt_33000.txt',
'Book 4 - The Goblet of Fire (A).txt_34000.txt',
'Book 4 - The Goblet of Fire (A).txt_35000.txt',
'Book 4 - The Goblet of Fire (A).txt_36000.txt',
'Book 4 - The Goblet of Fire (A).txt_37000.txt',
'Book 4 - The Goblet of Fire (A).txt_38000.txt',
'Book 4 - The Goblet of Fire (A).txt_4000.txt',
'Book 4 - The Goblet of Fire (A).txt_5000.txt',
'Book 4 - The Goblet of Fire (A).txt_6000.txt',
'Book 4 - The Goblet of Fire (A).txt_7000.txt',
'Book 4 - The Goblet of Fire (A).txt_8000.txt',
'Book 4 - The Goblet of Fire (A).txt_9000.txt',
'Book 5 - The Order of the Phoenix (A).txt_1000.txt',
'Book 5 - The Order of the Phoenix (A).txt_10000.txt',
'Book 5 - The Order of the Phoenix (A).txt_11000.txt',
'Book 5 - The Order of the Phoenix (A).txt_12000.txt',
'Book 5 - The Order of the Phoenix (A).txt_13000.txt',
'Book 5 - The Order of the Phoenix (A).txt_14000.txt',
'Book 5 - The Order of the Phoenix (A).txt_15000.txt',
'Book 5 - The Order of the Phoenix (A).txt_16000.txt',
'Book 5 - The Order of the Phoenix (A).txt_17000.txt',
'Book 5 - The Order of the Phoenix (A).txt_18000.txt',
'Book 5 - The Order of the Phoenix (A).txt_19000.txt',
'Book 5 - The Order of the Phoenix (A).txt_2000.txt',
'Book 5 - The Order of the Phoenix (A).txt_20000.txt',
'Book 5 - The Order of the Phoenix (A).txt_21000.txt',
'Book 5 - The Order of the Phoenix (A).txt_22000.txt',
'Book 5 - The Order of the Phoenix (A).txt_23000.txt',
'Book 5 - The Order of the Phoenix (A).txt_24000.txt',
'Book 5 - The Order of the Phoenix (A).txt_25000.txt',
'Book 5 - The Order of the Phoenix (A).txt_26000.txt',
'Book 5 - The Order of the Phoenix (A).txt_27000.txt',
'Book 5 - The Order of the Phoenix (A).txt_28000.txt',
'Book 5 - The Order of the Phoenix (A).txt_29000.txt',
'Book 5 - The Order of the Phoenix (A).txt_3000.txt',
'Book 5 - The Order of the Phoenix (A).txt_30000.txt',
'Book 5 - The Order of the Phoenix (A).txt_31000.txt',
'Book 5 - The Order of the Phoenix (A).txt_32000.txt',
'Book 5 - The Order of the Phoenix (A).txt_33000.txt',
'Book 5 - The Order of the Phoenix (A).txt_34000.txt',
'Book 5 - The Order of the Phoenix (A).txt_35000.txt',
'Book 5 - The Order of the Phoenix (A).txt_36000.txt',
'Book 5 - The Order of the Phoenix (A).txt_37000.txt',
'Book 5 - The Order of the Phoenix (A).txt_38000.txt',
'Book 5 - The Order of the Phoenix (A).txt_39000.txt',
'Book 5 - The Order of the Phoenix (A).txt_4000.txt',
'Book 5 - The Order of the Phoenix (A).txt_40000.txt',
'Book 5 - The Order of the Phoenix (A).txt_41000.txt',
'Book 5 - The Order of the Phoenix (A).txt_42000.txt',
'Book 5 - The Order of the Phoenix (A).txt_43000.txt',
'Book 5 - The Order of the Phoenix (A).txt_44000.txt',
'Book 5 - The Order of the Phoenix (A).txt_45000.txt',
'Book 5 - The Order of the Phoenix (A).txt_46000.txt',
'Book 5 - The Order of the Phoenix (A).txt_47000.txt',
'Book 5 - The Order of the Phoenix (A).txt_48000.txt',
'Book 5 - The Order of the Phoenix (A).txt_49000.txt',
'Book 5 - The Order of the Phoenix (A).txt_5000.txt',
'Book 5 - The Order of the Phoenix (A).txt_50000.txt',
'Book 5 - The Order of the Phoenix (A).txt_6000.txt',
'Book 5 - The Order of the Phoenix (A).txt_7000.txt',
'Book 5 - The Order of the Phoenix (A).txt_8000.txt',
'Book 5 - The Order of the Phoenix (A).txt_9000.txt',
'Book 6 - The Half Blood Prince (A).txt_1000.txt',
'Book 6 - The Half Blood Prince (A).txt_10000.txt',
'Book 6 - The Half Blood Prince (A).txt_11000.txt',
'Book 6 - The Half Blood Prince (A).txt_12000.txt',
'Book 6 - The Half Blood Prince (A).txt_13000.txt',
'Book 6 - The Half Blood Prince (A).txt_14000.txt',
'Book 6 - The Half Blood Prince (A).txt_15000.txt',
'Book 6 - The Half Blood Prince (A).txt_16000.txt',
'Book 6 - The Half Blood Prince (A).txt_17000.txt',
'Book 6 - The Half Blood Prince (A).txt_18000.txt',
'Book 6 - The Half Blood Prince (A).txt_19000.txt',
'Book 6 - The Half Blood Prince (A).txt_2000.txt',
'Book 6 - The Half Blood Prince (A).txt_20000.txt',
'Book 6 - The Half Blood Prince (A).txt_21000.txt',
'Book 6 - The Half Blood Prince (A).txt_22000.txt',
'Book 6 - The Half Blood Prince (A).txt_23000.txt',
'Book 6 - The Half Blood Prince (A).txt_24000.txt',
'Book 6 - The Half Blood Prince (A).txt_25000.txt',
'Book 6 - The Half Blood Prince (A).txt_26000.txt',
'Book 6 - The Half Blood Prince (A).txt_27000.txt',
'Book 6 - The Half Blood Prince (A).txt_28000.txt',
'Book 6 - The Half Blood Prince (A).txt_29000.txt',
'Book 6 - The Half Blood Prince (A).txt_3000.txt',
'Book 6 - The Half Blood Prince (A).txt_30000.txt',
'Book 6 - The Half Blood Prince (A).txt_31000.txt',
'Book 6 - The Half Blood Prince (A).txt_32000.txt',
'Book 6 - The Half Blood Prince (A).txt_33000.txt',
'Book 6 - The Half Blood Prince (A).txt_4000.txt',
'Book 6 - The Half Blood Prince (A).txt_5000.txt',
'Book 6 - The Half Blood Prince (A).txt_6000.txt',
'Book 6 - The Half Blood Prince (A).txt_7000.txt',
'Book 6 - The Half Blood Prince (A).txt_8000.txt',
'Book 6 - The Half Blood Prince (A).txt_9000.txt',
'Book 7 - The Deathly Hallows (A).txt_1000.txt',
'Book 7 - The Deathly Hallows (A).txt_10000.txt',
'Book 7 - The Deathly Hallows (A).txt_11000.txt',
'Book 7 - The Deathly Hallows (A).txt_12000.txt',
'Book 7 - The Deathly Hallows (A).txt_13000.txt',
'Book 7 - The Deathly Hallows (A).txt_14000.txt',
'Book 7 - The Deathly Hallows (A).txt_15000.txt',
'Book 7 - The Deathly Hallows (A).txt_16000.txt',
'Book 7 - The Deathly Hallows (A).txt_17000.txt',
'Book 7 - The Deathly Hallows (A).txt_18000.txt',
'Book 7 - The Deathly Hallows (A).txt_19000.txt',
'Book 7 - The Deathly Hallows (A).txt_2000.txt',
'Book 7 - The Deathly Hallows (A).txt_20000.txt',
'Book 7 - The Deathly Hallows (A).txt_21000.txt',
'Book 7 - The Deathly Hallows (A).txt_22000.txt',
'Book 7 - The Deathly Hallows (A).txt_23000.txt',
'Book 7 - The Deathly Hallows (A).txt_24000.txt',
'Book 7 - The Deathly Hallows (A).txt_25000.txt',
'Book 7 - The Deathly Hallows (A).txt_26000.txt',
'Book 7 - The Deathly Hallows (A).txt_27000.txt',
'Book 7 - The Deathly Hallows (A).txt_28000.txt',
'Book 7 - The Deathly Hallows (A).txt_29000.txt',
'Book 7 - The Deathly Hallows (A).txt_3000.txt',
'Book 7 - The Deathly Hallows (A).txt_30000.txt',
'Book 7 - The Deathly Hallows (A).txt_31000.txt',
'Book 7 - The Deathly Hallows (A).txt_32000.txt',
'Book 7 - The Deathly Hallows (A).txt_33000.txt',
'Book 7 - The Deathly Hallows (A).txt_34000.txt',
'Book 7 - The Deathly Hallows (A).txt_35000.txt',
'Book 7 - The Deathly Hallows (A).txt_36000.txt',
'Book 7 - The Deathly Hallows (A).txt_37000.txt',
'Book 7 - The Deathly Hallows (A).txt_38000.txt',
'Book 7 - The Deathly Hallows (A).txt_39000.txt',
'Book 7 - The Deathly Hallows (A).txt_4000.txt',
'Book 7 - The Deathly Hallows (A).txt_5000.txt',
'Book 7 - The Deathly Hallows (A).txt_6000.txt',
'Book 7 - The Deathly Hallows (A).txt_7000.txt',
'Book 7 - The Deathly Hallows (A).txt_8000.txt',
'Book 7 - The Deathly Hallows (A).txt_9000.txt',
'Book 8 - A clash of Kings (B).txt_1000.txt',
'Book 8 - A clash of Kings (B).txt_10000.txt',
'Book 8 - A clash of Kings (B).txt_11000.txt',
'Book 8 - A clash of Kings (B).txt_12000.txt',
'Book 8 - A clash of Kings (B).txt_13000.txt',
'Book 8 - A clash of Kings (B).txt_14000.txt',
'Book 8 - A clash of Kings (B).txt_15000.txt',
'Book 8 - A clash of Kings (B).txt_16000.txt',
'Book 8 - A clash of Kings (B).txt_17000.txt',
'Book 8 - A clash of Kings (B).txt_18000.txt',
'Book 8 - A clash of Kings (B).txt_19000.txt',
'Book 8 - A clash of Kings (B).txt_2000.txt',
'Book 8 - A clash of Kings (B).txt_20000.txt',
'Book 8 - A clash of Kings (B).txt_21000.txt',
'Book 8 - A clash of Kings (B).txt_22000.txt',
'Book 8 - A clash of Kings (B).txt_3000.txt',
'Book 8 - A clash of Kings (B).txt_4000.txt',
'Book 8 - A clash of Kings (B).txt_5000.txt',
'Book 8 - A clash of Kings (B).txt_6000.txt',
'Book 8 - A clash of Kings (B).txt_7000.txt',
'Book 8 - A clash of Kings (B).txt_8000.txt',
'Book 8 - A clash of Kings (B).txt_9000.txt',
'Book 9 - A dance with Dragons (B).txt_1000.txt',
'Book 9 - A dance with Dragons (B).txt_10000.txt',
'Book 9 - A dance with Dragons (B).txt_11000.txt',
'Book 9 - A dance with Dragons (B).txt_12000.txt',
'Book 9 - A dance with Dragons (B).txt_13000.txt',
'Book 9 - A dance with Dragons (B).txt_14000.txt',
'Book 9 - A dance with Dragons (B).txt_15000.txt',
'Book 9 - A dance with Dragons (B).txt_16000.txt',
'Book 9 - A dance with Dragons (B).txt_17000.txt',
'Book 9 - A dance with Dragons (B).txt_18000.txt',
'Book 9 - A dance with Dragons (B).txt_19000.txt',
'Book 9 - A dance with Dragons (B).txt_2000.txt',
'Book 9 - A dance with Dragons (B).txt_20000.txt',
'Book 9 - A dance with Dragons (B).txt_21000.txt',
'Book 9 - A dance with Dragons (B).txt_22000.txt',
'Book 9 - A dance with Dragons (B).txt_23000.txt',
'Book 9 - A dance with Dragons (B).txt_24000.txt',
'Book 9 - A dance with Dragons (B).txt_3000.txt',
'Book 9 - A dance with Dragons (B).txt_4000.txt',
'Book 9 - A dance with Dragons (B).txt_5000.txt',
'Book 9 - A dance with Dragons (B).txt_6000.txt',
'Book 9 - A dance with Dragons (B).txt_7000.txt',
'Book 9 - A dance with Dragons (B).txt_8000.txt',
'Book 9 - A dance with Dragons (B).txt_9000.txt',
'Book 10 - A feast for crows (B).txt_1000.txt',
'Book 10 - A feast for crows (B).txt_10000.txt',
'Book 10 - A feast for crows (B).txt_11000.txt',
'Book 10 - A feast for crows (B).txt_12000.txt',
'Book 10 - A feast for crows (B).txt_13000.txt',
'Book 10 - A feast for crows (B).txt_14000.txt',
'Book 10 - A feast for crows (B).txt_15000.txt',
'Book 10 - A feast for crows (B).txt_16000.txt',
'Book 10 - A feast for crows (B).txt_17000.txt',
'Book 10 - A feast for crows (B).txt_18000.txt',
'Book 10 - A feast for crows (B).txt_19000.txt',
'Book 10 - A feast for crows (B).txt_2000.txt',
'Book 10 - A feast for crows (B).txt_20000.txt',
'Book 10 - A feast for crows (B).txt_3000.txt',
'Book 10 - A feast for crows (B).txt_4000.txt',
'Book 10 - A feast for crows (B).txt_5000.txt',
'Book 10 - A feast for crows (B).txt_6000.txt',
'Book 10 - A feast for crows (B).txt_7000.txt',
'Book 10 - A feast for crows (B).txt_8000.txt',
'Book 10 - A feast for crows (B).txt_9000.txt',
'Book 11 - A game of Throne (B).txt_1000.txt',
'Book 11 - A game of Throne (B).txt_10000.txt',
'Book 11 - A game of Throne (B).txt_11000.txt',
'Book 11 - A game of Throne (B).txt_12000.txt',
'Book 11 - A game of Throne (B).txt_13000.txt',
'Book 11 - A game of Throne (B).txt_14000.txt',
'Book 11 - A game of Throne (B).txt_15000.txt',
'Book 11 - A game of Throne (B).txt_16000.txt',
'Book 11 - A game of Throne (B).txt_17000.txt',
'Book 11 - A game of Throne (B).txt_2000.txt',
'Book 11 - A game of Throne (B).txt_3000.txt',
'Book 11 - A game of Throne (B).txt_4000.txt',
'Book 11 - A game of Throne (B).txt_5000.txt',
'Book 11 - A game of Throne (B).txt_6000.txt',
'Book 11 - A game of Throne (B).txt_7000.txt',
'Book 11 - A game of Throne (B).txt_8000.txt',
'Book 11 - A game of Throne (B).txt_9000.txt',
'Book 12 - A storm of Swords (B).txt_1000.txt',
'Book 12 - A storm of Swords (B).txt_10000.txt',
'Book 12 - A storm of Swords (B).txt_11000.txt',
'Book 12 - A storm of Swords (B).txt_12000.txt',
'Book 12 - A storm of Swords (B).txt_13000.txt',
'Book 12 - A storm of Swords (B).txt_14000.txt',
'Book 12 - A storm of Swords (B).txt_15000.txt',
'Book 12 - A storm of Swords (B).txt_16000.txt',
'Book 12 - A storm of Swords (B).txt_17000.txt',
'Book 12 - A storm of Swords (B).txt_18000.txt',
'Book 12 - A storm of Swords (B).txt_19000.txt',
'Book 12 - A storm of Swords (B).txt_2000.txt',
'Book 12 - A storm of Swords (B).txt_20000.txt',
'Book 12 - A storm of Swords (B).txt_21000.txt',
'Book 12 - A storm of Swords (B).txt_22000.txt',
'Book 12 - A storm of Swords (B).txt_23000.txt',
'Book 12 - A storm of Swords (B).txt_24000.txt',
'Book 12 - A storm of Swords (B).txt_25000.txt',
'Book 12 - A storm of Swords (B).txt_26000.txt',
'Book 12 - A storm of Swords (B).txt_27000.txt',
'Book 12 - A storm of Swords (B).txt_28000.txt',
'Book 12 - A storm of Swords (B).txt_3000.txt',
'Book 12 - A storm of Swords (B).txt_4000.txt',
'Book 12 - A storm of Swords (B).txt_5000.txt',
'Book 12 - A storm of Swords (B).txt_6000.txt',
'Book 12 - A storm of Swords (B).txt_7000.txt',
'Book 12 - A storm of Swords (B).txt_8000.txt',
'Book 12 - A storm of Swords (B).txt_9000.txt',
'Book 13 - The Hunger Games (C).txt_1000.txt',
'Book 13 - The Hunger Games (C).txt_2000.txt',
'Book 14 - Catching Fire (C).txt_1000.txt',
'Book 14 - Catching Fire (C).txt_2000.txt',
'Book 15 - Mockingjay 1 (C).txt_1000.txt',
'Book 15 - Mockingjay 1 (C).txt_2000.txt',
'Book 15 - Mockingjay 1 (C).txt_3000.txt',
'Book 15 - Mockingjay 1 (C).txt_4000.txt',
'Book 16 - Mockingjay 2 (C).txt_1000.txt',
'Book 16 - Mockingjay 2 (C).txt_2000.txt',
'Book 16 - Mockingjay 2 (C).txt_3000.txt',
'Book 16 - Mockingjay 2 (C).txt_4000.txt',
'Book 16 - Mockingjay 2 (C).txt_5000.txt',
'Book 16 - Mockingjay 2 (C).txt_6000.txt',
'Book 16 - Mockingjay 2 (C).txt_7000.txt',
'Book 16 - Mockingjay 2 (C).txt_8000.txt',
'Book 17 - Gods of Space (D).txt_1000.txt',
'Book 17 - Gods of Space (D).txt_2000.txt',
'Book 18 - Monster of the Asteroid (D).txt_1000.txt',
'Book 18 - Monster of the Asteroid (D).txt_2000.txt',
'Book 19 - The Star-Master (D).txt_1000.txt',
'Book 19 - The Star-Master (D).txt_2000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_1000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_10000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_11000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_12000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_13000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_14000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_15000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_2000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_3000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_4000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_5000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_6000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_7000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_8000.txt',
'Book 20 - The Forsyte Saga Vol I (E).txt_9000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_1000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_10000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_11000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_12000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_13000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_14000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_15000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_2000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_3000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_4000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_5000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_6000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_7000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_8000.txt',
'Book 21 - The Forsyte Saga Vol II (E).txt_9000.txt',
'Book 22 - Child of the Sun (F).txt_1000.txt',
'Book 22 - Child of the Sun (F).txt_2000.txt',
'Book 23 - The Cosmic Derelict (F).txt_1000.txt',
'Book 23 - The Cosmic Derelict (F).txt_2000.txt',
'Book 24 - Meteor-Men of Mars (F).txt_1000.txt',
'Book 24 - Meteor-Men of Mars (F).txt_2000.txt',
'Book 25 - Pied Piper of Mars (F).txt_1000.txt',
'Book 25 - Pied Piper of Mars (F).txt_2000.txt',
'Book 26 - Stellar Showboat (F).txt_1000.txt',
'Book 26 - Stellar Showboat (F).txt_2000.txt']

# Precalculated Data for Efficiency

binary_x_train = [[1,0,1,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,1,1,1,1,1,1],
[1,0,1,0,1,1,1,1,1,1],
[1,0,1,0,1,1,1,1,1,1],
[1,1,1,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1]]

binary_x_test = [[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,0,1,1,1,0,1,0],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1,1,1],
[1,0,0,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[1,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[1,0,0,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[0,0,1,0,0,0,1,1,1,1],
[1,0,0,0,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1,1,1]]

binary_keywords = ['harry', 'ron', 'pot', 'herm', 'jk', 'rowl', 'al', 'nt', 'ther', 'back']