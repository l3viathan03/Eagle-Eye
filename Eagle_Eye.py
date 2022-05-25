# ================================================================================================ #
#                                                                                                  #
# OPEN-SOURCE INTELLIGENCE PROJECT: Eagle Eye                                                              #
#                                                                                                  #
# Description: This python script utilize Shodan Open Source Intelligence search engine to query   #
# data about any public IP address.                                                                #
#                                                                                                  #
# ================================================================================================ #

import sys
import shodan
from pyfiglet import Figlet

# Printing Banner
banner = Figlet(font='graffiti')
print(banner.renderText('     Eagle Eye'))
print(
'************************************************************************* \n'
'*                                                                      * \n'
'*      OPEN-SOURCE INTELLIGENCE PROJECT | 20151648@stu.uob.edu.bh      * \n'
'*      Open Source Intelligence search using Shodan API with Python    * \n'
'*      Created By Yusuf Almahmeed       | V2.0 - 25-5-2022             * \n'
'*                                                                      * \n'
'*************************************************************************'
)

# Calling Shodan API key
API_KEY = 'ZQnbdqMFzRswIAyScFlXqooAEyPXAFZ4'

# The list of properties we want summary information on
# We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
# default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
# to see the top 1,000 countries for a search query.
FACETS = [
    'org',
    'domain',
    'port',
    'ip',
    'country',
]

FACET_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'ip': 'Top 5 IP address',
    'country': 'Top 5 Countries',
}

print '\n Please choose the IOT device from the below menu to generate the report \n'

## Text menu in Python

def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. yawcam"
    print "2. HP Printers"
    print "3. Google Chromecast"
    print "4. Etherium Miners"
    print "5. Apple AirPlay Receivers"
    print "6. Exit"
    print 67 * "-"

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-6]: ")

    if choice==1:
        print "yawcam has been selected"
        ## You can add your code or functions here
        try:
            # Setup the api
            api = shodan.Shodan(API_KEY)

            # Generate a query string out of the command-line arguments
            query = 'Server: "yawcam"'

            # Use the count() method because it doesn't return results and doesn't require a paid API plan
            # And it also runs faster than doing a search().
            result = api.count(query, facets=FACETS)

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

            # Open a new file and write the output in it
            file_path = 'yawcam.txt'
            sys.stdout = open(file_path, "w")

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(1)

        loop=False # This will make the while loop to end as not value of loop is set to False
    elif choice==2:
        print "Menu 2 has been selected"
        ## You can add your code or functions here
        print "HP Printers"
        ## You can add your code or functions here
        try:
            # Setup the api
            api = shodan.Shodan(API_KEY)

            # Generate a query string out of the command-line arguments
            query = 'Serial Number:" "Built:" "Server: "HP HTTP"'

            # Use the count() method because it doesn't return results and doesn't require a paid API plan
            # And it also runs faster than doing a search().
            result = api.count(query, facets=FACETS)

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

            # Open a new file and write the output in it
            file_path = 'HP Printers.txt'
            sys.stdout = open(file_path, "w")

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(1)
        loop=False # This will make the while loop to end as not value of loop is set to False
    elif choice==3:
        print "Google Chromecast has been selected"
        ## You can add your code or functions here
        try:
            # Setup the api
            api = shodan.Shodan(API_KEY)

            # Generate a query string out of the command-line arguments
            query = 'Chromecast port:"8008"'

            # Use the count() method because it doesn't return results and doesn't require a paid API plan
            # And it also runs faster than doing a search().
            result = api.count(query, facets=FACETS)

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

            # Open a new file and write the output in it
            file_path = 'Google_Chromecast_Report.txt'
            sys.stdout = open(file_path, "w")

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(1)
        loop=False # This will make the while loop to end as not value of loop is set to False
    elif choice==4:
        print "Etherium Miners has been selected"
        ## You can add your code or functions here
        try:
            # Setup the api
            api = shodan.Shodan(API_KEY)

            # Generate a query string out of the command-line arguments
            query = 'product:"OpenEthereum"'

            # Use the count() method because it doesn't return results and doesn't require a paid API plan
            # And it also runs faster than doing a search().
            result = api.count(query, facets=FACETS)

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

            # Open a new file and write the output in it
            file_path = 'Etherium_Miners.txt'
            sys.stdout = open(file_path, "w")

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(1)
        loop=False # This will make the while loop to end as not value of loop is set to False
    elif choice==5:
        print "Apple AirPlay Receivers has been selected"
        ## You can add your code or functions here
        try:
            # Setup the api
            api = shodan.Shodan(API_KEY)

            # Generate a query string out of the command-line arguments
            query = 'airplay port:5353'

            # Use the count() method because it doesn't return results and doesn't require a paid API plan
            # And it also runs faster than doing a search().
            result = api.count(query, facets=FACETS)

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

            # Open a new file and write the output in it
            file_path = 'Apple_AirPlay_Receivers.txt'
            sys.stdout = open(file_path, "w")

            print 'Shodan Summary Information'
            print 'Query: %s' % query
            print 'Total Results: %s\n' % result['total']

            # Print the summary info from the facets
            for facet in result['facets']:
                print FACET_TITLES[facet]

                for term in result['facets'][facet]:
                    print '%s: %s' % (term['value'], term['count'])

                # Print an empty line between summary info
                print ''

        except Exception, e:
            print 'Error: %s' % e
            sys.exit(1)
        loop=False # This will make the while loop to end as not value of loop is set to False
    elif choice==6:
        print "Bye!!"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
