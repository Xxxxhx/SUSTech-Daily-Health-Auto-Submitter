# SUSTech Daily Health Auto Submitter

This is a daily health auto submitter for SUSTech students

## Warning

This program is written for my convenience, and I am not going to responsible for any consequences of using it.

## Prerequisites

- Python 3
- pywin32
- Windows (I don't have a Mac and welcome you to contribute your code for Mac users)

## Usage

### Fill the Form

Before the first time you use the script, you need to fill the fields in `content.json` and `header.json`

- `content.json`
    - `type`: I believe that 1 is for undergraduate students and 2 is for postgraduate students.
    - `dept`: I don't know the relationship between this field and the department. So I recommand you submit the report on your browser(Chrome/Edge) in develop mode and find this value.

- `header.json`
    - `userId`: Your SID


### Run

Make sure to open Wechat and place it on the taskbar, then run the following command:

```
python submit.py
```