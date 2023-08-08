# Flatlist

Small utility to install flatpaks from a list and update. To use simply run the following:

```
git clone https://github.com/xXCoolinXx/flatlist
cd flatlist
python flatlist.py
```
On the first run, everything you have already installed via the `flatpak` command will populate in the `flatpaks.txt` file. 

To add new flatpaks, you can simply add their `com.app.app` name to the end of the `flatpaks.txt`. This name can be found by searching with `flatpak search <app>`.

In the future, command line flags may be added to search for and add new flatpaks to the file, as well as to remove flatpaks from the file. 

This approach is inspired by [Nix](https://nixos.org), a declarative package manager. 
