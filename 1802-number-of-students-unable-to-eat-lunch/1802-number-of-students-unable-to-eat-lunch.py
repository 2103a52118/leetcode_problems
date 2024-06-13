class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        i = 0
        j = 0
        eat = 0
        while j < len(sandwiches):
            if students[i] == sandwiches[j]:
                eat += 1
                i += 1
                j += 1
            else:
                num = students[i]
                students.append(num)
                i += 1
                if (i > 5 * n):
                    break

        return n - eat