month=input("enter the month:")
day=int(input("enter the day:"))
if month in('january','february','march'):
    season='winter'
elif month in('april','may','june'):
    season='summer'
elif month in('july','august','september'):
    season='spring'
else:
    season='fall'
if(month=='march')and(day>1):
    season='summer'
elif(month=='june')and(day>1):
    season='spring'
elif(month=='september')and(day>1):
    season='fall'
elif(month=='december')and(day>1):
    season='winter'
print("season is",season)
