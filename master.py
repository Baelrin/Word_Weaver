import re


def read_story(file_path):
    """
    Reads the content of a file and returns its content as a string.

    :param file_path: Path to the file to be read.
    :return: Content of the file if successful, None otherwise.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def find_words_to_replace(story):
    """
    Finds and returns a set of words to replace in the story.

    :param story: The story string in which to find words to replace.
    :return: A set of words marked for replacement.
    """
    pattern = re.compile(r"\{.*?\}")
    return set(pattern.findall(story))


def replace_words(story, words_to_replace, answers):
    """
    Replaces words in the story that are found in `words_to_replace` with their corresponding replacements in `answers`.

    :param story: The original story string.
    :param words_to_replace: A set of words to replace in the story.
    :param answers: A dictionary mapping words to their replacements.
    :return: The story with the words replaced.
    """
    for word in words_to_replace:
        if word in answers:
            story = re.sub(re.escape(word), answers[word], story)
    return story


def get_answers(words_to_replace):
    """
    Prompts the user to enter replacements for the words to replace.

    :param words_to_replace: A set of words for which to get replacements.
    :return: A dictionary mapping each word to its replacement.
    """
    answers = {}
    for word in words_to_replace:
        while True:
            answer = input(f"Enter a word for {word}: ")
            if answer.strip():
                answers[word] = answer
                break
            else:
                print("Input cannot be empty or only spaces.")
    return answers


def main(story_path="story.txt"):
    """
    Main function to read a story, find and replace words, and print the updated story.

    :param story_path: The path to the story file.
    """
    story = read_story(story_path)
    if story is None:
        return

    words_to_replace = find_words_to_replace(story)
    answers = get_answers(words_to_replace)
    updated_story = replace_words(story, words_to_replace, answers)

    print(updated_story)


if __name__ == "__main__":
    main()
