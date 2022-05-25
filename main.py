from parser import parse


token = '5233084458:AAE79zJ8kI3Fx7nNmGkpTHI6pyRE-FcyGkI'

url = 'https://profile-psi-three.vercel.app/'


def main():
    global token, url
    parse(url)


if __name__ == "__main__":
    main()
