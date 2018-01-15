# Welcome:
You have found my notes for Applications of Quantum Mechanics, Chem231B at UCI (Winter 2018). 

Topics included are: (TBD)

## Instructors:
The instructor for the course is `Dr. Shaul Mukamel`.

#### Lecture:
MWF 10-10:50(am); PSCB 240

#### Discussions:
`Tuesday:` 1-1:50(pm); SSL 159. 

`Friday:` 12-12:50(pm); DBH 142. 

#### Textbook:
The suggested text for the class are:

Quantum Mechanics, Volume 1 and 2. Claude Cohen-Tannoudji, Bernard Diu, Frack Laloe
Publisher: Wiley-VCN, ISBN 978-0-471-164-33-3


## Lecture_notes:
Directory containing typed Lecture Notes from the course. 
Each lecture is written in a LaTex file (name.tex) and compiled to pdf. 

## Github Crashcourse
Github is essentially a tool for source control (tracking a document in time, saving all verisons and changes made to that document), and for working with other people.
Highlight working with others, we will use this tool to develop lecture notes for this course.
This is made extremly easy, you just need to read the below guide and should be ready to contribute to this project in a few minutes!
Please note: The tutorial will be for running on a mac, if you are using a different operating system the idea is the same, but you will need to look up your specific operating system install process (windows people may want to look into git bash). 

#### Github Install
To get started you will need to make a `Github` account; Please Note: most people see/use Github as a professional tool. 
Remember that when making your account (*(*(*_*)*)*)
You may find Github to be a useful tool and continue to use it in the future. 
If you use an edu email you will get access to some extra tools in Github which  may be useful in your future developments.

To make an account head over to the [GitHub](http://github.com) website and follow thier directions. 
With y our new github account you have access to the tools of Github, the online repository functionality.
However, you are not going to be working online, you will want to work on your local machine (your laptop).
To do this we need the second half of the software, known as `git`.

#### Git Install
On mac git will actually come installed on your device.
It will be an older version of git and you should really get the most recent version. 
To do this you are going to need Xcode and the Xcode command line tools, on mac you can follow the [Xcode](https://github.com/swflynn/fortran_tutorials/tree/master/fortran_crashcourse/00) install section here (Note: Just scroll down to the Xcode install section, you do not need anything else). 

Now that you have Xcode on your machine you can go download [Git}(https://git-scm.com/downloads). 
Run the dmg file and follow the prompts to get Git.
Once the install is done type the following into your terminal to make sure everything worked (do not type $, it just implies to be typed into terminal). 

`git --version`

Now that you have a working version of git you will want to set-up your username and email address on your laptop.
I would suggest using the same name and password as you used on Github since we are going to be using these accounts together. 

`$ git config --global user.name "your name here"`

`$ git config --global user.email "your_name@domain.ext"`

With this done you should now have both a Github account (on teh internet) and a Git account (on your local device).
Remember, we use the git account on our local machine to develop material, we then pass that to the Github account on the internet for everyone to use.

#### Git and Github Workflow
As you can see I have already made a Github Repo for the Course, so you will just need to copy it, make changes, and add them back to here. 

I suggest making a directory on yor local machine for ALL of your Github projects (this is just a suggestion, but most people make one location for all their projects locally). 
To do this make a directory somewhere on your coputer, you can name it whatever you want (`$ mkdir ~/Desktop/github`) is an example. 
Move to this directory, and inside it we are going to make a copy of this QM repo.
To do that use the following command

`$ git clone "url"`

Replace "url" with the url found on the [Github](https://github.com/swflynn/Courses_UCI) repo page under teh green tab called `Clone or Download`
As of writing this would translate to `git clone https://github.com/swflynn/Courses_UCI.git`. 

After this runs you should see all of the resources from the Github on your local machine.
Please note, this is a `clone` of the Github account, that you now own (it is indepedent of the version made by swflynn). 
You can make changes to everything within this file, it will only appear on your local machine, and not on the original Github owned by swflynn. 

Because the original repo (owned by swflynn) will be constantly changing as everyone develops and adds material we need to be sure we stay up-to-date.
To do this, before you start working on your own local copy (everytime you plan to work!) you should check to make sure you are up-to-date (fetch the online repo and merge it with your own).
This is done with the following command:

`$ git pull`

Now that you have an up-to-date version of the repo you are ready to make changes.
Open files, editthem, do whatever you want (Remember it is impossible to 'break' anything this is all your local version). 

Once you have made some changes  to things and want to save them type the following command

`$ git status`

This shows you all changes that you have made from the previouslys aved version of the repo (on your local account). 

To save all the changes you will need to tell git. 
A simple way to do this in one step is the following

`$ git add .`

Which will add all changes  to be  saved. 

Finally we needto commit to saving these changes. 
This is done using

`$git commit -m "add a brief message summarixing changes"`

The message should be short and informative, i.e. (update lecture 2 notes). 

With this done we have now saved our changes to the repo!
The next step is to push tehse changes to your (not swflynn) Github account for the world to see!

`$ git push`



