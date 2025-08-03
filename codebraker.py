"""
Code Breaker App

Encodes or decodes messages using frequency analysis from two predetermined key texts.
Maps each letter in the input message to a letter in the second key phrase based on frequency order.
"""

from collections import Counter

# Print welcome message
print("Welcome to my Code Breaker App!")

# Define non-letter characters to remove from input
non_letter_chars = " 0123456789.,;:!?'\"()[]{}<>-_=+`~@#$%^&*|\\/\n\t"

# Hardcoded key phrases for frequency analysis
key_phrase_1 = """
MY LORDS!” he shouted, his voice booming off the rafters. “Here is what I say to these
two kings!” He spat. “ Renly Baratheon is nothing to me, nor Stannis neither. Why
should they rule over me and mine, from some flowery seat in Highgarden or Dorne?
What do they know of the Wall or the wolfswood or the barrows of the First Men? Even
their gods are wrong. The Others take the Lannisters too, I’ve had a bellyful of them.” He
reached back over his shoulder and drew his immense two-handed greatsword. “Why
shouldn’t we rule ourselves again? It was the dragons we married, and the dragons are
all dead!” He pointed at Robb with the blade. “There sits the only king I mean to bow my
knee to, m’lords,” he thundered. “The King in the North!”
And he knelt, and laid his sword at her son’s feet.
“I’ll have peace on those terms,” Lord Karstark said. “They can keep their red castle and
their iron chair as well.” He eased his longsword from its scabbard. “The King in the
North!” he said, kneeling beside the Greatjon.
Maege Mormont stood. “The King of Winter!” she declared, and laid her spiked mace
beside the swords. And the river lords were rising too, Blackwood and Bracken and
Mallister, houses who had never been ruled from Winterfell, yet Catelyn watched them
rise and draw their blades, bending their knees and shouting the old words that had not
been heard in the realm for more than three hundred years, since Aegon the Dragon had
come to make the Seven Kingdoms one . . . yet now were heard again, ringing from the
timbers of her father’s hall:
“The King in the North!”
“The King in the North!”
“THE KING IN THE NORTH!”
"""

# Normalize and clean key_phrase_1
key_phrase_1 = key_phrase_1.lower()
for non_letter_char in non_letter_chars:
    key_phrase_1 = key_phrase_1.replace(non_letter_char, '')

# Frequency analysis for key_phrase_1
total_occurrences = len(key_phrase_1)
letter_counter = Counter(key_phrase_1)

# Print frequency table for key_phrase_1
print(f"\nFrequency analysis for: 'key_phrase_1'")
print("\nLetter\tOccurrence\tPercentage")
for key, value in sorted(letter_counter.items()):
    percentage = 100 * value / total_occurrences
    percentage = round(percentage, 2)
    print(f"{key}\t{value}\t\t{percentage}%")

# Build ordered letter list by frequency for key_phrase_1
ordered_letter_count = letter_counter.most_common()
key_phrase_1_ordered_letters = [pair[0] for pair in ordered_letter_count]

# Print ordered letters for key_phrase_1
print("\nLetters ordered by frequency:")
print(", ".join(key_phrase_1_ordered_letters))

# Hardcoded second key phrase for cipher mapping
key_phrase_2 = """
“And what of my wrath, Lord Stark?” she asked softly. Her eyes
searched his face. “You should have taken the realm for yourself. It was there for the
taking. Jaime told me how you found him on the Iron Throne the day King’s Landing
fell, and made him yield it up. That was your moment. All you needed to do was climb
those steps, and sit. Such a sad mistake.”
“I have made more mistakes than you can possibly imagine,” Ned said, “but that was not
one of them.”
“Oh, but it was, my lord,” Cersei insisted. “When you play the game of thrones, you win
or you die. There is no middle ground.”
.
"""

# Normalize and clean key_phrase_2
key_phrase_2 = key_phrase_2.lower()
for non_letter_char in non_letter_chars:
    key_phrase_2 = key_phrase_2.replace(non_letter_char, '')

# Frequency analysis for key_phrase_2
total_occurrences_2 = len(key_phrase_2)
letter_counter_2 = Counter(key_phrase_2)

# Print frequency table for key_phrase_2
print(f"\nFrequency analysis for: 'key_phrase_2'")
print("\nLetter\tOccurrence\tPercentage")
for key, value in sorted(letter_counter_2.items()):
    percentage = 100 * value / total_occurrences_2
    percentage = round(percentage, 2)
    print(f"{key}\t{value}\t\t{percentage}%")

# Build ordered letter list by frequency for key_phrase_2
ordered_letter_count_2 = letter_counter_2.most_common()
key_phrase_2_ordered_letters = [pair[0] for pair in ordered_letter_count_2]

# Print ordered letters for key_phrase_2
print("\nLetters ordered by frequency:")
print(", ".join(key_phrase_2_ordered_letters))

# Prompt user for encode/decode choice and message
choice = input("\n\nWould you like to encode or decode a message: ").lower()
phrase = input("What is the phrase: ").lower()

# Clean user message
for non_letter_char in non_letter_chars:
    phrase = phrase.replace(non_letter_char, '')

# Encode message using frequency mapping
if choice == "encode":
    encoded_phrase = []
    for letter in phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)
    print("\nThe Encoded message is:")
    print("".join(encoded_phrase))

# Decode message using frequency mapping
elif choice == "decode":
    decoded_phrase = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)
    print("\nThe Decoded message is:")
    print("".join(decoded_phrase))

# Handle invalid option
else:
    print("Please enter either 'encode' or 'decode' as your choice. Try again.")

print("\n\nThank you for using the Code Breaker App!")