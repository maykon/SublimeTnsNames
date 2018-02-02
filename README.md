# Sublime Text 3: tnsnames.ora Plugin

Open your `tnsnames.ora` file quickly.

## Usage

 - Simply hit `Ctrl+Shift+O` (on Windows and Linux) or `⌘+Shift+O` (on OS X) to bring up your `tnsnames.ora` file
 - Or you can open it via `Command Palette`, hit `Ctrl+Shift+P` and choose `Open tnsnames.ora File`

## Installation

To install this plugin, you have two options:


1. If you have Package Control installed, hit `Ctrl+Shift+P` and select `Package Control: Add Repository` and add de url `https://github.com/maykon/SublimeTnsNames`.

2. Simply search for `SublimeTnsNames` to install.

3. Clone source code to Sublime Text packages folder.

## Settings

This plugin has a three settings. If you create a file called `SublimeTnsNames.sublime-settings` in your `User` package you can override them.

 - `win_tnsnames_file_location`: location of `tnsnames.ora` file under Windows
 - `unix_tnsnames_file_location`: location of `tnsnames.ora` file under Unix
 - `osx_tnsnames_file_location`: location of `tnsnames.ora` file under OS X

``` JSON
{
   "windows_tnsnames_file_location": "C:/oracle/product/11.2.0/client_1/network/admin/tnsnames.ora",
   "linux_tnsnames_file_location": "",
   "osx_tnsnames_file_location": ""
}
```
