#####################################################################
#   Program Description:                                            #
#   This small utility calculates the total IT experience           #
#   of an individual who has worked in multiple companies.          #
#                                                                   #
#   Created by: Swadhin Kumar Mangaraj                              #
#   Initial Version on: 07-Feb-2020                                 #
#   Last Modified on: 07-Feb-2020                                   #
#                                                                   #
#   Assumptions:                                                    #
#   1. An average year consists of 365 days and 6 hours.            #
#   2. Since months in a year has variable number of days, the      #
#      average days in a month has been calculated as 365.25/12     #
#      = 30.4375 days.                                              #
#                                                                   #
#   Constraints:                                                    #
#   1. User input must have 3 distinct numeric values representing  #
#      number of years, months and days (along with any other text).#
#                                                                   #
#####################################################################

# An input is requested from user and stored in a variable as the duration in first five jobs
nameOfIndividual = str(input ("What's your name? "));
durationInJob1 = str(input ("How long did you work at your first job? "));
durationInJob2 = str(input ("How long did you work at your second job? "));
durationInJob3 = str(input ("How long did you work at your third job? "));
durationInJob4 = str(input ("How long did you work at your fourth job? "));
durationInJob5 = str(input ("How long did you work at your fifth job? "));

# Printing the original string as entered by user
print("**********************************************");
print("You have worked for", durationInJob1, "in your first job");
print("You have worked for", durationInJob2, "in your second job");
print("You have worked for", durationInJob3, "in your third job");
print("You have worked for", durationInJob4, "in your four job");
print("You have worked for", durationInJob5, "in your five job");
print("**********************************************");

# using List comprehension + isdigit() +split() for getting numbers from the string  
separatedYearMonthDayInJob1 = [int(incr) for incr in durationInJob1.split() if incr.isdigit()];
separatedYearMonthDayInJob2 = [int(incr) for incr in durationInJob2.split() if incr.isdigit()];
separatedYearMonthDayInJob3 = [int(incr) for incr in durationInJob3.split() if incr.isdigit()];
separatedYearMonthDayInJob4 = [int(incr) for incr in durationInJob4.split() if incr.isdigit()];
separatedYearMonthDayInJob5 = [int(incr) for incr in durationInJob5.split() if incr.isdigit()];

# print the separated number of years, months and days 
print("*****************************************************************************************");
print(nameOfIndividual, "has worked in his/her first job for: ", (separatedYearMonthDayInJob1[0]), "year(s)", (separatedYearMonthDayInJob1[1]), "month(s) and", (separatedYearMonthDayInJob1[2]), "day(s) !!!");
print(nameOfIndividual, "has worked in his/her second job for: ", (separatedYearMonthDayInJob2[0]), "year(s)", (separatedYearMonthDayInJob2[1]), "month(s) and", (separatedYearMonthDayInJob2[2]), "day(s) !!!");
print(nameOfIndividual, "has worked in his/her third job for: ", (separatedYearMonthDayInJob3[0]), "year(s)", (separatedYearMonthDayInJob3[1]), "month(s) and", (separatedYearMonthDayInJob3[2]), "day(s) !!!");
print(nameOfIndividual, "has worked in his/her fourth job for: ", (separatedYearMonthDayInJob4[0]), "year(s)", (separatedYearMonthDayInJob4[1]), "month(s) and", (separatedYearMonthDayInJob4[2]), "day(s) !!!");
print(nameOfIndividual, "has worked in his/her fifth job for: ", (separatedYearMonthDayInJob5[0]), "year(s)", (separatedYearMonthDayInJob5[1]), "month(s) and", (separatedYearMonthDayInJob5[2]), "day(s) !!!");
print("*****************************************************************************************");

#jobDurationInDays = float(0.0);     # Variable initialization
jobDurationInDays = ((separatedYearMonthDayInJob1[0] + separatedYearMonthDayInJob2[0] + separatedYearMonthDayInJob3[0] + separatedYearMonthDayInJob4[0] + separatedYearMonthDayInJob5[0]) * 365) + ((separatedYearMonthDayInJob1[1] + separatedYearMonthDayInJob2[1] + separatedYearMonthDayInJob3[1] + separatedYearMonthDayInJob4[1] + separatedYearMonthDayInJob5[1]) * 30) +(separatedYearMonthDayInJob1[2] + separatedYearMonthDayInJob2[2] + separatedYearMonthDayInJob3[2] + separatedYearMonthDayInJob4[2] + separatedYearMonthDayInJob5[2]);

print("Total number of days", nameOfIndividual, "has worked for is: ", jobDurationInDays);

# Calculate the total duration for which the individual has worked
totalNumberOfYears = int(jobDurationInDays/365.25);
totalNumberOfMonths = int((jobDurationInDays%365.25)/(365.25/12));
totalNumberOfDays = int((jobDurationInDays%(365.25/12)));

print("Total IT experience of", nameOfIndividual, "is: ", (totalNumberOfYears), "year(s)", (totalNumberOfMonths), "month(s) and", (totalNumberOfDays), "day(s) !!!");

##########################  END OF FILE #############################
