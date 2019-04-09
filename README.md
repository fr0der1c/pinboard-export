# pinboard-export

Export your Pinboard bookmarks in Netscape bookmark HTML format.

## Why I made this?
I no longer use Pinboard and I want to export all my Pinboard bookmarks to Chrome. Pinboard can only backup (export) all bookmarks without tag information so it is useless in my case. Having no option, I have to write a script to solve my own problem.

## Features
This script can seamlessly migrate your Pinboard bookmarks to Chrome, transforming all tags to folders. If you use slash `/` in tags, you can get nested folders. For example, if you have tags:
```
Design/Prototype
Design/SVG
Design/Keynote
```

You will get nested folder:
```
- Design
  - Prototype
  - SVG
  - Keynote
```

Really neat. Isn't it?

## Usage
1. Install Python dependencies: `pip install -r requirements.txt`
1. Fill in your Pinboard API Key
1. Run `python export.py`
1. Import generated `pinboard.html` in Chrome bookmark manager