# Challenge Name: Confetti
![quest](Question.png)

Given a png file. Assume this must be something to grab the flag in the png image file given. 



## Solution
Use binwalk command to check whether the PNG file given contains any others files. As the result, it contains a lot of others PNG image files and some is compressed in another file as well.  
![img1](checking.png)


Use binwalk command to extract it and you will get all the extracted file within the PNG file provided. 
`$ binwalk --dd=".*" confetti.png -e` 
![img2](sol.png)

Open the file explorer, and redirect to the folder that has been extracted. It is very obvious that there is a only PNG image file contain something inside. 
![img3](extracted_files.png)


Quickly double click to open the 1D8556 image file and you will get the flag. 
![img4](1D8556.png)


## Flag
That's the flag !
`actf{confetti_4_u}`