# instaDownloader
Instagram posts and profile picture downloader in python

## Features
- Bulk post downloaer
- Profile picture download
- Login for download post from private accounts
- Download stories (require login)
- Create zip archive with downloaded post
- Check if the profile is public or private
- Command line usage

## Usage
Execute the instaDow.py file and select the option:

`1. -- Download post from pubblic profile`

`2. -- Donload profile picture`

`3. -- Login and download post from private profile`

`4. -- Create an archive from downloaded directory`

`5. -- Check profile`

`6. -- Get profile info from username`

## Usage (Command Line)
 `instaDow.py --azione 5 --username ladygaga` or `instaDow.py --a 5 --u ladygaga`
 
 This performs step 5 (Check profile) on the username ladygaga

## Requirements
- instaloader
```
pip insall instaloader
```
- argparse
```
pip insall argparse 
```

## Prewiew
![1](./Screenshot/Screenshot_1.png)

![2](./Screenshot/Screenshot_2.png)

![3](./Screenshot/Screenshot_3.png)

![4](./Screenshot/Screenshot_4.png)

![5](./Screenshot/Screenshot_5.png)
