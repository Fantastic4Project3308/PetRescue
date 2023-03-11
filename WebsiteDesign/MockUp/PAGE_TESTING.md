# Home Page
### Page Description
* Company logo and banner
* Dog button
* Cat button
* About Us button

The homepage shows a banner with our company logo, FurEver Pet. Below the banner there are two buttons, one for cats and one for dogs. There is also an About Us button.

<figure width=100%>
<img src="Homepage.pdf" alt="Homepage" WIDTH=50%/></figure>
<figure width=100%></figure>

### Parameters needed for page
* Home page parameter: 
@app.route('/')

* Dog page parameter: 
@app.route('/dog')

* Cat page parameter: 
@app.route('/cat')

* About Us page parameter: 
@app.route('/aboutus')

### Data needed to render the page
* Dog and cat pictures for each button
* Picture for logo

### Link destination for the page
* Company logo and banner:
When a user clicks on this banner on any page, it will link back to the homepage.

* Dog button:
When a user clicks on the dog button, it will link to the dog page. 

* Cat button:
When a user clicks on the cat button, it will link to the cat page. 

* About Us button:
When a user clicks on the About Us, it will link to the company profile page.

### List of tests for verifying the rendering of the page
* Company logo and banner:
Clicking on the logo should return the user to the home page. If the user is already on the home page, nothing will happen.

* Dog button:
Clicking on the dog button should route the user to the dog page which shows the available dogs.

* Cat button:
Clicking on the cat button should route the user to the dog page which shows the available cats.

* About Us button:
Clicking on the About Us button should route the user to the company profile page.

_______________________________________________________________________
# Dog Page
### Page Description
* Company logo and banner
* Dog search bar
* Available dog buttons

The dog page shows a banner with our company logo, FurEver Pet. Below the banner on the left hand side, there is a search section with the options breed, age, size, gender, and color as search variables. Under each search variable there is a drop down list. Below the search section, there will be a search button to complete the search request. On the right hand side of the search section, there will be pictures of all available dogs that can be reduced as a result of the search section criteria. Each dog image is a link to the dog profile page.

<figure width=100%>
<img src="DogPage.pdf" alt="DogPage" WIDTH=50%/></figure>
<figure width=100%></figure>

### Parameters needed for page
* Home page parameter: 
@app.route('/')

* Dog page parameter: 
@app.route('/dog')

* Dog profile page parameter: 
@app.route('/dog/profile/animal_ID')

### Data needed to render the page
* Dog pictures for available dogs
* Name, breed, age, size, gender, and color data scrapped from website
* Picture for logo

### Link destination for the page
* Company logo and banner:
When a user clicks on this banner on any page, it will link back to the homepage.

* Search bar and button: 
When a user filters for the dog they want and presses the search button, it will narrow down the list of available dogs on the page.

* Dog selection: 
When a user decides on the dog they will click on a picture and it will direct them to the dog's profile page.

### List of tests for verifying the rendering of the page
* Company logo and banner: 
Clicking on the logo should return the user to the home page.

* Search bar and button: 
To verify that criteria was selected, we will check that the name of the dog that fits the criteria will show up. For example, Lola is a female puppy with brown hair. Lola will show up when we search for this criteria.
    
* Dog picture:
When a user clicks on a dog picture, a new tab will open with the dog profile. Everytime a user selects a new dog, another tab will open. By opening a new tab everytime a new dog is selected, we can keep our search variables on the dog search page. 

    
_______________________________________________________________________
# Cat Page
### Page Description
* Company logo and banner
* Cat side search bars
* Available cat buttons

The  page shows a banner with our company logo, FurEver Pet. Below the banner on the left hand side, there is a search section with the options breed, age, size, gender, and color as search variables. Under each search variable there is a drop down list. Below the search section, there will be a search button to complete the search request. On the right hand side of the search section, there will be pictures of all available cats that can be reduced as a result of the search section criteria. Each cat image is a link to the cat profile page.

<figure width=100%>
<img src="CatPage.pdf" alt="CatPage" WIDTH=50%/></figure>
<figure width=100%></figure>

### Parameters needed for page
* Home page parameter: 
@app.route('/')
    
* Cat page parameter:
@app.route('/cat')

* Cat profile page parameter:
@app.route('/cat/profile/animal_ID')

### Data needed to render the page
* Cat pictures for available cats
* Name, breed, age, size, gender, and color data scrapped from website
* Picture for logo

### Link destination for the page
* Company logo and banner: 
When a user clicks on this banner on any page, it will link back to the homepage.

* Search bar and button: 
When a user filters for the cat they want and presses the search button, it will narrow down the list of available cats on the page.

* Cat selection:
When a user decides on a cat they will click on a picture and it will direct to the cat's profile page.

### List of tests for verifying the rendering of the page
* Company logo and banner:
Clicking on the logo should return the user to the home page.

* Search bar and button:
To verify that criteria was selected, we will check that the name of the cat that fits the criteria will show up. For example, Tony is a male cat with white hair. Tony will show up when we search for this criteria.
    
* Cat picture: 
When a user clicks on a cat picture, a new tab will open with the cat profile. Everytime a user selects a new cat, another tab will open. By opening a new tab everytime a new cat is selected, we can keep our search variables on the cat search page.
    
_______________________________________________________________________
# Dog or Cat profile page (page layout will look the same)
### Page Description
* Company logo and banner
* Animal photo
* Profile section with: name, breed, age, gender, size, color, background, and shelter
* Adopt now button

The page shows a photo of the desired dog or cat, a brief description of the animal including the name, breed, age, gender, size, color, background, and shelter where the animal currently lives. The page also includes an "Adopt Now" link.

<figure width=100%>
<img src="AnimalBio.pdf" alt="AnimalBio" WIDTH=50%/></figure>
<figure width=100%></figure>

### Parameters needed for page
* Home page parameter:
@app.route('/')
    
* Adopt now page parameter:
    * @app.route('/dog/profile/animal_ID/adoptnow')
    * @app.route('/cat/profile/animal_ID/adoptnow')
    
### Data needed to render the page
* Cat/ dog pictures for selected cat/ dog
* Name, breed, age, gender, size, color, background, and shelter data scrapped from website
* Picture for logo

### Link destination for the page
* Company logo and banner:
When a user clicks on this banner on any page, it will link back to the homepage.

* Adopt now button:
When a user clicks on the adopt now button, the user will be directed to an adoption form page where the user can fill out the application.

### List of tests for verifying the rendering of the page
* Company logo and banner:
Clicking on the logo should return the user to the home page.

* Adopt now button:
Clicking on the adopt now button will take the user to an adoption form (in text).

_______________________________________________________________________
# Adoption page
### Page Description
* Company logo and banner
* Adoption form text

The adoption page shows a text form that a user will need to fill out in order to be considered as a potential adopter for the desired cat or dog.

<figure width=100%>
<img src="AdoptionForm.pdf" alt="AdoptionForm" WIDTH=50%/></figure>
<figure width=100%></figure>

### Parameters needed for page
* Home page parameter:
@app.route('/')
    
* Adopt now page parameter:
    * @app.route('/dog/profile/animal_ID/adoptnow')
    * @app.route('/cat/profile/animal_ID/adoptnow')
    
### Data needed to render the page
* Picture for logo
* Text form

### Link destination for the page
* Company logo and banner
When a user clicks on this banner on any page, it will link back to the homepage.

### List of tests for verifying the rendering of the page
* Company logo and banner
Clicking on the logo should return the user to the home page.
* Text: 
Ensure text is rendered on page.


_______________________________________________________________________
# About Us page
### Page Description
* Company logo and banner
* Company profile
* Mission statement
* Privacy profile
* Contact info

The above bullets will be text, each surrounded by a solid border.

<figure width=100%>
<img src="AboutUs.pdf" alt="AboutUs" WIDTH=50%/></figure>
<figure width=100%></figure>

### Parameters needed for page
* Home page parameter:
@app.route('/')
    
* About Us page parameter:
@app.route('/aboutus')
    
### Data needed to render the page
* Picture for logo
* Team created text

### Link destination for the page
* Company logo and banner:
When a user clicks on this banner on any page, it will link back to the homepage.

### List of tests for verifying the rendering of the page
* Company logo and banner:
Clicking on the logo should return the user to the home page.

* Text:
Ensure text is rendered on page.

_______________________________________________________________________
# Demo on how pages will link together
### Click on cat or dog button on homepage
When a user clicks on the cat button on the homepage, the user will be directed to the available cat page. On this page the user will filter the data for available cats. A user can then click on the desired cat photo which will route the user to the cat's profile page. If a user is interested in adopting the cat, then the user can click on the Adopt Now button. From here, the user is routed to the adoption form page where the user can fill out the form.

<figure width=100%>
<img src="ClickOnCatButton.pdf" alt="ClickOnCatButton" WIDTH=50%/></figure>
<figure width=100%></figure>

Routing works the same way if the user clicks on the dog button on the homepage.

<figure width=100%>
<img src="ClickOnDogButton.pdf" alt="ClickOnDogButton" WIDTH=50%/></figure>
<figure width=100%></figure>

### Click on About Us button on homepage
When a user clicks on the About Us button on the homepage, it will route the user to the company profile page.

<figure width=100%>
<img src="ClickOnAboutUsButton.pdf" alt="ClickOnAboutUsButton" WIDTH=50%/></figure>
<figure width=100%></figure>
