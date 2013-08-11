from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)

_SAT_MATH_CHOICES = (
    ('0', 'I did not take the SAT'),
    ('-99', 'I do not remember my SAT math score'),
    ('400', '400 or below'),
    ('410', '410'),
    ('420', '420'),
    ('430', '430'),
    ('440', '440'),
    ('450', '450'),
    ('460', '460'),
    ('470', '470'),
    ('480', '480'),
    ('490', '490'),
    ('500', '500'),
    ('510', '510'),
    ('520', '520'),
    ('530', '530'),
    ('540', '540'),
    ('550', '550'),
    ('560', '560'),
    ('570', '570'),
    ('580', '580'),
    ('590', '590'),
    ('600', '600'),
    ('610', '610'),
    ('620', '620'),
    ('630', '630'),
    ('640', '640'),
    ('650', '650'),
    ('660', '660'),
    ('670', '670'),
    ('680', '680'),
    ('690', '690'),
    ('700', '700'),
    ('710', '710'),
    ('720', '720'),
    ('730', '730'),
    ('740', '740'),
    ('750', '750'),
    ('760', '760'),
    ('770', '770'),
    ('780', '780'),
    ('790', '790'),
    ('800', '800'),
)

_HS_MATH_CHOICES = (
    ('Algebra', 'Algebra'),
    ('Geometry', 'Geometry'),
    ('Precalc_Analysis', 'Precalc/Analysis'),
    ('Non_AP_Calc', 'Non-AP Calculus'),
    ('AP_Calc_AB', 'AP Calculus AB'),
    ('AP_Calc_BC', 'AP Calculus BC'),
    ('equiv_115', 'The equivalent of Math 115 (Calc 1) at a College/University'),
    ('equiv_116', 'The equivalent of Math 116 (Calc 2) at a College/University'),
    ('equiv_215', 'The equivalent of Math 215 (Calc 3: Multivariable Calculus) at a College/University'),
    ('equiv_216', 'The equivalent of Math 216 (Calc 4: Differential Equations) at a College/University'),
    ('Other', 'Other'),
)

_ACT_MATH_CHOICES = (
    ('0', 'I did not take the ACT'),
    ('-99', 'I do not remember my ACT math score'),
    ('15', '15 or below'),
)

_PAS_PHYSICS_CHOICES = (
    ('UMich', "I've taken physics at U of M"),
    ('Com_College', "I've taken physics at a community college"),
    ('APB', 'AP Physics B'),
    ('APC', 'AP Physics C'),
    ('Honors', 'Honors High School Physics'),
    ('NonHonors', 'High School Physics'),
    ('None', 'I have never taken a physics class'),
)

_DECLARED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_SEMESTERS_COMPLETED_CHOICES = (
    ('9', 'More than 8 semesters'),
)

_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

_COURSE_CHOICES = (
    ('135', 'Physics 135'),
    ('235', 'Physics 235'),
    ('140', 'Physics 140'),
    ('240', 'Physics 240'),
)

_LEARNER_CHOICES = (
    ('auditory', 'I learn best when I hear the information like in lecture or when a friend explains it.  I digest information best by talking.'),
    ('diagram', "I learn best when there's a picture or diagram involved.  I digest information best by creating a visual representation."),
    ('text', "I learn best when there's a written description for me to read.  I digest information best by writing."),
    ('none', "I'm not really a particular type of learner."),
)

_CONCENTRATE_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Physics', 'Physics/Astrophysics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Biology_MCDB', 'Biology MCDB'),
    ('Biology_EEB', 'Biology EEB'),
    ('Health', 'Health-related Field (Physical Therapy, Pharmacology, Nursing, etc.)'),
    ('Humanities', 'Humanities'),
    ('Math', 'Mathematics'),
    ('Neurosci', 'Neuroscience'),
    ('Social_Science_not_Psych', 'Social Science (excluding Psychology)'),
    ('Psych_BBCS', 'Psychology or BBCS'),
    ('Education', 'Education'),
    ('IDK', 'I do not know'),
    ('Other', 'Other'),
)

_ATTITUDE_PHYSICS_NOEX_CHOICES = (
    ('negative', "I haven't had much experience, but I've heard it's hard, so I'm petrified."),
    ('neg_noexp', "I haven't had much experience, but I've heard it's hard, so I'm somewhat nervous, but I think I will get able to get my goal grade."),
    ('pos_noexp', "I haven't had much experience, but from what I know of it, it sounds interesting."),
    ('positive', "I haven't had much experience, but I think physics is really interesting and I'm excited to take this course."),
)

_HS_ACTIVITY_CHOICES = (
    ('Music', 'Music'),
    ('Sports', 'Sports'),
    ('Theater', 'Theater'),
    ('Clubs', 'Clubs'),
    ('Publications', 'Publications'),
    ('None', 'None'),
)

_POST_COLLEGE_CHOICES = (
    ('Employment', 'Employment'),
    ('Med_School', 'Medical School or other Health-related Professional School'),
    ('Dent_School', 'Dental School'),
    ('Education', 'Education (teaching, policy, or a certification program)'),
    ('Grad_Life_Sci', 'Graduate School in a Life Science discipline'),
    ('Grad_Other', 'Graduate School in another discipline'),
    ('IDK', "Unsure/I don't know"),
    ('Other', 'Other'),
)

_ATTITUDE_EXAM_CHOICES = (
    ('prefer', 'I prefer them to free response.'),
    ('fine', "They're fine.  I feel like they accurately assess my ability to solve physics problems."),
    ('dislike', "I don't feel like I get a fair chance to demonstrate my ability without having partial credit."),
    ('stress', 'They stress me out.'),
)

_ATTITUDE_PHYSICS_EXP__CHOICES = (
    ('negative', "I'm not a physics person."),
    ('neg_exp', "I heard this class is difficult, so I'm nervous about it."),
    ('pos_exp', "I struggled with physics in the past, so I'm nervous, but I think I will be able to get my goal grade."),
    ('positive', "I really enjoyed physics in the past and did well, so I'm not worried."),
)

_PARTNER_CHOICES = (
    ('Perfect_Partner', 'Yes, I have a perfect study partner.'),
    ('Know_Like_To', "I know someone and I'd like to study with them."),
    ('Know_Alone', "I know someone, but I'd like to study alone."),
    ('No', "No, I don't know anyone in this course."),
)

_HIGH_SCHOOL_CUMGPA_CHOICES = (
    ('2_0', 'Less than 2.0'),
    ('2_1', '2.1'),
    ('2_2', '2.2'),
    ('2_3', '2.3'),
    ('2_4', '2.4'),
    ('2_5', '2.5'),
    ('2_6', '2.6'),
    ('2_7', '2.7'),
    ('2_8', '2.8'),
    ('2_9', '2.9'),
    ('3_0', '3.0'),
    ('3_1', '3.1'),
    ('3_2', '3.2'),
    ('3_3', '3.3'),
    ('3_4', '3.4'),
    ('3_5', '3.5'),
    ('3_6', '3.6'),
    ('3_7', '3.7'),
    ('3_8', '3.8'),
    ('3_9', '3.9'),
    ('4_0', '4.0'),
)

_SLC_INTEREST_CHOICES = (
    ('Signed_Up', "Yes, I'm already signed up."),
    ('Yes_Not_Signed_Up', 'Yes, but I have not signed up yet.'),
    ('Not_Interested', "No, I'm not interested."),
    ('IDK', "What's the Science Learning Center?"),
)

GRADE_CHOICES_CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C', 'C'),
    ('C_minus_or_below', 'C minus or below'),
)

_GOAL_GRADE_RESET__CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C', 'C'),
    ('C_minus_or_below', 'C minus or below'),
    ('No', 'No thanks'),
)

_GOAL_GRADE_RESET_1_CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C', 'C'),
    ('C_minus_or_below', 'C minus or below'),
    ('No', 'No thanks'),
)

_ATTITUDE_MATH_CHOICES = (
    ('negative', 'I am not a math person.'),
    ('semi', "I wish there was a math review at the beginning.  I probably learned the math needed at some point, but I've forgotten a lot of it."),
    ('positive', 'I am confident in my math abilities.'),
)

_CUM_GPA_SURVEY_CHOICES = (
    ('2_0', '2.0 or lower'),
    ('2_1', '2.1'),
    ('2_2', '2.2'),
    ('2_3', '2.3'),
    ('2_4', '2.4'),
    ('2_5', '2.5'),
    ('2_6', '2.6'),
    ('2_7', '2.7'),
    ('2_8', '2.8'),
    ('2_9', '2.9'),
    ('3_0', '3.0'),
    ('3_1', '3.1'),
    ('3_2', '3.2'),
    ('3_3', '3.3'),
    ('3_4', '3.4'),
    ('3_5', '3.5'),
    ('3_6', '3.6'),
    ('3_7', '3.7'),
    ('3_8', '3.8'),
    ('3_9', '3.9'),
    ('4_0', '4.0'),
)

STUDY_RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

_EMPLOYMENT_CHOICES = (
    ('No_Job', 'I do not have a job'),
    ('Part_Time', 'I work a part-time job (20 hours or less a week)'),
    ('Full_Time', 'I work a full-time job (more than 20 hours a week)'),
)

_PARENT_ED_CHOICES = (
    ('Less_HS', 'Less than High School'),
    ('HS', 'High School/GED'),
    ('Some_College', 'Some College'),
    ('2_Year_College', '2-Year College Degree (Associates)'),
    ('4_Year_College', '4-Year College Degree (BA, BS)'),
    ('Masters', "Master's Degree"),
    ('Doctoral', 'Doctoral Degree'),
    ('Professional', 'Professional Degree (MD, JD)'),
)

_CONFIDENCE_CHOICES = (
    ('Not_confident', 'Not confident'),
    ('Somewhat_confident', 'Somewhat<br>confident'),
    ('Confident', 'Confident'),
    ('Very_confident', 'Very confident'),
)

_ANOTHER_HARD_CLASS_CHOICES = (
    ('yes', 'yes'),
    ('no', 'no'),
)

_REASON_CHOICES = (
    ('Physics_req', 'I am considering majoring in physics.'),
    ('Concentration_req', 'This physics course is required by my major.'),
    ('Grad_req', 'I need to take physics to prepare for my graduate/professional program.'),
    ('NS_Credit', 'For Natural Science credit.'),
    ('Interest', "I'm taking this class because of my interest in physics."),
)

_PAST_PHYSICS_WHE_CHOICES = (
    ('1', 'last year'),
    ('2', '2 years ago'),
    ('3', '3 years ago'),
    ('4', '4 years ago'),
    ('5', '5 or more years ago'),
)

_GOAL_GRADE_RESET__COPY2_CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C', 'C'),
    ('C_minus_or_below', 'C minus or below'),
    ('No', 'No thanks'),
)

_GOAL_GRADE_CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C', 'C'),
    ('C_minus_or_below', 'C- or below'),
)

_INVOLVED_IN_CHOICES = (
    ('Greek', 'Greek Life (Sororities/Fraternities)'),
    ('Sports', 'Sports/Club Sports'),
    ('Religious', 'Religious Organizations'),
    ('Research', 'Research (Thesis, UROP, Lab work)'),
    ('Volunteering', 'Volunteering'),
    ('Music_Art', 'Music/Art'),
    ('Other', 'Other Student Clubs/Organzations'),
)

_CLASS_STANDING_CHOICES = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
)

_BIRTHMO_CHOICES = (
    ('-1', 'Month'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

_MOVIE_CHOICES = (
    ('StarWars', 'Star Wars (4-6 with references to 1-3)'),
    ('StarTrek', 'Star Trek (J.J. Abrams movies with references to previous shows and movies)'),
    ('LOTR', 'Lord of the Rings (All movies with references to "The Hobbit")'),
    ('Harry', 'Harry Potter (All movies)'),
    ('no', "I don't like any of these movies"),
    ('none', 'I have not seen any of these movies'),
)

_COLLEGE_CHOICES = (
    ('LSA', 'LSA'),
    ('Engineering', 'Engineering'),
    ('Kinesiology', 'Kinesiology'),
    ('Other', 'Other'),
)


class Source1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_source1'
    HS_Activity = models.CharField(max_length=12, choices=_HS_ACTIVITY_CHOICES, null=True, blank=True)
    Movie = models.CharField(max_length=8, choices=_MOVIE_CHOICES, null=True, blank=True)
    Movie_Other = models.CharField(max_length=50, null=True, blank=True)
    Course = models.IntegerField(null=True, blank=True)
    Another_Hard_Class = models.CharField(max_length=3, choices=_ANOTHER_HARD_CLASS_CHOICES, null=True, blank=True)
    Learner = models.CharField(max_length=8, choices=_LEARNER_CHOICES, null=True, blank=True)
    Attitude_Exams = models.CharField(max_length=7, choices=_ATTITUDE_EXAM_CHOICES, null=True, blank=True)
    Attitude_Physics_Noexp = models.CharField(max_length=9, choices=_ATTITUDE_PHYSICS_NOEX_CHOICES, null=True, blank=True)
    Attitude_Physics_Exp = models.CharField(max_length=8, choices=_ATTITUDE_PHYSICS_EXP__CHOICES, null=True, blank=True)
    Attitude_Math = models.CharField(max_length=8, choices=_ATTITUDE_MATH_CHOICES, null=True, blank=True)
    SAT_Math = models.IntegerField(null=True, blank=True)
    ACT_Math = models.IntegerField(null=True, blank=True)
    HS_Math = models.CharField(max_length=16, choices=_HS_MATH_CHOICES, null=True, blank=True)
    Past_Physics = models.CharField(max_length=11, choices=_PAS_PHYSICS_CHOICES, null=True, blank=True)
    Past_Physics_When = models.IntegerField(null=True, blank=True)
    HS_Math_Other = models.TextField(null=True, blank=True)
    Goal_Grade = models.CharField(max_length=16, choices=_GOAL_GRADE_CHOICES, null=True, blank=True)
    Confidence = models.CharField(max_length=18, choices=_CONFIDENCE_CHOICES, null=True, blank=True)
    Partner = models.CharField(max_length=15, choices=_PARTNER_CHOICES, null=True, blank=True)
    Reason = models.CharField(max_length=17, choices=_REASON_CHOICES, null=True, blank=True)
    SLC_Interest = models.CharField(max_length=17, choices=_SLC_INTEREST_CHOICES, null=True, blank=True)
    Exam_1_Score = models.FloatField(null=True, blank=True)
    Exam_2_Score = models.FloatField(null=True, blank=True)
    Exam_3_Score = models.FloatField(null=True, blank=True)
    Exam_Final_Score = models.FloatField(null=True, blank=True)
    MP_PreExam_1 = models.FloatField(null=True, blank=True)
    MP_PreExam_2 = models.FloatField(null=True, blank=True)
    MP_PreExam_3 = models.FloatField(null=True, blank=True)
    Participation_PreExam_1 = models.FloatField(null=True, blank=True)
    Participation_PreExam_2 = models.FloatField(null=True, blank=True)
    Participation_PreExam_3 = models.FloatField(null=True, blank=True)
    Confidence_PreExam1 = models.CharField(max_length=20, null=True, blank=True)
    Confidence_PreExam2 = models.CharField(max_length=20, null=True, blank=True)
    Confidence_PreExam3 = models.CharField(max_length=20, null=True, blank=True)
    Confidence_PreFinal = models.CharField(max_length=20, null=True, blank=True)
    Goal_PreExam1_1 = models.TextField(null=True, blank=True)
    Goal_PreExam1_2 = models.TextField(null=True, blank=True)
    Goal_PreExam1_3 = models.TextField(null=True, blank=True)
    Goal_PreExam2_1 = models.TextField(null=True, blank=True)
    Goal_PreExam2_2 = models.TextField(null=True, blank=True)
    Goal_PreExam2_3 = models.TextField(null=True, blank=True)
    Goal_PreExam3_1 = models.TextField(null=True, blank=True)
    Goal_PreExam3_2 = models.TextField(null=True, blank=True)
    Goal_PreExam3_3 = models.TextField(null=True, blank=True)
    Goal_PreFinal_1 = models.TextField(null=True, blank=True)
    Goal_PreFinal_2 = models.TextField(null=True, blank=True)
    Goal_PreFinal_3 = models.TextField(null=True, blank=True)
    Reflection_PreExam2_1 = models.TextField(null=True, blank=True)
    Reflection_PreExam2_2 = models.TextField(null=True, blank=True)
    Reflection_PreExam3_1 = models.TextField(null=True, blank=True)
    Reflection_PreExam3_2 = models.TextField(null=True, blank=True)
    Reflection_PreFinal_1 = models.TextField(null=True, blank=True)
    Reflection_PreFinal_2 = models.TextField(null=True, blank=True)
    Goal_Grade_Reset_1 = models.CharField(max_length=16, choices=_GOAL_GRADE_RESET_1_CHOICES, null=True, blank=True)
    Goal_Grade_Reset_2 = models.CharField(max_length=16, choices=_GOAL_GRADE_RESET__CHOICES, null=True, blank=True)
    Goal_Grade_Reset_3 = models.CharField(max_length=16, choices=_GOAL_GRADE_RESET__COPY2_CHOICES, null=True, blank=True)
    Pred_Grade_Initial = models.FloatField(null=True, blank=True)
    Pred_Grade_Exam1 = models.FloatField(null=True, blank=True)
    Pred_Grade_Exam2 = models.FloatField(null=True, blank=True)
    Pred_Grade_Exam3 = models.FloatField(null=True, blank=True)
    Pred_Grade_Final = models.FloatField(null=True, blank=True)

class EmptySource(SubjectData):
    pass

class Common1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_common1'
    First_Name = models.CharField(max_length=20, null=True, blank=True)
    Last_Name = models.CharField(max_length=20, null=True, blank=True)
    uniqname = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=_GENDER_CHOICES, null=True, blank=True)
    BirthDay = models.IntegerField(null=True, blank=True)
    BirthMo = models.IntegerField(null=True, blank=True)
    BirthYr = models.IntegerField(null=True, blank=True)
    Semesters_Completed = models.IntegerField(null=True, blank=True)
    College = models.CharField(max_length=11, choices=_COLLEGE_CHOICES, null=True, blank=True)
    College_Other = models.CharField(max_length=30, null=True, blank=True)
    Concentrate__Engineering = models.NullBooleanField()
    Concentrate__Physics = models.NullBooleanField()
    Concentrate__Chemistry = models.NullBooleanField()
    Concentrate__Biology = models.NullBooleanField()
    Concentrate__Biology_MCDB = models.NullBooleanField()
    Concentrate__Biology_EEB = models.NullBooleanField()
    Concentrate__Health = models.NullBooleanField()
    Concentrate__Humanities = models.NullBooleanField()
    Concentrate__Math = models.NullBooleanField()
    Concentrate__Neurosci = models.NullBooleanField()
    Concentrate__Social_Science_not_Psych = models.NullBooleanField()
    Concentrate__Psych_BBCS = models.NullBooleanField()
    Concentrate__Education = models.NullBooleanField()
    Concentrate__IDK = models.NullBooleanField()
    Concentrate__Other = models.NullBooleanField()
    Concentrate_Other = models.TextField(null=True, blank=True)
    Declared = models.CharField(max_length=3, choices=_DECLARED_CHOICES, null=True, blank=True)
    Class_Standing = models.CharField(max_length=9, choices=_CLASS_STANDING_CHOICES, null=True, blank=True)
    Cum_GPA_Survey = models.CharField(max_length=3, choices=_CUM_GPA_SURVEY_CHOICES, null=True, blank=True)
    Employment = models.CharField(max_length=9, choices=_EMPLOYMENT_CHOICES, null=True, blank=True)
    Involved_In__Greek = models.NullBooleanField()
    Involved_In__Sports = models.NullBooleanField()
    Involved_In__Religious = models.NullBooleanField()
    Involved_In__Research = models.NullBooleanField()
    Involved_In__Volunteering = models.NullBooleanField()
    Involved_In__Music_Art = models.NullBooleanField()
    Involved_In__Other = models.NullBooleanField()
    Other_Commitment = models.TextField(null=True, blank=True)
    Post_College = models.CharField(max_length=13, choices=_POST_COLLEGE_CHOICES, null=True, blank=True)
    Parent_Ed = models.CharField(max_length=14, choices=_PARENT_ED_CHOICES, null=True, blank=True)
    High_School_CumGPA = models.CharField(max_length=3, choices=_HIGH_SCHOOL_CUMGPA_CHOICES, null=True, blank=True)


