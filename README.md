# Journey Journal
Journey Journal is an app for the modern explorer who would like to record and save their adventures. Journey Journal is a digitial travel jounal. If you have ever wanted to jouornal and remeber your trips, but don't want to take pen and paper with you on your travels, then Journey Journal is the app you've been waiting for.Journey JOurnal is a Django web-app written in python with the Django framework. 

<h2>Instructions for Installing Journey Journal</h2>

<h4> You will need to have command line tools installed for your computer to use terminal commands.
</h4>

  * Mac users - Open your terminal and type

    ```sh
    git --version
    ```

  * Linux/Windows users, please vist the [Git page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow the instructions for setup

<h4>You will now need to configure your git account. In the terminal window, type</h4>

  ```sh
  git config –global user.name “You Name”
  git config –global user.email “Your Email”
  ```

#### Create a new directory to store the files in. Type this into your terminal window.

  ```sh
  mkdir journeyJournal
  cd journeyJournal
  git clone git@github.com:amazoradi/Journey-Journal.git
  ```

#### If you do not have Python version 3 installed on your machine, visit the [Python Download Page](https://www.python.org/downloads/) or to install with command line,

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
```


#### Now you need to install all dependencies. We recommend using a virtual environment to prevent these from being installed globally.

#### First install virtualenv and create and enter a virtual environment, in the containing "Bangazon" folder:
```sh
pip install --user virtualenv
virtualenv myenv
source myenv/bin/activate
```
#### To install dependencies navigate to the cloned repository which contains a 'requirements.txt' file then run pip install requirements.txt

```sh
cd journeyJournal
pip install -r requirements.txt
```

#### Create the database by changing the permissions on this shell script and executing it with the following commands:

```sh
chmod +x django_data.sh
./django_data.sh website
```


#### You can now run the program by typing(You must be in the directory that contains the 'manage.py' file):

```sh
python manage.py runserver 8080
```
 #### navigate to localhost:8080 to access the website
 <h1 style="text-align:center; font-weight: bold;">Congratulations! You are now experiencing Journey Journal! </h1>

