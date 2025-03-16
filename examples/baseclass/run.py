from examples.baseclass.alice_and_bob import main

"""
This example shows the Person class with baseclass MutationTrackedObject, and tells the life story of instance Alice

Make sure to put an breakpoint on the line with the `print` function and take a look at
`example_person.MUTATIONS` for the full experience provided by the MutationTrackedObject baseclass
"""
example_person = main()

# place a breakpoint on the print() line below
# run it in debug mode
# and make sure to check out example_person.MUTATIONS for the full experience
print("Thank you for trying the example with the baseclass MutationTrackedObject!")
