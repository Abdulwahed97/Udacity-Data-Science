import time
import pandas as pd
import numpy as np


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
    city = input("Please input the city name: chicago, new york city and washington ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "City is name is invalid! Please input another name: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day? Please type your response.\n')

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
    # load file 
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start column to datetime()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Convert the End Time column to datetime()
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns using lambda 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

#Printing the time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: {} ".format(
        df['Start Station'].mode().values[0])
    )

    # display most commonly used end station
    print("The most common end station is: {}".format(
        df['End Station'].mode().values[0])
    )

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['combination'].mode().values[0])
    )
#Printing the time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
#  for duration end-start
    df['duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # display mean travel time
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Here are the counts of various user types:")
    print(df['User Type'].value_counts())
# because gender only for new york and chicago 
    if city != 'washington':
        # Display counts of gender
        print("Here are the counts of gender:")
        print(df['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
        
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    _start = 0
    end = 5

    display_active = input("if you want to see the raw data? Enter yes or no: ").lower()

    if display_active == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[_start:end,:])
            _start += 5
            end += 5

            display = input("Do you wish to continue?: ").lower()
            if display == 'no':
                break
    


def main():
	//?

    while 1==1:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
