# Steps for Windows users

Unfortunately, Anaconda does not install a shell that is fully compatible with Unix (macOS and Linux). Therefore, please install `git bash`, which is fully compatible.

## Step 1: install git bash

1. Download and install Git for Windows from: [www.gitforwindows.org](https://gitforwindows.org).

2. Say OK to all the default settings.

3. Add the program to the task bar or your shortcuts. You should see this symbol:

<img src="https://avatars.githubusercontent.com/u/4571183?s=200&amp;v=4" width="100" height="100" alt="@git-for-windows">

4. Launch git bash.

5. In some cases, this is all you need. If you can run this command in **git bash** (not Anaconda PowerShell Prompt) and you see a version, your setup is ready and you can exit this guide.

``` bash
$ python --version
Python 3.12.4
```

## Step 2: find the Conda initialization file

### Step 2.1: test default Conda initialization file

If that doesn't work, you will need to find the location of Anaconda Python to connect it to git bash.

1. To see if Anaconda Python is in the default location, run this command in **git bash** (not Anaconda PowerShell Prompt):

``` bash
. /c/Anaconda3/etc/profile.d/conda.sh
```

If the command succeeds, your Anaconda location is the default. The location `/c/Anaconda3/etc/profile.d/conda.sh` is the path for the Conda initialization. Remember this path and continue to Step 3.

### Step 2.2: find non-default Conda initialization file.

If the command fails, you need to find the location for Anaconda.

1. Open a text editor, like Notepad:

<img src="https://play-lh.googleusercontent.com/jD8waDJPN1yv4OdcB6_ILw9M4kyNPdtgBYtoTiPrYhxA1l4FLSKXXe4kAcDCjmtZmQ4=w240-h480" />

3. Run an **ANACONDA COMMAND PROMPT SHELL** (it's different from a Git Bash shell!). To do so, in the Windows search box, search for "Anaconda prompt", look for it, and press Enter to run it.

4. Type this command (and notice it's **conda**, not **anaconda**):

``` bash
where conda
```

You should see a list of paths that start with `C:\Users\...`. The first line ends with `conda.bat`. Take the first line and copy it into Notepad. Remove the text starting from `\Library`, change the initial `C:\` to `/c/`, and change all backslashes to forward slashes, from `\` to `/`. You should then see something like this in Notepad: `/c/Users/your-username/anaconda3`.

<img src="https://play-lh.googleusercontent.com/jD8waDJPN1yv4OdcB6_ILw9M4kyNPdtgBYtoTiPrYhxA1l4FLSKXXe4kAcDCjmtZmQ4=w240-h480" />

Now add this text to the end of path on Notepad: `/etc/profile.d/conda.sh`, so it becomes something like this:  `/c/Users/your-username/anaconda3/etc/profile.d/conda.sh`. This is your path for the Conda initialization. Remember this path and continue to Step 3.

<img src="https://play-lh.googleusercontent.com/jD8waDJPN1yv4OdcB6_ILw9M4kyNPdtgBYtoTiPrYhxA1l4FLSKXXe4kAcDCjmtZmQ4=w240-h480" />

## Step 3: connect git bash to Anaconda Python

4. In a **Git Bash shell** (not a CMD shell, nor a Power Shell, nor an Anaconda shell), edit the code below so the first line uses the Conda initialization path from steps 2.1 or 2.2 . Notice the space between the period and that path. Then press ENTER:

``` bash
echo ".    <your-conda-initialization-path-from-step-2>" >> ~/.bash_profile
echo "conda activate" >> ~/.bash_profile
echo 'alias python3="python"' >> ~/.bash_profile
```

Note that the last line creates an alias to call `python` whenever you type `python3`. This is for compatibility with my material (because some computers have both `python` for Python 2 and `python3` for Python 3).

For these changes to take effect, close your shell and open a new one. Then, every new Git Bash session will have conda available and automatically activate the base environment.

## Errors

### multiple tries

If you tried this multiple times and it still fails, clearing duplicate lines can help. Run this command in **git bash**:

``` bash
notepad ~/.bash_profile
```

which opens Notepad with a file. Check for existing Conda-related lines and remove duplicate source commands or manual exports lines (such as `export PATH=...`) that point to Conda. If your already tried multiple setups, clearing these lines helps prevent activation errors and duplicated prompts.

You may have an additional configuration file. Run this command:

``` bash
notepad ~/.bashrc
```

If this file has no lines, the file is not the source of the problem, so close Notepad. If you see any lines, please do the same procedure as above for the `~/.bash_profile` to clear any incorrect or conflicting lines and prevent activation errors or duplicated prompts.

### setup still fails

If you still have issues with git bash after this guide, please come to Office Hours and we will fix it for you. You can also contact Lianchen, who has a Windows computer and experience in setting up students' computers.

### Running Python opens the App store

If Windows open the Microsoft Store when you run `python` in a shell, please remove the execution aliases. Go to Settings > Apps and features > App Execution Aliases and turn off the items called "App Installer" that start with `python` and end with `.exe`. See [this thread](https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor/1461471#1461471) for details.

<img src="https://i.sstatic.net/cbdFj.png">
