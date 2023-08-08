# Flatlist

Small utility to install flatpaks from a list and update. To use simply run the following:

```
git clone https://github.com/xXCoolinXx/flatlist
cd flatlist
python flatlist.py
```
On the first run, everything you have already installed via the `flatpak` command will populate in the `flatpaks.txt` file. 

To add new flatpaks, you can simply add their `com.app.app` name to the end of the `flatpaks.txt`, or by installing them using the `flatpak` CLI and then running the script to add it to the `.txt` file. The application ID can be found by searching with `flatpak search <app>`.

Currently, you will have to both run `flatpak remove <app>` and remove it from the `flatpaks.txt` to remove the app entirely. In the future, a command line flag may be added to do this automatically.

This approach is inspired by [Nix](https://nixos.org), a declarative package manager. 
