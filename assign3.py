from durable.lang import *

with ruleset('interests'):

    @when_all((m.interest == 'Tech Jobs'))
    def tech_jobs(c):
        branch = print_branches()
        c.assert_fact('tech_jobs',{'branch':branch,'grade':c.m.grade})

    @when_all((m.interest=='Literature'))
    def lit(c):
        c.assert_fact('study', { 'interest': c.m.interest, 'grade':c.m.grade })
        c.assert_fact('work', { 'interest': c.m.interest, 'grade':c.m.grade })

    @when_all((m.interest=='Theatre'))
    def theatre(c):
        c.assert_fact('study', { 'interest': c.m.interest, 'grade':c.m.grade })
        c.assert_fact('work', { 'interest': c.m.interest, 'grade':c.m.grade })


    @when_all((m.interest=='Music'))
    def music(c):
        c.assert_fact('study', { 'interest': c.m.interest})
        c.assert_fact('work', { 'interest': c.m.interest })

    @when_all((m.interest=='Languages'))
    def lang(c):
        c.assert_fact('study', { 'interest': c.m.interest, 'grade':c.m.grade })
        c.assert_fact('work', { 'interest': c.m.interest, 'grade':c.m.grade })

    @when_all((m.interest=='Sports'))
    def sports(c):
        spt_type = input("Enter the type of sports (Indoor/Outdoor) you like to play? \t type(indoor/outdoor) \n")
        play_type = input("Which one like to play Single or Multi player? \t type(solo/multi)\n")
        c.assert_fact('sports', { 'type':spt_type, 'play_type':play_type})
        c.assert_fact('work', { 'interest': c.m.interest })

with ruleset('tech_jobs'):
    @when_all((m.branch=='CSE') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':'Web/Android/iOS devlopment, DevOps, Product Design, Testing'})

    @when_all((m.branch=='CSE') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':'Researcher in domain of ML,DL,NLP, Cybersecurity'})

    @when_all((m.branch=='ECE') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':'wirelesscommunication, vlsi, computer vision'})

    @when_all((m.branch=='ECE') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':'Researcher, chip designer, signal processing'})

    @when_all((m.branch=='CSAI') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':'Data science engineering, computer vision, ML/RL engineer'})

    @when_all((m.branch=='CSAI') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':' Researcher in domain of ML/DL/NLP/RL '})

    @when_all((m.branch=='CSD') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':'UI/UX design, Product Design, Human centered Interaction'})

    @when_all((m.branch=='CSD') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':' animation, image processing, digital art'})

    @when_all((m.branch=='CSB') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':'Web Developer, Biomedical engineer,biotechnologist'})

    @when_all((m.branch=='CSB') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':' Researcher in domain of psychology,genetics, biotech, climate'})

    @when_all((m.branch=='CSSS') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':'Web development, Ecological Economics,Applied Econometrics '})

    @when_all((m.branch=='CSSS') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':'Researcher in domain of Industrial Organisation, Spatial Analyses'})

    @when_all((m.branch=='CSAM') &(m.grade<=7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'pursue','object':'Web Development, Variational Calculus,Fractional Calculus, Approximation theory'})

    @when_all((m.branch=='CSAM') &(m.grade>7))
    def func(g):
        g.assert_fact({ 'subject': 'You can','predicate':'be','object':'Researcher in domain of algebra, calculus, Integral transforms '})

    @when_all(+m.subject)
    def output(d):
        print('Career Advice: {0} {1} {2}.'.format(d.m.subject, d.m.predicate, d.m.object))

with ruleset('sports'):

    @when_all((m.type=='indoor') & (m.play_type=='solo'))
    def mathct(e):
        e.assert_fact({ 'subject': 'You can','predicate':'professionally play','object': 'chess, carrom board'})

    @when_all((m.type=='indoor') & (m.play_type=='multi'))
    def mathct(e):
        e.assert_fact({ 'subject': 'You can','predicate':'professionally play','object': 'pool, pubg, air hockey'})

    @when_all((m.type=='outdoor') & (m.play_type=='solo'))
    def mathct(e):
        e.assert_fact({ 'subject': 'You can','predicate':'professionally play','object': 'Badminton, tennis, squash'})

    @when_all((m.type=='outdoor') & (m.play_type=='multi'))
    def mathct(e):
        e.assert_fact({ 'subject': 'You can','predicate':'professionally play','object': 'volleyball, football, cricket'})

    @when_all(+m.subject)
    def output(d):
        print('Career Advice: {0} {1} {2}.'.format(d.m.subject, d.m.predicate, d.m.object))

with ruleset('work'):

    @when_all((m.interest == 'Theatre'))
    def func(e):
        e.assert_fact({ 'subject': 'You can','predicate':'work in domain of ','object': 'Photography, Drama, Film production , and Videography '})

    @when_all((m.interest == 'Music'))
    def func(e):
        e.assert_fact({ 'subject': 'You can','predicate':'professionally conduct','object': 'Concert Band, solo music, group music/choir, Instrumental music' })
    
    @when_all((m.interest == 'Languages'))
    def func(e):
        e.assert_fact({ 'subject': 'You can','predicate':'teach','object': 'language you know and be a professional translator.' })

    @when_all((m.interest == 'Literature'))
    def func(e):
        e.assert_fact({ 'subject': 'You can','predicate':'work in','object': 'Poetry and  Novel clubs and give talks on the books'})

    @when_all((m.interest == 'Sports'))
    def func(e):
        e.assert_fact({ 'subject': 'You can','predicate':'work professionally as','object': 'sport coach for the sport you play well.' })

    @when_all(+m.subject)
    def output(d):
        print('Career Advice: {0} {1} {2}.'.format(d.m.subject, d.m.predicate, d.m.object))


with ruleset('study'):

    @when_all((m.interest == 'Literature') & (m.grade>=5))
    def func(d):
        d.assert_fact({'subject':'Complete if not done','predicate':'courses such as','object': 'fiction and biographies'})

    @when_all((m.interest == 'Literature') & (m.grade>=8))
    def func(d):
        d.assert_fact({ 'subject':'Complete if not done','predicate':'courses such as','object':'philosophy'})

    
    @when_all((m.interest == 'Theatre') & (m.grade>=5))
    def func(d):
        d.assert_fact({ 'subject':'Complete if not done','predicate':'courses such as','object':' Foundations and History, Dramatic Theory, Literature and Criticism.' })

    @when_all((m.interest == 'Theatre') & (m.grade>=8))
    def func(d):
        d.assert_fact({ 'subject':'Complete if not done','predicate':'courses such as','object':'Technical Theater' })


    @when_all((m.interest == 'Music'))
    def func(d):
        d.assert_fact({'subject':'Complete if not done','predicate':'courses such as','object':' fundamentals of music theory, Song writing' })

    
    @when_all((m.interest == 'Languages')  & (m.grade>=5))
    def func(d):
        d.assert_fact({ 'subject':'Complete if not done','predicate':'courses such as','object':' german and spanish speaking classes'})

    @when_all((m.interest == 'Languages')  & (m.grade>=8))
    def func(d):
        d.assert_fact({ 'subject':'Complete if not done','predicate':'courses such as','object':'chinese, japanese and russian' })

    @when_all(+m.subject)
    def output(d):
        print('Career Advice: {0} {1} {2}.'.format(d.m.subject, d.m.predicate, d.m.object))

def print_branches():
    branch_dict ={
        1:'CSE',
        2:'ECE',
        3:'CSAI',
        4:'CSB',
        5:'CSD',
        6:'CSAM',
        7:'CSSS'
    }
    print("Following are the branches in the database.")
    print("1. CSE")
    print("2. ECE")
    print("3. CSAI")
    print("4. CSB")
    print("5. CSD")
    print("6. CSAM")
    print("7. CSSS")
    while(True):
        indx = int((input('Enter the index of your branch that suits you! ')))
        if(indx >= 1 and indx <= 7):
            branch = branch_dict[indx]
            break
        else:
            print("Invalid Choice Entered! Enter again! ")
            print()
    return branch

def print_interests():
    interest_dict ={
        1:'Tech Jobs',
        2:'Literature',
        3:'Theatre',
        4: 'Music',
        5: 'Languages',
        6: 'Sports'
    }
    print("Following are the interest areas in the database")
    print("1. Tech Jobs")
    print("2. Literature")
    print("3. Theatre")
    print("4. Music")
    print("5. Languages")
    print("6. Sports")
    while(True):
        indx = int(float(input('Enter the index of the interest that suits you! ')))
        if(indx >= 1 and indx <= 6):
            interest = interest_dict[indx]
            break

        else:
            print("Invalid Choice Entered! Enter again! ")
            print()
    return interest


if __name__ == '__main__':
    #Starting the program
    print("--------------------------------")
    print('Designed By:-')
    print('Name - Ashita \t\t Roll No. - 2019028')
    print("--------------------------------\n\n")
    print('Welcome to career advisory system!')
    print()
    name = input("What's your name? ")
    print('\nHi {0}! Hope you are survivng well in IIITD.'.format(name))
    print('This system will help you suggest a career option based on your interests, courses taken and grade.')
    print()
    print("--------------------------------\n\n")
    # Input interest
    interest = print_interests()
    # Input grade
    while(True):
        grade = int(float(input('Enter your current CGPA: ')))
        if (grade >= 1 and grade <= 10) :
            break
        else:
            print('You did not enter the correct grade. Please enter again!')
            print()
    print("\n--------------------------------\n")
    assert_fact('interests', { 'interest': interest, 'grade': grade })
    print("\n--------------------------------\n")

