def parametr_args(argument, *args):
    print("zawartość args: {}".format(args))
    print("argument nazwany: {}".format(argument))
    for arg in args:
        print("argument z *args: {}".format(arg))

parametr_args('python', 'spam', 'eggs', 'test',)

print ("\n")

def parametr_kwargs(argument, **kwargs):
    print("argument: {}".format(argument))
    print("zawartość kwargs: {}".format(kwargs))

parametr_kwargs(dodatkowy=48, nastepny=111, argument=12)

# argument: 12g
# zawartość kwargs: {'dodatkowy': 48, 'nastepny': 111}
