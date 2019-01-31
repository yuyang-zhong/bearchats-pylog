import datetime
import os

### Utilities ###
cond = ["no so well", "alright", "well", "very well"]
he = ["he", "him", "his"]
she = ["she", "her", "her"]
they = ["they", "their", "their"]
tobes = ["is", "are"]
live = ["does not have plans yet",
        "currently looking", 
        "alreay found"]
places = ["on campus residence hall", 
            "on campus appartment", 
            "off campus appartment"]


class BearChats():
    """A BearChat object will collect and store information for a bear chat."""

    def __init__(self):
        """Create an empty BearChat."""

        self.time = str(datetime.datetime.now())

        # ask_name
        self.fn = None              # String
        self.ln = None              # String
        self.name = None            # String
        
        # ask_pronouns
        self.pronoun = None         # List of Strings
        self.tobe = None            # 
        
        # ask_classes
        self.class_cond = None      # Integer index
        self.class_note = None      # String
        
        # ask_habits
        self.habit_change = False   # Boolean
        self.new_habit = None       # String
        
        # ask_resources
        self.resources = None       # String
        
        # ask_success_goals
        self.success = None         # String
        self.goal1 = None           # String
        self.goal2 = None           # String
        self.goal3 = None           # String
        
        # ask_living
        self.living = None          # Integer index
        self.place = None           # Integer index
        
        # ask_relations
        self.relationship = None    # Integer index
        self.relate_note = None     # String
        
        # ask_concerns
        self.concerns = None        # String

        # print_report
        self.report = None


    def ask_name(self):
        if self.fn is None and self.ln is None:
            self.fn = input("** Resident First Name: ")
            self.ln = input("** Resident Last Name: ")
            self.name = self.fn + " " + self.ln

        else:
            print("Resident: %s", self.name)


    def ask_pronouns(self):
        if self.pronoun is None:
            pronoun_index = input("** Resident Pronouns (h/s/t): ")
            print("")

            while pronoun_index not in ["h", "s", "t"]:
                print("Invalid Argument. Try Again.") 
                pronoun_index = input("** Resident Pronouns (h/s/t): ")
                print("")

            if pronoun_index == "h":
                self.pronoun = he
                self.tobe = tobes[0]
            elif pronoun_index == "s":
                self.pronoun = she
                self.tobe = tobes[0]
            else: 
                self.pronoun = they
                self.tobe = tobes[1]

        else:
            print("Pronouns: %s", self.pronoun)


    def ask_classes(self):
        if self.class_cond is None and self.class_note is None:
            class_index = int(input("** Classes? (1-4, 4 best): "))
            print("")
            # add in error for entering non integer

            while class_index < 0 | class_index > 4:
                print("Invalid Argument. Try Again.") 
                class_index = int(input("** Classes? (1-4, 4 best): "))
                print("")

            self.class_cond = cond[class_index - 1]

            notes = input("Notes on classes (NA if none): \n>")
            print("")
            if not notes == "NA":
                self.class_note = notes

        else:
            print("Classes are going %s. Notes: %s", 
                self.class_cond, self.class_note)


    def ask_habits(self):
        if self.habit_change is False:
            changed_index = input("** Changed in study habits? (y/n): ")
            print("")

            while changed_index not in ["y", "n"]:
                print("Invalid Argument. Try Again.") 
                changed_index = input("** Changed in study habits? (y/n): ")
                print("")

            if changed_index == "y":
                self.habit_change = True
                self.new_habit = input("** New study habit(s): \n>")
                print("")

            else:
                self.habit_change = False

        else:
            print("New stuby habit(s): %s", self.new_habit)


    def ask_resources(self):
        if self.resources is None:
            self.resources =input("** Resources utilized: \n>")
            print("")

        else:
            print("Resources utilized: %s", self.resources)


    def ask_success_goals(self):
        if self.success is None:
            self.success = input("** Success of Last Semester: \n>")
            print("")
            self.goal1 = input("** Goal 1 for this semester: \n>")
            print("")
            g2 =  input("** Goal 2 for this semester (NA if none): \n>")
            print("")
            g3 =  input("** Goal 3 for this semester (NA if none): \n>")
            print("")

            if not g2 == "NA":
                self.goal2 = g2

            if not g3 == "NA":
                self.goal3 = g3

        else:
            print("Success of Last Semester: %s", self.success)
            print("Goals for this semester: ")
            print(self.goal1)
            print(self.goal2)
            print(self.goal3)


    def ask_living(self):
        if self.living is None and self.place is None:
            living_index = int(input("** Looking for housing? \n" +
                                    "(1 - no plan, 2 - looking, 3 - found) : "))
            print("")
            # add in error for entering non integer

            while living_index < 1 | living_index > 3:
                print("Invalid Argument. Try Again.") 
                living_index = int(input("** Looking for housing? \n" +
                                    "(1 - no plan, 2 - looking, 3 - found) : "))
                print("")

            self.living = live[living_index - 1]

            place_index = int(input("** Housing Plan? \n" +
                                    "(1 - campus reshall, " +
                                    "2 - campus apt, 3 - off campus) : "))
            print("")
            # add in error for entering non integer

            while place_index < 1 | place_index > 3:
                print("Invalid Argument. Try Again.") 
                place_index = int(input("** Housing Plan? \n" +
                                    "(1 - campus reshall, " +
                                    "2 - campus apt, 3 - off campus) : "))
                print("")

            self.place = places[place_index - 1]

        else:
            print("Search: %s", self.living)
            print("Plan: %s", self.place)


    def ask_relations(self):
        if self.relationship is None and self.relate_note is None:
            relate_index = int(input("** Floor/Room? (1-4, 4 best): "))
            print("")

            while relate_index < 0 | relate_index > 4:
                print("Invalid Argument. Try Again.") 
                relate_index = int(input("** Floor/Room? (1-4, 4 best): "))
                print("")
            # add in error for entering non integer

            self.class_cond = cond[relate_index - 1]

            notes = input("** Notes on relationships (NA if none): \n>")
            print("")

            if not notes == "NA":
                self.relate_note = notes

        else:
            print("Relationships with floor/roommates are %s. Notes: %s", 
                self.relationships, self.relate_note)


    def ask_concerns(self):
        if self.concerns is None:
            concerns = input("** Concerns? (NA if none): \n>")
            print("")

            if not concerns == "NA":
                self.concerns = concerns

        else:
            print("Concerns: %s", self.concerns)


    def print_report(self):
        self.report = ""

        # Name
        self.report += "Resident Name: %s %s\\n\\n" \
                        %(self.fn, self.ln)
        
        # Classes
        self.report += "%s %s doing %s in %s classes" \
                        %(self.fn, self.tobe, self.class_cond, self.pronoun[1])
        if self.class_note:
            self.report += ", and %s said that %s." %(self.pronoun[0], self.class_note)
        else: 
            self.report += ". "

        #


    def send_email(self):
        send = input("** Send email to ra-yuyang@berkeley.edu? (y/n): ")
        print("")

        while send not in ["y", "n"]:
            print("Invalid Argument. Try Again.") 
            send = input("** Send email to ra-yuyang@berkeley.edu? (y/n/a): ")
            print("")

        if send == "y":
            print("Sending Email...")
            os.system("echo %s | mail -s 'Bear Chat Log (%s)' ra-yuyang@berkeley.edu" 
                % (self.report, self.name))
            print("Email Sent.")

        elif send == "a":
            email = input("** Enter an alternative email address: ")
            print("Sending Email...")
            os.system("echo %s | mail -s 'Bear Chat Log (%s)' %s" 
                % (self.report, self.name, email))
            print("Email Sent.")

        else:
            print("Email not sent.")
            self.copy_to_clipboard()


    def copy_to_clipboard(self):
        copy = input("** Copy to clipboard? (y/n): ")
        print("")

        while copy not in ["y", "n"]:
            print("Invalid Argument. Try Again.") 
            copy = input("** Copy to clipboard? (y/n): ")
            print("")

        if copy == "y":
            os.system("echo %s | pbcopy" %self.report)
            print("Log copied to clipboard.")


    def ask_all(self):
        self.ask_name()
        self.ask_pronouns()
        self.ask_classes()
        self.ask_habits()
        self.ask_resources()
        self.ask_success_goals()
        self.ask_living()
        self.ask_relations()
        self.ask_concerns()


def main():
    print("||--------------######--------------||\n\n"
        + "Bear Chat Log Automated Generator\n"
        + "Created by Yuyang Zhong\n"
        + "University of California, Berkeley\n"
        + "Version 0.1 : Designed for Spring 2019 Bear Chats\n"
        + "Version Date : 31 January 2019\n"
        + "Licensed under Creative Commons BY-NC-SA 4.0\n\n"
        + "||--------------######--------------||")

    bc = BearChats()
    bc.ask_all()
    bc.print_report()
    bc.send_email()

main()










