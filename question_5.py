# 5. Quiz Game
# Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary (or list of dicts).
# Asks the user each question and records their answers.
# At the end, displays:
# The user’s score (e.g., 7/10)
# Correct answers for any questions they got wrong
# Skills practiced: loops, dictionaries, input, comparison, counters, print formatting

#questions , input of answers , compare the answer, give a score , return the question and anser of the wrong 

questions = {"""Q #1. "Aksumite currency" was unique in the ancient world for sub-Saharan Africa because it:
a)Was made of salt bars
b)Was made of gold dust measured by weight
c)Bore the cross and the effigy of the reigning king
d)Was minted in both gold and silver denominations
: """ : 'c',
"""Q #2. The "Aseb" or "Hatse" was a powerful royal title for a Queen in the medieval period. Which queen held this title as a co-ruler with her son?
a)Queen Eleni
b)Queen Gudit
c)Queen Sabla Wangel
d)Empress Taytu 
: """ : 'c',
"""Q #3. Before the rise of the Solomonic Dynasty, the Zagwe kings claimed their royal legitimacy through descent from:
a)The Prophet Muhammad
b)Moses wife
c)The last Aksumite Emperor 
d)The Queen of Sheba's other son
: """ : 'b',
"""Q #4. The "Stèle of the Vultures" in Tiya is famous for its carvings, which are believed to symbolize:
a)Ancient star charts
b)Male virility and warrior achievements
c)Victory in the Battle of Adwa
d)The tombs of ancient kings 
: """ : 'b',
"""Q #5. Which Ethiopian region is home to the "Sof Omar" cave system, one of the longest and most spectacular in Africa?
a)Tigray
b)Oromia
c)Amhara
d)Somali Region 
: """ : 'b',
"""Q #6. Which Portuguese explorer left a detailed written account of the Ethiopian court in the 1520s, titled "The Prester John of the Indies"?
a)Francisco Álvares
b)Vasco da Gama
c)Pedro Álvares Cabral
d)Pêro da Covilhã
: """ : 'a',
""" Q #7. The main Aksumite port city, crucial for trade with the Roman Empire and India, was called:
a)Zeila
b)Berbera
c)Adulis
d)Massawa
: """ : 'c',
"""Q #8. The traditional Ethiopian sport involving horseback riding, spear throwing, and stylized war dances is known as:
a)Genna
b)Gugs
c)Tigel
d)Qarsa
; """ : 'b',
"""Q #9. The "Makhzumi" dynasty was a Muslim sultanate that predated the Adal Sultanate and was located in the region of:
a)Fatagar 
b)Harar
c)Dawaro
d)Ifat
: """ : 'd',
"""Q #10.The ancient city of Harlaa is archaeologically significant for findings that indicate it was a major medieval trading
 hub with connections to:
a)China and India
b)The Americas
c)Australia
d)Scandinavia 
: """ : 'a'}
# user_answer = [] 
choice = ['a', 'b', 'c', 'd']
wrong_answer = []
right_answer = []
correction = {}
score = 0
# response = ""
print("                                                       ")

print ("----------  LETS PLAY 'DO YOU KNOW THE HISTORY OF ETHIOPIA ?' ----------")
print("                                                       ")
print("  --  Answer this questions by choosing the correct  multiple choice  --")
print("                                                       ")
for key , value in questions.items() :  
   print(key)
   response = input("Answer : " ).lower().strip()
   while response  not in choice:
        print("you have inserted invalid choice please try agin")
        response = input("Answer : " ).lower().strip()
        # user_answer.append(response)
   if response == value:
             score += 1
   else: wrong_answer.append(key), right_answer.append(value)

print("                                                                 ")
print(f"You have answerd {score} / {len(questions)}")
print("                                                                 ")
print("This are the questions you got wrong and the correct  choice")
print("                                                                 ")
correction = dict (zip (wrong_answer,right_answer))
for key, value  in correction.items():
   print(key, " " , value)