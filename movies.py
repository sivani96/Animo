import media
import animo

toy_story = media.Movie("Toy Story",
                        "A cowboy's story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



minion = media.Movie("Despicable Me",
                     "Minion rush",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Despicable_Me_Poster.jpg/220px-Despicable_Me_Poster.jpg",
                     "https://www.youtube.com/watch?v=TZkAcKCFIVo")


ratatoullie = media.Movie("Ratatoullie",
                          "A rat becomes a cook",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

cars = media.Movie("Cars",
                   "Racing Car",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Cars_2006.jpg/220px-Cars_2006.jpg",
                   "https://www.youtube.com/watch?v=WGByijP0Leo")

monster = media.Movie("Monsters Inc.",
                      "Monster's Land",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Monsters_Inc.JPG/220px-Monsters_Inc.JPG",
                      "https://www.youtube.com/watch?v=cvOQeozL4S0")

cloudy = media.Movie("Couldy with a chance of meat balls",
                     "Foad from the sky",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Cloudy_with_a_chance_of_meatballs_theataposter.jpg/220px-Cloudy_with_a_chance_of_meatballs_theataposter.jpg",
                     "https://www.youtube.com/watch?v=3xuCL6DSBA4")


movies = [toy_story, minion, ratatoullie, cars, monster, cloudy]
animo.open_movies_page(movies)

