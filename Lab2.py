def print_student_info(student):
    first_name = student["full_name"].split()[0]
    print(f"My name is {student['full_name']}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student['student_id']}.")
def add_pizza_toppings(student, toppings):
    student["pizza_toppings"].extend(toppings)
    student["pizza_toppings"] = sorted(student["pizza_toppings"])
    student["pizza_toppings"] = [topping.lower() for topping in student["pizza_toppings"]]
def print_pizza_toppings(student):
    print("My favourite pizza toppings are:")
    for i, topping in enumerate(student["pizza_toppings"]):
        print(f"- {topping}")
def print_movie_genres(student):
    genres = [movie["genre"] for movie in student["movies"]]
    num_genres = len(genres)
    genre_str = ", ".join(genres[:-1]) + " and " + genres[-1] if num_genres > 1 else genres[0]
    print(f"I like to watch {genre_str} movies.")
def print_movie_titles(movies):
    movie_titles = [movie["title"].title() for movie in movies]
    last_title = movie_titles.pop()
    fav_movies_string = ", ".join(movie_titles)
    print(f"Some of my favourite movies are {fav_movies_string} and {last_title}!")
def main():
    student = {
        "full_name": "Jayrajsinh Chavda",
        "student_id": 10285803,
        "pizza_toppings": ["PEPPERONI", "MUSHROOMS", "OLIVES"],
        "movies": [
            {"title": "the godfather", "genre": "crime"},
            {"title": "the Shawshank Redemption", "genre": "drama"}
        ]
    }
    student["movies"].append({"title": "the Dark Knight", "genre": "action"})
    print_student_info(student)
    print_pizza_toppings(student)
    add_pizza_toppings(student, ("SAUSAGE", "BACON"))
    print_pizza_toppings(student)
    print_movie_genres(student)
    print_movie_titles(student['movies'])
if __name__ == "__main__":
    main()