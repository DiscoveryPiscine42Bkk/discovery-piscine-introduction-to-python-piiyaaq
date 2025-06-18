import sys

if len(sys.argy) ! = 2:
     print("none")
elese:
     param = sys.argv(1)
     try:

        user_input = input ("what was the parameter. ")

        if user_input == param:
            print("Good job!")
        else:
            print("Nope, sorry...")
        except EOFError:

            print("\nNope, sorry...")