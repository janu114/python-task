def display_profile():
    print("\nUser profile:")
    name = user.get("name","N/A")
    hobby = user.get("hobby","N/A")
    print(f"{name}","{hobby}")