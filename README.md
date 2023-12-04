# Finance-Tracker-App
Finance Tracker App for CS 1530 Software Engineering

# How to run the web application (Windows):

After cloning the repository:

1. Make sure you have Python installed
2. Activate the virtual environment by opening the terminal (preferably in VSCode) and while in the repository's directory, type .\Scripts\activate (this command is Windows only)
    * Important Note: Some Windows users will get an error in the above command. 
                    One possible cause of such problem is the execution policy in  
                    your computer. To check what policy you have in your computer 
                    and change it if necessary is shown below:
        1.   Select Start > All Programs > Windows PowerShell version > Windows PowerShell.
        2.  Type Set-ExecutionPolicy RemoteSigned to set the policy to RemoteSigned.
        3. Type Set-ExecutionPolicy Unrestricted to set the policy to Unrestricted.
        4.  Type Get-ExecutionPolicy to verify the current settings for the execution policy.
        5.   Type Exit.
3. You should see (Finance-Tracker-App) next to your command line now
4. Run the main python script by typing py main.py / python main.py / python3 main.py etc.
5. CTRL + click on the link where it says "Running on <link>" to open the web app
