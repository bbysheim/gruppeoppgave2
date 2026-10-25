# Individual solution: Erling's project team
# The score represents how strongly the choises support trust and cooperation.

print("ERLING AND THE CITIZEN PORTAL")
print("Six weeks into the project, the team is facing disagreements.")
print("The first prototype is due in three weeks. Erling must make three decisions.\n ")

score = 0

#Decision 1: Silje and Elias
print("DECISION 1: how should Erling habdle the conlict between Silje and Elias?")
print("A. Arrange a meeting where both can explain their views. (+2 points)")
print("B. Speak to them individually. (+2 points)")
print("C. Postpone the conflict and hope they resolve it themselves. (+1 point)")

choice1 = input("Choose A, B, or C: "). strip().lower()
while choice1 not in ("a", "b", "c"):
    choice1 = input("Please enter A, B, or C:").strip().lower()

    if choice1 == "a":
        print("Both. explain their perspectives and may gain a better understanding of each other.")
        score += 2
    elif choice1 =="b":
        print("Each person can speak privately, but Erling may need a joint follow-up meeting.")
        score += 2
    else:
        print("They continue working, but the unresolved conflict may affect the next discussion.")
        score += 1

#Decission 2: Hamdi and Hallgeir
print("\nDECISSION 2: how should Erling handle their disagreement about citizen meetings?")
print("A. Arrangea joint meeting to discuss their needs. (+2 points)")
print("B. Speak with both and make a shared plan that considersb oth perspectives. (+2 points)")
print("C. Let them try to find a solution themselves. (+1 point)")

choice2 = input("Chose A, B, or C: "). strip().lower()
while choice2 not in ("a", "b", "c"):
    choice2 = input("Please enter A, B, or C: ").strip().lower()

    if choice2 == "a":
        print("They discuss their needs and try to agree on a solution.")
        score += 2
    elif choce2 == "b":
        print("Erling helps them make a plan that balances structure with open dialogue.")
        score += 2
    else:
        print("They have responsibility for solving the issue, but the disagreement may continue.")
        score += 1

#Decision 3: Motivation and the prototype deadline
print("\nDECISSION 3: What should Erling prioritise as rhe deadline approaches?")
print("A. Build relationships through cooperation and social activities. (+2 points)")
print("B. Make a work plan, clarify responsibilities, and follow up with the team. (+2 points)")
print("C. Focus on deliverables and postpone work on the conflicts. (+1 point)")

choice3 = input("Choose A, B, or c: ").strip().lower()
while choice3 not in ("a", "b", "c"):
    choice3 = input("Please enter A, B, or C: ") .strip().lower()

    if choice3 == "a":
        print("The team gets time to strenthen trust and communication.")
        score += 2
    elif choice3 == "b":
        print("The team gets clear tasks, responsabilities, and follow-up.")
        score += 2
    else:
        print("The team focusses on delivery, but unresolved conflict may weaken cooperation.")
        score += 1

# The total score determines one of the three endings in the group's flowchart.
print("\nFINAL RESULT")
print(f"Team cooperation score: {score} out of 6")

if score == 6:
    print("Ending 1: Good cooperation. The team restores trust and moves forward together.")
elif score >= 4:
    print("Ending 2: Partial resolution. Some conflicts remain, but the project continues.")
else:
    print("Ending 3: The project is at risk. Conflict may weaken the team and cause delays.")
    