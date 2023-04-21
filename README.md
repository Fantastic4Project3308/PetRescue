# FurEver Pet: Pet Rescue and Adoption Website

Welcome to the FurEver Pet Adoption Website! This platform helps users find their perfectly matching pet(s) based on various criteria, offering a warm and welcoming experience.

## Table of Contents

- [Team Information](#team-information)
- [Project Overview](#project-overview)
- [Repository Contents](#repository-contents)
- [Getting Started](#getting-started)
- [Acknowledgement](#acknowledgement)

## Team Information
**Team # 4 (Fantastic Four)**
* Mayra Weidner - MYWeidner, mawe7753@colorado.edu
* Brittany Bilotti - brbi1248 - brbi1248@colorado.edu
* Mayumi Shimobe - Mayumi-GT - mash8545@colorado.edu
* Zack Cheng - zacktcheng - tsch3115@colorado.edu

**Weekly Meetings**: Fridays at 12 PM MST (30 min to 1 hr via Zoom) from Feb to May 2023.

## Project Overview

### Project title
Pet Adoption Website

### Vision Statement
To create a website that allows people to search for a pet that is best suited for them based on a variety of criteria. We hope to produce a working website that looks warm and welcoming with our newfound html skills that can pull the user's criteria from a sql database.

### Motivation
We have a passion for rescuing animals and a deep desire to connect those with the same values with an animal in need.

### Risks and Mitigation Strategies
**Risks**:
* Only one team member has limited experience in HTML and SQL while the rest of the team has no experience
* The team does not have experience or knowledge of how to use Trello and very limited knowledge of Agile style meetings
* Difficulty scheduling due to time zone differences and no prior experience working with these team members
* Experience with command line is new

**Mitigation Strategies**:
* The team will use a search engine to research HTML and SQL that the team does not learn in class
* The team will practice with Trello and have each member take turns being the Scrum Master weekly so there is an equal opportunity to learn
* The team will keep an open line of communication and share scheduling conflicts
* The team will continue to practice command line and refer to the textbook

### Development method
The team will use scrum to develop the website. Sprints will typically last 2 weeks and will consist of developing a small working portion of our website. What the team accomplishes in each sprint will depend on the material learned in class. The team will update Trello as the project progresses. The team will also take turns in the Scrum Master role to allow for equal learning opportunities.

### Project Tracking Software
We use Trello to track our project progress. Access our Trello board [here](https://trello.com/w/fantasticfour82).

## Repository Contents, Structures, and Descriptions
This repository contains the following files and directories:
1. [README](README.md)
2. [Weekly Status](/WeeklyStatus/WEEKLY_STATUS.md)
3. [PAGE TESTING](/WebsiteDesign/MockUp/PAGE_TESTING.md)
4. [SQL TESTING](/SQL_TESTING.md)
5. [FINAL REPORT](/FINAL_REPORT.md)
6. Project presentation files from Milestone 5 (<b>link to be added</b>)
7. Video of demo (<b>link to be added</b>)
8. Source code
    - Below shows related repository structure and description.
    ```
    .
    ├── Furever.db
    ├── sql.py    
    ├── Furever.py  <== cloned, original from Lab 6 assignment
    ├── static
        ├── 
    │   ├── 
    │   └── . . .
    │── templates
    │   ├── 
    │   ├── 
    │   ├── 
    │   ├── 
    │   └──  
    ├── SQL_TESTING.md
    ├── Test_Queries.py
    ├── Test_Tables.py
    ├── setup.cmds <== cloned, original from CSPB3308 Lab 6 assignment
    ├── wsgi.py
    ├── prefix.py 
    ├── requirements.txt
    ├── WebsiteDesign
    │   └──  . . .
    ├── WeeklyStatus
    │   └── . . . <== include weekly activity report & minuites
    └── README.md <== YOU ARE HERE

    ```
    |Filename | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description |
    |--- |--- |--- |
    | Furever.db || xxx |
    | sql.py || xxx |
    | Furever.py || project code for Flask app with calls to **prefix.py** |
    | xxx || directory with images for the README and MY_README files |
    | samples || directory with files used for page generation |
    | static || directory with files needed for page display |
    | &nbsp;&nbsp;&nbsp;css || directory with files for xxx |
    | &nbsp;&nbsp;&nbsp;images || directory with images for xxx |
    | templates || directory with template HTML for rendering test pages for **prefix.py** and **Furever.py** |
    | SQL_TESTING.md || xxx |
    | Test_Queries.py || xxx |
    | Test_Tables.py || xxx |
    | setup.cmds || commands to setup a shell to run a Flask app |
    | wsgi.py || commands to setup a shell to deploy at Render.com |
    | prefix.py || Flask app containing routines needed to run web service on csel.io virtual machine with access from local browser |
    | requirements.txt || xxx |
    | WebsiteDesign || include desing drafts from Milestone 2-4 |
    | WeeklyStatus || include weekly activity report & minuites |
    | README.md | | general information about this project|
    <br>

9. Test cases
10. Documentation
    - This 'README.md' is the main documentation describing overview of this project.
    - 'Furever.py' is the main source code for the project. It uses Python as a programming language.
11. Link to Public Deployment (https://fureverpet.onrender.com/)

## Getting Started

Follow the instructions below to run Flask and host the PetRescue website locally.

### clone our repository

```
git clone https://github.com/Fantastic4Project3308/PetRescue.git
cd PetRescue
```

### set up python virtual env, and install & configure Flask

```
python3 -m venv venv
. venv/bin/activate
pip install Flask
pip install psycopg2-binary
source ./setup.cmds
```

### run flask to host our website locally
```
flask --app Furever.py run
```

Now, you can access our website by going to `http://localhost:3308/` using your browser.

## Acknowledgement
* We would like to express our gratitude to Prof. Knox for his invaluable support throughout this project. He consistently provided guidance and advice during his office hours and answered our questions on Piazza.
* In addition to the office hours and weekly assignment and learning materials, we also relied on the Google search engine to gain knowledge and find solutions to challenges we encountered along the way.
* Our team, the Fantastic Four, was truly awesome! The successful completion of this project was a result of the collective effort of each team member, who contributed their skills and dedication to create a remarkable pet adoption website.

