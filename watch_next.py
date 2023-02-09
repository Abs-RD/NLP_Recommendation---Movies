import spacy

# the model to be used
nlp = spacy.load('en_core_web_md')

# recently watched movie description
Planet_Hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""


# function to return which movies a user would watch next if they have watched Planet Hulk
# The function should take in the description as a parameter and return the title of the most similar movie.

def next_movie(description):
    # declare and initialize a list to store movies list
    movies_list = []
    
    # read data from movies.txt file
    with open("movies.txt", "r") as movies_file:
        for i in movies_file:
            movies = i.split(':')
            movies_list.append(movies)


    nlp_sentence = nlp(description)

    # declare and initialize list to store similarity values
    similarity_list = []
 
    # check the similarity between the movie description and the recently watched movie description
    for i in range(0, len(movies_list)):
        similarity_list.append(nlp(movies_list[i][1]).similarity(nlp_sentence))

    # find the maximum similarity value and its index
    max_similarity = max(similarity_list)    
    max_similarity_index = similarity_list.index(max_similarity)

    # return the title of the most similar movie
    return movies_list[max_similarity_index][0]

# call the function
print(f"Recommended movie to watch is {next_movie(Planet_Hulk)}")

