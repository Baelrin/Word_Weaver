import re


def read_story(file_path):
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
    pattern = re.compile(r"\{.*?\}")
    return set(pattern.findall(story))


def replace_words(story, words_to_replace, answers):
    for word in words_to_replace:
        if word in answers:
            story = story.replace(word, answers[word])
    return story


def get_answers(words_to_replace):
    answers = {}
    for word in words_to_replace:
        while True:
            if answer := input(f"Enter a word for {word}: "):
                answers[word] = answer
                break
            else:
                print("Input cannot be empty.")
    return answers


def main():
    story_path = "story.txt"
    story = read_story(story_path)
    if story is None:
        return

    words_to_replace = find_words_to_replace(story)
    answers = get_answers(words_to_replace)
    updated_story = replace_words(story, words_to_replace, answers)

    print(updated_story)


if __name__ == "__main__":
    main()
