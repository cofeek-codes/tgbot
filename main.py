from bot.bot import get_updates
from parser.parser import parse


url = 'https://profile-psi-three.vercel.app/'


def main():
    global url
    titles, skills = parse(url)

    get_updates()


if __name__ == "__main__":
    main()
