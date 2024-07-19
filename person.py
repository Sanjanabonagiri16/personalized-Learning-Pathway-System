import pandas as pd
data = pd.read_csv('users.csv')
print(data)
data['skills'] = data['skills'].apply(lambda x: x.split(';'))
data['preferences'] = data['preferences'].apply(lambda x: x.split(';'))
data['progress'] = data['progress'].astype(int)
print(data)
def recommend_next_steps(user_id):
    user = data[data['user_id'] == user_id].iloc[0]
    skills = user['skills']
    preferences = user['preferences']
    progress = user['progress']
    recommendations = []
    if 'Python' in skills:
        recommendations.append('Advanced Python Course')
    if 'Data Science' in skills:
        recommendations.append('Data Science Project')
    if 'Video' in preferences:
        recommendations.append('Watch Data Science Tutorials on YouTube')
    if 'Interactive' in preferences:
        recommendations.append('Interactive Python Challenges')
    return recommendations
user_id = 1
recommendations = recommend_next_steps(user_id)
print(f'Recommendations for user {user_id}: {recommendations}')
def main():
    print("Welcome to the Personalized Learning Pathway System!")
    user_id = int(input("Enter your user ID: "))
    recommendations = recommend_next_steps(user_id)
    print(f'\nRecommendations for user {user_id}:')
    for rec in recommendations:
        print(f'- {rec}')

if __name__ == "__main__":
    main()
