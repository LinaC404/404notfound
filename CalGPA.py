# 5-grade
# -----------------------------------------
# | Score	Point	   Score	   Point  |
# | 90-100	4.0-5.0	 Excellent 95	4.5   |
# |	80-89	3.0-3.9  Good 85	    3.5   |
# | 70-79	2.0-2.9	 Medium 75	    2.5   |
# | 60-69	1.0-1.9	 Pass 65	    1.5   |
# |	Below60	0.0	     Fail	        0.0   |
# -----------------------------------------
# Source -> https://lvyou.zjgsu.edu.cn/_upload/article/files/5e/2d/39f0186a4452bac06bcc02192eeb/a2a6565a-d888-41fa-b82b-b1a9530e9173.doc
# Credit->the credit of course; Point-> What I got from the course
credit1 = [1,2,1,4,6,4,1,1,1,3,1,1]
points1 = [3.8,1.7,3.6,2.7,2.7,1.3,1.4,3.6,3.0,3.5,2.2,3.7]
credit2 = [2,3,1,3,4,3,4,1,1,1,2,1]
points2 = [4.5,1.1,2.7,2.8,1.8,1.0,2.0,3.5,2.3,3.3,1.5,2.8]
credit3 = [3,1,3,3,0.5,3,2,1,2,3,1,1,1,1]
points3 = [2.4,2,2.4,2.6,3.8,2.7,4.2,1.5,2.8,3.4,3.5,3.9,1,0]
credit4 = [3,3,1,1,6,1,3,3,3,2,1,1]
points4 = [2.5,1.8,3.5,1.9,3.3,3.7,3.4,1.1,3.5,3.6,1.6,3.5]
credit5 = [3,2,2,3,1,3,2,3,2,2]
points5 = [2.9,4.5,3.5,1.3,2.4,3.3,2.2,3.9,2.4,4.6]
credit6 = [1,3,3,0.5,3,3,2,2,2,2,1]
points6 = [3.6,3.0,3.9,1.5,3.8,3.3,3.5,2.9,4.0,3.2,3.5]
credit7 = [2]
points7 = [3.6]

GPA_list = []
avg_GPA = 0
credit_list = [credit1, credit2, credit3, credit4, credit5, credit6, credit7]
point_list = [points1, points2, points3, points4, points5, points6, points7]
all_sum = 0

for i in range(0,len(credit_list)):
    term_sum = 0
    ter_GPA = 0
    for j in range(0,len(credit_list[i])):
        # print(credit_list[i][j],point_list[i][j])
        term_sum = term_sum + credit_list[i][j]*point_list[i][j]

    term_GPA = term_sum/sum(credit_list[i])
    all_sum = all_sum + term_sum
    GPA_list.append(term_GPA)

avg_GPA  = all_sum/sum(sum(flag) for flag in credit_list)
print(GPA_list)
print("AVG GPA: ",avg_GPA)
