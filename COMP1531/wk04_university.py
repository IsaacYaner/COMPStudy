class Course:
    def __init__(self, name):
        self._name = name    
        self._course_offerings =[]

    @property
    def name(self):
        return self._name

class CourseOffering:
    def __init__(self, course, term, year):
        self._course = course
        self._term = term
        self._year = year
        self._instructors = []
        
    def add_instructors(self,prof_list):
        self._instructors = prof_list

    @property
    def course(self):
        return self._course
    
    @property
    def instructors(self):
        return self._instructors

    @property
    def term(self):
        return self._term

    @property
    def year(self):
        return self._year

    def get_details(self):
        convenors = ""
        
        # Extract all instructors
        # for c in self._instructors:
        #     convenors += c._name + " "
        # Alternative syntax using list comprehension
        
        convenors = [c._name for c in self._instructors]
        details = "{} {} {} -instructors:{}".format(self._course.name, self._term, self._year, convenors)
        return details


class Professor:
    def __init__(self, name, empID):
        self._name = name
        self._empID = empID
        self._courses_taught = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def courses(self):
        return self._courses_taught

    def add_course_offering(self,cof):
        self._courses_taught.append(cof) 
    

class Chair(Professor):
    def __init__(self, name,empID,depName):
        super().__init__(name,empID)
        self._chairOf = depName

class Department:
    def __init__(self,name):
        self._name = name
        '''department aggregates lists of professors
           - hence, this aggregation is shown as an attribute inside Department
        ''' 
        self._professors = []
        self._courses = []

    def add_professor(self,prof):
        self._professors.append(prof)

    @property
    def name(self):
        return self._name

# Create an instance of department
d1 = Department("School of Computer Science")

# Create an instance of professor
p1 = Professor("john",123)

# Create an instance of chair
chair1 = Chair("andrew",234,d1)

# create a course instance
c1 = Course("COMP1531")

# create course-offering instances
cof1 = CourseOffering(c1,"T1",2019)
cof2 = CourseOffering(c1,"T3",2019)

# Add course-offerings to the professors
p1.add_course_offering(cof1)
p1.add_course_offering(cof2)
chair1.add_course_offering(cof2)

# Add the instructors to the course-offering
# This is now a bi-directional relationship 
# as course-offering knows the professors and 
# professors know the course-offering they teach

prof_list=[p1,chair1]
cof1.add_instructors(prof_list)
print(cof1.get_details())

