
print('\n')
print('    ╔╦╗╦ ╦╔═╗╦╔═╗  ╦  ╦╔╗ ╦═╗╔═╗╦═╗╦ ╦')
print('    ║║║║ ║╚═╗║║    ║  ║╠╩╗╠╦╝╠═╣╠╦╝╚╦╝')
print('    ╩ ╩╚═╝╚═╝╩╚═╝  ╩═╝╩╚═╝╩╚═╩ ╩╩╚═ ╩ ')

print('\n')
def print_table(albums):
    print("-------------------------------------------------------------------------")
    print('ARTIST | ALBUM | YEAR OF RELEASE | GENRE | DURATION ')
    print("-------------------------------------------------------------------------")
    for album in albums:
        print(' | '.join(album))
    print("-------------------------------------------------------------------------")
        # artist = album[0]
        # print(artist)
        # album_name = album[1]
        # print(album_name)
        # year = int(album[2])
        # print(year)
        # genre = album[3]
        # print(genre)
        # album_time = int(album[4])
        # print(album_time)

def display_menu():
    print('Menu:')
    print("1 -> Display All")
    print("2 -> Find album by genre ")
    print("3 -> Find album from time range")
    print("4 -> Find shortest/longest album")
    print("5 -> Find the album by artist")
    print("6 -> Find the album by album name")
    print("0 -> Exit")

       