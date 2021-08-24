import click


@click.command()
@click.argument('text_file_path', default ='C:/Users/hp/Documents/Quadratyx/QTX_Activities/inputVowel.txt')
def CLI_Vowel(text_file_path):
    """counts the no. of vowels in a text file."""

    v = ["a", "e", "i", "o", "u"]
    file = open(text_file_path, "r+")
    file1 = file.read()
    global count
    count = 0
    for i in file1.lower():
        if i in v:
            count = count + 1
    print("The vowel count is :{}".format(count))


if __name__ == '__main__':
    CLI_Vowel()
