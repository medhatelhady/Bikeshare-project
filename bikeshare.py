import time
import pandas as pd
import numpy as np
import pprint
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""
ask user to enter which day to filter data

return
      str (day) :name of the day that user enter
"""

def get_day_input():
    """
    ask user to enter which day to filter data

    return
            str (day) : name of the day user chose
    """
    # list of all available day (all 7 days)
    # all names in lower case
    days_of_week = [ 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # take inputs of day, lower it and remove extra spaces
    day = input('(If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').strip().lower()
    while day not in days_of_week:
        day = input('enter a valid day: ').strip().lower()
    print()
    day = day.capitalize() # convert first letter to be capital
    return day



def get_month_input():
    """
    ask user to enter which month to filter data

    return
            str (month) : name of the month user chose
    """
    # list of all available months (first 6 months)
    # all names in lower case
    months_set = ['january', 'february', 'march', 'april', 'may', 'june']
    # take input from user
    month = input('(If they chose month) Which month - January, February, March, April, May, or June?\n').strip().lower()

    # validate the input
    # if name of month is not valid, ask user to input it again
    # program should accept the name regardless of case sensetivity
    while month not in months_set:
        month = input('enter one of the first six months: ').strip().lower()
    print()
    # convert month from name to a number (january = 1, may = 5, and do on..)
    month = months_set.index(month) + 1
    return month



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    month = 'all'
    day = 'all'
    print('Hello! Let\'s explore some US bikeshare data!\n\n')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_options = {'chicago', 'new york', 'washington'}
    city = input('Would you like to see data for Chicago, New York, or Washington?\n').strip().lower()

    # check if name of city is available and valid or not
    # if it's not invalid, ask user to inter it again
    # program must handle case sensetivity
    while city not in city_options:
        city = input('enter a name of these cities: chicago, new york city, washington \n').strip().lower()
    print()

    # take input of user choice
    # if he going to chose month, day or both
    # if he didn't chose any of them, then ask him again
    choice = input('Would you like to filter the data by month, day, both or not at all?\n').strip().lower()
    done = False # indicator that user chose proper choice
    while done == False:

        if choice == 'both':
            # get user input for month (all, january, february, ... , june)
            month = get_month_input()

            #get user input for day of week (all, monday, tuesday, ... sunday)
            day = get_day_input()

            done = True
        elif choice == 'month':
            month = get_month_input()
            done =True
        elif choice == 'day':
            day = get_day_input()
            done = True
        else:
            print("Invalid input")
            choice = input('Would you like to filter the data by month, day, both or not at all?\n').strip().lower()
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # get csv file name from city data dict
    file_name = CITY_DATA[city]

    df = pd.read_csv(file_name)

    ''' Filter data file depending on month and day that user pick'''

    #convert start time column to datetime data type
    start_time_column = pd.to_datetime(df['Start Time'])


    # get month from start time column
    month_col = start_time_column.dt.month

    '''if user chose a month program will filter else no filteration'''
    if month != 'all':
        df = df[month_col == month]

    # get week day names from start time column
    day_name = start_time_column.dt.day_name()

    if day != 'all':
        df = df[day_name == day]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #convert start time column to datetime data type
    start_time_column = pd.to_datetime(df['Start Time'])


    # display the most common month
    common_month = start_time_column.dt.month.value_counts()
    print('the most common month is ', common_month.keys()[0], ' Count: ', common_month.values[0])

    # display the most common day of week
    common_day = start_time_column.dt.day_name().value_counts()

    print('the most common day is ', common_day.keys()[0], ' Count: ', common_day.values[0])

    # display the most common start hour
    common_start_hour = start_time_column.dt.hour.value_counts()
    print('the most common start hour is ', common_start_hour.keys()[0], ' Count: ', common_start_hour.values[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_statio_map = df['Start Station'].value_counts()

    print('The most commonly used start station is ', start_statio_map.keys()[0], ' Count: ',start_statio_map.values[0])

    #  display most commonly used end station

    end_station_map = df['End Station'].value_counts()

    print('The most commonly used end station is ', end_station_map.keys()[0], ' Count: ', end_station_map.values[0])


    # display most frequent combination of start station and end station trip

    # get value counts of both start and end station columns
    commom_start_end_station_map = (df['Start Station'] + '*' + df['End Station']).value_counts()

    # extract name of start and end station
    common_stations = commom_start_end_station_map.keys()[0].split('*')

    print('the most common start station is ', common_stations[0], 'and end station is ', common_stations[1], '  Count: ', commom_start_end_station_map.values[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is ', df['Trip Duration'].sum(), 'second')

    # display mean travel time

    print('Mean travel time is ', df['Trip Duration'].mean(), 'second')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print ('User Type : Count')

    # print the content of user dictionary
    for key, val in df['User Type'].value_counts().items():
        print(key, ' : ', val)

    print()
    # Display counts of gender
    if 'Gender' in df.columns:
        print('Gender : Count')

        # print the content of gender dictionary
        for key, val in df['Gender'].value_counts().items():
            print(key , ' : ' , val)

        print()
    # Display earliest, most recent, and most common year of birth

    # check if birth day column is in data frame because there is a data set dosn't contain this column
    if 'Birth Year' in df.columns:
        # display the minimum year value
        print('the earliest year of birthday is ', int(df['Birth Year'].min()))

        # display the maximum year value
        print('the most recent year of birth year is ', int(df['Birth Year'].max()))

        # display the most common year
        print('the most common year of birth year is ', int(df['Birth Year'].value_counts().keys()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_more_row(df):

    part_df = df.iloc[0:5].to_dict('index')
    for key in part_df.keys():

        # print dict in a nice format
        pprint.pprint(part_df[key])
        print()
    print('\n')

    # get input from user
    response = input('Would you like to see an indivisual trip data \"yes\" or \"no\"??\n')
    start_row = 5
    end_row = 10



    while end_row < df.shape[0] and response == 'yes':

        # convert data frame to dictionary
        part_df = df.iloc[start_row:end_row].to_dict('index')
        for key in part_df.keys():

            # print dict in a nice format
            pprint.pprint(part_df[key])
            print()
        print('\n')

        # update start and end row
        start_row += 5
        end_row += 5

        # ask user again if he want more data
        response = input('Would you like to see an indivisual trip data \"yes\" or \"no\"??\n').strip().lower()
    print('\n\n')


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_more_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
