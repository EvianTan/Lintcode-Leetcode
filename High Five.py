'''
High Five 

 Description
 Notes
 Testcase
 Judge
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Have you met this question in a real interview? Yes
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return 
'''

def highFive(self, results):
        # Write your code here
        dict = {}
        for x in results:
            if x.id not in dict:
                dict[x.id] = []
            dict[x.id].append(x.score)
            if len(dict[x.id]) > 5:
                index = 0
                for i in xrange(1, 6):
                    if dict[x.id][i] < dict[x.id][index]:
                        index = i
                dict[x.id].pop(index)
        res = {}
        for id, scores in dict.items():
            res[id] = sum(scores)/5.0
        return res