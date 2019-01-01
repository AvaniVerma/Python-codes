import webbrowser


class Movie():

    """This is a class description.
This class lists properties of movie."""
    
    def __init__(self, title, story, poster, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
