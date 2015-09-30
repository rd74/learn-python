name = 'Mikhail V. Marchenkov'
age = 41
height = 180
weight = 103
eyes = 'Brown'
teeth = 'white'
hair = 'Black'

print "Let's talk about %r." % name
print "He's %r cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's too heavy"
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r " \
    'depending on the ' \
    "coffee." % \
    teeth
print "If I add %d, %d, and %d I get %r." % \
    (age, height, weight, age + height + weight)

