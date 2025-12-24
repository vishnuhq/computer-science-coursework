import requests

# requests.post("https://ntfy.sh/pvv421",
#               data="Have a look at these cute puppies!!".encode(encoding='utf-8'),
#               headers={"Title": "Cute Dog Pics"})

requests.post("https://ntfy.sh/pvv421",
              data=open("puppy.jpg", "rb"),
              headers={"Title": "Have a look at these cute puppies!!", "Filename": "cutedogs.jpg"})

# read the docs to play with this: https://docs.ntfy.sh/
