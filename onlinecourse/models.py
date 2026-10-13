# Question model
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=50)

    def __str__(self):
        return "Question: " + self.content

    # Check if learner gets the score for this question
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(
            is_correct=True
        ).count()

        selected_correct = self.choice_set.filter(
            is_correct=True,
            id__in=selected_ids
        ).count()

        return all_answers == selected_correct


# Choice model
class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


# Submission model
class Submission(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id}"