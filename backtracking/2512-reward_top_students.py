# https://leetcode.com/problems/reward-top-k-students/submissions/1418553746

def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
    positive_set = set(positive_feedback) 
    negative_set = set(negative_feedback)  
    
    student_points = {}

    for i in range(len(student_id)):
        student_points[student_id[i]] = student_points.get(student_id[i], 0) + self.getFeedbackPoints(positive_set, negative_set, report[i])
    
    sorted_students = sorted(student_id, key=lambda x: (-student_points[x], x))

    return sorted_students[:k]


def getFeedbackPoints(self,positive_set,negative_set,feedback):
    words_of_feedback = feedback.split()
    total_score = 0
    for word in words_of_feedback:
        if word in positive_set:
            total_score += 3
        if word in negative_set:
            total_score -= 1
    return total_score