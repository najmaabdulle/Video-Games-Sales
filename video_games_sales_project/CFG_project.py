# 1. Introduction and welcome message
# 2. Csv file
# 3. Top 20 global sales
# 4. Interactive questions
# 5. Graphs
# 6. Quiz
# 7. Conclusion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def display_top_n(df, n=20):
    print(df.head(n).to_string(index=False))

def top_20_global_sales(df, n=20):
    total_sales = df.head(n)['global_sales'].sum()
    top_20 = df.head(n)[["rank", "name", "global_sales", 'na_sales', 'eu_sales', 'jp_sales', 'other_sales']].rename_axis("Rank").reset_index(drop=True)
    top_20['global_sales'] = top_20["global_sales"] * 1000000
    top_20["global_sales"] = top_20["global_sales"].map("{:,.0f}".format)
    top_20 = top_20.rename(columns={"global_sales": "Global Sales"})
    return total_sales, top_20


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def welcome_message():
    print("Welcome to the realm of Video Games Sales\n")

def get_user_name():
    return input("Before we get started, what is your name? ").capitalize()

def ask_to_proceed():
    response = input("Would you like to proceed with exploring video game sales data? (Y/N): ").upper()

    if response == 'Y':
        return True
    elif response == 'N':
        print("\n😢 Okay bye... If you change your mind, feel free to come back. Goodbye!")
        return False
    else:
        print("Invalid response. Please enter 'Y' or 'N'.")
        return ask_to_proceed()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ask_questions(df):
    while True:
        print("\nWhat would you like to explore?")
        print("1. Top-selling video games of all time")
        print("2. Most popular gaming platforms")
        print("3. Variation of video game sales by region")
        print("4. Quiz")
        print("5. Exit")

        while True:
            choice = input("Enter the number of your choice (1-5): ")

            if choice in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")

        if choice == "1":
            top_selling_games(df)
        elif choice == "2":
            popular_platforms(df)
        elif choice == "3":
            sales_by_region(df)
        # elif choice == "4":
        #     plot_top_countries_pie_chart(df)
        elif choice == "4":
            display_top_n(df)
            quiz(df)
        elif choice == "5":
            print("\nHope you enjoyed our project and quiz session! Goodbye!")
            break

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def popular_platforms(df):
    plot_platforms_histogram(df.head(20))

def top_selling_games(df):
    print("\nTop Selling Games of All Time:")
    print(df[['rank', 'name', 'platform', 'year', 'global_sales']].head(20).to_string(index=False))

def plot_platforms_histogram(df):
    sns.histplot(data=df, x='global_sales', bins=20, kde=True, color='green', edgecolor='white')
    plt.xlabel('Global Sales (in millions)')
    plt.ylabel('Frequency')
    plt.title('Global Sales Distribution for Top 20 Gaming Platforms', color='black')  # Set title color
    plt.show()

def plot_sales_by_genre_and_region(df):
    # Genre Sales Data
    genres = ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc', 'Shooter', 'Simulation', 'Action']
    genre_sales = [82.74, 40.24, 35.82, 33, 31.37, 30.26, 30.01, 29.02, 28.62]

    # Regional Sales Data
    region_data = {
        'NA Sales': df['na_sales'].sum(),
        'EU Sales': df['eu_sales'].sum(),
        'JP Sales': df['jp_sales'].sum(),
        'Other Sales': df['other_sales'].sum()
    }

    # Plotting Side by Side
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Stacked Bar Chart for Genre Sales by Region
    stacked_bar_data = {
        'Genres': genres,
        'NA Sales': [df[df['genre'] == genre]['na_sales'].sum() for genre in genres],
        'EU Sales': [df[df['genre'] == genre]['eu_sales'].sum() for genre in genres],
        'JP Sales': [df[df['genre'] == genre]['jp_sales'].sum() for genre in genres],
        'Other Sales': [df[df['genre'] == genre]['other_sales'].sum() for genre in genres]
    }
    stacked_bar_df = pd.DataFrame(stacked_bar_data)
    stacked_bar_df.set_index('Genres', inplace=True)
    stacked_bar_df.plot(kind='barh', stacked=True, ax=axs[0], colormap='Pastel1')
    axs[0].set_xlabel('Sales (in millions)')
    axs[0].set_ylabel('Genres')
    axs[0].set_title('Video Game Sales by Genre and Region')

    # Pie Chart for Regional Sales Distribution
    axs[1].pie(region_data.values(), labels=region_data.keys(), autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
    axs[1].axis('equal')
    axs[1].set_title('Video Game Sales Distribution by Region')

    plt.tight_layout()
    plt.show()

def sales_by_region(df):
    plot_sales_by_genre_and_region(df)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def quiz(df):
    total_questions = 3
    score = 0

    # Question 1
    question1 = "Which video game holds the top rank in global sales?"
    options1 = ["A. Wii Sports", "B. Super Mario Bros.", "C. Nintendo", "D. GTA 5"]
    correct_option1 = "A"
    print(f"\n{question1}\n")
    print("Options:")
    for option in options1:
        print(option)

    while True:
        user_answer1 = input("\nPlease choose either A, B, C, or D: ").upper()

        if user_answer1 in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice. Please choose either A, B, C, or D.")

    if user_answer1 == correct_option1:
        score += 1
        print("\n🎉 Yayyy! That's right! 😆")
        print("Did you know that Wii Sports was a commercial success it sold over 82 million copies worldwide. It became the best-selling Nintendo video game, the fourth-best-selling video game of all time, and the best-selling game exclusive to one console. It has been featured on television in Wii commercials, news reports, and other programming. 😁")
    else:
        print(f"\n😥 Oh no! That's not correct.\n")
        retry = input("Would you like to have another go at this question? (Y/N): ").upper()
        if retry == "Y":
            print("\nLet's try again!")
            while True:
                user_answer1 = input("\nPlease choose either A, B, C, or D: ").upper()
                if user_answer1 in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid choice. Please choose either A, B, C, or D.")

            if user_answer1 == correct_option1:
                score += 1
                print("\n🎉 Yayyy! That's right! 😆")
                print("Did you know that Wii Sports was a commercial success it sold over 82 million copies worldwide. It became the best-selling Nintendo video game, the fourth-best-selling video game of all time, and the best-selling game exclusive to one console. It has been featured on television in Wii commercials, news reports, and other programming. 😁")
            else:
                print("\n😓 Unfortunately, that's still incorrect.")
                see_answer = input("Would you like to see the correct answer? (Y/N): ").upper()
                if see_answer == "Y":
                    print(f"\nThe correct answer is A: Wii Sports.")
                    print(f"Wii was a commercial success, selling over 82 million copies worldwide, becoming the best-selling Nintendo video game, as well as the fourth-best-selling video game of all time and the best-selling game exclusive to one console. 😁")
        else:
            see_answer = input("Would you like to see the correct answer? (Y/N): ").upper()
            if see_answer == "Y":
                print(f"\nThe correct answer is A: Wii Sports.")
                print(f"Wii was a commercial success, selling over 82 million copies worldwide, becoming the best-selling Nintendo video game, as well as the fourth-best-selling video game of all time and the best-selling game exclusive to one console. 😁")
            score += 1

    # Question 2
    question2 = "What is the genre of the game 'Grand Theft Auto V'?"
    options2 = ["A. Sports", "B. Adventure", "C. Role-Playing", "D. Action"]
    correct_option2 = "D"
    print(f"\n{question2}\n")
    print("Options:")
    for option in options2:
        print(option)

    while True:
        user_answer2 = input("\nPlease choose either A, B, C, or D: ").upper()

        if user_answer2 in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice. Please choose either A, B, C, or D.")

    if user_answer2 == correct_option2:
        score += 1
        print("\n🎉 Yayyy! That's right! 😆")
        print("Did you know that real gang members helped make GTA 5, contributing their insights and thoughts on the script? This unconventional approach aimed at achieving a more authentic and realistic gaming experience.")
    else:
        print(f"\n😥 Oh no! That's not correct.")
        retry = input("Would you like to have another go at this question? (Y/N): ").upper()
        if retry == "Y":
            print("\nLet's try again!")
            while True:
                user_answer2 = input("\nPlease choose either A, B, C, or D: ").upper()
                if user_answer2 in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid choice. Please choose either A, B, C, or D.")

            if user_answer2 == correct_option2:
                score += 1
                print("\n🎉 Yayyy! That's right! 😆")
                print("Did you know that real gang members helped make GTA 5, contributing their insights and thoughts on the script? This unconventional approach aimed at achieving a more authentic and realistic gaming experience.")
            else:
                print("\n😓 Unfortunately, that's still incorrect.")
                see_answer = input("Would you like to see the correct answer? (Y/N): ").upper()
                if see_answer == "Y":
                    print(f"\nThe correct answer is D: Action.")
                    print(f"Did you know that real gang members helped make GTA 5, contributing their insights and thoughts on the script?")
        else:
            see_answer = input("Would you like to see the correct answer? (Y/N): ").upper()
            if see_answer == "Y":
                print("\nThe correct answer is D: Action. Did you know that real gang members helped make GTA 5, contributing their insights and thoughts on the script?")
            score += 1

    # Question 3
    question3 = "Which platform is most represented in the top 20 games?"
    options3 = ["A. X360", "B. NES", "C. Wii", "D. PS2"]
    correct_option3 = "C"
    print(f"\n{question3}\n")
    print("Options:")
    for option in options3:
        print(option)

    while True:
        user_answer3 = input("\nPlease choose either A, B, C, or D: ").upper()

        if user_answer3 in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice. Please choose either A, B, C, or D.")

    if user_answer3 == correct_option3:
        score += 1
        print("\n🎉 Yayyy! That's right! 😆")
        print("Did you know that Nintendo, established in 1889, is the oldest video game company in the world?")
    else:
        print(f"\n😥 Oh no! That's not correct.")
        retry = input("Would you like to have another go at this question? (Y/N): ").upper()
        if retry == "Y":
            print("\nLet's try again!")
            while True:
                user_answer3 = input("\nPlease choose either A, B, C, or D: ").upper()
                if user_answer3 in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid choice. Please choose either A, B, C, or D.")

            if user_answer3 == correct_option3:
                score += 1
                print("\n🎉 Yayyy! That's right! 😆")
                print(
                        "Did you know that Nintendo, established in 1889, is the oldest video game company in the world?")
            else:
                print("\n😓 Unfortunately, that's still incorrect.")
                see_answer = input("Would you like to see the correct answer? (Y/N): ").upper()
                if see_answer == "Y":
                    print("\nThe correct answer is C: Wii. The Wii platform is the most represented in the top 20 games. Did you know that Nintendo, established in 1889, is the oldest video game company in the world?")
        else:
            see_answer = input("Would you like to see the correct answer? (Y/N): ").upper()
            if see_answer == "Y":
                print(f"\nThe correct answer is C: Wii. The Wii platform is the most represented in the top 20 games.")
                print(f"Did you know that Nintendo, established in 1889, is the oldest video game company in the world?")
            score += 1

    # Print the final score and percentage
    print(f"\nYour final score is: {score}/{total_questions}")
    percentage_correct = (score / total_questions) * 100
    rounded_percentage = round(percentage_correct, 1)
    print(f"You answered {rounded_percentage}% of the questions correctly.")

    # Displaying a conclusion based on the user's performance
    if percentage_correct == 100:
        print("🌟 WOW! A perfect score! You're a gaming legend! 🌟")
    elif percentage_correct >= 75:
        print("👾 Impressive! You've got a solid grip on video game sales. Keep it up! 👏")
    elif percentage_correct >= 50:
        print("🎮 Not bad at all! You're on your way to becoming a video game sales guru! 🌐")
    else:
        print("🤔 Keep exploring! Every gamer starts somewhere, and you're on the right track! 🎮")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def data_conclusion(total_sales):
    print("\n🎮 Hooray! You've conquered the world of video game sales with us. Before you jet off, let's wrap things up with a quick recap. Ready for the grand finale? 🚀👾\n")
    print("- Bravo on completing this epic journey through the realm of video game sales! 🌟")
    print("- Did you know that the top 20 games alone raked in a jaw-dropping",
          f"${total_sales:,.2f} million in global sales? It's like conquering a treasure trove of gaming excellence!")
    print("- As we ventured into the popularity of gaming platforms and dove into regional sales,",
          "it's mind-blowing to witness how the gaming landscape has evolved across different corners of the world.")
    print("- And let's not forget the quiz – you absolutely crushed it! Your gaming knowledge is nothing short of legendary.")
    print("- However, if the quiz didn't go too well it's ok! Better luck next time! 😊")
    print("- Whether you're a seasoned gamer or just embarking on your gaming adventure,",
          "remember that the world of video games is vast and full of delightful surprises.")
    print("- Ready for more gaming insights in the future? Keep those game controllers charged,",
          "and until next time, may your victories in the gaming realm be legendary! Game on, adventurer! 🎮🌟\n")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    welcome_message()

    user_name = get_user_name()
    print(f"\n👋 Nice to meet you {user_name}! Let's explore some video game sales data.\n")

    if ask_to_proceed():
        file_path = "video_games_sales.csv"
        df = pd.read_csv(file_path)

        # Display top 20
        total_sales, _ = top_20_global_sales(df)
        display_top_n(df)
        print("*********************************************************************************************************************************************************************")

        # Run the quiz
        ask_questions(df)
        print("*********************************************************************************************************************************************************************")

        # Include data-based conclusion
        data_conclusion(total_sales)
        print("*********************************************************************************************************************************************************************")

        # Conclusion
        print("\n🎮 Thanks for exploring video game sales data and rocking the quiz!")
        print("🚀 We hope you had a great blast! Game on, and see you in the next level! 🕹️\n")
        print(
        "*********************************************************************************************************************************************************************")

    # else:
    #     print("\n😢 Okay, if you change your mind, we'll be here. Goodbye for now! 👋")

if __name__ == "__main__":
    main()
