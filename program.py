from worker import Worker
from manager import Manager
from contractor import Contractor

dare = Worker(101, 'Matthew Michael Murdock', 'Nelson & Murdock, Attorneys at Law, NY', 35, 1989,8, 100)
stark = Manager(202,'Tony Stark', 'Stark Tower, NY', 45, 1979,5000, 100)
hit = Contractor(47,'Agent 47', 'Adlerstrasse, Berlin', 30, 1995,50, 1000000)


print(dare)
print(stark)
print(hit)