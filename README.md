# WeVolunteer

## Summary:
According to the cdc.gov website, the risk for severe illness with COVID-19 increases with age, having older adults at the highest risk. Therefore people above the age of 60 are not recommended to go out to public spaces during these times. WeVolunteer is an application that helps to connect older adults in our community to volunteers willing to help out bring groceries, medicines, or other essentials.

We understand that senior citizens are not accustomed to using complex applications on a day to day basis, and keeping their needs in mind, WeVolunteer has integrated a chatbot. The senior citizens would have a conversation with the chatbot and provide the details required, and the chatbot then takes the information and updates it in the database. Any person without the knowledge of technology can easily communicate their requirements to the chatbot thereby enabling easy interaction and requests to be posted on the website by the senior citizens.

The volunteers can then login to the webpage, which then populates all the active requests from the database. If needed, volunteers can search for a suitable area (via zip code) for any help needed and pick requests convenient to them.

Once the request is picked, its status changes from active to inactive. And, both the volunteer and the registered senior citizen would be notified.

## Problem:

According to the cdc.gov website, the risk for severe illness with COVID-19 increases with age, having older adults at the highest risk. Therefore people above the age of 60 are not recommended to go out to public spaces during these times.

To reduce the risk of elderly people contracting the COVID-19, the need for an application which connects senior citizens to volunteers who can help deliver the required essentials like groceries and medicines in an efficient manner came into existence. 
 
Stores that provide home delivery facilities have heavy delivery charges or have a minimum requirement for bill amount.On the other hand, most of the existing applications that connect volunteers willing to purchase and deliver essentials to senior citizens have a convenience fee charged to elderly citizens for the service provided. Another issue faced is that most elderly are not well versed with technology, therefore find it very hard to navigate across the website and submit such requests.

Therefore this creates a necessity for an application that connects volunteers with senior citizens requests in an easy and efficient manner for no cost.

## Solution:
WeVolunteer connects volunteers with senior citizens in an easy and efficient manner to help deliver essential items (Groceries, medicines, etc.,). To cater to the elderly who aren't well versed with technology, we have created a chatbot where one can very easily chat/communicate with the bot to give the requirements and the bot then handles updating the database, thereby updating the webpage.

We have designed and developed a working prototype (proof of concept model) of the idea behind WeVolunteer Application.

### Technologies Used:
Chatbot: rasa nlu 2.1, Python <br>
Database: MySQL <br>
Frontend: HTML, CSS <br>
Backend: PHP <br>

The chatbot was created using rasa nlu 2.1. A model was trained and created to respond to generic queries and application specific questions such as the details of the person, address and the items required to be delivered.

The chatbot collects all the information and updates it into the mySQL database where it sets the order status to active. 

The webpage was developed using HTML and PHP where it displays all the active requests fetched from the database. If needed, the volunteer can filter the requests based on zip code, and then select the appropriate request that is convenient for them. Once the request is selected, it updates the mySQL database to change the status of the order to inactive and in turn removes it from the webpage.

## Next Steps:
<b> Security: </b> Login Ids need to be created for both elderly and volunteers to keep track of the orders. The elderly would also have to submit a picture of their age proof (stating they are above the age of 60) as a part of the validation process.

<b> Notification systems: </b> Once the order is picked by a volunteer both the volunteer and the elderly person submitting the request get an email and text notification. The volunteer also updates the information on WeVolunteer after the delivery of the requested items.

<b> Payment systems: </b> The elderly person registering on WeVolunteer also registers a credit card. Once the volunteer delivers the item, he/she will upload the bill to WeVolunteer and WeVolunteer will deduct the amount from the elderly persons card and transfer it to the volunteer.

