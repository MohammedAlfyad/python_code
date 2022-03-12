#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('Hello from Home')


# In[4]:


name = 'Alfyad'
age = 24

print(name)
print(age)


# In[10]:


grade = 70

if grade < 50:
    print('You Failed')
elif grade < 60:
    print('You Good')
elif grade < 85:
    print('You Very good')
else:
    print('You Excellent')


# In[17]:


programming_languages = ['C++' , 'Python' , 'C#' , 'Java' , 'Html' , 'CSS']
programming_languages[-4]


# In[19]:


programming_languages[1:4]


# In[22]:


programming_languages.append('Java Script')
programming_languages


# In[25]:


programming_languages.insert(3,'R')
programming_languages


# In[33]:


del programming_languages[4]
programming_languages


# In[39]:


programming_languages = ['C++' , 'Python' , 'C#' , 'Java' , 'Html' , 'CSS']
for programming_languages in programming_languages:
    print('I LOve ' + programming_languages)


# In[41]:


student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)


# In[44]:


student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# In[48]:


skill_languages = {
    'Html': '95%',
    'CSS': '80%',
    'Java Script': '75%',
    'Jquary': '50%',
}


# In[53]:


skill_languages['CSS']


# In[54]:


'Html' in skill_languages


# In[57]:


skill_languages['CSS'] = '83%'
skill_languages


# In[58]:


for key in skill_languages:
    value = skill_languages[key]
    print(key, 'his Rate', value)


# In[59]:


student_grades


# In[60]:


student_grades[2]


# In[63]:


student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records

