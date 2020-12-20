#!/usr/bin/env python
# coding: utf-8

# In[94]:


#Activity 1#
#Random list of 100 numbers#
import random
list1= [random.randint(0,100)
for x in range (0,100)]
list1


# In[95]:


#List divisible by 3#
div3list = [x for x in list1 if x % 3 == 0]
div3list


# In[96]:


#Length of list 1#
lengthoflist1= len(list1)
lengthoflist1


# In[97]:


#Length of divisible by 3 list#
lengthoflistdiv3 = len(div3list)
lengthoflistdiv3


# In[98]:


#Calculates difference between lists#
difference= lengthoflist1 - lengthoflistdiv3
difference


# In[99]:


#Runs the difference 3 times#
finallistdifference = []
for i in range(0,3):
    list1= [random.randint(0,100)
    for x in range (0,100)]
    div3list = [x for x in list1 if x % 3 == 0]
    lengthoflist1= len(list1)
    lengthoflistdiv3 = len(div3list)
    difference= lengthoflist1 - lengthoflistdiv3
    finallistdifference.append(difference)
finallistdifference



# In[100]:


#Mean of sample #
meansample = sum(finallistdifference)/float(len(finallistdifference))
meansample
#End of Activity 1#


# In[121]:


#Activity 2#
multiline_text  = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.

However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.

"My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?"

Mr. Bennet replied that he had not.

"But it is," returned she; "for Mrs. Long has just been here, and she told me all about it."

Mr. Bennet made no answer.

"Do you not want to know who has taken it?" cried his wife impatiently.

"You want to tell me, and I have no objection to hearing it."

This was invitation enough.

"Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week."

"What is his name?"

"Bingley."

"Is he married or single?"

"Oh! Single, my dear, to be sure! A single man of large fortune; four or five thousand a year. What a fine thing for our girls!"

"How so? How can it affect them?"

"My dear Mr. Bennet," replied his wife, "how can you be so tiresome! You must know that I am thinking of his marrying one of them."

"Is that his design in settling here?"

"Design! Nonsense, how can you talk so! But it is very likely that he may fall in love with one of them, and therefore you must visit him as soon as he comes."

"I see no occasion for that. You and the girls may go, or you may send them by themselves, which perhaps will be still better, for as you are as handsome as any of them, Mr. Bingley may like you the best of the party."

"My dear, you flatter me. I certainly have had my share of beauty, but I do not pretend to be anything extraordinary now. When a woman has five grown-up daughters, she ought to give over thinking of her own beauty."

"In such cases, a woman has not often much beauty to think of."

"But, my dear, you must indeed go and see Mr. Bingley when he comes into the neighbourhood."

"It is more than I engage for, I assure you."

"But consider your daughters. Only think what an establishment it would be for one of them. Sir William and Lady Lucas are determined to go, merely on that account, for in general, you know, they visit no newcomers. Indeed you must go, for it will be impossible for us to visit him if you do not."

"You are over-scrupulous, surely. I dare say Mr. Bingley will be very glad to see you; and I will send a few lines by you to assure him of my hearty consent to his marrying whichever he chooses of the girls; though I must throw in a good word for my little Lizzy."

"I desire you will do no such thing. Lizzy is not a bit better than the others; and I am sure she is not half so handsome as Jane, nor half so good-humoured as Lydia. But you are always giving her the preference."

"They have none of them much to recommend them," replied he; "they are all silly and ignorant like other girls; but Lizzy has something more of quickness than her sisters."

"Mr. Bennet, how can you abuse your own children in such a way? You take delight in vexing me. You have no compassion for my poor nerves."

"You mistake me, my dear. I have a high respect for your nerves. They are my old friends. I have heard you mention them with consideration these last twenty years at least."

"Ah, you do not know what I suffer."

"But I hope you will get over it, and live to see many young men of four thousand a year come into the neighbourhood."

"It will be no use to us, if twenty such should come, since you will not visit them."

"Depend upon it, my dear, that when there are twenty, I will visit them all."

Mr. Bennet was so odd a mixture of quick parts, sarcastic humour, reserve, and caprice, that the experience of three-and-twenty years had been insufficient to make his wife understand his character. Her mind was less difficult to develop. She was a woman of mean understanding, little information, and uncertain temper. When she was discontented, she fancied herself nervous. The business of her life was to get her daughters married; its solace was visiting and news. 
"""


# In[122]:


#Tells type#
type(multiline_text )


# In[123]:


#Gives overall length#
len(multiline_text )


# In[124]:


#Eliminates new lines#
multiline_text  = multiline_text .replace('\n'," ")
multiline_text 


# In[125]:


#Eliminates all symbols#
newmultiline = " "
for char in multiline_text:
    if char == " ":
        newmultiline += char
    elif char.isalnum():
        newmultiline += char
    else:
        newmultiline += " "
newmultiline

    


# In[126]:


#Breaks out every word that is being used in the paragraph#
listofwords = newmultiline.split()
listofwords


# In[127]:


#Total number of words#
len(listofwords)


# In[128]:


#Total number of unique words#
uniquewords = dict.fromkeys(listofwords) 
len(uniquewords.keys())


# In[129]:


#Counts the unique words#
for word in listofwords:
    if uniquewords [word] is None: 
        uniquewords[word] = 1
    else:
        uniquewords[word]+=1 
uniquewords


# In[132]:


#Breaks down the unique words that are being passed through in the top25#
top25 = sorted(uniquewords.items(), key=lambda x: x[1], reverse= True)
top25[:25]


# In[53]:


#Activity 3#
#Defines permutations
from itertools import(permutations,dropwhile)
get_ipython().run_line_magic('pinfo', 'permutations')


# In[54]:


#Defines dropwhile
get_ipython().run_line_magic('pinfo', 'dropwhile')


# In[77]:


#Prints all possible combos#
combo = permutations([0,1,2], 3)
for i in combo:
    print (i)
assert isinstance(i, tuple)


# In[78]:


#Drops 0
combolist = permutations([0,1,2], 3)
for i in combolist:
    print (list(dropwhile(lambda x: x <= 0, i)))


# In[79]:


#Defines type
type(i)


# In[106]:


#Combines numbers to make a full number# 
import math
def makenumber(newcombo):
    final=0
    for b in range(0, len(newcombo)):
        final += (newcombo.pop() * (math.pow(10,b)))
    return final
combolist = permutations([0,1,2],3)
for b in combolist:
    print(b)
per3 = permutations(range(3))
for num in per3:
    newcombo = list(dropwhile(lambda x:x == 0, num))
    print(makenumber(newcombo))


# In[150]:


#Activity 4#
from itertools import zip_longest
#Defines the csv title with header and line returning the value#
def return_dict_from_csv_line(header, line):
    zipline = zip_longest(header, line, fillvalue= None)
    retdict = {a[0]:a[1] for a in zipline}
    return retdict
#Opens the actual file reads it line by line#
with open ("/Users/Brett/Downloads/Data-Wrangling-with-Python-master/Lesson02/Activity04/sales_record.csv", "r") as fd:
    first_line = fd.readline()
    header = first_line.replace("\n", "").split(",")
    for i, line in enumerate(fd):
        line = line.replace("\n", "").split(",")
        print(return_dict_from_csv_line(head,newline))
        if i >0:
            break


# In[ ]:




