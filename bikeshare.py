import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please choose the city between Chicago, New York City, Washington: ')
        cities = ['chicago', 'new york city', 'washington']
        if city.lower() in cities:
            break
        else:
            print('The city name is wrong!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('please enter the month ')
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', \
                  'september', 'october', 'november', 'december']
        if month.lower() in months: # added lower to accept uppercase entries
            break
        else:
            print('month name is wrong! please check spelling and enter name of the month')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter day of week:')
        days = ['monday','tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day.lower() in days: # added lower to accept uppercase entries
            break
        else:
            print('day name is wrong! please check spelling and enter day again')
    #day = days.get(day)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',\
                  'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df.loc[df['month']==month]

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    print(df['month'].mode()[0]) # mode will give frequent month 

    # TO DO: display the most common day of week
    df['dayofweek'] = df['Start Time'].dt.weekday_name
    print(df['dayofweek'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print(df[['End Station', 'Start Station']].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print('No Gender column')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('earliest birth date :', df['Birth Year'].min())
        print('most recent birth date :', df['Birth Year'].max())
        print('most common birth year :', df['Birth Year'].mode())
    except KeyError:
        print('No Gender column') # added since some data files no gender col


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """

    start=0
    end=5
    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        # Check if response is yes, print the raw data and increment count by 5

        if answer.lower()=='yes':
                print(df.iloc[start:end])
                start += 5  #incrementing start and end values to show next 5 lines of data
                end += 5
        else:
            break
        # otherwise break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
