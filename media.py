import webbrowser
# Importing python library webbrowser


class Movie():
    """This Class provides a constructor to store film details \
    and a method to open the youtube video in a browser"""
    def __init__(
      self,
      film_title, film_storyline, poster_image, youtube_trailer):
        self.title = film_title
        self.storyline = film_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
