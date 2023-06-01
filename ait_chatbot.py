import random

# Define the patterns and responses
patterns = {
    'greeting': ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
    'leaving': ['bye', 'goodbye', 'good bye', 'end', 'stop', 'leave', 'see you', 'farewell'],
    'admission': ['admission', 'admissions', 'apply', 'requirements', 'eligibility'],
    'courses': ['courses', 'programs', 'departments', 'specializations'],
    'facilities': ['facilities', 'infrastructure', 'labs', 'library', 'hostel', 'sports facilities'],
    'contact': ['contact', 'address', 'phone', 'email'],
    'Clubs': ['club','clubs','extra curricular','activities','student development'],
    'Placements': ['Placements','job','placement'],
    'Residence': ['Hostel','residence','mess','food']
}

responses = {
    'greeting': ['Hello! How can I assist you?'],
    'admission': ['To apply for admission at Army Institute of Technology (AIT), you need to fulfill the following requirements:',
                  '- For undergraduate programs, candidates Admission to AIT is on the basis of All India Rank obtained in the  Joint Entrance Exam (JEE) Main.',
                  '- For postgraduate programs,  Candidate must have successfully completed his/her bachelors degree in Engineering/ Technology in any branch with a minimum score of 50 % (45 % for the reserved category) along with a valid non-zero GATE score',
                  'For detailed information and the admission process, please visit the AIT website on https://www.aitpune.com/'],
    'leaving': ['Thank you for your interaction! If you have any more questions in the future, feel free to ask. Have a great day!'],
    'courses': ['AIT offers the following undergraduate and postgraduate programs:',
                '- Bachelor of Engineering (B.E.) in Computer Engineering with 120 students in each year',
                '- Bachelor of Engineering (B.E.) in Electronics and Telecommunication Engineering with 120 students in each year',
                '- Bachelor of Engineering (B.E.) in Mechanical Engineering with 60 students in each year',
                '- Bachelor of Engineering (B.E.) in Information Technology with 120 students in each year',
                '- Master of Engineering (M. E.) in Data Science with 24 Seats each year',
                'For more details about the courses and their curriculum, please visit the AIT website.'],
    'facilities': ['Army Institute of Technology (AIT) provides excellent facilities to its students, including:',
                   '- Well-equipped laboratories with the latest technology',
                   '- Modern classrooms and lecture halls',
                   '- Library with a vast collection of books, journals, and e-resources',
                   '- Sports facilities for various indoor and outdoor games',
                   '- Hostel accommodation for both boys and girls',
                   '- Cafeteria serving hygienic food',
                   'The college prioritizes providing a conducive environment for learning and overall development.'],
    'contact': ['You can contact Army Institute of Technology (AIT) at the following address:',
                'Army Institute of Technology',
                'Dighi Hills, Alandi Road, Pune - 411015, Maharashtra, India',
                'Phone: 7249250184/ 7249250185',
                'Email: ait@aitpune.edu.in',
                'For more contact information and directions, please visit the AIT website.'],
    'Clubs' :  ['Ait consists of following clubs for overall development of students',
                'Sports Club',
                'Technical Board',
                'Cultural Board',
                'OSS Club',
                'Cycling Club',
                'Nature club',
                'NSS Club',
                'Robotics Club',
                'And many more'
                ],
    'Placements': ['AIT has a very good placement record with above 97 percentage successful placements',
                    'It records highest package of 1.12 crore per annaum. ',
                    'the average package is recorded to be 14 LPA for computer department and 8 LPA overall',
                    'Big companies such as amazon, microsoft, google, codenation, uber, cred etc are seen hiring from our college.'
                ],
    'Residence': ['AIT has large space for hostels and mess to failitate proper comfort to students in their residence',
                    'It has 8 different flanks of hostels divided among 4 batches of students',
                    'Girls are provided their separate hostels and mess facilities',
                    'AIT is known for its healthy and tasty food in mess to ensure good physical health of students'
                ]
}

# Function to match user input with patterns


def match_query(query):
    for intent, patterns_list in patterns.items():
        for pattern in patterns_list:
            if pattern in query.lower():
                return intent
    return None

# Function to generate a response based on the matched intent


def generate_response(intent):
    if intent in responses:
        return '\n'.join(responses[intent])
    else:
        return "I'm sorry, I don't have information about that at the moment."


# Main interaction loop
print("Welcome to the Army Institute of Technology (AIT) Chatbot!")
print("How can I assist you today?")

while True:
    user_input = input("> ")
    intent = match_query(user_input)
    print()
    response = generate_response(intent)
    print()
    print(response)
