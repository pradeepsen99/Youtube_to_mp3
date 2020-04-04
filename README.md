# Youtube_to_mp3
Takes in youtube links from a .txt file and downloads all of the songs from there as .mp3 sound files.

### Prerequisites

You will need the latest version of Python(python3).
```
To install go to https://www.python.org/downloads/ and download the respective files for your OS.
```

You will also need to install pytube and moviepy
```
pip install pytube3
```
```
pip install moviepy
```
### Installing

To run the code 
```
python3 song_downloader.py
```

To set the songs that are needed go to songs.txt and add the links seperating each link by a new line
```
Link #1
Link #2
```

The output should be something like this:
```
Downloading: Link #1 
Downloading: Link #2
MoviePy - Writing audio in ../downloaded_songs_mp3/file_name1.mp3
MoviePy - Done. 

MoviePy - Writing audio in ../downloaded_songs_mp3/file_name2.mp3
MoviePy - Done. 
```

## Authors

* **Pradeep Senthil** - *Initial work* - [pradeepsen99](https://github.com/pradeepsen99)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
