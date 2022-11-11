## Get started with the Amadeus Python SDK

With this repository you can make your first API call using the [Amadeus Python SDK](https://github.com/amadeus4dev/amadeus-python). 

### Prerequisites

Python 3.4+
An [Amadeus for Developers](https://developers.amadeus.com) account


### How to run the project

Clone the repository.

```sh
git clone https://github.com/amadeus4dev/amadeus-get-started-python.git
cd amadeus-get-started-python
```

Next create a virtual environment with [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html) and install the Python SDK.

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

For authentication add your API key/secret to your environmental variables.

```sh
export AMADEUS_CLIENT_ID=YOUR_API_KEY
export AMADEUS_CLIENT_SECRET=YOUR_API_SECRET
```

### License

This library is released under the [MIT License](LICENSE).

### Help

You can find us on [StackOverflow](https://stackoverflow.com/questions/tagged/amadeus) or join our developer community on
[Discord](https://discord.gg/cVrFBqx).