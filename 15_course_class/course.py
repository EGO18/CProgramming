class Course:
    """
        course_name (private)
        list of students (private)


        addStudent(self, student) shouldn't enroll the same student twice

        getCourseName

        getStudents

        getNumberOfStudents

        dropStudent(self,student) Should provide a message with a dropped student name.
        Should check does the student enroll the course (print message)

        __str__ info about the course
    """

    pass

class InPersonCourse(Course):
    """
        private (room_number)
        private schedule (MWF 11 am - 11:50 am)
        private max_seats

        Override addStudent method (check are there available seats) print appropriate message

        Override __str__
    """