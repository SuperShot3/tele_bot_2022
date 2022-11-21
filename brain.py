import nltk

BOT_CONFIG = {
    'intents': {
        'greeting': {
            'examples': ['hello', 'hi', 'good morning', 'привет', 'ghbdtn', 'здравствуйте', 'хаюшки'],
            'response': ['Hello', 'hello Sir', 'Im here to serve you ', 'Sawa di krap', 'Glad to see you',
                         'Welcome Sir', 'How can i Help you?']
        },
        'buy': {
            'examples': ['bye', 'good bye', 'see you', 'bye bye'],
            'response': ['Keep in touch', 'Good talking with you', 'Take care of yourself, and don’t get into trouble',
                         'Bye-Bye!'],
        },
        'insurance': {
            'examples': ['insurance', 'buy insurance', 'check insurance', ],
            'response': ['Please see down information', 'Please see down information', 'Please see down information'],
        },
        'help': {
            'examples': ['help'],
            'response': ['help'],
        }
    }
}
# Display all items
# for b in BOT_CONFIG['intents'].keys():
#     print('/////////////////////////////////')
#     print(b)
#     print('/////////////////////////////////')
#     for a in BOT_CONFIG['intents'][b]['examples']:
#         print(a)
