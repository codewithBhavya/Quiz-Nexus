import random
print("Welcome to Tech Quiz")

questions ={
    1: {
        "question": "What does 'CPU' stand for?",
        "options": {
            "a": "Central Processing Unit",
            "b": "Control Processing Unit",
            "c": "Computer Processing Unit",
            "d": "Central Power Unit",
        },
        "correct_answer": "a",
        "hint": "It is the brain of a computer responsible for executing instructions."
    },
    2: {
        "question": "What is the function of an 'SSD' in a computer?",
        "options": {
            "a": "Sound Signal Driver",
            "b": "Solid State Drive",
            "c": "System Software Download",
            "d": "Secondary Storage Device",
        },
        "correct_answer": "b",
        "hint": "It is a type of storage device that uses NAND-based flash memory."
    },
    3: {
        "question": "Which programming language is used for creating web pages?",
        "options": {
            "a": "Java",
            "b": "Python",
            "c": "HTML",
            "d": "Ruby",
        },
        "correct_answer": "c",
        "hint": "It stands for HyperText Markup Language and is the foundation of web development."
    },
    4: {
        "question": "What does 'URL' stand for?",
        "options": {
            "a": "Universal Resource Locator",
            "b": "Uniform Resource Locator",
            "c": "Universal Remote Locator",
            "d": "Uniform Remote Locator",
        },
        "correct_answer": "b",
        "hint": "It is the address used to identify resources on the internet."
    },
    5: {
        "question": "Which technology is used for wireless communication between devices?",
        "options": {
            "a": "Bluetooth",
            "b": "Infrared",
            "c": "NFC (Near Field Communication)",
            "d": "USB",
        },
        "correct_answer": "a",
        "hint": "It is commonly used for connecting peripherals to smartphones and computers."
    },
    6: {
        "question": "What does 'HTML5' refer to?",
        "options": {
            "a": "The latest version of the HyperText Markup Language",
            "b": "The fifth version of the Hypertext Transfer Protocol",
            "c": "A programming language for artificial intelligence",
            "d": "A gaming console developed by Sony",
        },
        "correct_answer": "a",
        "hint": "It includes new features like video, audio, and canvas elements for web development."
    },
    7: {
        "question": "What does 'GPS' stand for?",
        "options": {
            "a": "Global Positioning System",
            "b": "Geographic Positioning System",
            "c": "General Positioning Satellite",
            "d": "Global Position Satellite",
        },
        "correct_answer": "a",
        "hint": "It is used for determining the precise location of a person or device."
    },
    8: {
        "question": "Which programming language is often used for data analysis and machine learning?",
        "options": {
            "a": "JavaScript",
            "b": "C++",
            "c": "Python",
            "d": "Swift",
        },
        "correct_answer": "c",
        "hint": "It has gained popularity due to its ease of use and extensive libraries."
    },
    9: {
        "question": "What is the purpose of a 'firewall' in network security?",
        "options": {
            "a": "Enhancing internet speed",
            "b": "Preventing unauthorized access to a network",
            "c": "Increasing Wi-Fi range",
            "d": "Blocking spam emails",
        },
        "correct_answer": "b",
        "hint": "It acts as a barrier between a trusted network and an untrusted one."
    },
    10: {
        "question": "Which technology is used to make payments using a mobile device?",
        "options": {
            "a": "Bluetooth",
            "b": "Wi-Fi",
            "c": "NFC (Near Field Communication)",
            "d": "Infrared",
        },
        "correct_answer": "c",
        "hint": "It allows contactless payments by tapping the device on a compatible terminal."
    },
    11: {
        "question": "What does 'PDF' stand for?",
        "options": {
            "a": "Portable Document Format",
            "b": "Personal Data File",
            "c": "Print Document Format",
            "d": "Public Domain File",
        },
        "correct_answer": "a",
        "hint": "It is a file format used for representing documents independently of software and hardware."
    },
    12: {
        "question": "Which company developed the first commercially successful personal computer?",
        "options": {
            "a": "IBM",
            "b": "Microsoft",
            "c": "Apple",
            "d": "Dell",
        },
        "correct_answer": "a",
        "hint": "It was released in 1981 and was called IBM PC."
    },
    13: {
        "question": "Which technology is used for contactless data transfer over short distances?",
        "options": {
            "a": "NFC (Near Field Communication)",
            "b": "Bluetooth",
            "c": "Wi-Fi",
            "d": "GPS",
        },
        "correct_answer": "a",
        "hint": "It is commonly used for mobile payments and data sharing between devices."
    },
    14: {
        "question": "What does 'HTTP' stand for?",
        "options": {
            "a": "Hypertext Transfer Protocol",
            "b": "Hyperlink Transfer Protocol",
            "c": "Hypertext Text Protocol",
            "d": "Hyper Transfer Protocol",
        },
        "correct_answer": "a",
        "hint": "It is the foundation of data communication on the World Wide Web."
    },
    15: {
        "question": "Which technology is used to store data on optical discs like CDs and DVDs?",
        "options": {
            "a": "SSD",
            "b": "Blu-ray",
            "c": "USB",
            "d": "RAM",
        },
        "correct_answer": "b",
        "hint": "It offers higher storage capacity than traditional CDs and DVDs."
    },
    16: {
        "question": "What is the purpose of an 'ISP'?",
        "options": {
            "a": "Internet Service Provider",
            "b": "Internet Signal Processor",
            "c": "Internal System Protocol",
            "d": "International Security Program",
        },
        "correct_answer": "a",
        "hint": "It provides users with access to the internet."
    },
    17: {
        "question": "Which technology is used to identify and authenticate users based on physical characteristics?",
        "options": {
            "a": "Biometrics",
            "b": "Encryption",
            "c": "BlockChain",
            "d": "Virtual Reality"
        }
    },
    18: {
        "question": "What does 'RAM' stand for?",
        "options": {
            "a": "Read-Only Memory",
            "b": "Random Access Memory",
            "c": "Rapid Application Management",
            "d": "Remote Access Module"
        },
        "correct_answer": "b",
        "hint": "It is used for temporary storage of data that the CPU is currently processing."
    },
    19: {
        "question": "Which programming language is commonly used for front-end web development?",
        "options": {
            "a": "Java",
            "b": "C#",
            "c": "JavaScript",
            "d": "Ruby"
        },
        "correct_answer": "c",
        "hint": "It is primarily used for adding interactivity and dynamic content to websites."
    },
    20: {
        "question": "What is the purpose of a \"router\" in a computer network?",
        "options": {
            "a": "Transferring data between devices within a local network",
            "b": "Providing electrical power to devices",
            "c": "Connecting the computer to the internet",
            "d": "Storing files and folders for easy access"
        },
        "correct_answer": "a",
        "hint": "It directs data packets to their destination within a network."
    },
    21: {
        "question": "What is the primary function of an \"antivirus\" software?",
        "options": {
            "a": "Optimizing computer performance",
            "b": "Backing up data automatically",
            "c": "Protecting against malicious software",
            "d": "Managing network traffic"
        },
        "correct_answer": "c",
        "hint": "It helps safeguard your computer from viruses, malware, and other threats."
    },
    22: {
        "question": "Which technology is used to store data and software remotely over the internet?",
        "options": {
            "a": "Cloud computing",
            "b": "Virtual reality",
            "c": "Augmented reality",
            "d": "Machine learning"
        },
        "correct_answer": "a",
        "hint": "It allows access to data and applications from anywhere with an internet connection."
    },
    23: {
        "question": "What is the purpose of a \"GPU\" in a computer?",
        "options": {
            "a": "Managing the cooling system",
            "b": "Displaying images on the screen",
            "c": "Running antivirus scans",
            "d": "Performing complex graphical calculations"
        },
        "correct_answer": "d",
        "hint": "It is specifically designed to handle graphics processing tasks."
    },
    24: {
        "question": "What does \"IoT\" stand for?",
        "options": {
            "a": "Internet of Technology",
            "b": "Internet of Things",
            "c": "Integrated Online Tools",
            "d": "International Online Transactions"
        },
        "correct_answer": "b",
        "hint": "It refers to the network of interconnected devices and objects."
    },
    25: {
        "question": "Which technology is used to create a secure and encrypted connection between a user and a website?",
        "options": {
            "a": "HTTPS",
            "b": "FTP",
            "c": "SMTP",
            "d": "SNMP"
        },
        "correct_answer": "a",
        "hint": "It ensures data transmitted between the user and the website remains confidential."
    },
    26: {
        "question": "What is the purpose of a \"modem\"?",
        "options": {
            "a": "Displaying images on the screen",
            "b": "Converting digital data to analog signals and vice versa",
            "c": "Storing data temporarily",
            "d": "Controlling the cooling system"
        },
        "correct_answer": "b",
        "hint": "It is used to connect a computer to the internet over telephone lines."
    },
    27: {
        "question": "Which technology is used to display three-dimensional images and videos?",
        "options": {
            "a": "HD",
            "b": "3G",
            "c": "VR",
            "d": "LED"
        },
        "correct_answer": "c",
        "hint": "It creates a simulated environment that users can interact with."
    },
    28: {
        "question": "What does \"URL\" stand for?",
        "options": {
            "a": "Universal Resource Locator",
            "b": "Uniform Resource Locator",
            "c": "Universal Remote Locator",
            "d": "Uniform Remote Locator"
        },
        "correct_answer": "b",
        "hint": "It is the address used to identify resources on the internet."
    },
    29: {
        "question": "Which programming language is used for creating web pages?",
        "options": {
            "a": "Java",
            "b": "Python",
            "c": "HTML",
            "d": "Ruby"
        },
        "correct_answer": "c",
        "hint": "It stands for HyperText Markup Language and is the foundation of web development."
    },
    30: {
        "question": "What does \"CPU\" stand for?",
        "options": {
            "a": "Central Processing Unit",
            "b": "Control Processing Unit",
            "c": "Computer Processing Unit",
            "d": "Central Power Unit"
        },
        "correct_answer": "a",
        "hint": "It is the brain of a computer responsible for executing instructions."
    },
    31: {
        "question": "What is the function of an \"SSD\" in a computer?",
        "options": {
            "a": "Sound Signal Driver",
            "b": "Solid State Drive",
            "c": "System Software Download",
            "d": "Secondary Storage Device"
        },
        "correct_answer": "b",
        "hint": "It is a type of storage device that uses NAND-based flash memory."
    },
    32: {
        "question": "Which technology is used for wireless communication between devices?",
        "options": {
            "a": "Bluetooth",
            "b": "Infrared",
            "c": "NFC (Near Field Communication)",
            "d": "USB"
        },
        "correct_answer": "a",
        "hint": "It is commonly used for connecting peripherals to smartphones and computers."
    },
    33: {
        "question": "What does \"HTML5\" refer to?",
        "options": {
            "a": "The latest version of the HyperText Markup Language",
            "b": "The fifth version of the Hypertext Transfer Protocol",
            "c": "A programming language for artificial intelligence",
            "d": "A gaming console developed by Sony"
        },
        "correct_answer": "a",
        "hint": "It includes new features like video, audio, and canvas elements for web development."
    },
    34: {
        "question": "What does \"GPS\" stand for?",
        "options": {
            "a": "Global Positioning System",
            "b": "Geographic Positioning System",
            "c": "General Positioning Satellite",
            "d": "Global Position Satellite"
        },
        "correct_answer": "a",
        "hint": "It is used for determining the precise location of a person or device."
    },
    35: {
        "question": "Which programming language is often used for data analysis and machine learning?",
        "options": {
            "a": "JavaScript",
            "b": "C++",
            "c": "Python",
            "d": "Swift"
        },
        "correct_answer": "c",
        "hint": "it has gained popularity due to its ease of use and extensive libraries"
    },
     36: {
        "question": "What is the purpose of a 'firewall' in network security?",
        "options": {
            "a": "Enhancing internet speed",
            "b": "Preventing unauthorized access to a network",
            "c": "Increasing Wi-Fi range",
            "d": "Blocking spam emails"
        },
        "correct_answer": "b",
        "hint": "It acts as a barrier between a trusted network and an untrusted one."
    },
    37: {
        "question": "Which technology is used to make payments using a mobile device?",
        "options": {
            "a": "Bluetooth",
            "b": "Wi-Fi",
            "c": "NFC (Near Field Communication)",
            "d": "Infrared"
        },
        "correct_answer": "c",
        "hint": "It allows contactless payments by tapping the device on a compatible terminal."
    },
    38: {
        "question": "What does \"PDF\" stand for?",
        "options": {
            "a": "Portable Document Format",
            "b": "Personal Data File",
            "c": "Print Document Format",
            "d": "Public Domain File"
        },
        "correct_answer": "a",
        "hint": "It is a file format used for representing documents independently of software and hardware."
    },
    39: {
        "question": "Which company developed the first commercially successful personal computer?",
        "options": {
            "a": "IBM",
            "b": "Microsoft",
            "c": "Apple",
            "d": "Dell"
        },
        "correct_answer": "a",
        "hint": "It was released in 1981 and was called IBM PC."
    },
    40: {
        "question": "Which technology is used for contactless data transfer over short distances?",
        "options": {
            "a": "NFC (Near Field Communication)",
            "b": "Bluetooth",
            "c": "Wi-Fi",
            "d": "GPS"
        },
        "correct_answer": "a",
        "hint": "It is commonly used for mobile payments and data sharing between devices."
    },
    41: {
        "question": "What does \"HTTP\" stand for?",
        "options": {
            "a": "Hypertext Transfer Protocol",
            "b": "Hyperlink Transfer Protocol",
            "c": "Hypertext Text Protocol",
            "d": "Hyper Transfer Protocol"
        },
        "correct_answer": "a",
        "hint": "It is the foundation of data communication on the World Wide Web."
    },
    42: {
        "question": "Which technology is used to store data on optical discs like CDs and DVDs?",
        "options": {
            "a": "SSD",
            "b": "Blu-ray",
            "c": "USB",
            "d": "RAM"
        },
        "correct_answer": "b",
        "hint": "It offers higher storage capacity than traditional CDs and DVDs."
    },
    43: {
        "question": "What is the purpose of an \"ISP\"?",
        "options": {
            "a": "Internet Service Provider",
            "b": "Internet Signal Processor",
            "c": "Internal System Protocol",
            "d": "International Security Program"
        },
        "correct_answer": "a",
        "hint": "It provides users with access to the internet."
    },
    44: {
        "question": "Which technology is used to identify and authenticate users based on physical characteristics?",
        "options": {
            "a": "Biometrics",
            "b": "Encryption",
            "c": "Blockchain",
            "d": "Virtual Reality"
        },
        "correct_answer": "a",
        "hint": "It includes fingerprint, facial, and iris recognition."
    },
    45: {
        "question": "What does \"RAM\" stand for?",
        "options": {
            "a": "Read-Only Memory",
            "b": "Random Access Memory",
            "c": "Rapid Application Management",
            "d": "Remote Access Module"
        },
        "correct_answer": "b",
        "hint": "It is used for temporary storage of data that the CPU is currently processing."
    },
    46: {
        "question": "Which programming language is commonly used for front-end web development?",
        "options": {
            "a": "Java",
            "b": "C#",
            "c": "JavaScript",
            "d": "Ruby"
        },
        "correct_answer": "c",
        "hint": "It is primarily used for adding interactivity and dynamic content to websites."
    },
    47: {
        "question": "What is the purpose of a 'router' in a computer network?",
        "options": {
            "a": "Transferring data between devices within a local network",
            "b": "Providing electrical power to devices",
            "c": "Connecting the computer to the internet",
            "d": "Storing files and folders for easy access"
        },
        "correct_answer": "a",
        "hint": "It directs data packets to their destination within a network."
    },
    48: {
        "question": "What is the primary function of an anti-virus software?",
        "options": {
            "a": "Optimizing computer performance",
            "b": "backing up data automatically",
            "c": "protecting against malicious software",
            "d": "managing traffic network",
        },
        "correct_answer": "c",
        "hint": "it helps safeguard your computer from viruses,malware,and other threats"
    },
    49: {
        "question": "Which technology is used to store data and software remotely over the internet?",
        "options": {
            "a": "Cloud computing",
            "b": "Virtual Reality",
            "c": "Augmented reality",
            "d": "Machine learning",
        },
        "correct_answer": "a",
        "hint": "It allows access to data and applications from anywhere with an internet connection."
    },
    50: {
        "question": "what is the purpose of 'GPU' in a computer",
        "options": {
            "a": "Managing the cooling system",
            "b": "Displaying images on the screen",
            "c": "running antivirus scans",
            "d": "Performing complex graphical calculations",
        },
        "correct_answer": "d",
        "hint": "it is specifically designed to handle graphics processing tools" 
    }
}
def select_random_questions(questions, num_questions=10):
    question_keys = list(questions.keys())
    random.shuffle(question_keys)
    selected_questions = {key: questions[key] for key in question_keys[:num_questions]}
    return selected_questions

def display_question(question_number, question_info):
    print(f"Question {question_number}: {question_info['question']}")
    print("Options:")
    for option, text in question_info['options'].items():
        print(f"{option}: {text}")
    return input("Your answer: ").lower()

def main():
    num_questions = 10
    selected_questions = select_random_questions(questions, num_questions)

    correct_answers = 0
    for idx, (question_number, question_info) in enumerate(selected_questions.items(), start=1):
        user_answer = display_question(idx, question_info)
        if user_answer == question_info['correct_answer']:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {question_info['correct_answer']}\n")

    print(f"You answered {correct_answers} out of {num_questions} questions correctly.")

if __name__ == "__main__":
    main()