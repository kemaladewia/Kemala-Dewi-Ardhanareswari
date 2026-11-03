def build_profile(first, last, **user_info):
    """Buat dictionary berisi semua yang kita ketahui tentang seorang user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('kemala', 'dewi',
                            location='solo',
                            hometown='solo',
                            field='industrial engineering')
print(user_profile)