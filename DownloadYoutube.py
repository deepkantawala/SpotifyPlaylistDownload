import pytube as pt
import os


class GetYTSongs:
    def __init__(self, path):
        self.path = path
        self.create_path()

    def create_path(self):
        tmp = self.path.rstrip('/').split('/')
        for i in range(0, len(tmp)-1):
            if not os.path.exists('/'.join(tmp[:i+1])):
                os.mkdir('/'.join(tmp[:i+1]))

    def pytube_obj_to_dict(self, obj):
        """
        This method will convey pytube object to dict
        :param obj: pytube search object
        :return:
        """
        dict_obj = obj.__dict__
        return dict_obj['watch_url']

    def make_songs_query(self, res):
        """
        This method makes a query that will be used to get url from youtube with the help of pytube
        :param res: result from spotify api with song name and artist name
        :return:
        """
        temp_dict = {}
        for i in range(0, len(res)):
            b = res[i]
            # print(b)
            song = b['song']
            artist = b['artist']
            temp_dict[i] = f"{song} {artist}"
            # print(temp_dict)
        return temp_dict

    def map_songs_to_url(self, songs_query):
        """
        this method uses pytube to get first two url's of a youtube search query and returns a dict with song's name,
        first url, and alt url.
        :param songs_query:
        :return: returns a dict with song name, and two youtube url of that song.
        """
        temp_ulr_dict = {}
        search_error_songs = {}
        for i in range(0, len(songs_query)):
            try:

                search = pt.Search(songs_query[i])
                search_res = search.results
                url = self.pytube_obj_to_dict(search_res[0])
                alt_url = self.pytube_obj_to_dict(search_res[1])
                temp_ulr_dict[i] = {"name": songs_query[i], "first_url": url, "alt_url": alt_url}
                print(f"{i} out of {len(songs_query)} done!")
            except:
                print(f"Error searching {songs_query[i]}")
                search_error_songs[i] = songs_query[i]
        if search_error_songs:
            print(search_error_songs)
        return temp_ulr_dict

    def download_song(self, url_dict):
        """
        this method is used to download songs from youtube
        :param url_dict: a dict with song name, youtube url,and alternative url for the same song
        :return:
        """
        print("URL dict is: ", url_dict)
        for i in range(0, len(url_dict)):
            try:
                try:
                    yt = pt.YouTube(url=url_dict[i]['first_url'])
                    yt.streams.filter(only_audio=True)
                    yt.streams.get_highest_resolution().download(
                        filename=f"""{self.path.strip('/')}/{url_dict[i]['name'].replace(" ", "").replace('"', '').replace('/', '')}.mp3""")
                    print(url_dict[i]['name'], " Downloaded successfully!!")
                except Exception as e:
                    yt = pt.YouTube(url=url_dict[i]['alt_url'])
                    yt.streams.filter(only_audio=True)
                    yt.streams.get_highest_resolution().download(
                        filename=f"""{self.path.strip('/')}/{url_dict[i]['name'].replace(" ", "").replace('"', '').replace('/', '')}.mp3""")
                    print(url_dict[i]['name'], " Downloaded successfully with alt url!!")
            except Exception as e:
                print(e)
                print(f"error while downloading {url_dict[i]['name']}")

    def start(self, spotify_dict):
        """
        This is a start method for the class GetYTSongs which will call other methods in order to get the songs you want to download.
        :param spotify_dict: A dict that you get from spotify's api as response; it should contain data.
        :return:
        """
        print("Executing make_songs_query")
        query = self.make_songs_query(spotify_dict)
        print("Executing map_songs_to_url")
        url_query = self.map_songs_to_url(query)
        print("executing download_song")
        self.download_song(url_query)
