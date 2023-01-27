import random
when = ['Two years ago', 'In the middle of the night', 'Few years ago', 'Just yesterday','On 26th Jan 2023']
who = ['A girl', 'The twins', 'My mom', 'My son','Their grandma']
name = ['Dare', 'Jeremmy','Arby', 'Tobi', 'Seyi']
residence = ['Nigeria','India', 'Sweeden', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Licked a lot of ice cream', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))