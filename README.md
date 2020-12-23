# Youtube_to_mp3

Downloads specified YouTube videos and converts them into a specified .mp3 format.

### Prerequisites

- You will need Python version 3.9.0 for this to function. (Later versions not tested as of yet)
- setuptools
- [pydub](https://github.com/jiaaro/pydub)
- pip3
- [ffmpeg](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up) (Click on the link to see how to setup ffmpeg on different platforms)

## Installing the required 

On Mac with Homebrew:
```bash
brew install python@3.9
```
For other systems:
```
To install go to https://www.python.org/downloads/ and download the respective files for your OS.
```

You will also need to install 'setuptools' in order for the build to work.
```bash
pip3 install setuptools
```
## Installing

To run the code, go to the code directory and execute the following.
```bash
python3 setup build && python3 setup install && audiodl
```
This will both install the required prerequisites and launch the application.

To set the videos that are needed go to links.txt and add the links seperating each link by a new line:
```
Link #1
Link #2
```

The output should be something like this:
```zsh
❯ audiodl
[ DEBUG   ] Starting download worker processes...
[ INFO    ] Downloading https://www.youtube.com/watch?v=
[ INFO    ] Downloading https://www.youtube.com/watch?v=
[ SUCCESS ] Downloaded https://www.youtube.com/watch?v=
[ SUCCESS ] Downloaded https://www.youtube.com/watch?v=
[ DEBUG   ] Exiting download process.
[ INFO    ] Starting conversion of /Users/user/Downloads/Downloaded_Videos.
[ DEBUG   ] Input : /Users/user/Downloads/Downloaded_Videos
[ DEBUG   ] Output : /Users/user/Downloads/Converted_Videos
[ DEBUG   ] Workers : 5
[ DEBUG   ] Starting the conversion worker processes...
[ INFO    ] Converting 'Video File 1' to format 'mp3'...
[ INFO    ] Converting 'Video File 2' to format 'mp3'...
[ SUCCESS ] 'Video File 2' converted!
[ SUCCESS ] 'Video File 1' converted!
[ SUCCESS ] See /Users/user/Downloads/Converted_Videos for converted audio.
```

## Changing location configuration

You can change the directory where the songs.txt file is located. In addition, you can change the download locations for YouTube downloads and conversions inside the *main.py* file.
```python
c = Config(
  verbose=True,
  yt_dl_path=Path.home().as_posix() + "/Downloads/Downloaded_Videos", <- YouTube downloads location
  convert_path=Path.home().as_posix() + "/Downloads/Converted_Videos", <- Converted file location
  workers=5,
  out_format=".mp3"
)
link_file = Path.home().as_posix() + "/Downloads/links.txt"
```
By default on MacOS, YouTube downloads are at: */Users/user/Downloads/Downloaded_Videos*, converted files are located at: */Users/user/Downloads/Converted_Videos*, and links.txt is located at: */Users/user/Downloads/*

> For now this is the way to add links for downloads. Future updates will make it easier.
## Authors

* **Pradeep Senthil** - *Initial work* - [pradeepsen99](https://github.com/pradeepsen99)
* **Arnas Amankavicius** - *Contribution* - [ArnasAmankavicius](https://github.com/ArnasAmankavicius)

## Disclaimer & Fair Use Statement

This application may download copyrighted material, the use of which may not have been specifically authorized by the copyright owner. The material downloaded, with the use of this application, must be used without profit for research and educational purposes.

This should constitute a 'fair use' of any such copyrighted material (referenced and provided for in section 107 of the US Copyright Law).

If you wish to use any copyrighted material downloaded with the use of this application for purposes of your own that go beyond 'fair use', you must obtain expressed permission from the copyright owner.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
