# Challenge Name: Sleuthkit Apprentice
## Question
![[CTF2022/picoCTF2022/Forensic/Sleuthkit Apprentice/Question.png]]

In this challenge, we're giving a disk image in .gz extension and we need to use the file to find out the flag. 

## Solution
Download the file the use `$ gzip -d disk.flag.img.gz` to extract the file and I got the disk.flag.img file. 

Used the command `$ file disk.flag.img` to check out what is the type of the file that has been extracted. Within the file, there are a lot of partition and I assume this is a disk file. Even though, it still doesn't give me a big clue to solve this challenge. 

![[filecommand.png]]



To solve this challenge, I tried to search for the challenge title which is Sleuthkit Apprentice. I found out that this title was related to AutoSpy software. 

AutoSpy is a digital forensic platform that also serves as a graphical interface to The Sleuth Kit as well as other digital forensic tools. It is used to investigate what had happened in the computer as well as dig all the information in the device. 

Check out more on AutoSpy - https://www.sleuthkit.org/autopsy/





However, I do not have any experience and not familiar with the functionalities of the AutoSpy. Then, I tried to find is that any similar previous CTF with the keyword `forensic disk ctf` and I got this writeup https://blog.stalkr.net/2010/05/defcon-18-ctf-quals-writeup-forensics.html. Refer to the writeup, I tried to manually dig the information within the disk file through the cmd but I am still unable to get the flag. I think that there must be something wrong with the step of digging the disk manually. 

After that, I saw the author has posted below the writeup of how to use the SleuthKit with AutoSpy. 
AutoSpy Tutorial - https://blog.stalkr.net/2010/03/codegate-forensic-sleuthkit-autopsy.html 


First of all, create a new case and a host. After that, add the image file and key in the location of the file. In this case, I used Disk as the type of file and click next. 

![[AddImage.png]]


After that, click add in the next screen and I got all of the disk volume inside the disk file. Select a disk and click ANALYZE to start analyze the disk. 
![[diskdetails.png]]


I tried to use KEYWORD SEARCH function to find out the flag in all the disk and still can't get the flag. After that, I decided to use the most traditional way to find out the flag which is click one by one of the disk and all the folders/files in all the disk. 

Finally, the flag is in the /3/ disk with the path `/3/root/my_folder/`. Select the `flag.txt` and it can see the comment there, the `file.txt` was deleted and it had been stated as Deleted File Recovery Mode. It means that the file was recovered by the software. Select the `flag.uni.txt` and finally I've got the flag. 


![[noflag.png]]

![[CTF2022/picoCTF2022/Forensic/Sleuthkit Apprentice/flag.png]]




## Flag
That's the flag !
`
picoCTF{by73_5urf3r_42028120}
`