# PetRescue
Pet Rescue and adoption website

Project title: Pet Adoption Website

Team # 4 (Fantastic Four)

Team/Product Name: FurEver Pet

Team members: 
* Mayra Weidner - MYWeidner, mawe7753@colorado.edu
* Brittany Bilotti - brbi1248 - brbi1248@colorado.edu
* Mayumi Shimobe - Mayumi-GT - mash8545@colorado.edu
* Zack Cheng - zacktcheng - tsch3115@colorado.edu

Day/Time/TimeZone for the scheduled team weekly meeting (30 minutes via Zoom): Friday 12MST

Vision statement: To create a website that allows people to search for a pet that is best suited for them based on a variety of criteria. We hope to produce a working website that looks warm and welcoming with our newfound html skills that can pull the user's criteria from a sql database.

Motivation: why are you working on this project? We have a passion for rescuing animals and a deep desire to connect those with the same values with an animal in need.

Risks to project completion, possibly including:
* Only one team member has limited experience in HTML and SQL while the rest of the team has no experience
* The team does not have experience or knowledge of how to use Trello and very limited knowledge of Agile style meetings
* Difficulty scheduling due to time zone differences and no prior experience working with these team members
* Experience with command line is new

Mitigation Strategy for above risks
* The team will use a search engine to research HTML and SQL that the team does not learn in class
* The team will practice with Trello and have each member take turns being the Scrum Master weekly so there is an equal opportunity to learn
* The team will keep an open line of communication and share scheduling conflicts
* The team will continue to practice command line and refer to the textbook

Development method: The team will use scrum to develop the website. Sprints will typically last 2 weeks and will consist of developing a small working portion of our website. What the team accomplishes in each sprint will depend on the material learned in class. The team will update Trello as the project progresses. The team will also take turns in the Scrum Master role to allow for equal learning opportunities.

Project Tracking Software link: https://trello.com/w/fantasticfour82

## How to run Flask and host our PetRescue website on your laptop

### clone our repo 

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
