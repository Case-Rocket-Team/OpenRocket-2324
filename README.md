# Repository Name

This repository uses a `pre-commit` hook to automatically unzip `.ork` files and stage them for commit. The script for this hook is stored in `commit-hook.py` at the root of the repository.

## Setting Up the `pre-commit` Hook

1. **Ensure Python 3 is installed:** The script is written in Python 3. You can check if you have Python 3 installed by opening a terminal/command prompt and typing `python3 --version`. If Python 3 is installed, this will display the version number. If not, you'll need to [install Python 3](https://www.python.org/downloads/).

2. **Ensure Git is installed:** You can check if you have Git installed by opening a terminal/command prompt and typing `git --version`. If Git is installed, this will display the version number. If not, you'll need to [install Git](https://git-scm.com/downloads).

### Linux/MacOS

1. Open a terminal in the root directory of your Git repository.

2. Run the following command to copy the `pre-commit` hook to the correct location:

    ```bash
    cp commit-hook.py .git/hooks/pre-commit
    ```
3. Make the script executable:
    
    ```bash
    chmod +x .git/hooks/pre-commit
    ```

### Windows

1. Open a command prompt in the root directory of your Git repository.

2. Run the following command to copy the `pre-commit` hook to the correct location:
    ```bash
    copy commit-hook.py .git\hooks\pre-commit
    ```
    
## Configuring the `pre-commit` Hook

The `pre-commit` hook needs to know where your `.ork` files are stored. By default, it assumes they are in the same directory as the script. If your `.ork` files are stored in a different directory, you'll need to update the `ORK_DIR` variable in the `pre-commit` hook.

### Linux/MacOS

1. Find the absolute path of the directory where you have the github repository. You can do this by navigating to the directory in a terminal and running `pwd`.

2. Open the `pre-commit` hook in your favorite text editor. You can do this directly from the terminal. For example, if you use `nano`, you would run `nano .git/hooks/pre-commit`.

3. Find the line that looks like this:

    ```python
    ORK_DIR = 'path_to_your_ork_files'
    ```
4. Replace `'path_to_your_ork_files'` with the absolute path you found in step 1. Make sure to keep the quotation marks. The line should now look something like this:
    ```python
    ORK_DIR = '/home/username/OpenRocket-2324'
    ```
5. Save the file and exit the text editor


## Windows

1. Find the absolute path of the directory where your .ork files are stored. You can do this by navigating to the directory in File Explorer, clicking on the address bar, and copying the address.

2. Open the pre-commit hook in your favorite text editor. You might need to navigate to the .git\hooks directory in File Explorer, right-click on the pre-commit file, and choose Open with.

3. Find the line that looks like this:

    ```python
    ORK_DIR = 'path_to_your_ork_files'
    ```

4. Replace 'path_to_your_ork_files' with the absolute path you found in step 1. Make sure to keep the quotation marks, and use forward slashes (/) instead of backslashes (\). The line should now look something like this:

    ```python
    ORK_DIR = 'C:/Users/username/my_repository/ork_files'
    ```

5. Save the file and exit the text editor.


## Using the `pre-commit` Hook

Once the `pre-commit` hook is set up, it will run automatically every time you run `git commit`. It will unzip any `.ork` files in the specified directory, delete the zipped versions, and stage the unzipped files for commit.

If you need to change the directory where your `.ork` files are stored, edit the `ORK_DIR` variable in the `pre-commit` script.

Remember that this hook only runs on your local machine - it doesn't get shared when you push to a remote repository. If you're collaborating with others, they will have to set up the same hook on their own machines.
