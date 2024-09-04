test_scores= {'Alice': [85, 90, 88],
                      'Bob': [90, 92, 86],
                      'Timny': [100, 100, 100],
                      'Nick': [90, 100, 100]}

def find_top_students(test_scores):
    #finding the highest score
    highest_score = 0
    for student in test_scores:
        for score in test_scores[student]:
            if score > highest_score:
                highest_score = score
    #finding the student with the highest score their average score
    for student in test_scores:
        for score in test_scores[student]:
            if score == highest_score:
                average = sum(test_scores[student]) / len(test_scores[student])
                return student, average
            
if __name__ == "__main__":
    print(find_top_students(test_scores))