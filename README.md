# SCHEDULED-TWEET
now you can schedule or instantly post your tweet using this portal. 

# How TO Schedule A Tweet ?
follow these steps
 1. Create a user in **sqlite.db** 
 2. login inside the portal using the credentials you have created
 3. Click on the **Post Tweet** button
 4. write down the message you wish to tweet
 5. It will redirect you to twitter url where you have to authenticate your twitter account. After authentication twitter will provide you a PIN.
 6. Copy the pin & paste it in our portal
 7. Select a date & time when you want to post your tweet(Note that if you don't select any time it will post your tweet immediately)
 8. press Confirm button.

Tada:blush:	 now your post is scheduled. It will be executed on time.

# How Scheduled Tweet Works ?
apscheduler is used to run the background task for scheduled tweet. At present background task is executed after 3 min interval. you can rewrite the interval time inside twitter/schedulers.py file


# Installation process 
 1. Clone this project
 2. Create a virtual env & install required dependencies from requirements.txt
 3. Copy you **consumer_key** & **consumer_secret** from twitter developer account 
 4. create .env file & use these keys inside twitter/views.py file
 
 Run project:innocent:	
 
 CMD: python3 manage.py runserver
