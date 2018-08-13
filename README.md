[![Build Status](https://travis-ci.org/DrKimpatrick/DrKimpatrick.github.io.svg?branch=master)](https://travis-ci.org/DrKimpatrick/DrKimpatrick.github.io)

[![Maintainability](https://api.codeclimate.com/v1/badges/31c9b1fa601249ed9951/maintainability)](https://codeclimate.com/github/DrKimpatrick/DrKimpatrick.github.io/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/31c9b1fa601249ed9951/test_coverage)](https://codeclimate.com/github/DrKimpatrick/DrKimpatrick.github.io/test_coverage)


# Ride-my-way (Carpool Andela Bootcamp 09 Project)

Ride-my-way App is a carpooling application that provides drivers with the ability to create ride oﬀers  and passengers  to join available ride oﬀers.
## Overview
- ## User (s)
The users of the application are travelers and commuters who want to go from one place to 
another or users that are driving a trip and want to find passengers. Users can act as both passengers and 
drivers while using an application

- ### Driver
A driver is any person that owns a car and wants to go from one place to another and publishes 
his trip on the application in order to find passengers to share the ride with.

- ### Passenger
A passenger is any person that doesn’t own a car and wants to join a driver in a trip he posted 
and agrees to all the conditions specified (price and general behavior). 

## Installing
   - Download project
   Clone the project to your local computer
   
   - Prepare the installation environment
   pip install virtualenv or virtualenv name-it
   name-it is the name of the virtualenv
   cd name-it/scripts/activate | this activates the virtualenv
   
   - Install packages in the requirements.txt
   pip install -r requirements.txt 
 
 ## This appication is served by  
 - git-pages [GitHub Pages](https://drkimpatrick.github.io/UI/index.html).
 - Heroku [Heroku](https://safe-fjord-86755.herokuapp.com).
   - API end points
      - retrieve all users [Users](https://safe-fjord-86755.herokuapp.com//api/v1/users)
      - retrieve all rides [Rides](https://safe-fjord-86755.herokuapp.com//api/v1/rides)
      - retrieve a single ride [Single ride](https://safe-fjord-86755.herokuapp.com//api/v1/rides/<rideId>)
      - Request for a  ride [Request for a ride](https://safe-fjord-86755.herokuapp.com//api/v1/rides/<rideId>/requests)
      - Request for all ride requets [All ride requests](https://safe-fjord-86755.herokuapp.com//api/v1/rides/<rideId>/requests)
      - post rides [Rides](https://safe-fjord-86755.herokuapp.com//api/v1/rides)
      - post rides requets [Rides](https://safe-fjord-86755.herokuapp.com//api/v1/rides)
      - Signup [Signup](https://safe-fjord-86755.herokuapp.com//api/v1/users/signup)
      - Login [Login](https://safe-fjord-86755.herokuapp.com//api/v1/users/login)
   
## Acknowledgments
 Am grateful to the Andela group for giving me chance to building this app.   
 

   
