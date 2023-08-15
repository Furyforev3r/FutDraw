from draw import draw


def main():
    teams = input("Teams...\n- ").split(", ")
    draws = draw(teams)

    print(draws)


if __name__ == '__main__':
    main()
