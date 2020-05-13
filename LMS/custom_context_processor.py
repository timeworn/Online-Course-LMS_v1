from LMS.constants import Student, University, Teacher


def GlobalContext(request):
    return {
        'brand': 'MyBrand',
        'slug': request.path,
        'ROLE_STUDENT': Student,
        'ROLE_UNIVERSITY': University,
        'ROLE_TEACHER': Teacher
    }
