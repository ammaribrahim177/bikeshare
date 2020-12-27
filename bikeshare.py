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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to         handle invalid input
    city ='' 
    all_cities = sorted(set(CITY_DATA ))
    while city not in all_cities:
          city = input("\n plz input a  vaild city name (chicago, new york city, washington)\n")
    print("very good the choosen city is {}".format(city))
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month =input("\n plz inputinput for month (all, january, february, ... , june)")
    if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        print ("the selcted input is vaild your month is {}".format(month))
    else:
        print("invaild input")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =input("\n plz input input for day of week (all, monday, tuesday, ... sunday)")
    if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                    'saturday', 'sunday']:
        print ("the selcted input is vaild your day is {}".format(day))
    else:
        print("invaild input")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] =pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S.%f')
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print(popular_month)

    # TO DO: display the most common day of week
    day_of_week = df['day_of_week'].value_counts().idxmax()
    print(day_of_week)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print(popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    the_start_station = df['Start Station'].value_counts().idxmax()
    print(the_start_station)

    # TO DO: display most commonly used end station
    the_end_station = df['End Station'].value_counts().idxmax()
    print(the_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print(start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total trip dutation ",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print("mean" ,mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print(counts_of_user_types)

    # TO DO: Display counts of gender
    counts_of_gender = df['Gender'].value_counts()
    print(counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_brith_year = df['Birth Year'].min()
    print("earliest",earliest_brith_year)
    recent_brith_year = df['Birth Year'].max()
    print("recent",recent_brith_year)
    common_brith_year = df['Birth Year'].value_counts().idxmax()
    print("common",common_brith_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
