def GlobalContext(request):
    return {
        'brand': 'MyBrand',
        'slug': request.path
    }
