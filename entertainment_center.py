# -*- coding: utf-8 -*-

import fresh_tomatoes
import media

#Information required for page to generate
sound_music = media.Movie("The Sound of Music",
                          "1965",
                          "A woman leaves an Austrian convent to become a governess to the children of a Naval officer widower.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
                          "https://youtu.be/KuWsQSntFf0")


arsenic = media.Movie("Arsenic and Old Lace",
                      "1944",
                      "A drama critic learns on his wedding day that his beloved maiden aunts are homicidal maniacs, and that insanity runs in his family.",
                      "https://upload.wikimedia.org/wikipedia/en/5/5a/Arsenic_And_Old_Lace_Poster.jpg",
                      "https://youtu.be/qcwLsOE2cMU")


music_man = media.Movie("The Music Man",
                        "1962",
                        "Harold Hill poses as a boys' band leader to con naive Iowa townsfolk.",
                        "https://upload.wikimedia.org/wikipedia/commons/9/9e/Original_movie_poster_for_the_film_The_Music_Man_1962.jpg",
                        "https://youtu.be/cbiBx5T2uX0")


sting = media.Movie("The Sting",
                    "1973",
                    "In Chicago in September 1936, a young con man seeking revenge for his murdered partner teams up with a master of the big con to win a fortune from a criminal banker.",
                    "https://upload.wikimedia.org/wikipedia/en/9/9c/Stingredfordnewman.jpg",
                    "https://youtu.be/LN2hBOIXhBs")



sarafina = media.Movie("Sarafina",
                       "1992",
                       "South African teenagers fight against apartheid in the Soweto Uprising.",
                       "https://upload.wikimedia.org/wikipedia/en/d/d2/Sarafina_poster.jpg",
                       "https://youtu.be/tpYaGfnnnYI")



fantasia = media.Movie("Fantasia",
                       "1940",
                       "A collection of animated interpretations of great works of Western classical music.",
                       "https://upload.wikimedia.org/wikipedia/en/1/12/Fantasia-poster-1940.jpg",
                       "https://youtu.be/yYGWLnoQDMY")

#Creates a list of movies to open
movies = [sound_music, arsenic, music_man, sting, sarafina, fantasia]

#Call to open movies list and generate HTML page
fresh_tomatoes.open_movies_page(movies)       
                    
