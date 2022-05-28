class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("Name changed from", self.name, "to", self.change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("Age changed from", self.age, "to", self.change_age)

    def add_track(self, add_track):
        self.add_track = add_track
        print("Add track changed from", self.tracks, "to", self.add_track)

    def get_score(self):

        print("Score did not change from", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
