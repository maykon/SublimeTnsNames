# Sublime Text 3: TNSNamesORA Plugin

Open your `tnsnames.ora` file quickly.

## Usage

 - Simply hit `Ctrl+Shift+O` (on Windows and Linux) or `⌘+Shift+O` (on OS X) to bring up your `tnsnames.ora` file
 - Or you can open it via `Command Palette`, hit `Ctrl+Shift+P` and choose `Open TNSNames File`

## Installation

To install this plugin, you have two options:

1. If you have Package Control installed, simply search for `TNSNamesORA` to install.

2. Clone source code to Sublime Text packages folder.

## Settings

This plugin has a three settings. If you create a file called `SublimeTNSNamesORA.sublime-settings` in your `User` package you can override them.

 - `win_tnsnames_file_location`: location of `tnsnames.ora` file under Windows
 - `unix_tnsnames_file_location`: location of `tnsnames.ora` file under Unix
 - `osx_tnsnames_file_location`: location of `tnsnames.ora` file under OS X

``` JSON
{
   //PATH to `hosts` file depending on system
   "windows_tnsnames_file_location": "C:/Windows/System32/drivers/etc/hosts",
   "linux_tnsnames_file_location": "",
   "osx_tnsnames_file_location": ""
}
```
