![version](https://img.shields.io/github/manifest-json/v/linto-ai/vox_harvest) ![release](https://img.shields.io/github/v/release/linto-ai/vox_harvest)

# Vox Harvest
Vox Harvest is a simple GUI tool to record your voice and create a corpus in order to train a Text-To-Speech model.

**Disclaimer: This is an early development version published at this point for testing purposes. You might encounter bugs and broken functionalities.**

## Introduction
VH allows you to:
* Manage and prepare texts.
* Record your voice.

## Getting started
You can either use the source or the binary release.

**Using release is the recommended way as dependencies are sizable.**

### **From release**
Release are compiled version of the software directly usable.

Supported OS are:
* Ubuntu: [here](https://github.com/linto-ai/vox_harvest/releases/download/v0.1.2/vox_harvest-v0.1.2-ubuntu.tar.gz)
* Windows 10: [here](https://github.com/linto-ai/vox_harvest/releases/download/v0.1.2/vox_harvest-v0.1.2-windows.zip)

[*Note that windows version doesn't have a certificate yet and will trigger a unsigned warning.*]

### **From source**
For Linux only.

1. **Clone this repository.**
```bash
git clone https://github.com/Lokhozt/vox_harvest.git
cd vox_harvest
```

2. **Install dependencies.**
``` sudo apt-get update
sudo apt-get install portaudio19-dev python3 python3-pip
```
VH requires QT5 installed : [Qt Website](https://www.qt.io/download-qt-installer?hsCtaTracking=99d9dd4f-5681-48d2-b096-470725510d34%7C074ddad0-fdef-4e53-8aa8-5e8a876d6ab4)

3. **Install python dependencies**

It is recommended to work inside a virtual python environement.

(optional)
```bash
#create the venv
VENV_PATH=/path/to/venv
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python3 --no-site-packages $VENV_PATH
#activate the venv
source $VENV_PATH/bin/activate
```

Install python dependencies

```bash
cd vox_harvest
pip install -r requirements.txt
``` 

## Use it.
Launch vox harvest
1. Create a project
2. Add texts
3. Record

### **Launch vox harvest**

**On Linux**

Go into the vox_harvest folder extracted from the release archive.
```bash
./voxharvest
```
**On Window**

Execute the vox_harvest.exe in the folder extracted from the release archive.

**From sources**

Execute the main.py script.
```bash
(venv)$ python main.py
```

### **1. Create a project**
On the home screen click on `Create project`

![create screen](https://i.imgur.com/1XbPy42.png)

* Set the project's name, location and the speaker name.
* Set the audio parameters. (You won't be able to change it later {yet}).

Click on `create`.

A folder will be created at the selected location which contain several files:
* <project_name.proj> contains the project info. 
* text_bank.txt will contain the text to read.
* metadata.csv and the audio folder contain the audio and the transcriptions once you start recording.

Once the project is created, you gain access to the 3 tabs on the left hand side.
* The home tab display statistics and progression.
* The text tab allow you to add text to be read.
* The record tab allow you to record your voice.

### **2. Add text**
Go to the text tab (The book icon).

![text screen](https://i.imgur.com/9lbGyTG.png)

There is 2 options to add text:
* `Add raw text`: Add unformated text from a file. The text will be splitted in sentences and normalized (number and abbreviation will be extended).
* `Add formated text`: Add already formated text - One sentence per line and number and abbreviations already replaced.

### **3. Record**
Go the record tab (The microphone icon).

![record screen](https://i.imgur.com/4PYYfCf.png)

The text to read is displayed at the top.
* `Skip`: Go to the next sentence.
* `Split at cursor`: If the sentence is to long you can split it by setting you cursor to a location in the text and clicking the button. The text after the cursr will be placed as the next sentence.
* `Remove`: Remove the sentence from the text bank.

The displayed text to read is editable so you can, if necessary, change the text if there are mistakes, unextended abbreviations, number, ... The text saved in the metadata will be the text as it is when you validate the sample.

To record your sample:
* `Record`: (>Space<)Start the recording.
* `Stop`: (>Space<)Stop the recording.
* `Listen`: (>L<)Listen the recording.
* `Validate and next`: (>Enter<) The sample and its text is added to the recorded audio, go to the next sentence.

[The shortcuts will be modifiable in a future version]

## What Next ?
Once you have recorded enough of your voice and you want to build your own Text-to-speech you can take a look at (Mozilla-TTS)[https://github.com/mozilla/TTS]. 

## Licence
This software is published under the (GNU Affero v3)[http://www.gnu.org/licenses/agpl-3.0.html] Licence as it is whitout any garanty.