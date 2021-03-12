# Election-Analysis Using Python

## Overview of Election Audit

Election audit is a performance of review conducted after polls close for the purpose of determining whether the votes were counted accurately. In this Module, we helped a Colorado Board of Elections employee to complete the election audit of a recent local congressional election. During this practice, we used Python to write algorithms to assist the confirmation and analysis of the election results. We analyzed the election results on two levels: Candidate level and County level. For each level, we completed the following tasks.

-	Candidate level:

1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the total number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.

-	County level:

1.	The voter turnout for each county.
2.	The percentage of votes from each county out of the total count.
3.	The county with the highest turnout.

## Analysis

In this analysis, we used Python as the programming language, Visual Studio Code as the programming software. We are going to read in the CSV file that contains the election information. Then count the number of votes, percentage for each county and candidate. Based on the calculation, get the county with the largest turnout, and the candidate with the highest vote as the winner of this election. Finally wrote the output to a text file. 

1.	Used “IMPORT” statement in Python to add the dependencies. These dependencies will allow us to use the functions needed for this analysis.

    ![ss1](https://user-images.githubusercontent.com/79289806/110873865-a46e4380-82a0-11eb-900f-2d9b701213dc.png) 

2.	Created two variables to store the location for the CSV file that we are going read in, and the text file that we are going to write the final output.

    ![ss2](https://user-images.githubusercontent.com/79289806/110873866-a46e4380-82a0-11eb-9206-177ca721ff70.png)

3.	Initialized the total vote counter, and created list and dictionary for both candidate and county to store the values in the following steps. 

    ![ss3](https://user-images.githubusercontent.com/79289806/110873867-a46e4380-82a0-11eb-92ed-a19d2c28bdba.png)

4.	Read in the CSV file using reader object. The CSV file is opened as a text file with Python’s built-in open() function, which returns a file object. 

    ![ss4](https://user-images.githubusercontent.com/79289806/110873868-a46e4380-82a0-11eb-83d4-04d23be2add3.png)

5.	Before analysis, removed the header line from the CSV file by using next() function.

    ![ss5](https://user-images.githubusercontent.com/79289806/110873869-a506da00-82a0-11eb-88a8-0cb74b5f5888.png)

6.	Used For loop to loop through the rows in the file, created the following variables:

    (1) 	Iterate through the rows by adding 1 to total_votes. When the iteration complete get the number of total votes across all the records. 

     ![ss6](https://user-images.githubusercontent.com/79289806/110873871-a506da00-82a0-11eb-9fbc-bb96c33a4fd5.png)

    (2) 	When loop through the rows in the file, each row was read in from the CSV file as a list with 3 elements. Use the associated position number in the list to get the candidate name and county name. 

    ![ss7](https://user-images.githubusercontent.com/79289806/110873872-a506da00-82a0-11eb-8581-7d247d06e1b1.png)

    (3)    Used conditional statement to create a unique list of candidate name, and a dictionary with the candidate’s name as the key, the number of votes for each candidate as the value. 

    ![ss8](https://user-images.githubusercontent.com/79289806/110873873-a506da00-82a0-11eb-91d6-f363271d6214.png)


     (4)	Similar as the candidate section, used conditional statement to create a unique list of the county, and a dictionary with county’s name as the key, the number of votes for each county as the value.

    ![ss9](https://user-images.githubusercontent.com/79289806/110873855-a3d5ad00-82a0-11eb-81c8-8c72bcf6c560.png)

7.	After the initial calculations were ready, wrote the outputs to a text file. 

    ![ss10](https://user-images.githubusercontent.com/79289806/110873856-a3d5ad00-82a0-11eb-99b8-64657426e6a9.png)

     (1)    Wrote the total number of votes to the text file.

    ![ss11](https://user-images.githubusercontent.com/79289806/110873857-a3d5ad00-82a0-11eb-8ce8-c9e9fa72bfb7.png)

    (2)	    Based on the number of total votes and the votes for each county, calculated the percentage of vote for each county. Then compare the number of votes across all the counties, select the county with the largest number of votes, wrote to the text file.

    ![ss12](https://user-images.githubusercontent.com/79289806/110873858-a3d5ad00-82a0-11eb-9214-c420a285b9a4.png)


    (3)	    Similar as the county, calculated the percentage of votes for each candidate. Compare the count and percentage of votes across all the candidates, select the winner candidate and wrote to the text file.

    ![ss13](https://user-images.githubusercontent.com/79289806/110873859-a3d5ad00-82a0-11eb-87ef-2be60ad13cc0.png)


## Election-Audit Results:

From the analysis, we were able to get the number of votes in total, by county and by states. We were also able to select the largest county turnout and the winner candidate in this election. 

1.	There are 369,711 total votes in this election.

    ![ss14](https://user-images.githubusercontent.com/79289806/110873860-a3d5ad00-82a0-11eb-9294-d67594b07f39.png)

2.	There are three counties participated in this election: 

-	Jefferson: received 10.5% of the vote and 38,855 votes.
-	Denver: received 82.8% of the vote and 306,055 votes.
-	Arapahoe: received 6.7% of the vote and 24,807 votes.
 
    ![ss15](https://user-images.githubusercontent.com/79289806/110873861-a46e4380-82a0-11eb-93b3-81fa15464d43.png)
    
3.	Based on the calculation, Denver is the county with the largest 
turnout.

    ![ss16](https://user-images.githubusercontent.com/79289806/110873862-a46e4380-82a0-11eb-80f9-c1f539ac12b3.png)

4.	There are three candidates participated in this election:

-	Charles Casper Stockham: received 23.0% of the vote and 85,213 votes.
-	Diana DeGette: received 73.8% of the vote and 272,892 votes
-	Raymon Anthony Doane: received 3.1% of the vote and 11,606 votes

    ![ss17](https://user-images.githubusercontent.com/79289806/110873863-a46e4380-82a0-11eb-9762-1df332c19595.png)

5.	Based on the calculation, Diana DeGette is the winner of this election.

    ![ss18](https://user-images.githubusercontent.com/79289806/110873864-a46e4380-82a0-11eb-8484-7044b33e15b7.png)

## Election-Audit Summary:

The election audit is very important after the polls close to verify the accuracy of the vote counts. Election audit can be happened for any type of election. Depending on the size of the election, programmatically counting the votes and representing the outcome is more accurate and preferable. 

In this analysis, we used Python to read in the CSV file that contains the election information and calculated the vote counts for each county and candidate. Furthermore, we were able to use this script to get the winner of this election and the county with the largest turnout. 

This script can be used for any election events. Based on the type of election, we could load in the election data, get the count for each group of candidates of the selection, and select the winner.

Here are some examples:

1.	Election of team leader.

After collect the data for all the candidates, create a CSV file to store all the information. In this data we should have the name of the candidate, voted or not. We could use this script, read in the CSV file, loop through all rows in the data file, create a list of the name of the candidates, and the count of vote for each candidate. We could also use the script to give us the result of the elected team leader.

2.	Election of managers.

This script can also be used to analyze the results of the election of managers from different divisions of an organization at the same time. When collecting the data, we could have not only the candidate name, candidate vote, but also the division they applied for. Using the script, we could get the list of the divisions, the list of candidates, and cumulative number of the vote counts. Within each division, compare the count across all the candidates, select the final winner as the manger of the division. 

 


