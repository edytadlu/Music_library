import display
from display import *

def read_albums(file_path):
    data = []
    with open(file_path) as file:
        lines = file.readlines()  
    for line in lines:
        splitted_line = line.strip().split(',')
        data.append(splitted_line)
 
    return data


def album_by_genre(albums): 
    genre = ['progresive rock', 'pop', 'rock', 'hard rock', 'hip hop', 'ancient']
    genre = (", ".join(genre))
    user_genre = input('Choose the genre: ' + str(genre)+ '\n')
    new_albums = []
    for album in albums:
        if user_genre in album[3]:
            new_albums.append(album)
    return new_albums


def album_by_time_range(albums):
    user_range = input('Enter time range (e.g. 1997-2012) ')
    user_range = user_range.split('-')
    new_albums = []
    for album in albums:
        if int(user_range[0]) <= int(album[2]) and int(user_range[1]) >= int(album[2]):
            new_albums.append(album)
    return new_albums


def shortest_longest_album(albums):
    shortest = albums[0] # [b, n, h]
    longest = albums[0]
    for album in albums:
        if duration_to_seconds(album[4]) < duration_to_seconds(shortest[4]):
            shortest = album

        if duration_to_seconds(album[4]) > duration_to_seconds(longest[4]):
            longest = album
    return [shortest,longest] 


def duration_to_seconds(duration): # duration = 42:20
    minutes_seconds = duration.split(':') # minutes_seconds = ['42', '21']
    seconds = int(minutes_seconds[1]) + int(minutes_seconds[0]) * 60
    return seconds


def search_by_artist(albums):
    artist = input('Please enter artist: ')
    new_albums = []
    for album in albums:
        if artist.capitalize() in album[0]:
            new_albums.append(album)
    return new_albums


def search_by_album_name(albums):
    album_name = input('Please enter album name: ')
    new_albums = []
    for album in albums:
        if album_name.capitalize() in album[1]:
            new_albums.append(album)

    return new_albums


def main():
    path = "text_albums_data.txt"
    albums = read_albums(path)

    is_running = True
    while is_running:
        display_menu()
        user_choice = input('Your choice: ')
        if user_choice == '1':
            print_table(albums)
        elif user_choice == '0':
            is_running = False
        elif user_choice == '2':
            print_table(album_by_genre(albums))
        elif user_choice == '3': 
            print_table(album_by_time_range(albums))
        elif user_choice == '4':
            filtered_albums = shortest_longest_album(albums)
            print('The shortest album is: ')
            print_table([filtered_albums[0]])
            print('The longest album is: ')
            print_table([filtered_albums[1]])
        elif user_choice == '5':
            print_table(search_by_artist(albums))
        elif user_choice == '6':
            print_table(search_by_album_name(albums))


main() 
