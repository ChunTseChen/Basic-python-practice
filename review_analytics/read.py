datas = []
count = 0


def calculate_average_length_of_reviews(datas):
    sum_data_len = 0
    for data in datas:
        sum_data_len += len(data)
    print(f"Average data length: {sum_data_len / len(datas)}")


def filter_the_review_with_shorter_than_100_words(datas):
    result = []
    for data in datas:
        if len(data) < 100:
            result.append(data)
    print(f"There are {len(result)} reviews with shorter than 100 words.")


def filter_the_review_which_contains_good(datas):
    good = [data for data in datas if "good" in data]
    print(f"There are {len(good)} reviews which contain good words.")


with open("reviews.txt", "r") as f:
    for line in f:
        datas.append(line.strip())
        count += 1
        if count % 10000 == 0:
            print(len(datas))
        # print(len(data))

print(f"Finished reading {len(datas)} reviews")
calculate_average_length_of_reviews(datas)
filter_the_review_with_shorter_than_100_words(datas)
filter_the_review_which_contains_good(datas)
