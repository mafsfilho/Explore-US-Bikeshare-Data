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

    print('\nHello! Let\'s explore some US bikeshare data!')
    print("Don't worry about upper and lowercases. We will take care of it!")
    print("\nThe cities in our database are Chicago, New York City and Washington.\nThe months in our database are from January to June and you can select all of them by typing \"all\".")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        print("First, you'll need to choose between the following cities: Chicaco, New York City and Washington.")

        city = input("So now, select the city that you want to analyze: ").lower()

        try:
            city == CITY_DATA[city]
            break
        except KeyError:
            print("That\'s not a valid city. Your options are Chicago, New York City and Washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        print("\nOur data base has data from January to June, so you can select any of these months or select them all by typing \"all\".")

        month = str(input("\nSelect the month: ")).lower()

        month_options = ["all", "january", "february", "march", "april", "may", "june"]

        try:
            if month in month_options:
                break
            else:
                raise KeyError
        except:
            print("That\'s not a valid month. You can choose all of them by typing \"all\" or choose only one between January and June.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        print("\nEnter the day of the week that you want to analyze or type \"all\" to select all of them.")

        day = input("\nSelect the day of the week: ").lower()

        day_options = ["all", "monday", "thursday", "wednesday", "tuesday", "friday", "saturday", "sunday"]

        try:
            if day in day_options:
                break
            else:
                raise KeyError
        except:
            print("That\'s not a valid day of the week. Check if you're typing correctly. You can also select all of them by typing \"all\".")

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

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month

    df["day"] = df["Start Time"].dt.weekday_name

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        df = df[df["month"] == month]

    day = day.title()

    if day != "All":
        df = df[df["day"] == day]

    # This will show the head of a raw data using a while loop and offer to show more of it if the user want to
    while True:

        n = 5
        q1 = input("\nDo you want to see the raw data? ").lower()

        try:
            if q1 == "yes":
                print()
                print(df.head(n))

                while True:
                    q2 = input("\nDo you want to see more of the raw data? ")
                    try:
                        if q2 == "yes":
                            n += 5
                            print()
                            print(df[n-5:n])
                        elif q2 == "no":
                            break
                        else:
                            raise KeyError
                    except:
                        print("Your answer is not valid. Type \"yes\" or \"no\".")
                break

            elif q1 == "no":
                break
            else:
                raise KeyError
        except:
            print("Your answer is not valid. Type \"yes\" or \"no\".")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]

    months = {1: "january",
              2: "february",
              3: "march",
              4: "april",
              5: "may",
              6: "june"}

    print("The most common month is {}.".format(months[common_month]))

    # TO DO: display the most common day of week
    common_day = df["day"].mode()[0]

    print("The most common day is {}.".format(common_day))

    # TO DO: display the most common start hour

    df["hour"] = df["Start Time"].dt.hour

    common_hour = df["hour"].mode()[0]

    print("The most common start hour is {}:00.".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]

    print("The most commonly used start station is {}.".format(common_start_station))

    # TO DO: display most commonly used end station
    common_start_station = df["End Station"].mode()[0]

    print("The most commonly used end station is {}.".format(common_start_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["start and end stations"] = "from " + df["Start Station"] + " to " + df["End Station"]

    common_path = df["start and end stations"].mode()[0]

    print("The most commonly used path departs {}.".format(common_path))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df["Trip Duration"].sum()

    print("The total time our bikes have been rented is {} seconds.\n".format(total))

    # TO DO: display mean travel time
    mean = df["Trip Duration"].mean()

    print("Our bikes are rented for {0: .2f} seconds on average.".format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()

    print("Count of user types \n{}.\n".format(user_types))


    # TO DO: Display counts of gender
    try:
        user_gender = df["Gender"].value_counts()
        print("Count of user gender \n{}.\n".format(user_gender))
    except:
        print("We don't have the user gender statistic from Washington.\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = int(df["Birth Year"].min())
        most_recent_yob = int(df["Birth Year"].max())
        most_common_yob = int(df["Birth Year"].mode()[0])
        print("The earliest year of birth signed in our data base is {}. \nThe most recent year of birth is {}. \nAnd the most common year of birth is {}.".format(earliest_yob, most_recent_yob, most_common_yob))
    except:
        print("We don't have the year of birth statistics from Washington.")

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

        while True:

            try:
                restart = input("\nWould you like to restart? ")
                if restart.lower() == "yes":
                    print()
                    print("Rebooting...")
                elif restart.lower() == "no":
                    break
                else:
                    raise KeyError
            except:
                print()
                print("Your answer is not valid. Please type \"yes\" or \"no\".")


if __name__ == "__main__":
	main()
