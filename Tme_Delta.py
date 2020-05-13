# Problem:

# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format

# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t1 and time t2 .

# Constraints

# Input contains only valid timestamps
# . year <= 3000.
# Output Format

# Print the absolute difference (t1-t2) in seconds.

# Sample Input 0:
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# Sample Output 0:
# 25200
# 88200

# Explanation 0
# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7*3600 seconds or 25200 seconds.

# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24*3600 + 30*60 = 88200

#Approach 1

from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))


#Approach 2(Using Calender)

from datetime import date
import calendar
T=int(input())
for x in range(T):
    t1=list(map(str,input().split(" ")))
    t2=list(map(str,input().split(" ")))
    hrs=int(''.join(list(t1[4])[0:2]))-(int(''.join(list(t2[4])[0:2])))
    mins=int(''.join(list(t1[4])[3:5]))-(int(''.join(list(t2[4])[3:5])))
    secs=int(''.join(list(t1[4])[6:]))-(int(''.join(list(t2[4])[6:])))
    hrtz1=int(''.join(list(t1[5])[1:3]))
    hrtz2=int(''.join(list(t2[5])[1:3]))
    mintz1=int(''.join(list(t1[5])[3:]))
    mintz2=int(''.join(list(t2[5])[3:]))
    month1=t1[2]
    month2=t2[2]
    d0=date(int(t1[3]),list(calendar.month_abbr).index(month1),int(t1[1]))
    d1=date(int(t2[3]),list(calendar.month_abbr).index(month2),int(t2[1]))
    delta=d0-d1
    dayz=delta.days
    if(str(list(t1[5])[0])== "-"):
        hrs=hrs+hrtz1
        mins=mins+mintz1
        
    if(str(list(t1[5])[0])== "+"):
        hrs=hrs-hrtz1
        mins=mins-mintz1
        
    if(str(list(t2[5])[0])=="-"):
        hrs=hrs-hrtz2    
        mins=mins-mintz2
        
    if(str(list(t2[5])[0])=="+"):
        hrs=hrs+hrtz2
        mins=mins+mintz2

    difference=dayz*86400 + hrs*3600 + mins*60+secs
    print(abs(difference))