
# This line is necessary.
from gevent import monkey
monkey.patch_all()

from getpass import getpass
from salesforce_streaming_client import SalesforceStreamingClient


def main():
    print("hello!")

    oauth_info = get_oauth_info()

    print(oauth_info)

    # todo: use ServiceApplicationClient class

    with ClientOne(
        oauth_client_id=oauth_info[0],
        client_secret=oauth_info[1],
        username=oauth_info[2]
    ) as client:
        client.subscribe('/u/aaa', 'shutdown_myself')
        client.start()
        client.block()

    # v = getpass('input user name.')
    # print(v)

class ClientOne(SalesforceStreamingClient):
    def shutdown_myself(self, connect_response_element):
        connect_response_element_payload = \
            connect_response_element['data']['payload']
        self.result = connect_response_element_payload
        self.shutdown()

def get_oauth_info():
    # Yes, it's annoying that you can't see these that are not
    # secret echoed.  But getpass() is smart about where it opens the input
    # stream, so I'm using it for now.
    oauth_client_id = getpass(
        'Enter full path to a test config file, or '
        'enter an oauth2 client identifier: '
    )

    config_fileh = None
    try:
        config_fileh = open(oauth_client_id, 'r')
    except IOError:
        client_secret = getpass('Enter oauth2 client secret: ')
        username1 = getpass('Enter first username: ')
        username2 = getpass('Enter second username: ')
        sandbox = getpass('Enter yes if sandbox: ') == 'yes'
    else:
        lines = config_fileh.readlines()
        oauth_client_id = lines[0].rstrip()
        client_secret = lines[1].rstrip()
        username1 = lines[2].rstrip()
        username2 = lines[3].rstrip()
        sandbox = lines[4].rstrip() == 'yes'

    return (
        oauth_client_id,
        client_secret,
        username1,
        username2,
        sandbox
    )

if __name__ == "__main__":
    main()