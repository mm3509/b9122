# Steps for Windows users

Install git bash from here: [https://gitforwindows.org/](https://gitforwindows.org/)

Launch "git bash" (which has an icon with four colors).

In some cases, that's all you need. If you can run this command and see a version, your setup is ready:

``` bash
$ python --version
Python 3.12.4
```

If that doesn't work, you can run the Conda setup with:

```
. /c/Anaconda3/etc/profile.d/conda.sh
```

In that case, run this command, so every git bash shell is connected to Anaconda:

``` bash
echo ". /c/Anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
```

If that fails, you need to find where Conda is installed. Start an **Anaconda Command Shell** (not git bash, nor CMD, nor PowerShell, nor Anaconda PowerShell Prompt---I know, it's confusing), and type:

``` bash
where anaconda
```

You then need to find the location of the `conda.sh` file around that directry. Once you find it, e.g. if it is `C:\Users\User-Name\AppData\Local\Continuum\Anaconda2\Scripts\profile.d\conda.sh`, then you shoudl run this command in **git bash** (notice the replacement of backslash with forward slash, and the conversion of `C:/` to `/c/`):

``` bash
echo ". /c/Users/User-Name/AppData/Local/Continuum/Anaconda2/Scripts/profile.d/conda.sh" >> ~/.bashrc
```

Please ask us or the TAs for help, or refresh the page to see the latest version of this guide.
