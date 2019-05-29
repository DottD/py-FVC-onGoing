# py-FVC-onGoing

This is a Python template for FVC-onGoing Fingerprint Orientation Extraction competition.

## How to use

* Download this repo

```bash
git clone https://github.com/DottD/py-FVConGoing.git
```

* Edit the file `fvc_extract.py`, putting your algorithm in it. If you need external files, put them next to it.

* The two files `Extractor.exe` and `fvc_extract.py`, and all your additional files must be put into a [Python embeddable distribution for Win32](https://www.python.org/ftp/python/3.7.3/python-3.7.3-embed-win32.zip).

* Any extra dependencies, must be installed in a system-wide version of Python 3 for Win32; then, copy the relevant folders in `<your-syswide-python>\Lib\site-packages` to the `Lib` folder inside the Python embeddable folder (eventually create it). Finally, add `/Lib` to the `pythonXX_.pth` file in your embeddable distribution.

## How to contribute

By now, the only supported competition is _Fingerprint Orientation Extraction_. If you need to participate to other competitions of FVC-onGoing and you wish to contribute to this repo, please let me know, and I'll point you to the right direction privately.
