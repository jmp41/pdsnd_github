import time
import pandas as pd
import numpy as np
# This .py file analyze data from bike demand.


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
day_data = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        city = input('Which city are you interested in?\n').lower()
        if city in ['chicago','new york city','washington']:
            break
        print('Invalid inputs. Please try again.\n')

    # get user input for month (all, january, february, ... , june)
    while 1:
        month = input('Which month are you interested in?\n').lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        print('Invalid inputs. Please try again.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        day = input('Which day in a week are you interested in?\n').lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        print('Invalid inputs. Please try again.\n')

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
    df['day'] = df['Start Time'].dt.dayofweek
    if month!='all':
        df = df[df['month']==month_data[month]]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day_data[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print('The most common month:', list(month_data.keys())[df['month'].mode()[0] - 1])

    # display the most common day of week
    print('The most common day of week:', list(day_data.keys())[df['day'].mode()[0]])

    # display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    print('The most common start hour:', df['start hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station:',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used start station:',df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] +' To '+ df['End Station']
    print('The most popular trip:',df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    df['End Time'] = pd.to_datetime(df['End Time'])
    start_time = time.time()

    # display total travel time
    df['trip duration'] = df['End Time'] - df['Start Time']
    print('Total travel time:', df['trip duration'].sum(axis=0))

    # display mean travel time
    print('Mean travel time:', df['trip duration'].mean(axis=0))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print('User types count:\n',df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('User gender count:\n',df['Gender'].value_counts())
    except:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # Display earliest, most recent, and most common year of birth
    try:
        print('Earliest year of birth:',df['Birth Year'].min())
        print('Most recent year of birth:',df['Birth Year'].max())
        print('Most common year of birth:',df['Birth Year'].mode()[0])
    except:
        print('Birth year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[start_loc:(start_loc+5),:])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        view_data = view_display

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	# Analyze bikeshare data change 3
	print('start analyzing bikeshare data') #change 1
	main()
	print('finish analyzing bikeshare data') #change 2
