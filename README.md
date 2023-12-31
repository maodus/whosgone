<h1 align="center">Who's Gone?</h1>

## Project Info
Utilizing Instagram's user data download feature, this utility serves to show you all of the people that did not reciprocate your Instagram follow and vice-versa. Unlike many other web based solutions to this problem, this program can handle large data sets of follower/following user data, and does not have to rely on Instagram's annoying rate limits.

Additionally, since this application is locally operated, the risk of your Instagram account being flagged as a bot account or being rate-limited is fully mitigated.

<br/>

![dont follow you back or you dont follow back](https://i.imgur.com/DJpC2Od.png)

## Privacy
This application, as seen in the [source code](./whosgone/utils/extractor.py), will not ananylze any user data except for the user's Instagram followers and following. Nothing more is done with the data after analysis. An internet connection is **not** used nor is it required for running this program.

<br/>

## Getting Started
*This program has only been tested on Python version 3.10.2 (64 bit), so if your Python installation does not end up working with this app, please install the version that the project has been tested with*.

### Installation
1. Install [Python3](https://www.python.org/downloads/)
2. Clone the repo<br/>
```git clone https://github.com/maodus/whosgone.git```

### Usage
Before using this app, you will want to obtain your **JSON** Instagram data in the `.zip` file format. This will **NOT** work if you select the **HTML** configuration when downloading. More info [here](https://help.instagram.com/181231772500920).

1. Download your Instagram usage data. **Do not unzip the file**.
2. Run `whosgone.py`
   * For Windows CMD: ```python whosgone.py``` or ```whosgone.py```
   * For UNIX (Mac/Linux): ```python3 whosgone.py``` or ```python whosgone.py```
3. When prompted, type in a valid file path that points to your zipped data file. The zip file does not have to be inside the same directory.
4. Check out your results in `/ig_results/`.

</br>

## Roadmap
- [ ] Update the program output in order to increase readability. **(WIP)**
- [ ] Ensure cross-platform support.
- [ ] Create a graphical interface for a better user experience.
