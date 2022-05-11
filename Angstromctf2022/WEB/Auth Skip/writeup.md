# Challenge Name: Auth Skip
![quest](Question.png)

We are given a link which redirect us to a login website page and also a index.js file which is the source of the website. 

Link: https://auth-skip.web.actf.co/

![img1](Website.png)

Source: index.js

![img2](index.js.png)

## Solution
Based on the link and source codes provided, we need to bypass the login page to get the flag. According to the source code, we can know that if the user cookies value is set to "admin", then it will give us the flag. 

Thus, open the website link using burpsuite browser and set the user cookies value to "admin" and click forward, then it will give us the flag. 

![img3](cookie.png)

![img4](flag.png)


## Flag
That's the flag !
`actf{passwordless_authentication_is_the_new_hip_thing}`