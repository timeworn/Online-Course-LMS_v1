Student = 'Student'
Teacher = 'Teacher'
University = 'University'


MEMBERSHIP = {
    Student: {
        'price': 0.00,
        'is_start': True,
        'icon_name': 'person',
        'title': 'Student',
        'description': 'Access to over 1.000 high quality courses. For individuals.',
        'is_free': True,
    },
    Teacher: {
        'price': 19.00,
        'is_start': False,
        'icon_name': 'group',
        'title': 'Teacher',
        'description': 'Starts with Teacher accounts with more seats available.',
        'is_free': False,
    },
    University: {
        'price': 49.00,
        'is_start': False,
        'icon_name': 'business_center',
        'title': 'University',
        'University': 'Starts with Teacher accounts with more seats available.',
        'is_free': False
    }
}
