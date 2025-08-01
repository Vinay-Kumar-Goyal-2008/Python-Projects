import requests
import random
import html
def quiz():
    try:
        
        score=0
        def decoration():
            print('='*80)
            print()
        def inversedecoration():
            print()
            print('='*80)
        decoration()
        print('Welcome to General knowledge quiz program')
        inversedecoration()

        print()
        print('='*20,'Instructions','='*20)
        print()
        print('''
            1. System will ask you 20 questions related to general knowledge
            2. For each correct option you will get 5 marks
            3. For each wrong option you will get -1 marks
            4. if you scored more than 50 marks you will be considered as pass
            5. All the best
            ''')
        print()
        print('='*53)
        print()

        data=requests.get('https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=multiple').json()['results']
        for i in data:
            decoration()
            print(html.unescape(i['question']))
            options=i['incorrect_answers']+[i['correct_answer']]
            random.shuffle(options)
            for j,k in enumerate(options):
                print(j+1,'  ',k)
            ch=int(input('Enter your choice:-   '))
            if ch>=1 and ch<=4:
                print()
                if (i['correct_answer']==options[ch-1]):
                    print('Correct answer!!!')
                    score+=5
                else:
                    print('Incorrect Answer!!!')
                    score-=1
                print()
            else:
                decoration()
                print('Invalid choice!!')
                continue
        print('Your score;-   ',score)
        decoration()
        if score>=50:
            
            print('You have passed the gk test')
        else:
            print('You have not passed the gk test')
        inversedecoration()

    except Exception as e:
        print(e)

if __name__=='__main__':
    quiz()