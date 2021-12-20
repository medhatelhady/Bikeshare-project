# bikeshare project

# goal
- practise python coding
- using pandas and numpy to work with data


# this program do multiple task 
1 - chose data file depending on ciyt that user input.
	note that we have a limited number of choices. we have only three cities which are Chicago, New York and Washington
2 - filter the data chossen depending on month and day that user enter but first we have to ask him if he want to filter months or days or both 
	of them or he don't want to make filter
3 - after this process program excute a banch of functions to get information about chossen data like: 
   most common day of week
   most common hour of day
   most common start and end stations used 
   most common user type
   most common user gender
   etc...
   
4 - program ask you if you want to repeat the process or finish the program


# libaries used in program

three main libraries 
- pandas and numpy which work directly with data. actually the make working with data so easy
- time to calculate time of excution

Method used in the program

- get_day_input method: it ask user to input a day of week and check if this is a valid day

- get_month_input method: it ask user to input a month (one of the first six monthes) 

- get_filters method: this method invoke the previous two method in it. it ask user to input city name and return city name , month and day 

- load_data method: this method pick data file according to city name and filter this data
	it returns data after filteration
    
- time_stats method: make some calculations to print most common day of week and most common hour of day

- station_stats method: print most common start station, most common end station and most common trip from start to end (i.e., most frequent combination of start station and end station)

- trip_duration_stats method: print total travel time and average travel time

- user_stats method : print counts of each user type and counts of each gender (only available for NYC and Chicago) and earliest, most recent, most common year of birth (only available for NYC and Chicago)

# tools
- python 
- jupyter notebook

# Resource
1- stack over flow
2- python for data analysis book 

