# CODSOFT-Task3-Rec# ======================================
# Recommendation System (Content-Based)
# ======================================

recommendations = {
    "action": [
        "Avengers: Endgame",
        "John Wick",
        "Mission Impossible",
        "The Dark Knight",
        "Mad Max: Fury Road"
    ],

    "comedy": [
        "3 Idiots",
        "The Hangover",
        "Home Alone",
        "Jumanji",
        "Free Guy"
    ],

    "horror": [
        "The Conjuring",
        "Annabelle",
        "IT",
        "The Nun",
        "Insidious"
    ],

    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar",
        "Dune"
    ],

    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You",
        "Your Name"
    ]
}

print("=" * 45)
print("     Movie Recommendation System")
print("=" * 45)

print("\nAvailable Categories:")
for category in recommendations:
    print("-", category)

choice = input("\nEnter your favorite category: ").lower().strip()

if choice in recommendations:
    print("\nRecommended Movies:\n")
    for i, movie in enumerate(recommendations[choice], start=1):
        print(f"{i}. {movie}")
else:
    print("\nSorry! Category not found.")
    print("Please choose from the available categories.")

print("\nThank you for using the Recommendation System!")ommendationSystem
